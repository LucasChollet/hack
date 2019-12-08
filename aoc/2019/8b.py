from __future__ import print_function
import fileinput

w, h = 25, 6
line = list(fileinput.input())[0].rstrip()
pic = ['2'] * (w * h)
for layer in range(0, len(line), w*h):
    for i in range(0, w*h):
        if pic[i] == '2':
            pic[i] = line[layer + i]
for y in range(0, w*h, w):
    print(''.join(pic[y:y + w]).replace('0', ' '))
