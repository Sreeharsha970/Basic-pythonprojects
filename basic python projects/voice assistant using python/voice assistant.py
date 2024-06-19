import speech_recognition as sr   #speech recognition and web browser are the modules
                                  # sr means aliyas name 
import webbrowser               # webbrowser is used to search in webbrowser


sr.Microphone(device_index=1)   

r=sr.Recognizer()           #recognizer is used to record the talk it passes to r


r.energy_thresold=500  

with sr.Microphone() as source:    # if microphone as source print speak
    print("speak")                 #mike work means it will speak
    audio=r.listen(source)         #we sended source to microphone the source will converted 
                                   # to audio format like mp3
    try:
        text= r.recognize_google(audio)  # audio changes to text ,we have to change
        print("you said : {}".format(text)) 
        url='http://www.google.co.in/search?q=' # url condition pass 
        search_url=url+text                    #google.com+text
        webbrowser.open(search_url)             #assign to search url variable
    except:
        print("can't recognize")
        
        
        
            


