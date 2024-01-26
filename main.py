import logging, tweepy, asyncio, os, random, yaml, pytz
from colorlog import ColoredFormatter
from datetime import datetime
from asyncio import tasks
import helpers.apis

with open("creds.yml") as file:
    config = yaml.safe_load(file)

client = tweepy.Client(config['BEARER-TOKEN'],config['API-KEY'], config['API-KEY-SECRET'], config['ACESS-TOKEN'], config['ACESS-TOKEN-SECRET'])

auth = tweepy.OAuth1UserHandler(
    config['API-KEY'], config['API-KEY-SECRET'], config['ACESS-TOKEN'], config['ACESS-TOKEN-SECRET']
)

api = tweepy.API(auth)

log_formatter = ColoredFormatter(
    "%(log_color)s%(asctime)s - %(levelname)s - %(message)s%(reset)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red',
    }
)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
logger.addHandler(console_handler)



async def upload_twitter_media(file_name: str):
   "Upload media to X/Twitter, once complete. Return a tweepy.Media object."

   try:
     media = api.media_upload(file_name)
     return media
   except Exception as e:
      raise e
    

   

async def run_tweet_process():
    return_with_delay = True

    while True:
      try:
        if return_with_delay:
           await asyncio.sleep(30)
        else:
           await asyncio.sleep(3) # wait a tiny delay, so we dont ratelimit as harder!
           return_with_delay = True
           pass

        # then unpause the thread, continue as normal...
        logger.info("Starting the tweet process! (1/6)")

        function_choices = [
           helpers.apis.call_dog_api,
           helpers.apis.call_cat_api,
        ]

        logger.info("Contacted API, waiting for result. (2/5)")

        function_choice = random.choice(function_choices)
        image_url = await function_choice(config['OTHER-API-TOKEN'])

        logger.info("Contacted API, return sucess. No issues raised (2/5) ✓")
        logger.info("Downloading image... (3/5)")

        download_image = await helpers.apis.download_image(image_url)

        logger.info("Downloaded, no issues raised (3/6) ✓")
        logger.info("Uploading media to twitter... (4/6)")

        upload_media = await upload_twitter_media("save.png")

        logger.info("Uploaded media to twitter, no issues raised (4/5) ✓")
        logger.info("Posting to page, waiting for result. (5/5)")

        est_timezone = pytz.timezone('US/Eastern')
        time_now = datetime.now(est_timezone)
        current_time_12h = time_now.strftime("%I:%M %p")

        post_tweet = client.create_tweet(text=f"Heres your hourly pet picture! 🐶🐈🕒\n\n 🕒Time (EST): {current_time_12h}\n\n 🔗 Image link: {image_url}", media_ids=[upload_media.media_id])

        logger.info("Sucesfully posted to page! (5/5) ✓")
        logger.warn("Restarting wait!...")
      except Exception as e:
        logger.critical(e)
        return_with_delay = False
        continue
          


if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # loop.run_forever(run_tweet_process())
    logger.info("Process has begun. Initalizing the async loop.")
    loop = asyncio.get_event_loop()
    loop.create_task(run_tweet_process())
    logger.info("Process has begun. Initalization sucess. ✓")
    loop.run_forever()
