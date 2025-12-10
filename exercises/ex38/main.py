import requests
import selectorlib
from datetime import datetime
import sqlite3

connection = sqlite3.connect("data.db")

URL = "https://programmer100.pythonanywhere.com/"

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temp"]
    return value

def store(extracted):
    now =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temps VALUES(?,?)", (now, extracted))
    connection.commit()

scraped = scrape(URL)
extracted = extract(scraped)
store(extracted)
print(extracted)
