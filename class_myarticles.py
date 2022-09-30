from numpy import number
import random
import openai

class myArticles:
    # Like a constructor
    def __init__(self):
        self.article_folder = "./articles/"
        self.article_file = "articles.json"
    
    # The __str__() function controls what should be returned when the class object is represented as a string.
    def __str__(self):
        return "Title: " + self.title 
    

    def get_articles(self, article_content):
        print ("ARTICLE REWRITTEN...")
        response = "test"
        # response = openai.Completion.create(
        # model="text-davinci-001",
        # prompt="Riscrivi il seguente articolo usando parole diverse:" + article_content,
        # temperature=0.4,
        # max_tokens=64,
        # top_p=1,
        # frequency_penalty=0,
        # presence_penalty=0
        # )
        
        #extract the text from the response
        # text = response['choices'][0]['text']
        text = response
        
        # Save the text to a file
        rnd_num = random.randint(11111, 55553)
        file = open(self.trimmed_title_underscored + str(rnd_num) + "_out.txt", "w+")
        file = file.write(text)
        
        # Print the content of output.txt
        print("\n" + text)
    
    # Just to keep truck
    title = ""
    trimmed_title = ""
    trimmed_title_underscored = ""
    content = ""
    article_folder = ""
    article_file = ""