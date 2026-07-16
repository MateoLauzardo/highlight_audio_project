import winsound

# function receives a file name and plays the audio file using winsound
def play_audio_from_text(file):
    
    winsound.PlaySound(file, winsound.SND_FILENAME)
    