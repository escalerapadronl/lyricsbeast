from bs4 import BeautifulSoup
import requests as req

url = req.get('http://www.popvortex.com/music/charts/top-rap-songs.php')
soup = BeautifulSoup(url.content, 'lxml')

chart_wrapper = soup.find('div', class_="chart-wrapper")


count = 1
song_details = {
    'title': '',
    'artist': ''
}
for child in chart_wrapper.children:
    song_box = chart_wrapper.find_all('div', id="chart-position-" + str(count))
    count += 1
    for song in song_box:
        song_info = song.find_all('p', class_='title-artist')
        for song in song_info:
            song_title = song.find("cite", class_='title')
            song_artist = song.find('em', class_='artist')
            song_details['title'] = song_title.text
            song_details["artist"] = song_artist.text
print(song_details)







