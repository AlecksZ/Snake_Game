Snake Game (Python OOP Project)

This project is a recreation of the classic Snake Game built in Python using the Turtle graphics library. The goal of the project was to strengthen my understanding of Object-Oriented Programming (OOP) principles by designing the game as a collection of independent, reusable classes.

How the Program Works

The game creates a 600x600 pixel game window and continuously updates the screen while moving the snake across the board. The player controls the snake as it searches for randomly generated food. When the snake eats food, it grows longer and the score increases. If the snake collides with a wall or its own body, the game resets.

The project is organized into separate classes, each responsible for a specific part of the game:

Snake Class – Handles snake creation, movement, growth, and resetting after collisions.
Food Class – Generates food at random locations and randomly changes its color each time it respawns.
Scoreboard Class – Tracks and updates the player's score and manages game resets.

The main game loop coordinates interactions between these objects, detects collisions, updates the score, and controls the game's overall flow.


Technologies Used:
Python
Turtle Graphics
Object-Oriented Programming (OOP)
Random Module
