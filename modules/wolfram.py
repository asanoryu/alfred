# -*- coding: utf-8 -*-

import wolframalpha
from StringIO import StringIO
import urllib
from PIL import Image
from vocabulary import print_alfred
import io



APP_ID = 'GWAQXT-H7K2GRUURP'

def load_image(url):
    #print url
    fd = urllib.urlopen(url)
    image_file = io.BytesIO(fd.read())
    im = Image.open(image_file)
    im = im.resize((1366,768),Image.ANTIALIAS)

    im.show()
    
def get_wolfram_alpha(q):
    client = wolframalpha.Client(APP_ID)
    res = client.query(q)
   # if res.results:
    #    print_alfred(next(res.results).text)
   
    try:
        for pod in res.pods:
            if pod['@title'] == 'Result':
                print_alfred(pod.text)
            elif pod['@title'] == 'Plots':
                load_image(pod['subpod'][0]['img']['@src'])
            elif pod['@title'] == 'Plot':
                load_image(pod['subpod']['img']['@src'])
    except AttributeError:
        print_alfred('I am sorry but I couldn\'t find anything about it,sir')
        
            
        #print '-' * 60

