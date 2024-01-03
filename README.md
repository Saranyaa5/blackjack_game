# blackjack_game

## Files Description

1. **main_file.py:**
   - This is the main Python script that contains the logic for the Blackjack game.
   - It defines functions for playing the game, determining the winner, and managing the user and computer hands.
   - The script uses the `art` library to display ASCII art for the game's logo.
2. **art.py:**
   - This file contains ASCII art that serves as the logo for the Blackjack game.
   - The ASCII art is imported into the `main_file.py` script to display a visual representation of the game.
# rules of the game
## Card Values
1.Number cards (2-10) are worth their face value.
2.Face cards (Jack, Queen, King) are each worth 10 points.
3.An Ace can be worth 1 or 11 points, depending on which value benefits the player.
# How to Play
1.At the start, both the player and the computer dealer are dealt two cards.
2.The player decides whether to request an additional card (y for yes, n for no).
3.If the player's hand exceeds 21 points, and there's an Ace in the hand, the Ace is automatically converted to a value of 1.
4.After the player's turn, the computer dealer will draw cards until its hand reaches a minimum score of 17.
5.The winner is determined based on the final scores. The player wins if:
6.The player's score is closer to 21 than the dealer's score.
7.The dealer's score exceeds 21.
8.The game provides feedback on whether the player won, lost, or the match resulted in a draw.
