from collections import Counter

"""
Declaring and Counting String Length, Number of Words in String
using Module collections
"""
sentence = "the cat sat on the mat with the rat cat and rat were playing in the mat and the cat was happy with rat on the mat"

print("Sentence is: ",sentence)
print("Length of sentence:", len(sentence))
print("Number of Occurrences of 'cat': ", sentence.count('cat'))
#Split sentence, generating List
words = sentence.split()
print("Words ", words)
print("Type Words: ",type(words))
sentence = "the cat sat on the mat with the rat cat and rat were playing in the mat and the cat was happy with rat on the mat"
print(dict(Counter(sentence)))

from datetime import datetime
import time
