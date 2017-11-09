import abc
from datetime import datetime


class WriteFile(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, filename):
        self.filename = filename

    @abc.abstractmethod
    def write(self, data):
        pass

    def write_line(self, text):
        with open(self.filename, 'a') as handle:
            handle.write(text + '\n')


class DelimFile(WriteFile):
    def __init__(self, filename, delim):
        super(DelimFile, self).__init__(filename)
        self.delim = delim

    def write(self, lyst):
        temp_list = []
        for element in lyst:
            if self.delim in element:
                temp_list.append('"{}"'.format(element))
            else:
                temp_list.append(element)
        line = self.delim.join(temp_list)
        self.write_line(line)


class LogFile(WriteFile):
    def write(self, line):
        date = datetime.now()
        datestr = date.strftime('%Y-%m-%d  %H:%M')
        self.write_line('{}      {}'.format(datestr, line))


logfile = LogFile('log.txt')
logfile.write('hehe')
logfile.write('po')

delimfile = DelimFile('delim.txt', ',')
delimfile.write(['a', 'b', 'c', 'd,a'])
