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

#### How to Play
![howToPlay](https://github.com/fabiocmad/mine-field/blob/main/images/intro.png)

#### Choose difficulty level
![level](https://github.com/fabiocmad/mine-field/blob/main/images/level_input.png)

#### Map
![map](https://github.com/fabiocmad/mine-field/blob/main/images/map_scratch.png)

#### Get user name
![username](https://github.com/fabiocmad/mine-field/blob/main/images/name_input.png)

#### User input data validation
![validationOne](https://github.com/fabiocmad/mine-field/blob/main/images/updating_worksheet.png)
![validationTwo](https://github.com/fabiocmad/mine-field/blob/main/images/data_validation.png)


### Future Features

## Data Model

## Testing
### Bugs
#### Solved Bugs
#### Remainging Bugs
#### Validator Testing

## Deployment

## Credits
