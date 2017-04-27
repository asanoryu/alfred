# -*- coding: utf-8 -*-

#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
from vocabulary import print_debug,print_error
import pyaudio
import wave
import sys

BING_API_KEY ='14cd961449e146448fa63338717ac552'
# obtain audio from the microphone
def get_audio_input(r):
    
    with sr.Microphone() as source:
        
        r.adjust_for_ambient_noise(source)
        print("audio input>>>")
        audio = r.listen(source)
        
    return audio

def bing_recog(audio,r):
    try:
        bing_res =  r.recognize_bing(audio, key=BING_API_KEY)
    except sr.UnknownValueError:
        print_error( "Bing could not understand audio")
        return False
    except sr.RequestError as e:
        print_error( "Sphinx error; %s" % str(e))
        return False
    return bing_res
    
def sphx_recog(audio,r):
    try:
        sphx_res =  r.recognize_sphinx(audio,language='en-US')
    except sr.UnknownValueError:
        print_error( "Sphinx could not understand audio")
        return False
    except sr.RequestError as e:
        print_error( "Sphinx error; %s" % str(e))
        return False
    return sphx_res
        
def google_recog(audio,r):
    try:
        
        googl_res =r.recognize_google(audio)
    except sr.UnknownValueError:
        print_error("Google Speech Recognition could not understand audio")
        return False
    except sr.RequestError as e:
        print_error("Could not request results from Google Speech Recognition service; {0}".format(e))
        return False
    return googl_res
    
        
def speech_recog():
    r = sr.Recognizer()
    
    r.energy_threshold = 1500
        #r.phrase_time_limit = 2
        #r.phrase_timeout = 2
    r.pause_threshold = 0.8
    #r.timeout = 5
    try:
        aud_inp = get_audio_input(r)
    except OSError,e:
        print_debug('timed out %s' % str(e))
    except Exception,e:
        print_error('on getting audio %s' % str(e))
        return False
    print_debug('Got audio...replaying trying sphx recog')
    #play_audio(aud_inp)
    res = sphx_recog(aud_inp,r)
    if not res:
        print_debug('shpx failed trying bing')
        res = bing_recog(aud_inp,r)
        if not res:
            return False
    return res
    
    # recognize speech using Google Speech Recognition
   


class AudioFile:
    chunk = 1024

    def __init__(self, file):
        """ Init audio stream """ 
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True
        )

    def play(self):
        """ Play entire file """
        data = self.wf.readframes(self.chunk)
        while data != '':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()

# Usage example for pyaudio
def play_audio(audio):
    a = AudioFile(audio)
    a.play()
    a.close()

    
    