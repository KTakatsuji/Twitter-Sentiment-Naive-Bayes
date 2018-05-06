
import pandas as pd

#import my csv files
happy = pd.read_csv('happy_words.csv')
sad = pd.read_csv('sad_words.csv')
unsmile = pd.read_csv('unsmile_words.csv')
fun = pd.read_csv('fun_words.csv')


wordbag = pd.concat([happy,sad,unsmile,fun]).drop_duplicates(subset = 'word').reset_index(drop=True)

print(wordbag)

wordbag.to_csv('wordbag.csv')

