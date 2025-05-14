import os
from instagrapi import Client

cl = Client()

username = os.getenv("username")
password = os.getenv("password")

cl.login(username, password)

# Follow users from hashtag
hashtag = "gymgear"
medias = cl.hashtag_medias_recent(hashtag, amount=5)

for media in medias:
    cl.media_like(media.id)
    cl.user_follow(media.user.pk)

print("Bot ran successfully.")
