
import os

basedir = os.path.abspath(os.path.dirname(__file__))


WEATHER_DEFAULT_CITY = "Kazan,Russia"
WEATHER_API_KEY = " a2186766ba0d4e1d918161740191712"
WEATHER_URL ='http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = 'postgres://KiDD:LearnPython2020@threedshare.c2ki110jyhpp.us-west-2.rds.amazonaws.com:5432/learnPython'