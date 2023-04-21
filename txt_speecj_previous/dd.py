# Import the necessary libraries
import pyttsx3

# Define the engine
engine = pyttsx3.init()

# Set the input text and language code
input_text = "Hello, how are you?"

language_code = "en" # for English
# language_code = "bn" # for Bengali

# Set the voice parameters
voices = engine.getProperty('voices')
for voice in voices:
    if language_code in voice.languages[0] if voice.languages else []:
        engine.setProperty('voice', voice.id)
        break

# Set the audio parameters
engine.setProperty('rate', 150) # you can adjust the speaking rate
engine.setProperty('volume', 1) # you can adjust the volume

# Synthesize the speech
engine.say(input_text)
engine.runAndWait()

# Save the output to a file
engine.save_to_file(input_text, 'output.mp3')
engine.runAndWait()
print('Audio content written to file "output.mp3"')
