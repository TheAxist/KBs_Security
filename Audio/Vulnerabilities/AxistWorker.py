

from gtts import gTTS


text = "Fixes include:

Network fix:
Can stop attacks with proper egrees filtering. The string has to go to a command and control center and reach out to download malware and continue running."


# Create a gTTS object
tts = gTTS(text, lang='en')
tts.save("Log4J.mp3")

print("The mp3 file has been created.")

