#imports
from asyncore import write
from dataclasses import dataclass
import requests
import json
import csv
import pandas as pandasForSortingCSV
from time import sleep
import argparse



def intro():

    parser = argparse.ArgumentParser( prog='NBA CLI app',
                                      description="""
    Detailed app about informations from best basketball league worldwide.
    Program made by Piotr Jagiello
    """,
    epilog='copyright (c) 2022 Piojagcodes'
)

    parser.add_argument('-p', '--prt', default='[DEFAULT]', help='This is the help of this add_argument')
    args = parser.parse_args()

    if args.prt != '[DEFAULT]':
        print(args.prt + ': has been printed...')
    else:
        print(args.prt + ':DEFAULT')
    
    
    

#function for requesting data
def grouped_teams():
    global csvData
    response = requests.get("https://www.balldontlie.io/api/v1/teams/")
    response.raise_for_status()
    data = response.json()
    print(data)
    feed = []

    csvheader = ['Division', 'Full_name']

    for x in data["data"]:
        listing = [x["division"],x["full_name"]]
        feed.append(listing)

    with open('nba_teams.csv', 'w', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(csvheader)
        writer.writerows(feed)
        print("Finished.")

    csvData = pandasForSortingCSV.read_csv('nba_teams.csv')

    print("\bBefore sorting:")
    print(csvData)

    csvData.sort_values(["Division"],
                    axis=0,
                    ascending=[True],
                    inplace=True)
    print("\nAfter sorting:")
    print(csvData)


def players_stats():
        response = requests.get("https://www.balldontlie.io/api/v1/players/")
        response.raise_for_status()
        data = response.json()
        print(data)
        feed = []

    
        csvheader = ['first_name', 'last_name', 'height_inches', 'weight_pounds']

        for x in data["data"]:
            listing = [x["first_name"],x["last_name"], x["height_inches"], x["weight_pounds"]]
            feed.append(listing)

        with open('nba_players.csv', 'w', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(csvheader)
            writer.writerows(feed)
            print("Finished.")
            print(csvData)
            

        
        
if __name__ == "__main__":
    intro()
    grouped_teams()
    players_stats()
"""
    print("Enter number:")

global_input = 1
x = input()
x = global_input
if global_input == 1:
    
"""
   
     