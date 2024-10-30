import requests
import pandas as pd

# Define constants
TOKEN = 'your_personal_access_token_here'
HEADERS = {'Authorization': f'token {TOKEN}'}

# Initialize lists to store data
users_data = []
repos_data = []

def fetch_data(url, params=None):
    """ Helper function to make requests with error handling """
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
