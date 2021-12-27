# api: http://acnhapi.com/
# api documentation: http://acnhapi.com/doc

import time
import requests
import json
import pandas as pd
from requests.api import get


'''
describe the API 
    ----This is an API that gathers and returns specific data relating to Animal Crossing
            villagers. Lines 1 and 2 will refer you to the site and documentation

todo:
    make the request
        ----line 34
    parse the response
        ----lines 35-43
    and either:
        pretty-print the data (if it is short)
                ----I did this (lines 45 and 51)
        write it to a CSV file if it is long (include this CSV file in your repo) 
                ----And this ("Kody_data_project_part_4.csv") [line 62]

'''


def get_vil(id, attribute):
    url = "http://acnhapi.com/v1/villagers"
    url += "/"+str(id)

    response = requests.get(url)
    results = json.loads(response.text)
    df = pd.json_normalize(results)

    attributes = pd.Series(dtype=str)
    attributes["name"] = df["name.name-USen"][0]
    attributes["birthday"] = df["birthday-string"][0]
    attributes["species"] = df["species"][0]
    attributes["saying"] = df["catch-phrase"][0]
    attributes["hobby"] = df["hobby"][0]

    print("\n\nYou wanted the", attribute, "attribute! That is",
          attributes.iloc[int(attribute)-1], "which is their", attributes.keys()[int(attribute)-1], "of course!\n")

    time.sleep(2)  # just to make it more fun and engeretic
    print("I'm so sorry, I love this villager! I can't keep it to myself!\nI NEED to tell you more!\n\n")
    time.sleep(3)
    print("So their name is",
          attributes["name"], "and they were born on",
          attributes["birthday"], ".\nBut even more fun is that they are a",
          attributes["species"],
          "! I know! Isn't that fun!? They also have their\nclassic catch-phrase, \"", attributes["saying"],
          "\". Such a classic! Oh and if you ever see them and want to start a conversation,\nTheir hobby is", attributes["hobby"], "!")

    time.sleep(2)
    filename = attributes["name"] + "_data_project_part_4.csv"
    print("Oh there is so much more, especially with different languages!\nI'll write all that info in a new file called", filename, "okay?")
    time.sleep(3)
    df.to_csv(filename)
    print("Okay I wrote it! Have a great day! :)")


def display_options():
    print("Please insert a number coorilating to the stat you want to view")
    print("1\tname\n2\tbirthday\n3\tspecies\n4\tsaying\n5\thobby")
    while True:
        user_input = input("I'd like to know ___! ")
        try:
            if(int(user_input) > 0 and int(user_input) < 6):
                return user_input
        except:
            print("I'm so sorry! Please input a valid number! :)")
            continue


def get_vil_id():
    while True:
        vil_id = input(
            "Currently there are 391 villagers in the ACNH api. Please enter a valid id (1-391) ")
        try:
            if int(vil_id) > 0 and int(vil_id) < 392:
                return int(vil_id)
        except:
            continue


print("Hi! My name is Isabelle! I am a character in Animal Crossing New Horizons!\nAnd I made this so you can research different villagers that can be on your island!")

vil_id = get_vil_id()
attribute = display_options()
get_vil(vil_id, attribute)
