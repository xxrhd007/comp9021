# Written by *** for COMP9021

# Prompts the user for a positive integer.
# - When written in base 3, its consecutive digits read
#   from left to right represent the directions to take, with
#   * 0 meaning going South,
#   * 1 meaning South West,
#   * 2 meaning South East.
#
# Prints out:
# - the representation of the second digit in base 3;
# - the corresponding sequence of directions to take, as arrows;
# - the sequence of arrows again, but nicely displayed.
#
# The leftmost arrow is printed out with no space to the left.
#
# The arrows are the Unicode characters of code point
# 0x21e9 and 0x2b02 and 0x2b03.

import sys

try:
    encoded_directions = int(input('Enter a positive integer: '))
    if encoded_directions < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

def convert(x):
    s=[]
    while(x!=0):
        s.append(x%3)
        x=x//3
    return s[::-1]
if encoded_directions==0:
    a=[]
    a.append(0)
else:
    a=convert(encoded_directions)

tinydict = {0: chr(0x21e9), 2:chr(0x2b02) , 1: chr(0x2b03)}
print('In base 3, the input reads as: ',end='')
for i in range(len(a)):
    print(a[i],end='')
print("\n")
print("So that's how you want to go: ",end='')
for i in range(len(a)):
    print(tinydict[a[i]],end='')
print('\n')
print("Let's go then!")
count=0
tindex=len(a)-1
while(tindex>=0):
    if(a[tindex]==1):
        break
    tindex-=1
for i in range(tindex+1):
    if (a[i]==1):
        count+=1
    if (a[i]==2):
        count-=1
space=[]
if count<0:
    space.append(0)
else:
    space.append(count)
j=1
while(j<=len(a)-1):
    if a[j-1]==1:
        space.append(space[j-1]-1)
    if a[j-1]==0:
        space.append(space[j-1])
    if a[j-1]==2:
        space.append(space[j-1]+1)
    j=j+1
for i in range(len(space)):
    print(' '*space[i]+tinydict[a[i]]) 

# INSERT YOUR CODE HERE
