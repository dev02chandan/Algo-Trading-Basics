import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access API key
API_KEY = os.getenv("API_KEY")

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={API_KEY}'
r = requests.get(url)
data = r.json()

print(data)