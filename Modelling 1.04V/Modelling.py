from random import random

r = 0.0
m = 0.0
h = 0.0
h0 = -1.0
time = 0.0
R_stup = 0.023
m_gr = 0.4
I0 = 0.009
Mtr = 0.01
a = 0.0
I_ = 0.0
g = 9.819

while m < 0.1 or m > 0.9:
    print ("Enter mass:")
    m = float(input())
    if m < 0.1 or m > 0.9:
        print ("mass must be between 0.1 and 0.9")

while r < 0.07 or r > 0.23:
    print ("Enter radius:")
    r = float(input())
    if r < 0.07 or r > 0.23:
        print ("radius must be between 0.07 and 0.23")

while h0 < 0.0 or h0 > 1.0:
    print ("Enter h0:")
    h0 = float(input())
    if h0 < 0.0 or h0 > 1.0:
        print ("h0 must be between 0.0 and 1.0")

while h < 1.0:
    I_ = I0 + 4 * m_gr * r * r
    a = (R_stup * (R_stup * m * g - Mtr)) / (I_ + m * R_stup * R_stup)
    if a <= 0:
        break
    h = (1 - h0) + a * time * time / 2
    time += (0.01 + random() / 100)

format(time, '.2f')
print 'time = ' + format(time, '.2f') + 'c'
