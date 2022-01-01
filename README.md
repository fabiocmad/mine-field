
--------------------------------------------------
# Minefield Project
Check out the live version on Heroku: https://minefield-fabio.herokuapp.com/

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
As explained suring introduction, in any instance the user can hit a mine. If that happens, the game is automatically lost, and the objective is to clear the board without hitting any mines.
<p align="center">
   <img src="https://github.com/fabiocmad/mine-field/blob/main/images/game_lost.png"/>
</p>

#### PEP8 Before
Duriong PEP8 verification a few errors were foung, mostly on too many spaces, or lines too long that would not fit the terminal. Those errors were fixed.
<p align="center">
   <img src="https://github.com/fabiocmad/mine-field/blob/main/images/pep8_before.png"/>
</p>

#### PEP8 After
After fixes, PEP8 did not show any issues whatsoever.
<p align="center">
   <img src="https://github.com/fabiocmad/mine-field/blob/main/images/pep8_after.png"/>
</p>

### Future Features
* Allow player to select board size
* Allow player to see hints on proximity of mines if the input choosen was not a mine
* Update Google Sheets with User name, inputs, and score based on level played and timestamp up to that point
* Create scoreboard and print to the terminal the top players

## Data Model
I decided to use a matrix model for my board, it allows iteration through the lists and compare user unputs with position on the board.

A map is initialized and created once user chooses a level, and each level has a number of mines as values attached to a key on a dictionary. That dictionary can be updated and code maintenance and code review can easily be kept.

Several functions are used based on detailed wireframe line of thought. The init_game holds the majority of the code and works along a game_loop functions for repeated actions during the game that need to happen often. Refactoring code was as important step during the thought process of this game and I tried to implement it as best as I could.

## Testing
I tested the project with the following tests:

* Passed the code on PEP8 and confirmed there are no problems
* Gave invalid inputs on name, game actions, and levels to choose from 
* Checked on local terminal and on Heroku

### Bugs
#### Solved Bugs
* When I fist wrote the project I realised I needed to spend more time on the data structure logic implementation. I was using a lot of funcions and methods separately that would potentially be better off together, realised that by fixing input by input separately (name, level, game choices)
* I decided then to create two main functions with several methods each and work on a scrum style separating each by tasks, to make the best of the time

#### Remaining Bugs
* No remaining bugs with the features implemented so far

#### Validator Testing
* PEP8 - No erros returned after first ones were fixed

## Deployment
* Deployment on Herokuocorred with no issues and test was succesfull.
<p align="center">
   <img src="https://github.com/fabiocmad/mine-field/blob/main/images/heroku.png"/>
</p>


## Credits
https://stackoverflow.com/questions/35589938/input-string-only
https://www.w3schools.com/python/python_while_loops.asp
https://stackoverflow.com/questions/16635073/validating-user-input-strings-in-python
https://github.com/tchapi/markdown-cheatsheet/blob/master/README.md
https://www.w3schools.com/python/python_booleans.asp

