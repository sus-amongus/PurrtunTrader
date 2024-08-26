import datetime
import logging
from api import get_market_data, place_order, get_portfolio

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler("purrtun_trader.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
one_second = datetime.timedelta(seconds=1)


def calculate_ma(prices):
    # Simple Moving Average calculation
    return sum(prices) / len(prices)


class PurrtunTrader:
    def __init__(self, api_key, discord_id, trade_amount):
        if api_key is None:
            raise ValueError("API key is required")
        self.api_key = api_key
        self.discord_id = discord_id
        self.trade_amount = trade_amount  # Amount to trade (e.g., $100,000)
        self.asset_price_history = []  # Initialize asset price history
        self.short_period = 20  # Short-term Moving Average period
        self.long_period = 60  # Long-term Moving Average period
        self.holding_position = False  # Flag to track if currently holding a position
        self.last_tick = datetime.datetime.now()
        self.profit = 0.0  # Track profit made
        self.last_buy_price = 0.0  # Track the last buy price
        logger.info("PurrtunTrader initialized with trade amount of ${:.2f}".format(trade_amount))

    def calculate_shares_to_buy(self, current_price, available_shares):
        max_shares = self.trade_amount // current_price
        to_buy = min(max_shares, available_shares)
        return int(to_buy)

    def calculate_max_shares_to_sell(self, cat_color):
        portfolio = get_portfolio(self.api_key, self.discord_id)
        for holding in portfolio.get('holdings', []):
            if holding['stock']['catColor'] == cat_color:
                return holding['numberOfShares']
        return 0

    def run(self, cat_color):
        now = datetime.datetime.now()
        if now - self.last_tick < one_second:
            return
        else:
            self.last_tick = now

        try:
            market_data = get_market_data(self.api_key, cat_color)
            current_price = market_data['price']
            available_shares = market_data['availableShares']
            self.asset_price_history.append(current_price)

            # Adjust history size if necessary
            if len(self.asset_price_history) > self.long_period:
                self.asset_price_history = self.asset_price_history[-self.long_period:]

            # Calculate Moving Averages
            if len(self.asset_price_history) >= self.long_period:
                short_ma = calculate_ma(self.asset_price_history[-self.short_period:])
                long_ma = calculate_ma(self.asset_price_history[-self.long_period:])

                # Decision-making based on Moving Average crossover
                if short_ma > long_ma:
                    # Buy signal or hold position
                    if not self.holding_position:
                        shares_to_buy = self.calculate_shares_to_buy(current_price, available_shares)
                        if shares_to_buy > 0:
                            buy_order = place_order(self.api_key, cat_color, "buy", num_shares=shares_to_buy)
                            logger.info(f"Bought {shares_to_buy} shares of {cat_color} at price {current_price}")
                            self.last_buy_price = current_price
                            self.holding_position = True

                elif short_ma < long_ma:
                    # Sell signal or close position
                    if self.holding_position:
                        shares_to_sell = self.calculate_max_shares_to_sell(cat_color)
                        if shares_to_sell > 0:
                            sell_order = place_order(self.api_key, cat_color, "sell", num_shares=shares_to_sell)
                            profit_made = (current_price - self.last_buy_price) * shares_to_sell
                            self.profit += profit_made
                            logger.info(f"Sold {shares_to_sell} shares of {cat_color} at price {current_price}")
                            logger.info(f"Profit made on this trade: {profit_made:.2f}")
                            logger.info(f"Total profit so far: {self.profit:.2f}")
                            self.holding_position = False

        except Exception as e:
            logger.error(f"Error handling market data for {cat_color}: {e}")
