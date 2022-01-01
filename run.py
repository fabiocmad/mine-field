import datetime
import gspread
import random
import dateutil
from google.oauth2.service_account import Credentials

EASY = "easy"
MEDIUM = "medium"
HARD = "hard"

mines_dict = {
    EASY: 5,
    MEDIUM: 8,
    HARD: 10
}

MINE = "*"

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
    Get player name at the beginning of each new game
    """
    print("Hello player! Please add your name:")
    print("Example: 'John', 'Michael', 'Bernard'")

    user_name = input("Name: ")
    print("\n")
    while not user_name:
        user_name = input("We really need to know your name: ")
    return user_name


def how_to_play():
    """
    Rules of the game that will be shown at beginning of each game
    Or whenever the user wants a reminder of the rules and how to play
    """
    print("*********************** MINEFIELD - Rules of the game. ************************************\n")
    print("The game begins with the board covered in tiles.")
    print("Choose a column and a row respectively when prompted.")
    print("If not a mine, a number of close mines will be shown. This will help you on where the mines are so that you can mark them")
    print("Objectice is to clear the board without hitting any mines.")
    print("If you hit a mine, game is over.")
    
    print("To see this message again, type 'help' at any time.\n")
    print("********************************************************************************************\n")



def get_difficult_level(user_name):
    """
    Get user choice of difficulty level of the game and validate the data
    """
    difficult = False

    while not difficult:
        difficult_level = input(f'Hi {user_name}, please choose difficult level -> easy, medium or hard: ')

        if difficult_level == 'easy':
            difficult = True
            difficult_level = EASY
            print("\n")
            pass
        elif difficult_level == 'medium':
            difficult = True
            difficult_level = MEDIUM
            print("\n")
            pass
        elif difficult_level == 'hard':
            difficult = True
            difficult_level = HARD
            print("\n")
            pass
        else:
            print("Invalid data, needs to be easy, medium or hard.\n")
            difficult = False
            
    return difficult_level
    


def generate_map(difficult_level):
    """
    Generates a new map
    """
    empty_matrix = [
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "]
    ]
    matrix = [
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "]
    ]
    
    for i in range(mines_dict.get(difficult_level, 5)):
        value_pos = None
        x = 0
        y = 0
        while value_pos != " ":
            x = random.randint(0, 7)
            y = random.randint(0, 7)
            value_pos = matrix[x][y]
        
        matrix[x][y] = MINE

    return matrix, empty_matrix



def press_enter_to_start():
    """
    User press enter to continue or to start the game
    """
    input("Press enter to start the game.")


def get_player_move(user_name):
    """
    Get player movement choice on mine field
    """
    while True:
        print(f"Hello {user_name}. Please choose a column and a row, separated by comas. ")
        print("Example: 3, 4\n")
        movement_data = input("Please choose your input or type 'help': ")

        if movement_data == "help":
            how_to_play()
            continue

        movement_data = movement_data.split(",")

        if validate_data(movement_data):
            print("Data is valid!")
            break

    return movement_data


def validate_data(values):
    """
    Inside the try, check if all inputs are integers.
    Raises ValueError if they are not integers,
    or if theres no two values for columns and row
    """
    # Validation to try if values provided by user
    # for choices on the map are in the format
    # expected i.e. (5, 6), int and int
    try:
        [int(value) for value in values]
        if len(values) != 2:
            raise ValueError(
                f'Two values are needed, you provided {len(values)}'
            )
    except ValueError as e:
        print(f"Seems like you typed {e}. It's an invalid value, please try again.")
        return False

    return True


def update_score_worksheet(data):
    """
    Update scores worksheet, add new row with the two numbers provided
    """
    print("Updating score worksheet...")
    scores_worksheet = SHEET.worksheet("score")
    scores_worksheet.append_row(data)
    print("Score worksheet updated sussessfully.\n")


def init_game():
    """
    Starts a new game with instructions, and collects the name of the new user
    """
    how_to_play()
    user_name = get_player_name()
    difficult_level = get_difficult_level(user_name)
    map, empty_map = generate_map(difficult_level)
    press_enter_to_start()
    start_time_game = datetime.datetime.now()
    game_state = "progress"

    return (user_name, difficult_level, start_time_game, game_state, map, empty_map)


def restart_game():
    """
    Restart game with instructions, and collects the name of the new user
    """
    how_to_play()
    user_name = get_player_name()
    difficult_level = get_difficult_level(user_name)
    empty_map = generate_map(difficult_level)
    press_enter_to_start()
    game_state = "progress"

    return (user_name, difficult_level, game_state, empty_map)


def show_player_map(player_map):
    pretty_map = ""
    for row in player_map:
        pretty_map += "-----------------\n"
        pretty_row = "|"
        for column in row:
            pretty_row += (column + "|")
        pretty_map += (pretty_row + "\n")
    pretty_map += "-----------------\n"
    print(pretty_map)

    return (pretty_map)



def game_loop(user_name, initial_game_state, map, empty_map):
    """
    While game is not won neither lost, this loop will continue happening
    """
    game_state = initial_game_state
    
    while game_state == "progress":
        show_player_map(empty_map)
        data = get_player_move(user_name)
        print(data)
        row, col = data
        row = int(row)
        col = int(col)
        print("Found", map[row][col])
        
        if map[row][col] == MINE:
            print("You hit a BOMB! You lost!")
            map[row][col] = "*"
            game_failed()
            break

        map[row][col] = "X"
        empty_map[row][col] = "X"
        

    
    end_time_game = datetime.datetime.now()
    return (game_state, map, end_time_game)


def game_completed():
    score_data = [num for num in data]
    update_score_worksheet(score_data)
    game_state = "completed"
    pass


def game_failed():
    game_state = "failed"
    print("Thanks for playing!")
    print("--- End of the game --- type 'python3 run.py to restart' --- \n")
    pass
    

(user_name, difficult_level, start_time_game, game_state, map, empty_map) = init_game()

(game_state, map, end_time_game) = game_loop(user_name, game_state, map, empty_map)

if game_state == "failed":
    game_failed(user_name, difficult_level)
elif game_state == "completed":
    duration = dateutil.relativedelta.relativedelta(end_time_game, start_time_game)
    duration_text = "%d hours, %d minutes and %d seconds" % (duration.hours, duration.minutes, duration.seconds)
    game_completed(user_name, difficult_level, duration_text)



