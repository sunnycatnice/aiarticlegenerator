import openai

class myArticles:
    #Like a constructor
    # def __init__(self, title):
    #     self.title = title
        # self.author = author
        # self.date = date
        # self.url = url

    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    #The __str__() function controls what should be returned when the class object is represented as a string.
    def __str__(self):
        return "Title: " + self.title 
    
    @staticmethod
    def get_articles(article_content):
        print ("ARTICLE REWRITTEN...")
        response = openai.Completion.create(
        model="text-davinci-001",
        prompt="Riscrivi il seguente articolo usando parole diverse:" + article_content,
        temperature=0.4,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        
        #extract the text from the response
        text = response['choices'][0]['text']
        
        # #save the text to a file
        file = open("output.txt", "w+")
        file = file.write(text)
        
        #print the content of output.txt
        print("\n" + text)