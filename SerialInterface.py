__author__ = 'Florian'
import serial
import re


class SerialReader():

    def __init__(self, com_port, baud_rate):
        self.conn = serial.Serial(com_port, baud_rate)
        self.conn.flushInput()

    def get_line(self):
        return self.conn.readline()

    def close_conn(self):
        self.conn.close()

    def flush(self):
        self.conn.flushInput()

class CsvWriter():

    def __init__(self, filename):

        # while os.path.exists(filename + str(i)):
        #     i += 1

        #if not os.path.exists(filename):
        self.csv_file = open(filename, 'w')
        # else:
        #     new_filename = filename.split('.csv')[0] + '_copy.csv'
        #     print('File', filename, ' exists new filename: ', new_filename)
        #     self.csv_file = open(new_filename, 'w')

    def write_csv(self, data):

        if type(data) == str:
            self.csv_file.write(data)

        elif type(data) == list:
            for line in data:
                self.csv_file.write(line+'\n')

    def close_csv(self):
        self.csv_file.close()