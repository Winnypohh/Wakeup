![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Text Adventure Game "Wake up!!!"


Wake up game is simple text based game where you need to follow a story and
answer the question. Game has a age group 18 and over to add some more choices.
Story should make you get out easy if you read all the story from start.

HOW TO PLAY.

First you need to Run Program.
Next you need to add your name and age if you under age you can't play 
and you need to Run Program again.
If you are over 18 it will let you play the game.
Game starts with story how the day started in the game.
Every end has a Question.
Questions are simple correct full answer (yes or no, left or right ...).
They are provided always end of the text you need only to get end of the game. Any wrong answer takes you back 
to start the game no need to but your name or age in for play.
If you make a spelling mistake on answer you need to start again  from start.

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

-----
Happy coding!