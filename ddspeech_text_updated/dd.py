import pyttsx3

# Define the engine
engine = pyttsx3.init()

# Read the input text from a file
with open('input.txt', 'r') as f:
    input_lines = f.readlines()
input_text = ' '.join(input_lines)

# Set the language code
language_code = "en" # for English
# language_code = "bn" # for Bengali

# Set the voice parameters
voices = engine.getProperty('voices')
for voice in voices:
    if language_code in voice.languages:
        if 'female' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
else:
    engine.setProperty('voice', voices[0].id)

# Set the audio parameters
engine.setProperty('rate', 170) # you can adjust the speaking rate
engine.setProperty('volume', 2) # you can adjust the volume

# Synthesize the speech
engine.say(input_text)
engine.runAndWait()

# Save the output to a file
engine.save_to_file(input_text, 'output.mp3')
engine.runAndWait()
print('Audio content written to file "output.mp3"')
