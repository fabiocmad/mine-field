import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('mine_field')


def get_player_name():
    """
    Get user name input
    """
    print("Hello player! Please add your name:")
    print("Example: 'John', 'Michael', 'Bernard'")

    data_str = input("Name: ")
    print(f'The data provided is {data_str}')

get_player_name()
