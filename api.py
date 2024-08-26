import requests

API_BASE_URL = "https://api.purrtun.com/v1"


def get_market_data(api_key, cat_color):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    try:
        response = requests.get(f"{API_BASE_URL}/market/{cat_color}", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(err.response.text)
        raise


def place_order(api_key, cat_color, action, num_shares):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    order_data = {
        "numShares": num_shares,
        "action": action
    }
    try:
        response = requests.post(f"{API_BASE_URL}/trade/{cat_color}", headers=headers, json=order_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(err.response.text)
        raise


def get_portfolio(api_key, discord_id):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    try:
        response = requests.get(f"{API_BASE_URL}/portfolio/{discord_id}", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(err.response.text)
        raise
