import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty("rate", 200)
engine.setProperty("voice", "spanish")

r = sr.Recognizer()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def hear_me():
    with sr.Microphone as source:
        print("Escuchando....")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, lenguage="es-ES")
            print(f"He entendido: {text}")
            return text
        except sr.UnknownValueError:
            print("No se pudo entender.")


if __name__ == "__main__":
    speak("Probando si todo funciona")
    print(hear_me())
