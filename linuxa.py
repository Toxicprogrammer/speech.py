import speech_recognition as sr
import webbrowser as wb
import os
import speak


sr.Microphone(device_index=4)
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

r = sr.Recognizer()

with sr.Microphone() as source:
    print ('linuxa is listening!')
    audio = r.listen(source)
    print ('Done!')
    text = r.recognize_google(audio,language='en-GB')
    print('Linuxa thinks you said:\n' + text)
    lang = 'en'

    speak.tts(text, lang)
    if "search" in text:
        f_text1 = 'https://www.google.co.in/search?q=' + text
        wb.get(chrome_path).open(f_text1)
    if "play" in text:
        f_text = 'https://www.youtube.com/results?search_query=' + text
        wb.get(chrome_path).open(f_text)
    if "system open PPT" in text:
       f_text2 = 'https://prezi.com/view/BxntnMYgksJ7tiJCnyAc/' 
       wb.get(chrome_path).open(f_text2)
    if "system open CMD" in text :
        command='cmd'
        os.system(command)
    if "system open Turbo C" in text :
        os.startfile('C:/Users/sagar jain/Desktop/TurboC.exe.lnk')
    if "system open RC" in text :
        os.startfile('c:/Program Files/R/R-3.5.1/bin/x64/Rgui.exe')
    if "open KBC" in text :
        os.startfile('F:/gaming/GAMESzone/New Games/sagar/Games/KBC.EXE')
