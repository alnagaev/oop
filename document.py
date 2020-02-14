class Document:
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        if not hasattr(character, 'character'):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    @property
    def string(self):
        return "".join((str(c) for c in self.characters))

    def get_document(self):
        print(','.join(self.characters))

    def delete(self):
        del self.characters[self.cursor.position]

    def backspace(self):
        del self.characters[self.cursor.position -1]

    def save(self):
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))    
        f.close()


class Cursor:
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1

    def back(self):
        self.position -= 1

    def home(self):
        try:
            while self.document.characters[self.position-1].character != '\n':
                self.position -= 1
                if self.position == 0:
                    # Got to beginning of file before newline
                    break
        except IndexError as ie:
            print(str(ie))
            pass

    def end(self):
        try:
            while self.position < len(self.document.characters) and self.document.characters[
                self.position].character != '\n':
                    self.position += 1
        except IndexError as ie:
            print(str(ie))
            pass


class Character:
    def __init__(self, character,
        bold=False, italic=False, underline=False):
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''
        return bold + italic + underline + self.character



class SlotsClass:
    __slots__ = ('foo', 'bar')

class ChildSlotsClass(SlotsClass):
    __slots__ = ()

# >>> obj = ChildSlotsClass()
# >>> obj.foo = 5
# >>> obj.baz = 6
# >>> obj.something_new = 3
# Traceback (most recent call last):
#   File "python", line 12, in <module>