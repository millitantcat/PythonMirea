"""class StateMachine:
    state = 'A'

    def clone(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise KeyError

    def trace(self):
        if self.state == 'A':
            self.state = 'C'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'G'
            return 4
        elif self.state == 'D':
            self.state = 'D'
            return 6
        elif self.state == 'F':
            self.state = 'C'
            return 9
        else:
            raise KeyError


def main():
    return StateMachine()"""


class StateMachine:
    state = 'A'

    def chalk(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'V'
            return 2
        elif self.state == 'C':
            self.state = 'C'
            return 4
        elif self.state == 'D':
            self.state = 'D'
            return 6
        elif self.state == 'E':
            self.state = 'C'
            return 8
        else:
            raise KeyError

    def visit(self):
        if self.state == 'A':
            self.state = 'F'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise KeyError


def main():
    o = StateMachine()
    return o

