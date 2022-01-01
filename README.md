## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

--------------------------------------------------
# Minefield Project

## About the game
Minefield is a Python terminal game, which runs on a mock terminal on Heroku.

Minefield is a single-player puzzle video game. The objective of the game is to clear a square board containing hidden "mines" without detonating any of them, with help from clues about the number of neighbouring mines in each field.

## Wireframe
![Wireframe](https://github.com/fabiocmad/mine-field/blob/main/images/Wireframe.png)

## How to play
Minefield is based on the classid Minesweeper game, you can read more about it on https://en.wikipedia.org/wiki/Minesweeper_(video_game).

In this version, the player enter their name, the level of difficulty, and the input values to open the minefield.

For each non-mined guess, the surrounding spaces will reveal any close mines to that specifically move.

The objetive of the game is to clear all the board without hitting any mines, if any mines are hit, the game is lost.

## Features

### Existing Features
* Random board generation of mines
* User chooses level of difficulty
* Player cannot see where the mines were randomly placed

#### How to Play
Instructions on how to play are given at the beggining of the game. Player can get familiar with the objective and gets instructions how to get help during the game if needed.
<p align="center">
   <img src="https://github.com/fabiocmad/mine-field/blob/main/images/intro.png"/>
</p>

#### Choose difficulty level
Player can choose between "easy", "medium" and "hard" levels. Each level has a hidden code on the backend with a dictionary that has key:values depending on the difficulty the user chooses. The harder the level, the bigger will be the number of mines ramdonly placed at the board.

<p align="center">
   <img src="https://github.com/fabiocmad/mine-field/blob/main/images/level_input.png"/>
</p>

#### Map
After difficulty is choosen, the map is generated according to the respective number of mine of that level.
<p align="center">
   <img src="https://github.com/fabiocmad/mine-field/blob/main/images/map_scratch.png"/>
</p>

#### Map Updated
When user starts inputing their moves, an updated map is printed for each turn, to show the user the movements they have already done.
<p align="center">
   <img src="https://github.com/fabiocmad/mine-field/blob/main/images/map_updated.png"/>
</p>

#### Get user name
At the beginning of each game, user needs to provide their names. If gives a more personalised experience and in the future that data can be used to store values and scores, as it will be mentiopned on the "Future Implementations" of this readme file, for more information.
<p align="center">
   <img src="https://github.com/fabiocmad/mine-field/blob/main/images/name_input.png"/>
</p>

#### Name Validation
Once user adds their name, a validation is needed to make sure that theres no black spaces or that user is not just hitting enter, thus in such cases, a while loop keeps asking the questions until we have an expected answer, in ordert to go ahead with the game.
<p align="center">
   <img src="https://github.com/fabiocmad/mine-field/blob/main/images/name_validation.png"/>
</p>

#### User input data validation
I created a test on a google sheet to make sure the data could be transferred on a future ocasion (user name, inputs, level choices and timestamp for example) that data could be user to improve user experience with time - this will be mentioned on future implementation section on this file too.
<p align="center">
   <img src="https://github.com/fabiocmad/mine-field/blob/main/images/updating_worksheet.png"/>
</p>

Data validation is needed on the inputs for the map choices to make sure we cover any potential gaps from the user. In this case, the validation occurs to make sure the data is not empty and not a radom string, and if so, flags to the user that the format is not the expected, and that a new input should be typed, considering the correct parameters.
<p align="center">
   <img src="https://github.com/fabiocmad/mine-field/blob/main/images/data_validation.png"/>
</p>

#### Help during the game
During the game, and as explained on the intro of the game, user can ask for 'help' at anytime. This will call a introduction function that will print to the terminal the rules of the game again, and cthe game can continue as normal.
<p align="center">
   <img src="https://github.com/fabiocmad/mine-field/blob/main/images/help.png"/>
</p>

#### Level Input Validation
Validation for the level is needed to make sure user is writing within the expected parameters. In this case they are "easy", "medium" and "hard" as described on the printed message requesting such data. In case the data difer from expectation, a new message is printed to the terminal reminding user what needs to be typed and which choices they have to do so.
<p align="center">
   <img src="https://github.com/fabiocmad/mine-field/blob/main/images/level_validator.png"/>
</p>

#### Game lost
<p align="center">
   <img src="https://github.com/fabiocmad/mine-field/blob/main/images/game_lost.png"/>
</p>

#### PEP8 Before
<p align="center">
   <img src="https://github.com/fabiocmad/mine-field/blob/main/images/pep8_before.png"/>
</p>

#### PEP8 After
<p align="center">
   <img src="https://github.com/fabiocmad/mine-field/blob/main/images/pep8_after.png"/>
</p>

### Future Features

## Data Model

## Testing
### Bugs
#### Solved Bugs
#### Remainging Bugs
#### Validator Testing

## Deployment

## Credits
