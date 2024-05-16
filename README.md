# Political Troll Tweets Analysis

#### -- Project Status: [Completed]

## Project Intro/Objective

We perform exploratory data analysis on Russian, Chinese and Indonesian information operations, to uncover the trolls' tradecraft and modus operandi against a target populace. This analysis wil enable intelligence and security entities to recognize and disrupt trolls waging information warfare.

<p align="center">  
    <img src="https://github.com/QuekJingHao/political-troll-tweets-analysis/blob/main/2_Misc/logo.png" width="300" height="300">
</p>

### Methods Used
* Inferential Statistics
* Data Visualization

### Technologies
* Python
* Pandas, BERTopic
* Jupyter 
* Azure ML Studio

## Project Description

Information warfare (_information / influence operations / IO_) is defined as the collection of data, and circulation of propaganda to gain strategic advantage over an adversary. The most notible aspect of such operations is the dissemination of disinformation, to exploit existing societal grievances and divisions. These methods aim to sow discord and distrust, influence the population's beliefs and manipulate public perception, steering the messes toward a direction beneficial to the adversary.

With the success of the Russian Internet Research Agency (IRA) in meddling with the US presidential election of 2016, other state actors are learning of this success and slowly, incorporate IO tradecraft. Given the proliferation of IO, it is pertinent that the defense community learn to detect, disrupt and dismantle IO that seeks to forment socio-politcal change. This area is a core tenant of counterintelligence work. 

In this project, we will exploit several open-source datasets available in the Information Operations Archive (IOA). We will conduct  exploratory data analysis (EDA) on three countries, namely Russia, China and Indonesia. The series of EDA notebooks is an example of data-driven intelligence analysis, enabling intelligence and security agencies to recognize and disrupt trolls waging information warfare on social media platforms.



## Details of Project

This section will first go over the structure of the repository and the project. 

The EDA notebooks are located in ```3_Notebooks/eda/```. The directory contains the following files:

1. data sampling/: contains the Jupyter notebook and Python scripts to sample the very huge (~5GB) datasets to form the sample dataset for analysis
2. eda/: contains ```CN.ipynb, RU.ipynb, IND.ipynb``` eda notebooks. It also contains all of the plots and charts for each of the three analyses

The raw datasets are not included in this repository.

Next, we will summarize the key steps in the project:

1. Data Understanding
2. Data Preparation
3. Modelling and Evaluation


### 1. Data Understanding

Datasets for each of the countries are downloaded from the Information Operations Archive, which can be accessed through:

https://transparency.twitter.com/en/reports/moderation-research.html

This archive that is a result of Twitter's concerted effort to disclose disinformation and social engineering campaigns. For this project, we have selected the following datasets for our analysis:

Russia:

1. Russia_GRU_Feb_2021.csv
2. Russia_IRA_Feb_2021.csv
3. Russia_IRA_Oct_2018.csv
4. Russia_Jan_2019.csv
5. Russia_May_2020.csv


China:

1. China_Changyu_Culture_Dec_2021.csv
2. China_May_2020.csv
3. China_S1_Aug_2019.csv
4. China_S2_Aug_2019.csv
5. China_S3_Sept_2019.csv
6. China_Xinjiang_Dec_2021.csv


Indonesia:

1. Indonesia_Feb_2020.csv

Due to the sheer size of the datasets, we will only take a random sample of the tweets for China and Russia.


#### Dataset Field Descriptions

Each of the IOA datasets contain 30 columns. The field descriptions can be found in the Dataset Readme of each of the disclosed repositories. We will present the list here:

<pre>
* tweetid - tweet identification number
* userid - user identification number (anonymized for users which had fewer than 5,000 followers at the time of suspension) 
* user_display_name - the name of the user (same as userid for anonymized users)
* user_screen_name - the Twitter handle of the user (same as userid for anonymized users)
* user_reported_location - the user's self-reported location (*)
* user_profile_description - the user's profile description (*)
* user_profile_url - the user's profile URL (*)
* follower_count - the number of accounts following the user (*)
* following_count - the number of accounts followed by the user (*)
* account_creation_date - date of user account creation
* account_language - the language of the account, as chosen by the user
* tweet_language - the language of the tweet
* tweet_text - the text of the tweet (mentions of anonymized accounts have been replaced with anonymized userid)
* tweet_time - the time when the tweet was published (UTC)
* tweet_client_name - the name of the client app used to publish the tweet
* in_reply_to_tweetid - the tweetid of the original tweet that this tweet is in reply to (for replies only)
* in_reply_to_userid - the userid of the original tweet that this tweet is in reply to (for replies only)
* quoted_tweet_tweetid - the tweetid of the original tweet that this tweet is quoting (for quotes only)
* is_retweet - True/False, is this tweet a retweet
* retweet_userid - for retweets, the userid who authored the original tweet
* retweet_tweetid - for retweets, the tweetid of the original tweet
* latitude - geo-located latitude, if available 
* longitude - geo-located longitude, if available 
* quote_count - the number of tweets quoting this tweet
* reply_count - the number of tweets replying to this tweet
* like_count - the number of likes that this tweet received (^)
* retweet_count - the number of retweets that this tweet received (^)
* hashtags - a list of hashtags used in this tweet
* urls - a list of urls used in this tweet
* user_mentions - a list of userids who are mentioned in this tweet (includes anonymized userids)
* poll_choices - if a tweet included a poll, this field displays the poll choices separated by |

(*) - at the time of suspension
(^) - these engagement counts exclude engagements from users who are suspended, deleted or otherwise actioned against by Twitter at the time of this data release
</pre>


### 2. Data Preparation

This section we will go over some of the key steps in the ```/data sampling``` methodology.

For Russia and China, we want to pick a half a random sample of the entire combined dataframe. We will only select tweets whereby the ```tweet_language == 'en'``` and randomly shuffle the dataframe before exporting out. We also perform some fundamental data cleaning steps, such as:

1. Remove emoji
2. Remove tags
3. Remove hashtags
4. Remove "amp"
5. Remove links


### 3. Modelling and Evaluation

We will summarize the key data aggregation steps used in the EDA notebooks.

In each of the three notebooks, we perform the following analysis:

1. Determine Earliest and Latest Records Tweets
2. Determine Earliest and Latest Account Creation Times
<<<<<<< HEAD
3. Calculate account statistics
=======
3. Exploring User Display Names
4. Exploring User Reported Locations
5. Calculate Proportion of Retweets
6. Calculate Account Statistics
7. Plot Number of Accounts Created against Time
8. Plot Number of Tweets Generated against Time
9. Generate Wordcloud from Hashtags Corpus
10. Generate Wordcloud from Profile Description Corpus
11. Topics Evolution
12. Plot Top 10 Most Frequently Used Words
13. Topic Modelling
>>>>>>> beb8d3d (Changed readme)



## **Summary of Analysis**

From the intelligence gathered in the three notebooks, we summarize our analysis here.

### **Russia**

Russian information operations display a great depth of sophistication in exploiting known societal grievance, to manipulate the populace against one another. This can be seen in the vast number of topics and angles that the trolls exploited to achieve this goal. The tweets spew by the trolls show a great depth of understanding and mastery of existing sensitive topics, issues and social grievances of the US populace. The trolls are able to impersonate individuals with conflicting beliefs, and pit them against one another. Broadly speaking, the aim of Russian information operations is to spread distrust, sow hatred and inflame tensions within the US society, in an attempt to confuse and polarise the populace further.


### **China**

Chinese information operations display a precise, focused and concerted effort in just issue - Xinjiang. In particular, the denial of human rights abuses in Xinjiang. The Chinese operations appear to attack international critics of the harsh treatments of Uyghurs, by justifying that these measures are in a attempt to stop or prevent terrorism, and separatism from taking place in China. They deny these allegations and decry their critics to stop spreading rumors about Xinjiang. The operatives often justify their actions as counterrorist in nature, combating religious extremism and separatism. The operatives simultaneously paints Xinjiang as a region whose populace is joyful, happy and fulfilled, and decry any western criticism as fabrications and rumor.



### **Indonesia**

Indonesian operations appear to only target the West Papua separatist movement. In particular, the Indonesian operation seem to post pro-government narratives on West Papua. This is an effort on the part of the government, to strengthen its claims on West Papua, and weaken the separatist movement. The operatives often highlight and emphasize the efforts by the Indonesian government to improve the lifes and welfare West Papuans - such as through improving infrastructure, conservation of its rainforests, installing electricity, increasing the amount of imports into the region, and rasing the socio-economic status of West Papuans.



## Featured Deliverables

This last section presents the plots and charts for each of the countries

### 1) Number of Accounts Created against Time




### 2) Number of Tweets Generated Created against Time




### 4) Word Frequency Plot





### 5) Profile Description Wordcloud




### 6) Hashtags Wordcloud




### 7) Topics Evolution



### 8) Examples of Topics Exploited





