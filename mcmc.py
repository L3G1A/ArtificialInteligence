import random


print("Part A. The sampling probabilities")


print("P(C|-s,r) = <.87805, .12195>")

print("P(C|-s,-r) = <.31034, .68966>")

print("P(R|c,-s,w) = <.98701, .01299>")

print("P(R|-c,-s,w) = <.82609, .17391>")

print("")









print("Part B. The transition probability matrix")
print("        S1         S2        S3         S4")
print("S1    0.9322     0.0065    0.0610     0.0000")
print("S2    0.4935     0.1620    0.0000     0.3448")
print("S3    0.4390     0.0000    0.4701     0.0909")
print("S4    0.0000     0.1551    0.4091     0.4357")
 

Cloudy =    [(.5,.5)]
Sprinkler = [(.1,.9),(.5,.5)]
Rain =     [(.8,.2),(.2,.8)]
WetGrass = [(.99,.01),(.95,.05),(.9,.1),(.05,.95)]
sampleSize = 1000000
countCond = 0
count = 0
for i in range(sampleSize):
    trueRain = random.random()

    falseSprinkler = random.random()
    trueCloud = random.random()

    trueWetGrass =  random.random()
    if(trueCloud < Cloudy[0][0]):
        if(falseSprinkler <= Sprinkler[0][1]):
            if(trueRain < Rain[0][0]):    
                if(trueWetGrass < WetGrass[2][0]):
                    countCond += 1
                    count += 1
            else:
                if(trueWetGrass < WetGrass[3][0]):
                    countCond += 1
                    count += 1
 
    else:
        if(falseSprinkler <= Sprinkler[1][1]):
            if(trueRain < Rain[1][0]):    
                if(trueWetGrass < WetGrass[2][0]):
                    countCond += 1
            else:
                if(trueWetGrass < WetGrass[3][0]):
                    countCond += 1


print("")
print("Part C. The probability for the query")
print("P(C|-s,w) = <" , round((count/countCond), 4) , ", " , round((1 - count/countCond), 4) , ">")




