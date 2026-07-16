from transformers import pipeline
import scipy.io.wavfile
import numpy as np


# reliable neural TTS that runs on Windows via the transformers pipeline.
# (swapped from gepard-1.0, which needs vLLM and doesn't run cleanly on Windows.)
pipe = pipeline("text-to-speech", model="facebook/mms-tts-eng")


# SECTION - function to read clipboard content and pass it to AI agent
def make_audio_from_text(text):

    # Generate speech from text
    audio = pipe(text)

    # the model gives raw sound numbers, sometimes shaped like [[...]].
    # np.squeeze flattens that to a plain 1-D list of samples scipy can save.
    samples = np.squeeze(audio["audio"])

    # saved audio file
    scipy.io.wavfile.write(
        "output.wav",
        rate=audio["sampling_rate"],   # how fast to play the samples
        data=samples,                  # the raw sound numbers
    )
