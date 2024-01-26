# Hourly Pets Twitter

Hourly pets twitter is a Twitter bot, coded in python that posts a picture of a furry friend every hour! Simple as that! Images are grabbed from the [Dog](https://dog.ceo) & [Cat](https://thecatapi.com) API.

This program uses , [tweepy](https://github.com/tweepy/tweepy), asyncio and various other libs to make this project possible!

Twitter page: https://twitter.com/PetsHourly

## Installation & Usage

**It is recommended to create a virtual environment, learn more [here](https://docs.python.org/3/library/venv.html)**

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary packages for this project.

```bash
pip install -r requirements.txt
```
Create a new file named creds.yml, and in the format of.

```yaml
API-KEY: 
API-KEY-SECRET: 
BEARER-TOKEN: 

ACESS-TOKEN: 
ACESS-TOKEN-SECRET: 

OTHER-API-TOKEN: 
```

Put all of your credentials here, the ``OTHER-API-TOKEN`` should be the same as your original API key.
 
Once complete, run the  command

```bash
py main.py
```
And enjoy! I wont provide on how to setup for docker etc.
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


## License

[GNU GPL](https://choosealicense.com/licenses/gpl-3.0/)
