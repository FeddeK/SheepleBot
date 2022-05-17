import os
import praw
from keep_alive import keep_alive
# from replit import db

phrase = "sheeple"
reply = "wAkE uP sHeEpLe!!!111 🐑"

reddit = praw.Reddit(
  client_id = os.environ['client_id']
  ,client_secret = os.environ['client_secret']
  ,username = os.environ['username']
  ,password = os.environ['password']
  ,user_agent = "<SheepleBot>"
)

def clean_string(raw_string):
  cleaned_string = raw_string.lower()
  return cleaned_string

class RedditBot:
  def __init__(self):
    pass
    # if len(db) == 0:
    #   pass
    # else:
    #   print("Pulling from DB")

  def find_match(self, comment):
    if phrase in clean_string(comment.body):
      if comment.author != "Sheeple_Bot":
        self.make_reply(comment)

  def make_reply(self, comment):
    try:
      comment.reply(reply)
      print(comment.reply, comment.author)
    except Exception as e:
      print(e)

keep_alive()
subreddit = reddit.subreddit("all")
bot = RedditBot()

for comment in subreddit.stream.comments(skip_existing=True):
  bot.find_match(comment)