import speech_recognition
import time
import pyttsx3
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
engine = pyttsx3.init() 

RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()

def display_face(image):
    image = Image.open(image).convert('1')
    disp.image(image)
    disp.display()


while True:
    # print("Input option you want:")
    # x = input()
    # print(x)

    robot_ear = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        robot_ear.adjust_for_ambient_noise(mic, duration = 1)
        print("Robot: I'm Listening")
        # audio = robot_ear.listen(mic)
        audio = robot_ear.listen(mic)
    print("Uhmm.....")

    # try:
    #     print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    # except sr.UnknownValueError:
    #     print("Sphinx could not understand audio")  
    # except sr.RequestError as e:
    #     print("Sphinx error; {0}".format(e))
    
    try:
       you = robot_ear.recognize_google(audio, key="AIzaSyDW6GXZXssJ0X93wj-ptokIxzbittAq3IY")
    except:
       you = ""
       print("You:" + you)

    if you =="hello":
        image = "sad-face.png"
    elif you == "fun":
        image = "happy-face.png"
    elif you == "":
        image = "happy-face.png"
    elif you == "today":
        image = "face_ID.png"
    elif you == "bye":
        break
    else:
        image = "I'm fine thank you and you"

    display_face(image)
    engine.say(you)
    engine.runAndWait()
