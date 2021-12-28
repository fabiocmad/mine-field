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

    user_name = input("Name: ")


def how_to_play():
    """
    Rules of the game that will be shown at beginning of each game
    Or whenever the user wants a reminder of the rules and how to play
    """
    
def get_player_move():
    """
    Get player movement choice on mine field
    """
    column = input("Please choose a column: ")
    row = input("Please choose a row: ")

    print(f'You choose column {column} and row {row}')

get_player_move()
