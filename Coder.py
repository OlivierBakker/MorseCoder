import re
import array
import SerialInterface


class InvalidCodeError(Exception):
    pass


class SepError(Exception):
    pass


class EndOfMessage(Exception):
    pass


def get_code(file='MorseCode'):

    code = open(file, 'r')
    code_dict = {}

    for line in code:

        line = line.strip()
        letter = re.search('<letter>([A-z]*)</letter>', line)
        code = re.search('<code>(.*)</code>', line)

        if letter:
            cur_letter = letter.group(1)
            code_dict.update({cur_letter: 0})

        if code:
            cur_code = code.group(1)
            code_dict[cur_letter] = cur_code
            code_dict.update({cur_code: cur_letter})

    return code_dict


class MorseCode():
    code_dict = get_code()

    def __init__(self, morse_code=list(), string_rep=str()):

        self.morse_code = morse_code
        self.string_rep = string_rep
        self.index = 0
        self.char_sep = ' '
        self.word_sep = '|'

        if morse_code:
            self.decode()
        elif string_rep:
            self.encode()

    def __str__(self):
        return 'STRING: '+self.string_rep+'\nCODE:\t'+self.word_sep.join(self.morse_code)

    def __len__(self):
        return len(self.morse_code)

    def __iter__(self):
        return self

    def __bytes__(self):
        return '|'.join(self.morse_code).encode('utf-8')

    def __eq__(self, other):

        if self.string_rep == other.string_rep:
            return True
        else:
            return False

    def __next__(self):

        if self.index == self.__len__():
            self.index = 0
            raise StopIteration
        else:
            self.index += 1
            return self.morse_code[self.index-1]

    def encode(self):

        string_rep = self.string_rep.split(self.word_sep)
        for word in string_rep:
            self.morse_code.append(self.char_sep.join([self.code_dict[x] for x in word.upper()]))

        return self

    def decode(self):

        decoded_msg = []
        try:

            for word in self.morse_code:
                word = word.split(self.char_sep)
                decoded_msg.append(''.join([self.code_dict[char] for char in word]))

            self.string_rep = self.word_sep.join(decoded_msg)

        except KeyError:
            raise InvalidCodeError('Invalid morse code in the code: ' +
                                   str(self.morse_code) +
                                   ' Perhaps the serparators have been misconfigured?')

        return self


class Queue():

    def __init__(self):
        self._q_list = list()

    def __str__(self):
        return ''.join(self._q_list)

    def __len__(self):
        return len(self._q_list)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, item):
        self._q_list.append(item)

    def dequeue(self):
        assert not self.is_empty(), "Cannot dequeue from an empty queue"
        return self._q_list.pop(0)

    def dump(self):
        dump_list = list()

        for i in range(0, len(self._q_list)):
            dump_list.append(self.dequeue())

        return dump_list

    def clear(self):
        self._q_list = []


class MorseParser():

    def __init__(self, char_time=100, dot='.', dash='-', sep=' '):
        self.char_time = char_time
        self.dot = dot
        self.dash = dash
        self.sep = sep
        self.ser = SerialInterface.SerialReader('/dev/ttyACM0', 115200)
        self.queue = Queue()

    def parse_line(self, input_char):

        raw = re.search('State: (\\d) Time: (\\d*)', input_char)
        state = int(raw.group(1))
        time = int(raw.group(2))

        if state == 0:
            if time > 20*self.char_time:
                raise EndOfMessage

            elif time > 10*self.char_time and len(self.queue) > 1:
                self.queue.enqueue('|')

            elif time > 3*self.char_time < 10*self.char_time and len(self.queue) > 1:
                self.queue.enqueue(' ')

        else:
            if time > 3 * self.char_time:
                cur_char = self.dash
            else:
                cur_char = self.dot

            self.queue.enqueue(cur_char)

    def join_queue(self):
        code = ''.join(self.queue.dump())
        code.rstrip(' ')
        code.lstrip(' ')
        return code.split('|')

    def read(self):

        self.ser.flush()
        while True:
            try:
                self.parse_line(self.ser.get_line().decode())
            except EndOfMessage:
                return self.join_queue()



#msg = MorseParser().read()
msg = ['... --- ...', '... --- ...']
mc = MorseCode(morse_code=msg)
print(mc.__bytes__())
# print(mc)
#
# msg_2 = 'SOS|SOS'
# mc_2 = MorseCode(string_rep=msg_2)
# print(mc_2)
