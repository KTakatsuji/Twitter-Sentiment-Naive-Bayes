# Twitter-Sentiment-Naive-Bayes
Twitter Sentiment Analysis using Naive Bayes

You can follow the explanation for my code on my medium: https://medium.com/@koshut.takatsuji/twitter-sentiment-analysis-with-full-code-and-explanation-naive-bayes-a380b38f036b

Also check out my personal site: koshu.me

This program can be followed by going through part1 through part6 sequentially. 

But as a whole the general steps I take to complete this project are:
1. Get a twitter API and download Tweepy to access the twitter api through python
2. Download twitter tweet data depending on a key word search “happy” or “sad”
3. Format my tweets so that no capitalization, punctuation, or non ascii characters are present, as well as splitting the tweet into an array holding each word in a separate holder
4. Create a bag of common words that appear in my tweets
5. Create a frequency table of words that have positive and negative hits
6. Test my frequency table by using test sentences
