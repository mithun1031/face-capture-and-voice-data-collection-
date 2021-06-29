from typing import Text
from gtts import gTTS
import os
import time
import speech_recognition as sr


def recognize():
    final = dict()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        myText = ("can you please say your name")
        language = 'en'
        output = gTTS(text=myText, lang=language, slow=False)
        output.save("name.mp3")
        os.system("start name.mp3")
        time.sleep(3)
        print('name listening.....')

        audio = r.listen(source)

        try:

            text= r.recognize_google(audio)

            print('you said: {}'.format(text))

        except:
            print('sory not recg')
        time.sleep(1)

        myText = ("contact number")
        language = 'en'
        output = gTTS(text=myText, lang=language, slow=False)
        output.save("contact.mp3")
        os.system("start contact.mp3")
        time.sleep(3)
        print('contact listening.....')

        audio = r.listen(source)

        try:

            contact= r.recognize_google(audio)
            print('you said: {}'.format(contact))

        except:
            print('sory not recg')
        ''.join(contact)
        # print(contact)
        final['contact'] = contact
        final['name']  = text
        return final

        
        

        



