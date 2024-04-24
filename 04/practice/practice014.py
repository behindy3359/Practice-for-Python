class Pen():
    def writeLetter(self):
        print('글씨를 쓴다.')

class Pencil(Pen):
    def writeLetter(self):
        print('연필로 글씨를 쓴다.')

class Ballpen(Pen):
    def writeLetter(self):
        print('볼펜으로 글씨를 쓴다.')

class Fountainpen(Pen):
    pass

pen_pencil = Pencil()
pen_pencil.writeLetter()

pen_ballpen = Ballpen()
pen_ballpen.writeLetter()

pen_fountainpen = Fountainpen()
pen_fountainpen.writeLetter()

pen = pen_pencil
pen.writeLetter()
pen = pen_ballpen
pen.writeLetter()
pen = pen_fountainpen
pen.writeLetter()