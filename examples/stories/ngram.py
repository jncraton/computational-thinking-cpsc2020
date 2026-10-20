import random

corpus = open('stories.txt').read()

prompt = input("Enter prompt: ").strip() + " "

while True:
    for n in range(min(20, len(prompt)), 1, -1):
        location = corpus.find(prompt[-n:], random.randrange(len(corpus)))
        
        if location != -1:
            prompt += corpus[location+n:].split()[0] + " "
            print(prompt.split()[-1] + " ", end="")
            break
