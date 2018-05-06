

import pandas as pd
import numpy as np

ftable = pd.read_csv('ftable.csv')
ftable = ftable[ftable['word'] != 'sad']
ftable = ftable[ftable['word'] != 'sad,']
ftable = ftable[ftable['word'] != ':(']
ftable = ftable[ftable['word'] != 'fun']
ftable = ftable[ftable['word'] != 'happy,']
ftable = ftable[ftable['word'] != 'happy']
ftable = ftable.drop_duplicates(subset = 'word')

test = 'i dont know what to do anymore'
positive_instance = 24070.0
negative_instance = 23930.0

#split all the words in my text
test_words = test.split()

prob_positive = float(positive_instance/(positive_instance+negative_instance))
prob_negative = 1 - prob_positive

pos_word = 1.0*prob_positive
neg_word = 1.0*prob_negative
for i in range(len(test_words)):
    word = test_words[i]
    #print(word)
    index_val = ftable.index[ftable['word'] == word]
    if (len(index_val) > 0):
        #print(index_val[0])
        pos_val = ftable['positive'].iloc[index_val[0]]
        neg_val = ftable['negative'].iloc[index_val[0]]
        pos_word = pos_word * pos_val/positive_instance
        neg_word = neg_word * neg_val/negative_instance
        
if pos_word > neg_word:
    print("The sentence was POSITIVE, with a probability of")
    print(pos_word/(pos_word+neg_word))
else:
    print("The sentence was NEGATIVE, with a probability of")
    print(neg_word/(pos_word+neg_word))

#print(pos_word)
#print(neg_word)



