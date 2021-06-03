import speech_recognition as sr
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki


listener = sr.Recognizer()

speaker = pyttsx3.init()

""" RATE"""
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 150)

va_name = 'Mr.Bot'


def speak(text):
    speaker.say(text)
    speaker.runAndWait()


speak("I'm " + va_name + " Tell me your what you want, master ")


def take_command():
    command = ""
    try:

        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if va_name in command:
                command = command.replace(va_name + ' ', '')

    except:
        print("Check your Microphone")
        speak("Pardon me master! I didn't get you. Could you please repeat it again???")
    return command



while True:
    user_command = take_command()
    if 'quit' in user_command or 'close' in user_command or 'shut up' in user_command:
        speak("See you again master. I'll be there when ever you call me")
        break

    elif 'time' in user_command:
        current_time = dt.datetime.now().strftime("%I:%M %p")
        speak(current_time)
        
    elif 'play' in user_command:
        user_command = user_command.replace('play ','')
        speak("Yes master! Playing "+user_command+ ', enjoy master.')
        pk.playonyt(user_command)
        break

    elif 'search for' in user_command or 'google' in user_command:
        user_command = user_command.replace('search for ','')
        user_command = user_command.replace('google ', '')
        speak('Yes master! Searching for'+ user_command)
        pk.search(user_command)
        
    elif 'who is' in user_command or 'what is' in user_command:
        user_command = user_command.replace('who is ','')
        user_command = user_command.replace('what is ','')
        info = wiki.summary(user_command, 2)
        speak(info)
        
    elif 'who are you'in user_command:
        speak("I'm "+va_name+", your virtual assistant, master. Tell me what you want, master")
        
    else:
        speak("Pardon me master! I'm unable to answer your question since it's outta my reach")

