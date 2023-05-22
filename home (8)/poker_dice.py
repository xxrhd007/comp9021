from random import randint
pdict={'Ace':0, 'King':1, 'Queen':2,'Jack':3 ,'10':4,  '9':5}
dreverse={0:'Ace',1:'King',2:'Queen',3:'Jack',4:'10',5:'9'}
time={0:"second",1:"third"}
def roll(x):
    dice = [0,1, 2,3, 4, 5]
    x.append(dice[randint(0, 5)])
    return x

def play():
    y = pick()
    y = sorted(y)
    print("The roll is: ", end="")
    print(dreverse[y[0]], dreverse[y[1]], dreverse[y[2]], dreverse[y[3]], dreverse[y[4]])
    cardset(y)
    j = 0
    while j < 2:
        try:
            a = []
            c = []
            change = str(input("Which dice do you want to keep for the "+str(time[j])+" roll? "))
            a.append(change.split())
            if len(a[0]) == 1:
                if change == "All" or change == "all":
                    print('Ok, done.')
                    break
            for x in a[0]:
                if x in pdict.keys():
                    c.append(pdict[x])
                else:
                    raise IOError
            c=sorted(c)
            if len(c) > 5:
                raise IOError
            elif len(c)==5 and y==c:
                print('Ok, done.')
                break


            for x in c:
                if x not in y:
                    raise IOError
            y=c
            for i in range(5 - len(y)):
                roll(y)
            y = sorted(y)
            print("The roll is: ", end="")
            print(dreverse[y[0]], dreverse[y[1]], dreverse[y[2]], dreverse[y[3]], dreverse[y[4]])
            cardset(y)
            j += 1
        except IOError:
            print ("That is not possible, try again!")
    # REPLACE PASS ABOVE WITH YOUR CODE


    # REPLACE PASS ABOVE WITH YOUR CODE

    
def roll(x):
    dice = [0,1, 2,3, 4, 5]
    x.append(dice[randint(0, 5)])
    return x


def pick():
    i = 0
    hand = []
    while i <= 4:
        roll(hand)
        i+=1

    else:
        return hand

def cardset(y):
    temp = sorted(y)
    pair = ([x for x in temp if temp.count(x) > 1 and temp.count(x) < 3])
    triple = ([x for x in temp if temp.count(x) == 3])
    four = ([x for x in temp if temp.count(x) == 4])
    five = ([x for x in temp if temp.count(x) == 5])
    str1 = [0,1, 2, 3, 4]
    str2 = [1,2, 3, 4, 5]
    if len(triple) == 3 and len(pair) == 2:
        triple.sort()
        print("It is a Full house")
    elif len(pair) == 4:
        pair.sort()
        print("It is a Two pair")
    elif len(pair) == 2:
        print("It is a One pair")
    elif len(triple) == 3 and len(pair) != 2:
        print("It is a Three of a kind")
    elif len(four) == 4:
        print("It is a Four of a kind")
    elif temp == str1 or temp == str2:
        print("It is a Stright")
    elif len(five) == 5:
        print("It is a Five of a kind")
    else:
        print("It is a Bust")

def cardset1(y):
    temp = sorted(y)
    pair = ([x for x in temp if temp.count(x) > 1 and temp.count(x) < 3])
    triple = ([x for x in temp if temp.count(x) == 3])
    four = ([x for x in temp if temp.count(x) == 4])
    five = ([x for x in temp if temp.count(x) == 5])
    str1 = [0,1, 2, 3, 4]
    str2 = [1,2, 3, 4, 5]
    if len(triple) == 3 and len(pair) == 2:
        triple.sort()
        return "Full house"
    elif len(pair) == 4:
        pair.sort()
        return "Two pair"
    elif len(pair) == 2:
        return "One pair"
    elif len(triple) == 3 and len(pair) != 2:
        return "Three of a kind"
    elif len(four) == 4:
        return "Four of a kind"
    elif temp == str1 or temp == str2:
        return "Straight"
    elif len(five) == 5:
        return "Five of a kind"
    else:
        return "Bust"    

def simulate(n):
    
    hands = {
        "Five of a kind": 0,
        "Four of a kind": 0,
        "Full house": 0,
        "Straight": 0,
        "Three of a kind": 0,
        "Two pair": 0,
        "One pair": 0,
    } 
    
    for _ in range(n):
        y=pick()
        result=cardset1(y)
        if result != "Bust":
            hands[result] += 1


    for hand, count in hands.items():
        print(f'{hand:15}: {(count/n*100):.2f}%')
# DEFINE OTHER FUNCTIONS
