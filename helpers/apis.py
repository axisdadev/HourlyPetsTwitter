import aiohttp, asyncio

class CantCallAPI(Exception):
    "Unable to call the API of choice."

async def call_dog_api(auth: str):
    # The most simplest method! Somehow...
    url_to_call = "https://dog.ceo/api/breeds/image/random"

    try:
     async with aiohttp.ClientSession() as session:
        async with session.get(url_to_call) as response:
           if response.status == 200:
            response = await response.json()
            return response['message']
           else:
              raise CantCallAPI
    except Exception as e:
       raise e


async def call_cat_api(auth: str):
    # A bit more complicated, indeed
    url_to_call = f"https://api.thecatapi.com/v1/images/search?api_key={auth}"

    try:
     async with aiohttp.ClientSession() as session:
        async with session.get(url_to_call) as response:
           if response.status == 200:
              response = await response.json()
              return response[0]['url']
           else:
              raise CantCallAPI
    except Exception as e:
       raise e

async def download_image(url: str):
   try:
      async with aiohttp.ClientSession() as session:
         async with session.get(url) as response:
            if response.status == 200:
               content = await response.read()

               with open("save.png", "wb+") as f:
                  f.write(content)
            else:
               raise CantCallAPI
   except Exception as e:
      raise e
   
call_dog_api_v = call_dog_api
call_cat_api_v = call_cat_api