import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


x=0
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[x].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def audio():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if '' in command:
                print(command)
    except:
        pass
    return command

talk('Hellow sir, i am your virtual assistant, you can name me of your choice and call so')

#name = "papa"
#with sr.Microphone() as source:
#    talk('name me..')
#    voice = listener.listen(source)
#    command = listener.recognize_google(voice)
#    command = command.lower()
talk('name me..')
#audio()
name = audio()
print(name)
talk('wow... you named me '+ name +' that is so nice...')

talk('am i a boy, or, a girl')
#audio()
gender = audio()
if 'boy' in gender:
  x=0
  talk('wow you mean i am male... that is good')
elif 'girl' in gender:
  x=1
  talk('wow you mean i am female... that is awesome')

talk('hello boss... this is' + name + '... how can i help you')

def take_command():
    try:
        with sr.Microphone() as source:
            print('i am listening you...')
            talk('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if name in command:
                command = command.replace(name,"")
                print(command)
    except:
        pass
    return command

def run_VA():
    command = take_command()
    if "play" in command:
        song = command.replace("play","")
        talk("playing" + song)
        print("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('now its' + time)
    elif "tell me about" in command:
        subject = command.replace("tell me about", "")
        info = wikipedia.summary(subject,3)
        print(subject)
        print(info)
        talk(info)
    elif 'who am i' in command:
        print('Praveen Shiva Shankara Doss')
        talk('You are my boss, mr.Praveen Shiva Shankara Doss , im am so proud of you , you are a genious,'
             'you are such an amazing person, i am proud to be your assistant , i can do anything for you , what can i do for you ,'
             'I can even die for your words , you are my god ')
    elif 'who are you' in command:
        print(name)
        talk('i am' + name + ', the virtual assistant, developed by you, i can chat with you, and do some things to assist you,'
             'and make your work eazy, i am under developement')
    elif 'stop listening' in command:
        exit()
    else:
        print('Could not understand')
        talk('Sorry, i could not understand that please repeat')


while True:
    run_VA()
