print('내장된 모듈 사용하기')

import sys
print('모듈 경로 :',sys.path)

import math
print(math.pi)
print(math.sin(math.radians(30)))

import calendar
calendar.setfirstweekday(6)
calendar.prmonth(2024,4)
del calendar

import os
print(os.getcwd())
print(os.listdir('/'))
