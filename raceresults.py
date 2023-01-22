def raceWinner(me,one,two,three):
    if(me<one):
        return("Gold Medal")
    elif(me<two):
        return("Silver Medal")
    elif(me<three):
        return("Bronze Medal")
    else:
        return("No Medal")
print(raceWinner(4,3,5,6))
