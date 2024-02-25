import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()
    print("Welcome to RobotSpeaker Created by Reekparna")
    while True:
        x = input("Enter what do you want me to say (enter 'q' to quit): ")
        if x == "q":
            break
        engine.say(x)
        engine.runAndWait()



