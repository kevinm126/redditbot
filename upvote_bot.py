import praw
from praw.reddit import Submission
from textblob import TextBlob
reddit = praw.Reddit('bot')
subreddit = reddit.subreddit('BotTown2')
for Submission in subreddit.top(limit = None):
    Submission.comments.replace_more(limit = None)
    print(Submission.title)
    for comment in Submission.comments:
        print(Submission.title)
        blob = TextBlob(comment.body.lower())
        if 'biden' in comment.body.lower():
            commentstr = str(comment.body)
            print(commentstr)
            print('biden = ', blob.sentiment.polarity)
            if blob.sentiment.polarity > 0:
                comment.upvote()
                print('voting up for + biden')
            if blob.sentiment.polarity < 0: 
                comment.downvote()
                print('voting down for - biden')
        if 'trump' in comment.body.lower():
            commentstr = str(comment.body)
            print(commentstr)
            print('trump = ', blob.sentiment.polarity)
            if blob.sentiment.polarity < 0: 
                comment.upvote()
                print('voting up for - trump')
            if blob.sentiment.polarity > 0:
                comment.downvote()
                print('voting down for + trump')

for submission in subreddit.new(limit=None):
            sentence = TextBlob(submission.title.lower())
            if 'biden' in submission.title.lower():
                if sentence.sentiment.polarity > 0:
                    submission.upvote()
                    print(submission.title)
                if sentence.sentiment.polarity < 0: 
                    submission.downvote()
                    print(submission.title)
            if 'trump' in submission.title.lower():
                if sentence.sentiment.polarity < 0: 
                    submission.upvote()
                    print(submission.title)
                if sentence.sentiment.polarity > 0:
                    submission.downvote()
                    print(submission.title)