from flask import Flask, render_template

import feedparser
import validators

from time import mktime
from datetime import datetime
import locale

app = Flask(__name__)

locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

@app.template_filter('convertTime')
def convertTime(timeVar):
    return (datetime.fromtimestamp(mktime(timeVar))).strftime("%d. %B %Y")

@app.route("/")
@app.route("/feeds")
def displayRSS():
    fileHandler = open("urls.txt", "r")
    sites = [feedparser.parse(x) for x in sorted(fileHandler.readlines()) if validators.url(x)]
    fileHandler.close()

    # try: 
    #   parse aus config file vars wie feedCount
    #   am besten wohl mit configparser https://docs.python.org/3/library/configparser.html
    # expect:
    #   wenn Fehler dann returne den halt
    #   return Excepetion
    #   Excepation as e
    #   return "Fehler du Depp: "+e

    # LEGACY Version - only entries, no site names etc.
    # feedCount = 2
    # counter = 0
    # feedEntries = []
    # for site in sites:
    #     while (counter < feedCount) and (counter < len(site.entries)):
    #         feedEntries.append(site.entries[counter])
    #         counter += 1
    #     counter = 0
    #     feedEntries.append("BREAKER")
    # return render_template('feeds.html', feedEntries=feedEntries)

    feedCounter = 3
    counter = 0
    feeds = {}
    for site in sites:
        feeds[site.feed] = []
        while (counter < feedCounter) and (counter < len(site.entries)):
            feeds[site.feed].append(site.entries[counter])
            counter += 1
        counter = 0

    return render_template('feeds.html', feeds=feeds)


@app.route("/impressum")
def displayImprint():
    return render_template('impressum.html', title="Impressum")