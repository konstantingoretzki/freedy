from flask import Flask, render_template

import feedparser
import validators

from time import mktime
from datetime import datetime
import locale

app = Flask(__name__)

# needed for changing months to German for date entries
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

# custom filter for getting the published_date in the following format: 1. September 2018
@app.template_filter('convertTime')
def convertTime(timeVar):
    return (datetime.fromtimestamp(mktime(timeVar))).strftime("%d. %B %Y")

@app.route("/")
@app.route("/feeds")
def displayRSS():
    fileHandler = open("config/urls.txt", "r")
    sites = [feedparser.parse(x) for x in sorted(fileHandler.readlines()) if validators.url(x)]
    fileHandler.close()

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
    
    # TODO: Get vars from config file using configparser 
    # Change for desired amount of post showed from one site
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
    # TODO: Add full-fledged GDPR imprint
    return render_template('impressum.html', title="Impressum")
