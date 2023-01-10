from help_utils import *

import hashlib
import requests

import pandas as pd

from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
from flask import Flask, make_response
from datetime import date, datetime, timezone

from xml.dom import minidom
import xml.etree.ElementTree as ET

def extract_date():
    dt = datetime.now()
    dt = dt.replace(tzinfo=timezone.utc)
    dt = dt.strftime("%a, %d %b %Y %H:%M:%S %z")
    return dt

def extract_blog():
    URLO = "https://www.ons.gov.uk/economy/economicoutputandproductivity/output/articles/ukeconomylatest/2021-01-25"
    
    CLS = ['Date','Title','Link','Description','GUID']
    DFO = pd.DataFrame(columns=CLS)
    dt = extract_date()
    
    RESP=requests.get(URLO)
    HTML=RESP.text

    SOUP = BeautifulSoup(HTML, "lxml")
    ARTS = SOUP.find_all("div", {"class": "section__content--markdown section__content--markdown--neutral-article"})

    for ART in ARTS:
        if len(ART) > 1:

            tt = ART.select('h2,h3')

            if tt:
                tt = tt[0].text 

                try:
                    lk = ART.find_all('a', href=True)[-2]
                    lk = lk.get('href')
                except:
                    lk = None

                ds = ART.text

                gd = 'guid{0}'.format(tt)
                gd = str(int(hashlib.sha256(gd.encode('utf-8')).hexdigest(), 16) % 10**8 + 1)
                
                row = [dt, tt, lk, ds, gd]
                DFR = pd.DataFrame([row], columns=CLS)
                DFO = pd.concat([DFO,DFR], axis=0)
                
    DFO = DFO.reset_index(drop=True).copy()
    return DFO

def transform_feed():
    fg = FeedGenerator()
    fg.title('UK Economy RSS')
    fg.description('RSS feed capturing updates to the ONS UK Economy blog')
    fg.link(href='https://github.com/tdrgregw/sandbox_actions/blob/main/misc/rss/test_rss.xml')
    #fg.image(url_for('static', filename='icon.png'))

    DFO = extract_blog()
    for index, row in DFO.iterrows():
        fe = fg.add_entry()
        
        fe.title(row.Title)
        fe.description(row.Description)
        fe.link(href=str(row.Link))
        
        fe.guid(row.GUID, permalink=False)
        fe.pubDate(row.Date)
        fe.author(name="Gregory Weegenaar", email="Gregory.Weegenaar@tdrcapital.com")

    XML = fg.rss_str()
    XML = XML.decode("utf-8")
    return XML

def transform_xml(XML):
    TREE = ET.ElementTree(ET.fromstring(XML))
    ROOT = TREE.getroot()
    XMLO = minidom.parseString(ET.tostring(ROOT)).toprettyxml(indent="   ")
    return XMLO

def load_feed():
    XMLR = transform_feed()
    XMLO = transform_xml(XMLR)
    with open('misc/rss/UK_economy_rss.xml', 'w', encoding = 'utf-8') as f:
        f.write(XMLO)

    