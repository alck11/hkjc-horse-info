import math
import random
import sys
from decimal import Decimal as dml

print "This will simulate the 'Birthday Problem' by generating XX random"
print "numbers between 1 and 365 (inclusively).\n"

people = 25

trials = 10

matches = 0
nomatches = 0
total_trials = trials

def findmatches(numbers):
    s = set()
    ans = False
    for number in numbers:
        if numbers.count(number) > 1:
            s.add(number)
            ans = True
    return ans, s

while trials > 0:
    trials -= 1

    # Seed random with the current time, creates more "randomness" on each iteration
    random.seed()

    #generate a list of "people" length, where each element is a random number between from 1 (inclusive) to 366 (non-inclusive)
    numbers = [random.randrange(1, 366) for i in range(people)]

    #print "Here is the list of numbers: "
    #for number in numbers:
        #print number

    a, b = findmatches(numbers)

    if a:
        matches += 1

    #print "Trial:",total_trials - trials

result = dml(matches) / dml(total_trials) * 100
expected = (1 - dml(math.factorial(365)) / ( 365**people * math.factorial(365-people)))*100
if result != 0:
    pe = abs((expected - dml(result)) / dml(result)) * 100
else:
    print "\nPlease enter more trials, to prevent a division by zero!\n", sys.exit()

print "\n\nNumber of successful trials: ", matches
print "Percent of successful trials: ", round(result, 4)
print "\nExpected percent of number of successful trials:", round(expected, 4)
print "\nPercent of error:", round(pe, 4)
