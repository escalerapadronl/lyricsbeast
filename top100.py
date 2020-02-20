from bs4 import BeautifulSoup
import requests as req
import csv
import pandas as pd

url = req.get('http://www.popvortex.com/music/charts/top-rap-songs.php')
soup = BeautifulSoup(url.content, 'lxml')

chart_wrapper = soup.find('div', class_="chart-wrapper")

def collect_data():
    count = 1
    song_details = {
        'title': [],
        'artist': []
    }

    for child in chart_wrapper.children:
        song_box = chart_wrapper.find_all('div', id="chart-position-" + str(count))
        count += 1
        for song in song_box:
            song_info = song.find_all('p', class_='title-artist')
            for song in song_info:
                song_title = song.find("cite", class_='title')
                song_artist = song.find('em', class_='artist')
                song_details['title'].append(get_only_title(song_title.text.lower()))
                song_details["artist"].append(get_first_artist(song_artist.text.lower()))

    df = pd.DataFrame(song_details)
    df = df.drop_duplicates()
    df.to_csv("songinfo.csv")

def remove_spaces():
    song_no_spaces = {
        'title': [],
        'artist': []
    }
    with open("songinfo.csv", "r+") as csv_file:
        writer = csv.reader(csv_file)
        for row in writer:
            song_no_spaces['title'].append(row[1].replace(" ", ""))
            song_no_spaces['artist'].append(row[2].replace(" ", ""))

        df = pd.DataFrame(song_no_spaces)
        df.to_csv("songinfonospaces.csv")

def get_only_title(original_title):
        temp_title = ""
        for i in original_title:
            if i == "(":
                return temp_title
            else:
                temp_title = temp_title + i
        return temp_title

def get_first_artist(original_artist):
    temp_artist = ""
    for i in original_artist:
        if i == ",":
            return temp_artist
        else:
            temp_artist = temp_artist + i
    return temp_artist

def get_only_letter(title, artist):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

def main():
    collect_data()
    remove_spaces()

main()
