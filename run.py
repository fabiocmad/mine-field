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
    print("*********************** MINEFIELD - Rules of the game. ***********************\n")
    print("The game begins with the board covered in tiles. Click on any tile to uncover it.")
    print("Choose a column and a row respectively when prompted.")
    print("If not a mine, a number of close mines will be shown. This will help you deduce where the mines are so that you can mark them")
    print("Objectice is to clear the board without hitting any mines.")
    print("If you hit a mine, game is over.")
    
    print("To see this message again, type 'help' at any time.\n")
    print("********************************************************************************************")
    
def get_player_move():
    """
    Get player movement choice on mine field
    """
    print("Please choose a column and a row, separated by comas. ")
    print("Example: 3, 4\n")
    movement_data = input("Please choose: ")

    movement_data = movement_data.split(",")
    validate_data(movement_data)


def validate_data(values):
    """
    Inside the try, check if all inputs are integers.
    Raises ValueError if they are not integers,
    or if theres no two values for columns and row
    """
    try:
        [int(value) for value in values]
        if len(values) != 2:
            raise ValueError(
                f'Two values are needed, you provided {len(values)}'
            )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.')

get_player_move()