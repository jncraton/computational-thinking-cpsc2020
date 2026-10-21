---
reading: '[N-gram](https://en.wikipedia.org/wiki/N-gram)'
teaching_goal: Students will understand n-grams and use string methods to build a simple character n-gram model.
learning_objectives:
  - Define n-grams (unigrams, bigrams, trigrams)
  - Use string slicing to extract n-grams from a corpus
  - Use string.count to calculate frequencies
  - Build a generative model that predicts the next character
---

# Exploring Natural Language

## Exercise

[Simon Says](https://open.kattis.com/problems/simonsays)

## TinyStories

> a synthetic dataset of short stories that only contain words that a typical 3 to 4-year-olds usually understand

- [TinyStories: How Small Can Language Models Be and Still Speak Coherent English?](https://arxiv.org/abs/2305.07759)
- [19MB validation set download](https://huggingface.co/datasets/roneneldan/TinyStories/resolve/main/TinyStories-valid.txt)

## Reading the File

```python
corpus = open('stories.txt').read()
```

## String Method Exploration

- [str.count](https://docs.python.org/3/builtins/stdtypes.html#str.count)
- [str.split](https://docs.python.org/3/builtins/stdtypes.html#str.split)
- [str.lower](https://docs.python.org/3/builtins/stdtypes.html#str.lower)

## N-gram

- A sequence of n adjacent symbols
- Symbols can be letters, words, or phonemes
- Collected from a text corpus

## Types

- Unigram: size 1
- Bigram: size 2
- Trigram: size 3

## Example

- Corpus: "banana"
- Bigrams: "ba", "an", "na", "an", "na"

## Frequency

- N-grams are often analyzed by frequency
- Higher frequency suggests higher probability
- Used in predictive text and speech recognition

## Example

- "the" is a very common word unigram
- "of the" is a common word bigram

---

[Google Books N-grams](https://books.google.com/ngrams/graph)

## String Slicing

- Use slicing to extract n-grams
- `text[i:i+n]` gets a substring of length n

## Example

```python
text = "banana"
n = 2

for i in range(len(text) - n + 1):
    print(text[i:i+n])
```

## Counting

- Use `string.count()` to find occurrences

## Example

```python
text = "banana"
print(text.count("an"))
```

## Exercise

Create a program that takes a string and prints all bigrams

## Solution

```python
text = input("Enter a string: ")

for i in range(len(text) - 1):
    print(text[i:i+2])
```

## Building a Model

- A model maps a prefix to a set of possible next characters
- We can use string methods to find all occurrences of a prefix
- For each occurrence, identify the character that follows

## Generative Model

- A generative model predicts the next character
- It chooses the most frequent character following a prefix

## Example

- Prefix: "ba"
- Corpus: "banana", "bandana"
- Next characters: "n", "n"
- Prediction: "n"

## Simplified Approach

- Storing and training a model requires data structures that we have not used yet
- We can take a non-parametric approach by simply looking for an occurrence of an n-gram starting from a random position in the corpus

## Final Exercise

Create a program that generates a sequence of characters based on a corpus and a starting prefix

## Solution
