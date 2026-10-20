import random

corpus = open('stories.txt').read()

prompt = input("Enter prompt: ").strip() + " "

while True:
    for n in range(min(20, len(prompt)), 1, -1):
        search_start = random.randrange(len(corpus))
        location = corpus.find(prompt[-n:], search_start)
        
        if location != -1:
            next_word = corpus[location+n:].split()[0] + " "
            prompt += next_word
            print(next_word + " ", end="")
            break
