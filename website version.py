#install libraies 
pip install flask wikipedia
!pip install wikipedia
import wikipedia
import time

#search for page/show results
while True:
    request = str(input("what do you want to learn about now? :"))
    print(" ")
    try:
        summary = wikipedia.summary(request)
        time.sleep(3)
        print(summary)
        print(" ")
        print("keep in mind although it is rare incorrect information can come out of this so whilst this is enough to give you an idea about a subject and can start you off with research take this information as a grain of salt snd do your own research")
    except:
        print("something went wrong. this is usually because nothing can be found on wikipedia, try using one word/simple querys or just go on wikipedia yoursellf. im sorry we couldnt help you")
    print(" ")
    time.sleep(3)