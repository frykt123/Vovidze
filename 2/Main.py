import vk
import tokenFile
import time



token = tokenFile
session = vk.Session(token.value)
api = vk.API(session)
friends = api.friends.get()
friends_info = api.users.get(user_ids=friends)
geolocation = []
photosCompleted = 0
js_code = ""

print('')
print("Геолокация ВК фото.")
print('Друзей: ' + str(len(friends)))


for id in friends:
        try:
            albums = api.photos.getAlbums(owner_id=id)
            time.sleep(0.5)
            print('Обрабатываем id <' + str(id) + '>')
            for album in albums:
                try:
                    print('Пытаемся получить фото из альбома...')
                    photos = api.photos.get(owner_id=id, album_id=album['aid'])
                    print('Обрабатываем фотографии альбома ' + str(album['aid']) + ' пользователя ' + str(
                        api.users.get(user_id=id)))

                    for photo in photos:

                        if 'lat' in photo and 'long' in photo:
                            print('')
                            print('||||Есть фото с геометкой |||')
                            print('')
                            geolocation.append((photo['lat'], photo['long'], photo['src_big'], photo['pid']))
                            photosCompleted += 1

                    time.sleep(0.5)
                except:
                    print('Что-то не так с фото, пропускаем.')
                    pass
        except:
            print('////////////////////////////////////////')
            print('Поймали блок от ВК, пробуем снова')
            print('////////////////////////////////////////')



for loc in geolocation:
    js_code += '\nvar marker' + str(
    loc[3]) + ' = new google.maps.Marker({position: {lat: %s, lng: %s}, map: map});\n' % (loc[0], loc[1])
    js_code += '\n marker' + str(loc[3]) + '.addListener("click", function() {infowindow.setContent("<img src=' + str(
    loc[2]) + '>"' + ');infowindow.open(map, marker' + str(loc[3]) + ');});'
    html = open('map.html').read()
    html = html.replace('/* PLACEHOLDER */', js_code)
    f = open('VKPhotosGeoLocation.html', 'w')
    f.write(html)
    f.close()

print('')
print('==========================================')
print('Работа программы завершена. Собрали ' + str(photosCompleted) + ' фото. ')














