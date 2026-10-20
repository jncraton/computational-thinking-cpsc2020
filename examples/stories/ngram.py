import random
import time

corpus = open('stories.txt').read()

prompt = input("Enter prompt: ")
print(prompt, end="")

while True:
    for n in range(min(20, len(prompt)), 1, -1):
        search_start = random.randrange(len(corpus))
        location = corpus.find(prompt[-n:], search_start)
        
        if location != -1:
            next_char = corpus[location+n]
            prompt += next_char
            print(next_char, end="")
            time.sleep(0.05)
            break
