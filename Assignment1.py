import sys

#this function takes in the city you are going from and returns the staright lines distances to the target city
def getCityStraightLineDistance(cityName):
    distancesFile = open('distances.txt', 'r')
    lines = distancesFile.readlines()
    for line in lines:
        if(line.split('-')[0] == cityName):
            return(int(line.split('-')[1].replace('\n','')))

#this is the main function, does all of the algo

def aStar(startingNode, goalNode):
    striaghtLineDistance = getCityStraightLineDistance(startingNode)

    #open up the map file and turn it into a dict of the cities and their possible moves
    mapFile = open('map.txt', 'r')
    lines = mapFile.readlines()
    currentNode = startingNode
    bestRoute = startingNode + " - "
    map = {}

    for line in lines:
        leftCity = line.split('-')[0]
        rightCities = line.split('-')[1].split(',')
        movableCities = []
        for city in rightCities:
            distance = city.split('(')[1].split(')')[0].replace('\n', '')
            city = city.split('(')[0]
            movableCities.append(city + "," + distance)
        map[leftCity] = movableCities

    paths = []#string values of all the paths
    pathsCost = []#costs of the current nodes 
    pathsDistances = []#current non straight line distance we are traving in this nodes

    paths.append(currentNode )
    pathsCost.append(0)#cost of the current path is default to 0
    pathsDistances.append(0)
    notDone = True
    i = 0
    currentNodes = [startingNode + " - "]
    currentCosts = [0]

    currentDistances = [0]

    while(notDone == True):
        #create the temp node stores
        tempNodes = []
        tempCosts = []
        tempDistances = []

        z = 0
        for node in currentNodes:
            if(node.split(' - ')[len(node.split(' - ')) - 1] == goalNode):
                #if path is already complete just put it back to temp
                i += 1
                tempNodes.append(node)
                tempCosts.append(currentCosts[z])
                tempDistances.append(currentDistances[z])

            else:
                currentNode = node.split(' - ')[len(node.split(' - '))-2]    

                for transitions in map[currentNode]:
                     #if node is not complete makes sure we can move to a unique palce

                    if(transitions.split(",")[0] == goalNode):
                        tempCosts.append(currentCosts[z] + int(transitions.split(",")[1]) + striaghtLineDistance)# costs is the f = g + h; so current distance traveled + the striaght line distance
                        tempNodes.append(node + transitions.split(",")[0] )
                        tempDistances.append(currentDistances[z] + int(transitions.split(",")[1]) )

                    else:
                        if transitions.split(",")[0] in node:
                            #do nothing if we are backtracking
                            tet = ''
                        else:

                            tempCosts.append(currentCosts[z] + int(transitions.split(",")[1]) + striaghtLineDistance)
                            tempDistances.append(currentDistances[z] + int(transitions.split(",")[1]) )

                            tempNodes.append(node + transitions.split(",")[0] + " - ")
            z += 1

        #finalize

        currentNodes = tempNodes
        currentCosts = tempCosts
        currentDistances = tempDistances
        checkForAllDoneRoutes = 0

        for j in currentNodes:
            if goalNode in j:
                checkForAllDoneRoutes += 1
        if(checkForAllDoneRoutes == len(currentNodes)):
            notDone = False

    y = 0
    bestRoute = ''
    finalCost = 0
    finalDistance = 0
    for j in currentNodes:
        if(finalDistance == 0):
            bestRoute = j
            finalDistance = currentDistances[y]   
        if(finalDistance > currentDistances[y]):
            bestRoute = j
            finalDistance = currentDistances[y]
        y += 1
 
    return startingNode, goalNode, bestRoute, finalDistance


#some set ups, like the end position
goalNode = "Bucharest"         
city = sys.argv[1]#system variable from command line


if(city == goalNode):
    #check to make sure
    print("Your Are Already In " + goalNode)    
else:
    #run the algo and print the data
    startingNode, goalNode, bestRoute, finalCost = aStar(city, goalNode)
    print("From City: " + startingNode)
    print("To City: " + goalNode)
    print("Best Route: " + bestRoute)
    print("Total distance: " + str(finalCost))