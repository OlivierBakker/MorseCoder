import Coder
import SerialInterface

def main():

    ser = SerialInterface.SerialReader('/dev/ttyACM0', 115200)
    mp = Coder.MorseParser()
    while True:

        try:
            cur_chr = ser.get_line().decode()
            val = mp.interpret_word(cur_chr)
            if val:
                break

        except KeyboardInterrupt:
            print(mp.msg)
            break
    print(val)




if __name__ == '__main__':
    main()