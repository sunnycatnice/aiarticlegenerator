#!/bin/zsh
#simple script to add to ~/.zshrc and ~/.bashrc the openai key
#make sure to have zsh installed!
#the key is passed as first argument or enter from stdin

#if $1 is empty, the script will ask for the key
if [ -r $1 ]
then
    echo -n "Please enter your OpenAI key: "
    read KEY
else
    KEY=$1
fi

#check if the key is valid, by checking if it starts with sk-
#use a for loop to ask for the key again if it is not valid
while [[ $KEY != sk-* ]]
do
    echo "The key is not valid, please try again"
    echo -n "Please enter your OpenAI key: "
    read KEY
done

if ! grep -q "OPENAI_API_KEY" ~/.zshrc; then
    echo "OPENAI_API_KEY not found in ~/.zshrc, adding it...\n"
    printf "\nexport OPENAI_API_KEY=$KEY" >> ~/.zshrc
    #echo with green color key added!
    echo -e "\e[32mKey added!\e[0m\n"
else
    echo "OPENAI_API_KEY found in ~/.zshrc, make sure to check if it's a functioning key!\n"
fi

if ! grep -q "OPENAI_API_KEY" ~/.bashrc; then
    echo "OPENAI_API_KEY not found in ~/.bashrc, adding it...\n"
    printf "\nexport OPENAI_API_KEY=$KEY" >> ~/.bashrc;
    #echo with green color key added!
    echo -e "\e[32mKey added!\e[0m\n"
else
    echo "OPENAI_API_KEY found in ~/.bashrc, make sure to check if it's a functioning key!\n"
fi

source ~/.zshrc; source ~/.bashrc; exec zsh