# simple python progam using openai to rewrite web articles using GPT-3
# using python 3.10

import os
import openai
import json
from class_myarticles import myArticles

openai.api_key = os.getenv("OPENAI_API_KEY")

#print green color
print("\033[92m" + "Welcome to the article rewriter\n")

if(openai.api_key == None):
    print("\033[91m" + "--------------------- ERROR ----------------------")
    print("Please set the OPENAI_API_KEY environment variable.")
    print("--------------------------------------------------" + "\033[0m\n")
    exit(1)

print("---------------------------- OPENAI KEY ----------------------------")
print("Your OpenAI Key: " + openai.api_key)
print("--------------------------------------------------------------------\n" + "\033[0m")

#write a function to read articles.json, article by article and append to a string
def read_articles():
    art_count = 1
    myarticle = myArticles()
    
    with open(myarticle.article_folder + myarticle.article_file) as f:
        d = json.load(f)
        articles = d["articles"]

    #loop through articles and append to a string
    for article in articles:
        print(articles[article]["title"])
        title = articles[article]["title"]
        print(articles[article]["content"])
        content = articles[article]["content"]

        #open content and read the file in it
        with open(myarticle.article_folder + content) as f:
            content = f.read()
            print(content)
        
        # Fill data in the class
        myarticle.title = title
        myarticle.trimmed_title = title[:10]
        myarticle.trimmed_title_underscored = myarticle.trimmed_title.replace(" ", "_")
        myarticle.content = content
        
        myarticle.get_articles(content)
        
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

print ("End!")
