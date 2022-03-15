import typer
import requests
import csv
import json
import pandas as pandasForSortingCSV
from tqdm import tqdm
from time import sleep
import sqlite3 

existing_usernames = ["rick", "morty"]



def main(username: str):
    user_choice = -1
    while user_choice != 5:
        maybe_create_user(username=username)
        user_choice = int(input("Choose number: "))

        if user_choice == 1:
            nba_teams_output_csv()
        print()
        if user_choice == 5:
            request_for_nba_teams_data()
        if user_choice == 2:
            request_for_nba_players_data()
        if user_choice == 3:
            nba_team_output_json()
        else:
            break
        
        

    

 
greet = typer.style("NBA CLI App", fg=typer.colors.GREEN, bold=True)
message = greet
typer.echo(message)




def maybe_create_user(username: str = typer.Argument(..., help="The name of the user to greet")):
    """
    App made by Piotr Jagiello
    
    """
    message_start = "Welcome to NBA CLI App "
    if username in existing_usernames:
        typer.echo("The user already exists")
        raise typer.Exit()
    if username == "root":
        typer.echo("The root user is reserved")
        raise typer.Exit(code=1)
    if not username:
        typer.echo("No provided users")
        raise typer.Abort()
        
    else:
        typer.echo(f"{message_start}: {username}")
    

# Downloading Nba team from API
def request_for_nba_teams_data():
    global csvData
    response = requests.get("https://www.balldontlie.io/api/v1/teams/")
    
    
    for i in tqdm(range(200)):  
        sleep(.01) 

    response.raise_for_status()
    data = response.json()
    print(data)
    typer.echo(f"Sended request for Nba data")



def nba_teams_output_csv():
    global csvData
    response = requests.get("https://www.balldontlie.io/api/v1/teams/")
    data = response.json()
    feed = []
    for i in tqdm(range(1)):  
        sleep(.01) 

        csvheader = ['Division', 'Full_name']

        for x in data["data"]:
            listing = [x["division"],x["full_name"]]
            feed.append(listing)

# opening .csv file
        with open('nba_teams.csv', 'w', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(csvheader)
            writer.writerows(feed)
            print("Finished.")
            f.close()
                

        csvData = pandasForSortingCSV.read_csv('nba_teams.csv')

        print("\bBefore sorting:")
        print(csvData)

        csvData.sort_values(["Division"],
                    axis=0,
                    ascending=[True],
                    inplace=True)
        print("\nAfter sorting:")
        print(csvData)

def request_for_nba_players_data():
        response = requests.get("https://www.balldontlie.io/api/v1/players/")
        response.raise_for_status()
        data = response.json()
        print(data)
        feed = []



def nba_team_output_json():

    for i in tqdm(range(1)):  
            sleep(.01) 
            response = requests.get("https://www.balldontlie.io/api/v1/teams/")
            data = response.json()
            feed = []
            for x in data["data"]:
                listing = [x["division"],x["full_name"]]
                feed.append(listing)
            with open('nba_team_data.json', "w") as f:
                json.dump(data, f)
                f.close()


    
    
    
    
            







if __name__ == "__main__":
    typer.run(main)







