# -*- coding: utf-8 -*-
import time
from termcolor import colored
import pyttsx



def get_timed_greeting():
    hour =  (time.strftime("%H"))
    if int(hour) in range(6,12):
        return 'Good morning , sir'
    elif int(hour) in range(13,17):
        return 'Good afternoon , sir'
    else:
        return 'Good evening , sir'
        
def print_debug(string):
    print colored('<debug>:' + string, 'blue')
    
def print_error(string):
    print colored('<error>' + string, 'red')

def print_alfred(string):
    print colored('Alfred:' + string, 'green')
    alfred_says(string)

        
def alfred_says(string):
    words = string.split(' ')
    try:
        words.remove(',')
    except ValueError:
        pass
    string = ' '.join(words)
    speech_eng = pyttsx.init()
    speech_eng.setProperty('rate',180)
    speech_eng.setProperty('voice', 'english_rp')
    speech_eng.setProperty('age', 100)
    speech_eng.say(string)
    a = speech_eng.runAndWait()
    
def get_2grains(words):
    grains = []
    for idx,word in enumerate(words):
        try:
            grains.append('%s %s' % (word, words[idx + 1]))
        except IndexError:
            #print 'last word. no more 2 grains'
            pass
    return grains

def get_search_q(words, mod=None):
    proto_q = []
    if not mod:
        limiter_words = ['for','is','about','on','me']
    else:
        limiter_words = ['to', 'find', 'wolfram','calculate','plot','for','about','on']

    for idx,word in enumerate(words):
        if word in limiter_words:
            proto_q.append(words[idx+1:])
            
    if type(proto_q[0]) == list:
        real_q = proto_q[-1]
    else:
        real_q = proto_q
    for idx,word in enumerate(real_q):
        if word in ['a','an','the'] and idx == 0:
            real_q.remove(word)
    return ' '.join(real_q)
    

def word_check(wordList,checkList):
    grains = get_2grains(wordList)
    
    if not any(x in wordList for x in checkList):
        return any(x in grains for x in checkList)
    else:
        return any(x in wordList for x in checkList)
 
commands = {
    'greetings': ['hello','hi','good morning','good afternoon','good evening', 'hey', 'hola', 'oi'],
    'courtesy' : ['how are', 'sup'],
    'farewells' : ['bye','see you','see you','later','goodbye','cya','cyas'],
    'search' : ['find', 'search for','get me', 'what is', 'who is','tell me','you know'],
    'thanks' : ['thanks','thank you', 'much obliged'],
    'joke' : ['joke', 'funny','something funny','jokes'],
    'introduction' : ['i am', 'my name'],
    'wolfram' : ['wolfram','plot','calculate', 'science database', 'batcomputer' ]
}

responses = {
             
    'greetings' : ['Hello , sir','How can I help , sir?', get_timed_greeting()],
    'courtesy' : ['Quite well , sir', 'Fine , thank you for asking','Could be better , but could be worse'],
    'farewells' : ['Goodbye , sir', 'See you later','Farewell , sir'],
    'affirmitive' : ['Yes , sir', 'Quite', 'Indeed', 'Got it', 'Affrimitive'],
    'negative' : ['No , sir','Negative'],
    'thanks' : ['You are quite welcome , sir', 'My pleasure','Anytime', 'Of course'],
    'joke' : [ 'Sir, may I suggest you try to avoid landing on your head?', 
    'A gentleman is one who never hurts anyone\'s feelings unintentionally',
              'Why did the sword swallower swallow an umbrella?\nHe wanted to put something away for a rainy day!',
              'I don\'t make jokes. I just watch the government and report the facts.',
              'Jesus fed 5,000 people with two fishes and a loaf of bread. That\'s not a miracle. That\'s tapas',
              'Standing in the park, I was wondering why a Frisbee gets larger the closer it gets. Then it hit me.',
              'I needed a password eight characters long so I picked Snow White and the Seven Dwarfs.',
              'I went to buy some camouflage trousers the other day but I couldn\'t find any.',
              'I\'m on a whiskey diet. I\'ve lost three days already.'
              ]
}

excuses = ['I didn\'t get that', 'Excuse me , sir?','I don\'t know how to do that sir', 'I don\'t know what you mean']

startworking = ['Right away , sir','I am on it , sir','Of course','Let me see what I can do']

workdone = ['Here is what I got , sir', 'Task is finished', 'This is what I found']

already_did = ['I did that not so long ago', 'I just told you that', 'Again , sir?', 
'That is fun - let\'s just do the same thing all day']