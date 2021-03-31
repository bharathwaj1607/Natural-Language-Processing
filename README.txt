AUTHOR:
M. Bharathwaj
https://github.com/bharathwaj1607

SUMMARY:
This is a Twitter Sentiment Analysis Project where tweet details of a particular hashtag/trend is scraped and a sentiment analysis is performed to understand the emotion of the tweet.

COMPONENTS:
.env_sample                    : Sample credentials format
settings.py                    : File to load the secret credentials
TwitterSentimentAnalysis.ipynb : Main project file 

WORKFLOW:
1. Setup a Twitter Developer account to fetch personalized access tokens, API keys 
2. Setup an environment variable file to secretly store the keys
3. Create a settings.py file to load the .env file and initialize the credentials
4. In the project file, call the settings.py file to import the keys
5. Three inputs are taken from the user namely:
    Hashtag --> The tweets to be analysed in a particular hashtag/trend
    Timeline --> Date range for which the tweets need to be retrieved
    Tweet count --> Number of tweets to be retrieved for that particular hashtag/trend
6. Once the input is fetched, several parameters such as the username, location, tweet, retweet count etc are extracted, thanks to the Twitter API
7. These parameters are inputted into a dataframe
8. Sentiment Analysis using Natural Lanugage Toolkit's Vader method is implemented to find the polarity score for each tweet
9. Relevant logic is applied to understand the emotion from the compound score
10. For this combination of parameter, the final output displays the percentage of positive and negative sentiment related to the tweets

