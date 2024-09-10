import pandas as pd
import requests
pd.set_option('display.max_columns', None)
import time
import numpy as np
from unidecode import unidecode
import random




def extractTeamInformation(teams_list, season_list):
    nba_df = pd.DataFrame()
    for season in season_list:
        for team in teams_list:
            url = 'https://www.basketball-reference.com/teams/' + team + '/' + season + '/gamelog/'
            print(url)
            team_df = pd.read_html(url, header=1, attrs={'id':'tgl_basic'})[0]
            team_df.info()
            team_df = team_df[(team_df['Rk'].str!= '') & (team_df['Rk'].str.isnumeric())]
            team_df = team_df.drop(columns= ['Rk', 'Unnamed: 24'])



            team_df.insert(loc=0, column='Season', value=season)
            team_df.insert(loc=1, column='Team', value=team.upper())

            nba_df = pd.concat([nba_df, team_df], ignore_index=True)
            time.sleep(random.randint(4,6))
    
    return nba_df

def extractPlayerCareerStatsData(lname,fname, year):
    if len(lname) >= 5:
        lname = lname[0:5] 
    if len(fname) >= 2:
        fname = fname[0:2]
    firstLetterLname = lname[0:1]
    fullName = lname + fname 



    print(fullName)
    url = "https://www.basketball-reference.com/players/" + firstLetterLname + '/' + fullName + '01.html'
    print(url)
    player_df = pd.read_html(url, header=0, attrs={'id':'per_game'})[0]
    print(player_df.info())
    print(player_df)

    return player_df

if __name__ == "__main__":
    #nba_df = extractTeamInformation(['ATL'], ['2014'])
    #nba_df.to_excel("Team Stats.xlsx")
    extractPlayerCareerStatsData("bryant", "kobe", "2024")
