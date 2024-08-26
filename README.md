# Purrtun Trader Bot

A bot for EDUCATIONAL PURPOSES and NOT FOR ACTUAL USE which trades IMAGINARY currency in the IMAGINARY economy of Purrtun which I AM NOT RESPONSIBLE IF YOU LOSE ANY CATBUX!!!!!! Purrlease don't yell at me if you lose all your cat stocks and your house and home and family ok thanks bye

## Getting Started

Follow these steps to set up your development environment and configure the bot.

### Virtual Environment Setup

1. **Clone the repository** (if applicable):
    ```bash
    do you need instructions to clone a repo??? look it up man
    ```

2. **Create and activate the virtual environment**:

    On macOS/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    On Windows:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### `.env` File Setup

1. **Create a `.env` file** in the root of your project:
    ```bash
    touch .env
    ```

2. **Add environment variables** to the `.env` file:
    ```env
    API_SECRET=your-api-secret-here
    DISCORD_ID=your-discord-id-here
    ```

    Replace `your-api-SECRET-here` and `your-discord-id-here` with your actual values.

### Configure the Bot

1. **Choose a stock** for the bot to trade by setting the `stock` variable in the script:
    ```python
    stock = "jazz"  # Replace "jazz" with your most favorite cat
    ```

2. **Set the trading amount** by adjusting the value passed to the `PurrtunTrader` class:
    ```python
    trader = PurrtunTrader(API_SECRET, DISCORD_ID, 1_000_000)  # Replace 1_000_000 with your desired amount
   # yes this is valid python you can underscore your numbers for readability
   # bet you didnt know that!!!!!!!!!
    ```

    This sets the initial amount of money the bot will use for trading.

### Running the Bot

After configuring the `.env` file and setting the desired stock and trading amount, you can run the bot with the following command:

```bash
python main.py
