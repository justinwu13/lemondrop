# lemondrop

A solver for a funny little game featured in the 1993 Wizard of Oz video game for the SNES. The game can also be played in the web [here](https://aphotic.space/pub/games/lmndrop/). The rules are simple: you start with the numbers 1-12 available, and every turn, you roll two dice. Take the sum of the two dice, and to finish your turn, you look at your numbers and either choose to use up the sum or two other numbers that add up to the sum of the dice. For example, if you roll a 3, you can either use up your 3 or use up both the 1 and 2. You can only use each number from 1-12 once. As you might discover, the game is far from easy to win - for starters, you'll have to roll two sixes (a 1/36 chance!) at some point to use up your 12.

## Solver

The solver is quite rough around the edges, wrote it quite long ago. Uses a dynamic programming approach to determine the expected value of simpler game states and works its way up to the starting state. The game states are represented with a 12-bit number: the leftmost bit represents whether the 1 is available (1 for available, 0 for unavailable), 2nd leftmost represents the 2, and so on.

## Files

The `lemondropodds.py` file calculates the expected values of all game states and produces a text file `dropsodds.txt` that displays the results.

The `lemondropsolver.py` file calculates the expected values of all game states and stores all optimal decisions. The file `dropsolver.txt` is produced which displays the results in a table.
