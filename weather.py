import requests
from bs4 import BeautifulSoup
import datetime


class Weather:

  def __init__(self, city):
    self.city = city
    self.url = f"https://www.weathersa.co.za/?city={self.city}"
    self.html = requests.get(self.url).content
    self.soup = BeautifulSoup(self.html, 'html.parser')

  def today(self):
    # creating url and requests instance

    # getting raw data

    today = {
      "City":
      self.city,
      "Current Date":
      datetime.datetime.now().strftime("%A, %d %B %Y"),
      "Current Time":
      datetime.datetime.now().strftime("%H:%M"),
      "Current Temp":
      self.soup.find('span', attrs={
        'class': 'celsi'
      }).text + self.soup.find('sup', attrs={
        'class': 'celsius'
      }).text.strip(),
      "Description":
      self.soup.find('div', attrs={
        'class': 'describ'
      }).text,
      "Humidity":
      self.soup.find('span', attrs={
        'class': 'pull-right humiditySide'
      }).text,
      "Min Temperature":
      self.soup.find('span', attrs={
        'class': 'pull-right minSide celsi'
      }).text,
      "Max Temperature":
      self.soup.find('span', attrs={
        'class': 'pull-right maxSide celsi'
      }).text,
      "Weather Condition":
      self.soup.find('span', attrs={
        'class': 'pull-right cloudiSide'
      }).text,
      "Wind Speed":
      self.soup.find('span', attrs={
        'class': 'pull-right windSpeedSide'
      }).text.replace('\xa0 | \xa0', '').strip(),
      "Wind Direction":
      self.soup.find('span', attrs={
        'class': 'pull-right windDirecSide'
      }).text,
      "Rain Amount":
      self.soup.find('span',
                     attrs={
                       'class': 'pull-right PrecipitationAmountSide'
                     }).text,
      "Rain Probability":
      self.soup.find('span',
                     attrs={
                       'class': 'pull-right PrecipitationPropabilitySide'
                     }).text.strip(),
      "Sunrise":
      self.soup.find('span', attrs={
        'class': 'pull-right sunriseSide'
      }).text.replace('/', '').strip(),
      "Sunset":
      self.soup.find('span', attrs={
        'class': 'pull-right sunsetSide'
      }).text
    }

    return today  #pd.DataFrame(today).transpose()

  def forecast(self):
    forecast = [{
      "day":
      self.soup.find('h4', attrs={
        'class': f'cday-{num}'
      }).text,
      "icon":
      self.soup.find('a', attrs={
        'class': f'icon-{num}'
      }).text,
      "description":
      self.soup.find('a', attrs={
        'class': f'description-{num}'
      }).text,
      "humidity":
      self.soup.find('a', attrs={
        'class': f'humidity-{num}'
      }).text + ' %',
      "minimum":
      self.soup.find('a', attrs={
        'class': f'min-{num}'
      }).text,
      "maximum":
      self.soup.find('a', attrs={
        'class': f'max-{num}'
      }).text,
      "cloud cover":
      self.soup.find('a', attrs={
        'class': f'cloudi-{num}'
      }).text,
      "wind direction":
      self.soup.find('a', attrs={
        'class': f'windDirec-{num}'
      }).text,
      "wind speed":
      self.soup.find('a', attrs={
        'class': f'windSpeed-{num} km/h'
      }).text,
      "rain probability":
      self.soup.find('a', attrs={
        'class': f'precipitationPropability-{num}'
      }).text + ' %',
      "rain amount":
      self.soup.find('a', attrs={
        'class': f'precipitationAmount-{num}'
      }).text + ' mm',
      "visibility":
      self.soup.find('a', attrs={
        'class': f'visibility-{num}'
      }).text,
      "sunrise":
      self.soup.find('a', attrs={
        'class': f'sunrise-{num}'
      }).text,
      "sunset":
      self.soup.find('a', attrs={
        'class': f'sunset-{num}'
      }).text,
    } for num in range(0, 6)]

    return forecast


# city = Weather('Pretoria')
# print(city.today())
