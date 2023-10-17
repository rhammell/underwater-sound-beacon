import time
import board
import audiobusio
import audiocore

# Audio output object
audio = audiobusio.I2SOut(board.D24, board.D25, board.A3)

# Define sound to play
sound = '3_meters'

# Open sound wave file
wave_file = open('sounds/' + sound + '.wav', 'rb')
wave = audiocore.WaveFile(wave_file)

# Main loop
while True:
    # Play selected sound
    print("Playing:", sound)
    audio.play(wave)

    # Delay
    time.sleep(5)