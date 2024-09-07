# quotes/utils.py

# quotes/utils.py

import requests

def get_quote_of_the_day():
    url = "https://api.forismatic.com/api/1.0/"
    params = {
        'method': 'getQuote',
        'format': 'json',
        'lang': 'en'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        return {"quote": data.get("quoteText", "No quote found"), "author": data.get("quoteAuthor", "Unknown")}
    except requests.RequestException as e:
        print(f"Error fetching quote: {e}")
        return {"quote": "Unable to fetch quote", "author": "Unknown"}
