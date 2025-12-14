import requests

API_KEY = "198668c0246b4455802154026250412"

def get_weather(city):
    base_url = "http://api.weatherapi.com/v1/current.json"

    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "no"
    }

    try:
        response = requests.get(base_url, params=params, timeout=5)

        if response.status_code != 200:
            return None, "Weather service is unavailable."

        data = response.json()

        if "error" in data:
            return None, data["error"]["message"]

        return data, None

    except requests.exceptions.RequestException:
        return None, "Network error."

