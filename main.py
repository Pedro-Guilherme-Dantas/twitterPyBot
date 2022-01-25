import tweepy
import nasapy
import urllib.request
from datetime import date

def main():
    # APOD download
    today = str(date.today())
    api = nasapy.Nasa(key="")
    information_dict = api.picture_of_the_day(today, hd=True)

    url = information_dict["url"]
    media_type = information_dict["media_type"]
    description = information_dict["title"]

    # Tweet post
    twitter_api_key = ''
    twitter_api_secret_key = ''
    twitter_acess_key = ''
    twitter_acess_secret = ''
    twitter_auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret_key)
    twitter_auth.set_access_token(twitter_acess_key, twitter_acess_secret)

    twitter_api = tweepy.API(twitter_auth)
    if media_type == "video":
        twitter_api.update_status("Astronomy Picture of the Day:\n"+description+"\n"+url)
    else:
        urllib.request.urlretrieve(url,"your-project-directory/apod.jpg")
        media = twitter_api.media_upload("your-project-directory/apod.jpg")
        twitter_api.update_status(status="Astronomy Picture of the Day:\n"
            +description, media_ids=[media.media_id])

# exec
main()