# import dependencies and 
import numpy as np
import pandas as pd
import matplotlib.pyplot as mpp
import re
import nltk
import demoji

from wordcloud import WordCloud
from matplotlib.pyplot import figure

from sklearn.feature_extraction.text import TfidfVectorizer

"""
Function definitions for text processing
"""

def text_processing(text):
    
    remove_emoji = demoji.replace(text, repl = '')
    remove_tags = r'@[A-Za-z0-9|:|_]+'
    remove_hashtags = r'#[A-Za-z0-9]+'
    remove_RT = r'RT'
    remove_amp = r'&amp'
    remove_links = r'http.+'

    # include - these steps yields the best performance
    text_rtn = remove_emoji
    text_rtn = re.sub(remove_tags, '', text_rtn)
    text_rtn = re.sub(remove_hashtags, '', text_rtn)
    text_rtn = re.sub(remove_RT, '', text_rtn)
    text_rtn = re.sub(remove_amp, '', text_rtn)
    text_rtn = re.sub(remove_links, '', text_rtn)

    return text_rtn.lower().strip()



"""
Function declarations for data visualizations
"""

def word_freq_tfidf(df_text_column):
    
    # use the tfidf vectorizer to get the term frequencies
    vectorizer = TfidfVectorizer(stop_words = 'english')
    vectors = vectorizer.fit_transform(df_text_column)
    
    feature_names = vectorizer.get_feature_names_out()
    term_frequency_list = vectors.todense().tolist()
    
    df_tfidf = pd.DataFrame(term_frequency_list, columns = feature_names)
    
    df_tfidf = df_tfidf.transpose().sum(axis = 1)
    
    return df_tfidf.sort_values(ascending = False)


def word_distribution(feq, num, color, no, figsize, title, xlabel, ylabel, save_name):
    
    feq.head(num).plot(x      = 'tokens',
                       y      = 'frequency',
                       kind   = 'barh', 
                       color  = color, 
                       figsize = figsize).invert_yaxis()
    
    #mpp.figure(no, (width, height))
    mpp.yticks(fontsize = 15)
    mpp.title(title, fontsize = 25, weight = 'bold')
    mpp.xlabel(xlabel, fontsize = 20)
    mpp.ylabel(ylabel, fontsize = 20)
    mpp.savefig(save_name, dpi = 300)
    pass
    
    

def plot_wordcloud(feq, background_color, colormap, max_words, title, no, width, height, save_name):
    wordcloud = WordCloud(width = 3000, 
                          height = 2334, 
                          random_state = 1, 
                          background_color = background_color, 
                          colormap = colormap, 
                          max_words = max_words, 
                          collocations = False,
                          normalize_plurals = False).generate_from_frequencies(feq)

    #fig = mpp.gcf()
    #fig.set_size_inches(15, 10)
    #fig.set_dpi(100)
    mpp.figure(no, (width, height), dpi = 300)
    frame1 = mpp.gca()
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)
    mpp.title(title, fontsize = 16)
    mpp.imshow(wordcloud)
    mpp.savefig(save_name, dpi = 300)
    pass

def topic_wordcloud(topic_model, topic, country, width, height, data_path):
    text = {word: value for word, value in topic_model.get_topic(topic)}
    wc = WordCloud(width = 1500, 
                   height = 1000,
                   background_color = "white", 
                   max_words = 500, 
                  random_state = 1)
    wc.generate_from_frequencies(text)

    mpp.figure(topic, (width, height), dpi = 200)
    frame1 = mpp.gca()
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)
    mpp.imshow(wc, interpolation = 'bilinear')
    mpp.axis('off')

    save_name = data_path + f"/{country}_topic_{str(topic + 1)}.png"
    
    # remember to save the wordcloud!
    mpp.savefig(save_name, dpi = 300)
    #mpp.show()

