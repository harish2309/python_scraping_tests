# importing the module
import praw
import pandas as pd
from praw.models import MoreComments

# initialize with appropriate values
client_id = "dqHADFw_G-EtzxEmkD2qKA"
client_secret = "kyyU_NVszMxRX1-0ApAGMba7niMTtQ"
username = "Windows_Insiders"
password = "<enter pass>"
user_agent = "based app by /harish"

# creating an authorized reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

subreddit = reddit.subreddit("random")

df = pd.DataFrame([vars(post) for post in subreddit.hot(limit=5)])

df = df[["title", "score", "url"]]

df.to_csv('csv_file', index=False, encoding='utf-8')

datas = pd.read_csv("csv_file")
print(datas.to_string())
