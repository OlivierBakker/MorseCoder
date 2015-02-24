import Sound
import time
from Coder import MorseCode, MorseParser, InvalidCodeError


class MorseTester():

    def __init__(self):
        self.sound = Sound.Beep()

    def play_morse(self, morse_code):

        for x in morse_code:
            for letter in x:

                if letter == '.':
                    self.sound.play_dit()
                elif letter == '-':
                    self.sound.play_dah()
                elif letter == '|':
                    time.sleep(0.7)
                else:
                    time.sleep(0.1)

    def test(self, input_morse, template_morse):

        return_bool = False
        print(input_morse, template_morse)

        if input_morse == template_morse:
            return_bool = True

        return return_bool


in_msg = 'hallo'
mc = MorseCode(string_rep=in_msg)
mt = MorseTester()
mp = MorseParser()
mc_2 = ''

while True:
    try:
        mt.play_morse(mc.morse_code)
        cur_morse = MorseParser().read()
        mc_2 = MorseCode(morse_code=cur_morse)
        print(mc_2)
    except InvalidCodeError as e:
        print(e)
    print(mt.test(mc_2.morse_code, mc.morse_code))