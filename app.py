from flask import Flask, request, render_template
from enum import Enum
from datetime import datetime, date
import csv
app = Flask(__name__)

filename='SongOfTheDay.csv'
class Indices(Enum):
    song_name=0
    date_released=1
    album_name=2
    band_name=3
    song_link=4
    album_link=5
    date_to_publish=6
song_data = {}
last_date_checked = date.today()
def reload_song_data(filename):
    print("reading file data")
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            publish_date = row[Indices.date_to_publish.value]
            if publish_date == date.today().strftime('%Y-%m-%d'):
                print("found song")
                song_data['song_name'] = row[Indices.song_name.value]
                song_data['date_released'] = row[Indices.date_released.value]
                song_data['album_name'] = row[Indices.album_name.value]
                song_data['band_name'] = row[Indices.band_name.value]
                song_data['song_link'] = row[Indices.song_link.value]
                song_data['album_link'] = row[Indices.album_link.value]
                return
reload_song_data(filename)
@app.route("/")
def hello_world():
    global last_date_checked
    if(date.today() != last_date_checked):
        print("reloading date date")
        reload_song_data()
        last_date_checked = date.today()
    return render_template('index.html', 
    song_name = song_data['song_name'], 
    release_year = song_data['date_released'][:4],
    date_released = song_data['date_released'], 
    album_name = song_data['album_name'], 
    band_name = song_data['band_name'], 
    song_link = song_data['song_link'], 
    album_link = song_data['album_link'])

