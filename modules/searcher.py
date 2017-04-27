# -*- coding: utf-8 -*-

import duckduckgo as ddg
import urllib2 
from bs4 import BeautifulSoup

import re
import requests
from termcolor import colored

def google_scrape(q):
    #url
    url = 'http://www.google.com/search'
    
    #Parameters in payload
    payload = { 'q' : q, 'start' : '0' }
     
    #Setting User-Agent
    my_headers = { 'User-agent' : 'Mozilla/11.0' }
     
    #Getting the response in an Object r
    r = requests.get( url, params = payload, headers = my_headers )
    
    #Read the reponse with utf-8 encoding
    #print( r.text.encode('utf-8') )
    return BeautifulSoup( r.text,'html.parser')
    

def google_pretty_print(soup):
    print '-'*30

    gclasses = soup.find_all('div', class_='g')
    
   
    for div in gclasses:
        
        try:
            h3 = div.find('h3', class_='r')
            span = div.find('span', class_='st')
            
            print colored('\t' + re.sub('<[^<]+?>', '', span.text),'yellow')            
            print '\t\t' + re.search('url\?q=(.+?)\&sa', h3.a['href']).group(1) 
            print '-'* 15
        except:
            continue
    #End





def ddg_rel_search(q):
    try:
        return ddg.query(q)
    except urllib2.URLError:
        print 'Alfred: There is a problem connecting to search engine'

    
def ddg_pretty_print(res):
    if type(res) != ddg.Results:
        return False
        
    if len(res.related) == 0:
        print colored('Alfred: There are no related topics this','green')
        return
    print '-' * 30
    print colored('Related topics','green')
    print ' '
    for r in res.related[:10]:
        
        print colored('\t' + r.text,'yellow')
        print '\t\t' + r.url
        
        