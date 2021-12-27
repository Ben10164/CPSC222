import requests  # a library for making http requests

import json
import random
# demonstration of API usage with a trivia serivce
url = "https://opentdb.com/api.php?amount=10&category=28&difficulty=hard"
response = requests.get(url=url)
# print(response.text)

json_object = json.loads(response.text)


# extract and print the questions

results_array = json_object["results"]
for obj in results_array:
    print(obj["question"])  # has a char issue
    # must decode response
    question = requests.utils.unquote(obj["question"])
    if(obj["type"] == "multiple"):
        # use random
        # build up a list of the possible answers
        answers = [obj["correct_answer"]] + obj["incorrect_answers"]
        random.shuffle(answers)
        for answer in answers:
            print("\t" + requests.utils.unquote(answer))
    print("****")
# df.index = pd.todatetime(df.index)
# then use resample

