import speech_recognition as sr
from googletrans import Translator

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Please speak clearly into the microphone...")
        recognizer.adjust_for_ambient_noise(source)
        
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=60)

    try:
        print("Recognizing speech...")
        speech_text = recognizer.recognize_google(audio)
        print(f"You said: {speech_text}")
        return speech_text
    except sr.UnknownValueError:
        print("Sorry, I did not understand the speech.")
        return None
    except sr.RequestError:
        print("Sorry, I couldn't request results from the speech recognition service.")
        return None

def translate_text(text):
    translator = Translator()
    try:
        # Translating to French
        translated = translator.translate(text, dest='fr')
        print(f"Translated Text (French): {translated.text}")
        return translated.text
    except Exception as e:
        print(f"An error occurred during translation: {e}")
        return None

def main():
    while True:
        # Ask if user wants to continue or exit
        user_input = input("Press '1' to stop the program, or any other key to continue: ")

        if user_input == '1':
            print("Exiting program...")
            break  # Exit the loop and stop the program

        # Continue to recognize and translate speech
        speech_text = recognize_speech_from_mic()

        if speech_text:
            translated_text = translate_text(speech_text)
            if translated_text:
                print(f"Final Translated Text: {translated_text}")
            else:
                print("Translation failed.")
        else:
            print("No speech recognized to translate.")

if __name__ == "__main__":
    main()
