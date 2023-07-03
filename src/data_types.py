class base:
    def __init__(self):
        pass

    def __str__(self):
        return str(self.value)

    def __getitem__(self, key):
        if key == 0:
            return self.value
        elif key == 1:
            return self.type
        else:
            return self.value

class INTEGER(base):
    def __init__(self, value=0):
        self.value = int(value)
        self.type = 'INTEGER'
        super().__init__()

    def set_value(self, new_value):
        self.value = int(new_value)

class REAL(base):
    def __init__(self, value=.0):
        self.value = float(value)
        self.type = 'REAL'
        super().__init__()

    def set_value(self, new_value):
        self.value = float(new_value)

class STRING(base):
    def __init__(self, value=''):
        self.value = str(value)
        self.type = 'STRING'
        super().__init__()

    def set_value(self, new_value):
        self.value = str(new_value)

class CHAR(base):
    def __init__(self, value=''):
        self.value = str(value)[0]
        self.type = 'CHAR'
        super().__init__()

    def set_value(self, new_value):
        self.value = str(new_value)[0]

class BOOLEAN(base):
    def __init__(self, value=True):
        self.value = bool(value)
        self.type = 'BOOLEAN'
        super().__init__()

    def __str__(self) -> str:
        return {True: 'TRUE', False: 'FALSE'}[self.value]

    def set_value(self, new_value):
        self.value = bool(new_value)

class ARRAY(base):
    def __init__(self, value={}):
        self.value = value
        self.type = 'ARRAY'
        super().__init__()

    def __str__(self) -> str:
        l = []
        for i in self.value.values():
            l.append(str(i[0]))
        return '[' + ', '.join(l) + ']'

    def set_value(self, value):
        self.value = value