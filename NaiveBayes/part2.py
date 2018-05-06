

import pandas
import string

#import my csv file
df = pd.read_csv('unsmile.csv')

#Remove any rows with a "nan" in them
df = df.dropna(axis=0, how = 'any')

#Make it so that any non readable text gets converted into nothing
def removetext(text):
    return ''.join([i if ord(i) < 128 else '' for i in text])

#Here I am doing the actual removing
df['text'] = df['text'].apply(removetext)

#Make all my texts lower case
df['text'] = df['text'].apply(lambda x: x.lower())

#Get rid of all weird punctuation and extra lines
df['text'] = df['text'].apply(lambda x: x.replace('.',' '))
df['text'] = df['text'].apply(lambda x: x.replace('\n',' '))
df['text'] = df['text'].apply(lambda x: x.replace('?',' '))
df['text'] = df['text'].apply(lambda x: x.replace('!',' '))
df['text'] = df['text'].apply(lambda x: x.replace('"',' '))
df['text'] = df['text'].apply(lambda x: x.replace(';',' '))
df['text'] = df['text'].apply(lambda x: x.replace('#',' '))
df['text'] = df['text'].apply(lambda x: x.replace('&amp',' '))
df['text'] = df['text'].apply(lambda x: x.replace(',',' '))

#Here I get each unique keyword from my dataframe
array = df['text'].str.split(' ', expand=True).stack().value_counts()
#print(array) to see what this looks like

#I make a dataframe of the words and the frequency with which the words appear 
d = {'word': array.index, 'frequency':array}
df2 = pd.DataFrame(data = d)

#I get rid of any words that are mentioned less than 10 times
df2['frequency'] = df2['frequency'][df2['frequency'] > 10] 

#Remove any rows with a "nan" in them
df2 = df2.dropna(axis=0, how = 'any')

#Drop any obvious signs of these words being :(
df2 = df2.drop([':(','https://t',':((', ':(((', ':((((', ':(((((', ':', '(', ''])

#Convert my dataframe into a csv file
df2.to_csv('unsmile_words.csv', header=True, index=False, encoding='utf-8')




