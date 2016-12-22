import pyowm
import datetime
print("OpenWeatherMap")
owm = pyowm.OWM('66e17093b04397104960767aaed6fb63')
observation = owm.weather_at_place('Rostov-on-Don,ru')
weather = observation.get_weather()
location = observation.get_location()
translate = {'Rostov-on-Don':'Ростов-на-Дону', 'RU':'Россия', 'Rostov-na-Donu':'Ростов-на-Дону'}


def weatherToWord():
    if 0<=weather.get_clouds()<=10:
        return 'ясная'
    if 10<=weather.get_clouds()<=30:
        return 'немного облачная'
    if 30<=weather.get_clouds()<=70:
        return 'пасмурная'
    if 70<=weather.get_clouds()<=100:
        return 'мрачная'

print(owm)
print(weather)
print()
print('Погода в городе ' + translate[location.get_name()] + ' (' + translate[location.get_country()] + ')' +
      ' на сегодня в ' + str(datetime.datetime.now().strftime('%H:%M'))+ ' ' + weatherToWord() + ', облачность составляет ' +
      str(weather.get_clouds()) + '%, давление ' + str(weather.get_pressure()['press']) + ' мм. рт. ст., температура '
      + str(int(weather.get_temperature('celsius')['temp'])) + ' градусов Цельсия, ночью ' +
      str(int(weather.get_temperature('celsius')['temp_min'])) + ', днем ' + str(int(weather.get_temperature('celsius')['temp_max']))  +  ', ветер ' + str(weather.get_wind()['speed']) + ' м.\с.')

