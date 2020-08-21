import praw
import pandas as pd
import sys

reddit = praw.Reddit(client_id='FehZ4evVDDabHA', client_secret='slhHkZ41KAVPgCWmE3181-885g4', user_agent='AITAClassifier')
aita = reddit.subreddit('AmITheAsshole')

postLimit = 1000
posts = []

# Get top posts
for post in aita.top("all",limit=postLimit):
    if post.num_comments and post.link_flair_text in ["Not the A-hole","Asshole"]:
        posts.append([post.title,post.selftext,post.link_flair_text])


# Get top posts
for post in aita.controversial("all",limit=postLimit):
    if post.num_comments and post.link_flair_text in ["Not the A-hole","Asshole"]:
        posts.append([post.title,post.selftext,post.link_flair_text])

posts = pd.DataFrame(posts,columns=['title', 'text', 'status'])
posts.to_csv("aitaPosts.csv",index=False)