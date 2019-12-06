# import SentimentIntensityAnalyzer class 
# from vaderSentiment.vaderSentiment module. 

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 

df =pd.read_csv('Datasource.csv', encoding ="latin-1")
df.columns

for sentence in df.Reviews:
    
    print('\n',sentence)
    # Create a SentimentIntensityAnalyzer object. 
    sid_obj = SentimentIntensityAnalyzer() 
        
    # polarity_scores method of SentimentIntensityAnalyzer 
    # oject gives a sentiment dictionary. 
    # which contains pos, neg, neu, and compound scores. 
    sentiment_dict = sid_obj.polarity_scores(sentence)
    #print(sentiment_dict) 
    
    
    #print("Overall sentiment dictionary is : ", sentiment_dict) 
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 
        
    print(" Sentence Overall Rated As", end = " ") 
    
    Positive_text = " "
    
    # decide sentiment as positive, negative and neutral 
    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")
        
    elif sentiment_dict['compound'] <= - 0.05 :
        print("Negative") 
    
    else : 
       print("Neutral")




