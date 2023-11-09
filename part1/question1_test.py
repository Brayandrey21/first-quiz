from question1 import get_city_weather

def test_get_city_weather():

  assert get_city_weather("Quito") == "19° degrees and humidity"

  assert get_city_weather("New York") == "13° degrees and cloudy"
