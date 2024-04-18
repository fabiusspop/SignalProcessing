import numpy as np
import cv2
import soundcard as sc  # Get it from https://github.com/bastibe/SoundCard

imWidth, imHeight = 1024, 512

def draw_wave(screen, mono_audio, xs, title="oscilloscope", gain=5):
    screen *= 0
    ys = imHeight / 2 * (1 - np.clip(gain * mono_audio[0:len(xs)], -1, 1))  # the y values of the waveform
    pts = np.array(list(zip(xs, ys))).astype(np.int)  # pair up xs & ys
    cv2.polylines(screen, [pts], False, (0, 255, 0), thickness=6)  # connect points with lines
    cv2.imshow(title, screen)  # show what we've got

default_mic = sc.default_microphone()
screen = np.zeros((imHeight, imWidth, 3), dtype=np.uint8)  # 3=color channels
xs = np.arange(imWidth).astype(np.int)  # x values of pixels

while True:  # keep looping until someone stops this
    with default_mic.recorder(samplerate=44100) as mic:
        audio_data = mic.record(numframes=1024)  # get some audio from the mic
        draw_wave(screen, audio_data[:,0], xs)  # draw left channel
        key = cv2.waitKey(1) & 0xFF  # keyboard input
        if key == ord('q'):  # if 'q' is pressed
            break
cv2.destroyAllWindows()

