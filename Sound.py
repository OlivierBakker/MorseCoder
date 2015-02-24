import os


class Beep():

    def play_dit(self):
        os.system('paplay Sounds/dit.wav')

    def play_dah(self):
        os.system('paplay Sounds/dah.wav')
