class solvers:
    def __init__(self, bands):
        self.bands = bands

    def calculate(self):
        res = {'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4', 'green': '5',
               'blue': '6', 'purple': '7', 'gray': '8', 'white': '9', 'gold': '10', 'silver': '11'}
        code = self.bands.split(" ")
        print(code)

        if int(res[code[2]]) == 0:
            power = int(res[code[0]] + res[code[1]]) * 1
        elif int(res[code[2]]) == 1:
            power = int(res[code[0]] + res[code[1]]) * 10
        elif int(res[code[2]]) == 2:
            power = int(res[code[0]] + res[code[1]]) * 100
        elif int(res[code[2]]) == 3:
            power = int(res[code[0]] + res[code[1]]) * 1000
        elif int(res[code[2]]) == 4:
            power = int(res[code[0]] + res[code[1]]) * 10000
        elif int(res[code[2]]) == 5:
            power = int(res[code[0]] + res[code[1]]) * 100000
        elif int(res[code[2]]) == 6:
            power = int(res[code[0]] + res[code[1]]) * 1000000
        elif int(res[code[2]]) == 7:
            power = int(res[code[0]] + res[code[1]]) * 10000000
        elif int(res[code[2]]) == 10:
            power = int(res[code[0]] + res[code[1]]) * 0.1
        elif int(res[code[2]]) == 11:
            power = int(res[code[0]] + res[code[1]]) * 0.01

        if power < 1000:
            output = str(round(power, 2)) + ' ohm'
        elif power < 1000000:
            if int(power / 1000) == float((power / 1000)):
                output = str(int(power / 1000)) + 'k ohm'
            else:
                output = str(power / 1000) + 'k ohm'

        else:
            if int(power / 1000000) == float(power / 1000000):
                output = str(int(power / 1000000)) + 'M ohm'
            else:
                output = str(float(power / 1000000)) + 'M ohm'

        if code[3] == 'gold':
            output += (' 5%')
        elif code[3] == 'silver':
            output += (' 10%')

        answer = input('enter answer [1k ohm 5%]: ')

        if answer == output:
            print('Correct !')
        else:
            print('Incorrect')

        return output