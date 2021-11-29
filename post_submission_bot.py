import random
import praw
import time
reddit = praw.Reddit('bot')
subreddit = reddit.subreddit("politics")

for i, submission in enumerate(subreddit.top(limit = 300)):
    reddit.subreddit("BotTown2").submit(title = submission.title,url=submission.url)
    reddit.validate_on_submit = True
    print(submission.title)
    print("i =" ,i)
    time.sleep(50)
