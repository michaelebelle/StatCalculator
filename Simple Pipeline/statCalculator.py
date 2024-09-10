import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import gatherBasketballStats
from sklearn.model_selection import train_test_split
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import os 
import predictions 
import getpass



def displayInputOptions():
    # user = os.getlogin()
    user = getpass.getuser()
    choice = None
    while choice is None or choice.isnumeric() == False:
        choice = simpledialog.askstring("Hello " + user + ", what function would you like to perform?", 
        "1. Predict Stats of a particular player for next season (Enter '1')\n2. Predict the stats of a player for their next game (Enter '2')\n3. Get the stats for a particular player in a particular season (Enter '3')\n4. Get the stats of the last game of a particular player (Enter '4')\n")
        if choice is None or choice.strip() == "": 
            exit()
        elif choice.isnumeric() == False:
            messagebox.showerror("Input Error", "Error: Your input is not a number. Please input the number option you would like to perform")

    if choice == "1":
        predictStats()               
    elif choice == "2":
        exit()
    elif choice == "3":
        getSeasonStats()
    elif choice == "4":
        exit()
    else: 
        messagebox.showerror("Invalid Option", "Not a Valid Option")


def getSeasonStats():
    player = simpledialog.askstring("Choice: Get Player Stats for a Season", "Input the player's last name and firstname seperated by a space as well as the season. ORDER MATTERS\nEx: 'Bryant Kobe'")    
    playerName = player.split()
    lname = playerName[0]
    fname = playerName[1]
    statChoice = None
    while statChoice is None or statChoice.isnumeric() == False:
        statChoice = simpledialog.askstring("Which stat would you like to see?", "1. Points (Enter '1')\n2. Rebounds (Enter '2')\n3. Assists (Enter '3')")
        print("StatChoice: ", statChoice)
        if statChoice.isnumeric() == False:
            messagebox.showerror("Input Error", "Error: Your input is not a number. Please input the number option you would like to perform")
    
    season = simpledialog.askstring("Which season?", "Ex: '1996-97'")
    if statChoice == "1":
        stats = gatherBasketballStats.getPlayerStatsSeason(lname, fname, season)
        stat = stats["PTS"]
        stat = stat[0]
        predictionStr = "{fname} {lname} averaged {stat} points during the {season} season".format(fname=fname, lname=lname, season=season, stat=stat)
        messagebox.showinfo("Stat", predictionStr)
    if statChoice == "2":
        stats = gatherBasketballStats.getPlayerStatsSeason(lname, fname, season)
        stat = stats["TRB"]
        stat = stat[0]
        predictionStr = "{fname} {lname} averaged {stat} rebounds during the {season} season".format(fname=fname, lname=lname, season=season, stat=stat)
        messagebox.showinfo("Stat", predictionStr)                      
    if statChoice == "3":
        stats = gatherBasketballStats.getPlayerStatsSeason(lname, fname, season)
        stat = stats["AST"]
        stat = stat[0]
        predictionStr = "{fname} {lname} averaged {stat} assists during the {season} season".format(fname=fname, lname=lname, season=season, stat=stat)
        messagebox.showinfo("Stat", predictionStr) 

def predictStats():
    player = simpledialog.askstring("Choice: Predict Player Stats for next season", "Input the player's last name and firstname seperated by a space. ORDER MATTERS\nEx: 'Bryant Kobe'")
    playerName = player.split()
    lname = playerName[0]
    fname = playerName[1]

    statChoice = None
    while statChoice is None or statChoice.isnumeric() == False:
        statChoice = simpledialog.askstring("Which stat would you like to predict?", "1. Points (Enter '1')\n2. Rebounds (Enter '2')\n3. Assists (Enter '3')")
        print("StatChoice: ", statChoice)
        if statChoice.isnumeric() == False:
            messagebox.showerror("Input Error", "Error: Your input is not a number. Please input the number option you would like to perform")
    if statChoice == "1":
        prediction = predictions.createModelNextSeasonStats(lname, fname, "PTS")
        predictionStr = "We predict that {fname} {lname} will average {prediction} points next season".format(fname=fname, lname=lname, prediction=prediction)
        messagebox.showinfo("Prediction", predictionStr)
    if statChoice == "2":
        prediction = predictions.createModelNextSeasonStats(lname, fname, "TRB") 
        predictionStr = "We predict that {fname} {lname} will average {prediction} rebounds next season".format(fname=fname, lname=lname, prediction=prediction)
        messagebox.showinfo("Prediction", predictionStr)                       
    if statChoice == "3":
        prediction = predictions.createModelNextSeasonStats(lname, fname, "AST") 
        predictionStr = "We predict that {fname} {lname} will average {prediction} assists next season".format(fname=fname, lname=lname, prediction=prediction)
        messagebox.showinfo("Prediction", predictionStr)

def takeUserInput():
    user = os.getlogin()
    user = getpass.getuser()
    root = Tk()
    button = Button(root, text="Begin Using StatCalculator", command=displayInputOptions())
    print("Hello {name}, what would you like to do today?")
    print("1.Predict Stats of a particular player for next season")
    print("2. Get the awards that a player won during a particular season")
    print("3. Get the stats for a particular player in a particular season")
    print("4. Get the stats of the last game of a particular player")



if __name__ == "__main__":
    displayInputOptions()
    # predictions.createModelNextSeasonStats("bryant", "kobe", "2024")