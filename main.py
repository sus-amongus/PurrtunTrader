from bot import PurrtunTrader
from dotenv import load_dotenv, dotenv_values
load_dotenv()
config = dotenv_values(".env")

API_SECRET = config["API_SECRET"]
DISCORD_ID = config["DISCORD_ID"]
stock = "jazz"

if API_SECRET is None or DISCORD_ID is None:
    print("Mrowwww.... purrlease create your .env file.... then put in your values like KEY=\"VALUE\"")

if __name__ == "__main__":
    trader = PurrtunTrader(API_SECRET, DISCORD_ID, 1_000_000)

    try:
        while True:
            trader.run(stock)
    except ValueError as e:
        print(e)
