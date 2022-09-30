# simple python progam using openai to rewrite web articles using GPT-3
# using python 3.10

import os
import openai
import json
import pandas as pd
from class_myarticles import myArticles

openai.api_key = os.getenv("OPENAI_API_KEY")

print(openai.api_key)

#string to indicate the article folders
article_folder = "./articles/"

#write a function to read articles.json, article by article and append to a string
def read_articles():
    art_count = 1
    with open(article_folder + "articles.json") as f:
        d = json.load(f)
        articles = d["articles"]
    #loop through articles and append to a string
    for article in articles:
        print(articles[article]["title"])
        title = articles[article]["title"]
        print(articles[article]["content"])
        content = articles[article]["content"]
        #open content and read the file in it
        with open(article_folder + content) as f:
            content = f.read()
            print(content)
        
        current_article = myArticles(title, content)
        current_article.get_articles(content)
        
        #print a prompt to ask the user if he wants to proceed with other articles
        while True:
            proceed = input("Do you want to proceed with other articles? (y/n): ")
            if proceed == "y":
                art_count += 1
                break
            elif proceed == "n":
                return
            else:
                print("Invalid input. Please try again")
            
            
      
read_articles()

print ("file saved!")
