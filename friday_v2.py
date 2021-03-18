import speech_recognition as sr
import os
from playsound import playsound
import webbrowser
import random

speech = sr.Recognizer()

greeting_dict = {'hello': 'hello', 'hi': 'hi'}
open_launch_dict = {'open': 'open', 'launch': 'launch'}
social_media_dict = {'facebook': 'https://www.facebook.com', 'twitter': 'https://www.twitter.com'}

mp3_greeting_list = ['mp3/Friday/greeting_accept.mp3',
                     'mp3/Friday/greeting_accept_2.mp3']  # Yes Mr Mild // How can I help you sir
mp3_open_launch_list = ['mp3/Friday/open_1.mp3']


def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)


def read_voice_cmd():
    voice_text = ''
    print('Listening...')
    with sr.Microphone() as source:
        audio = speech.listen(source=source, timeout=10, phrase_time_limit=5)
    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print('Network error.')
    except sr.WaitTimeoutError:
        pass

    return voice_text


def is_valid_note(dict, voice_note):
    for key, value in dict.items():
        try:
            if value == voice_note.split(' ')[0]:
                return True
                break
            elif key == voice_note.split(' ')[1]:
                return True
                break
        except IndexError:
            pass
    return False


if __name__ == '__main__':

    playsound('mp3/Friday/greeting.mp3')  # Hello Sir. This is your Artificial Intelligence Friday

    while True:

        voice_note = read_voice_cmd().lower()
        print('cmd : {}'.format(voice_note))

        if is_valid_note(greeting_dict, voice_note):
            print('In greeting...')
            play_sound(mp3_greeting_list)
            continue
        elif is_valid_note(open_launch_dict, voice_note):
            print('In open...')
            play_sound(mp3_open_launch_list)
            if(is_valid_note(social_media_dict, voice_note)):
                key = voice_note.split(' ')[1]
                webbrowser.open((social_media_dict.get(key)))
            else:
                os.system('explorer C:\\ {}'.format(voice_note.replace('open ', '').replace('launch ', '')))
        elif 'bye' in voice_note:
            exit()
