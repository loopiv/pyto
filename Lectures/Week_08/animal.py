class Animal(object):
    def __init__(type='animal', name='Thing', legs=4, speak='Hello.', bad_speak='No.', tail=True, *args, **kwargs):
        self.type = type
        self.name = name
        self.legs = legs
        self.speak = speak
        self.bad_speak = bad_speak
        self.tail = tail

    def getType(self):
        return self.type

    def walk(self):
        print('I am walking ' + self.name + '.')
