# StatCalculator
An application to return NBA stats for given NBA players and teams with a twist. This one predicts stats using machine learning.
Components of the application:
- Web Scraper- This sources the data for the application. I am web scraping the basketball reference website to pull player and team data.
- Predictions module - This module performs the data transformation to give the data back to the user in a readable format as well as performs the machine learning to predict stats. Using sci-kit learn at the moment, but will experiment with TensorFlow
- Stat Calculator GUI - Interactive GUI that lets the user choose between the applications functions. User at the moment has the choice to predict a player's stats in the next season, get a player's stats for a specific season, predict a player's stats for their next game, and get the stats of a player's last game

