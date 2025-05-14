from instagrapi import Client

username = "grindsupplygear"
password = "Maxwell2011"

cl = Client()
cl.login(username, password)

# Follow users from a hashtag
hashtag = "gymgear"
medias = cl.hashtag_medias_recent(hashtag, amount=5)

for media in medias:
    cl.media_like(media.id)
    cl.user_follow(media.user.pk)

print("Bot ran successfully.")