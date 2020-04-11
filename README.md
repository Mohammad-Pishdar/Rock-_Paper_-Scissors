# About this project
In this project, we apply your Python and object-oriented programming skills to build a program that plays the game of Rock Paper Scissors. We build classes that represent the game and its players. We'll write computer players that follow various different strategies, as well as a human player class that lets a human play the game against the computer.  
From that humble beginning, we will add classes and modify methods, expanding it into a full game. We'll use the `input` function to read the human player's moves from the keyboard, and `print` the results of each round. We'll use subclasses to build more intelligent computer players. And we'll test our code at every step by running the program, or by `import`ing it to test specific functions and methods.
# Getting Started
**1. Create a player subclass that plays randomly**  
The starter `Player` class always plays `'rock'`. That's not a very good strategy! Create a subclass called `RandomPlayer` that chooses its move at random. When you call the `move` method on a `RandomPlayer` object, it should return one of `'rock'`, `'paper'`, or `'scissors'` at random.  

**2. Keep score**  
The starter `Game` class does not keep score. It doesn't even notice which player won each round. Update the `Game` class so that it displays the outcome of each round, and keeps score for both players. We can use the provided `beats` function, which tells whether one move beats another one. Make sure to handle ties — when both players make the same move!

**3. Create a subclass for a human player**  
Create a `HumanPlayer` subclass, whose `move` method asks the human user what move to make. Set the program to play a game between `HumanPlayer` and `RandomPlayer`.

**4. Create player classes that remember**  
At the end of each game round, the `Game` class calls the `learn` method on each player object, to tell that player what the other player's move was. This means we can have computer players that change their moves depending on what has happened earlier in the game. To do this, we will need to implement `learn` methods that save information into instance variables.  
Create a `ReflectPlayer` class that remembers what move the _opponent_ played last round, and plays that move _this_ round. (In other words, if we play `'paper'` on the first round, a `ReflectPlayer` will play `'paper'` on the second round.)  
Create a `CyclePlayer` class that remembers what move _it_ played last round, and cycles through the different moves. (If it played `'rock'` this round, it should play `'paper'` in the next round.)

**5. Validate user input**  
The human player might sometimes make typos. If they enter <kbd>roxk</kbd> instead of  <kbd>rock</kbd>, the <code>HumanPlayer</code> code should let them try again. 

**6. Announce the winner**  
It's up to us how long the game should run. We could choose to continue until the player types `quit`, or we could have the game run until one player is ahead by three points, or any other rule that makes sense. At the end of the game, have it print out which player won, and what the final scores are.


