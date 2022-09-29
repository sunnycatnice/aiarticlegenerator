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

if ! grep -q "OPENAI_API_KEY" ~/.zshrc; then
    echo "OPENAI_API_KEY not found in ~/.zshrc, adding it...\n"
    echo "export OPENAI_API_KEY=$KEY" >> ~/.zshrc
else
    echo "OPENAI_API_KEY found in ~/.zshrc, check if it's a functioning key...\n"
fi

if ! grep -q "OPENAI_API_KEY" ~/.bashrc; then
    echo "OPENAI_API_KEY not found in ~/.bashrc, adding it...\n"
    echo "export OPENAI_API_KEY=$KEY" >> ~/.bashrc;
else
    echo "OPENAI_API_KEY found in ~/.bashrc, check if it's a functioning key...\n"
fi

source ~/.zshrc; source ~/.bashrc