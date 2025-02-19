# lemondrop

A solver for a funny little game called Lemon Drop Elimination featured in the 1993 Wizard of Oz video game for the SNES. The game can also be played in the web [here](https://aphotic.space/pub/games/lmndrop/). The rules are simple: you start with the numbers 1-12 available, and every turn, you roll two dice. Take the sum of the two dice, and to finish your turn, you look at your numbers and either use up one or two numbers that sum up to the same sum as the dice. For example, if you roll a 3, you can either use up your 3 or use up both the 1 and 2. You can only use each number from 1-12 once, and if you have no valid moves after a roll, you lose. As you might discover, the game is far from easy to win - for starters, you'll have to roll two sixes (a 1/36 chance!) at some point to use up your 12.

## Solver

The solver uses a dynamic programming approach to determine the expected value of simpler game states and works its way up to the starting state. The game states are represented with a 12-bit number: the leftmost bit represents whether the 1 is available (1 for available, 0 for unavailable), 2nd leftmost represents the 2, and so on. For each possible game state, the solver determines the move that provides the greatest chance of success.

## Files

The `lemondropsolver.py` file calculates the expected values of all game states and stores all optimal decisions. The file `dropsolver.txt` is produced which displays the results in a table. The table is read by first finding your game state - for instance, 101101010111 indicates that you have 1, 3, 4, 6, 8, 10, 11, 12 still available and 2, 5, 7, 9 unavailable. Then, find the column for the dice roll that you receive to find the optimal decision. A 0 means that you have no valid moves left. The expected values are also shown in the file - as you can see, you start with an expected value of 0.00286, which means you have a 0.286% (1 in 350) chance of rolling well enough to win if you play optimally for the rest of the game.
