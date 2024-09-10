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


def createModelNextSeasonStats(lname,fname, stat):
    dataset = gatherBasketballStats.extractPlayerCareerStatsData(lname,fname)
    print(dataset.info())
    idx = 0
    dataset.insert(idx, 'SeasonNum', value=np.arange(len(dataset)))
    dataset.info()
    print(dataset['SeasonNum'])
    dataset = dataset.dropna()

    x = dataset[["SeasonNum"]]
    y = dataset[[stat]]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3, random_state=42)
    regressorObject = LinearRegression()
    print("X train values: ", x_train.values)
    print("Y train values: ", y_train.values)    
    regressorObject.fit(x_train.values, y_train.values)


    plt.scatter(x_train, y_train, color="red")
    plt.plot(x_train, regressorObject.predict(x_train))
    
    print(len(x))
    regressorObject.predict([[len(x) + 1]])
    prediction = regressorObject.predict([[len(x) + 1]])
    return prediction

def displayInputOptions():
    user = os.getlogin()
    choice = "F"
    while choice.isnumeric() == False:
        choice = simpledialog.askstring("Hello " + user + " what would you like to do today?", 
        "1. Predict Stats of a particular player for next season (Enter '1')\n2. Predict the stats of a player for their next game (Enter '2')\n3. Get the stats for a particular player in a particular season (Enter '3')\n4. Get the stats of the last game of a particular player (Enter '4')\nNote a blank response will end the program")
        print("Choice is: ", choice)
        if choice is None or choice.strip() == "": 
            print("Choice is none")
            exit()
        elif choice.isnumeric() == False:
            messagebox.showerror("Input Error", "Error: Your input is not a number. Please input the number option you would like to perform")

    if choice == "1":
        player = simpledialog.askstring("Choice: Predict Player Stats for next season", "Input the player's last name and firstname seperated by a space. ORDER MATTERS\nEx: 'Bryant Kobe'")
        playerName = player.split()
        lname = playerName[0]
        fname = playerName[1]
        print(lname)
        print(fname)
        stat = "F"
        while stat.isnumeric() == False:
            stat = simpledialog.askstring("Which stat would you like to predict?", "1. Points (Enter '1')\n2. Rebounds (Enter '2')\n3. Assists (Enter '3')")
            if choice.isnumeric() == False:
                messagebox.showerror("Input Error", "Error: Your input is not a number. Please input the number option you would like to perform")
        if stat == "1":
            prediction = createModelNextSeasonStats(lname, fname, "PTS")
            predictionStr = "We predict that {fname} {lname} will average {prediction} points next season".format(fname=fname, lname=lname, prediction=prediction)
            messagebox.showinfo("Prediction", predictionStr)
        if stat == "2":
            prediction = createModelNextSeasonStats(lname, fname, "TRB") 
            predictionStr = "We predict that {fname} {lname} will average {prediction} rebounds next season".format(fname=fname, lname=lname, prediction=prediction)
            messagebox.showinfo("Prediction", predictionStr)                       
        if stat == "3":
            prediction = createModelNextSeasonStats(lname, fname, "TRB") 
            predictionStr = "We predict that {fname} {lname} will average {prediction} rebounds next season".format(fname=fname, lname=lname, prediction=prediction)
            messagebox.showinfo("Prediction", predictionStr)                
    elif choice == "2":
        exit()
    elif choice == "3":
        exit()
    elif choice == "4":
        exit()
    else: 
        messagebox.showerror("Invalid Option", "Not a Valid Option")

def takeUserInput():
    user = os.getlogin()
    root = Tk()
    button = Button(root, text="Begin Using StatCalculator", command=displayInputOptions())
    print("Hello {name}, what would you like to do today?")
    print("1.Predict Stats of a particular player for next season")
    print("2. Predict the stats of a player for their next game")
    print("3. Get the stats for a particular player in a particular season")
    print("4. Get the stats of the last game of a particular player")



if __name__ == "__main__":
    displayInputOptions()
    # createModelNextSeasonStats("bryant", "kobe", "2024")

