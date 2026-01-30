#Magic8Ball.py
#Name:Talia Astorino
#Date:1/30/2026
#Purpose: Using variables and assignments, numeric data types, arithmetic operators, and type conversion.

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
print("Magic 8 Ball")
answers = [
    "It is certain.",
    "Without a doubt.",
    "It is decidedly so.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Reply hazy, try again.",
    "Concentrate and ask again."
]
  
  #Prompt the user for their question.
question = input("Ask the Magic 8 Ball a question. ")
  #Answer question randomly with one of the options from your earlier list.
answer = random.choice(answers)
print(answer)

if __name__ == '__main__':
  main()
