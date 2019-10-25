#!/bin/python3

import math
import os
import random
import re
import sys
import time

listOfPoints = []

def breakingRecords(scores):
    minimum = maximum = scores[0]
    minCount = maxCount = 0
    for score in scores:
        if score > maximum:
            maximum = score
            maxCount+=1
        elif score < minimum:
            minimum = score
            minCount+=1
    return (maxCount, minCount)

print("This program will determine how many times the record for most points and the record for least points are broken based on a list of points from several games.\n")

time.sleep(5)

countOfGames = int(input("To start, first input the number of games you participated in during the season: "))

print("Now, input the points you earned in each game, in the the order of oldest to most recent.\n")

for game in range (countOfGames):
  points = int(input("Points for game " + str(game + 1) + ": "))
  listOfPoints.append(points)

result = breakingRecords(listOfPoints)

time.sleep(1)
print("\nTimes most points record was broken: " + str(result[0]))

time.sleep(1)
print("Times least points record was broken: " + str(result[1]))

time.sleep(1)
#Simple replace the current image with the ascii art.  
print(r"""

              .-=========-.
              \'-=======-'/
              _|   .=.   |_
             ((|  {{1}}  |))
              \|   /|\   |/
               \__ '`' __/
                 _`) (`_
               _/_______\_
              /___________\

  """)

time.sleep(20)