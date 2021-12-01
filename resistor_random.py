import random
import time

time_delay = int(input('enter time delay: '))

color1 = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'gray', 'white']
color2 = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'gray', 'white']
color3 = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'gold', 'silver']
color4 = ['gold', 'silver']

ran_c1 = random.choice(color1)
ran_c2 = random.choice(color2)
ran_c3 = random.choice(color3)
ran_c4 = random.choice(color4)

all_ran = ran_c1,ran_c2,ran_c3
ran = ' '.join(all_ran)
power = 0

def decode_resistor_colors(bands):