import io


class WriteMyStuff(object):
    def __init__(self, writer):
        self.writer = writer

    def write(self):
        write_text = "This is a silly message"
        self.writer.write(write_text)


fh = open('test.txt', 'w')
w1 = WriteMyStuff(fh)
w1.write()
fh.close()

sioh = io.StringIO()
w2 = WriteMyStuff(sioh)
w2.write()

print('File object: ', open('test.txt', 'r').read())
print('StringIO object: ', sioh.getvalue())
