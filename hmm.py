import sys

selected_file = sys.argv[1]
f = open(selected_file, "r")
lines = f.read().split('\n')

for line in lines:
    values = line.split(',')
    a = float(values[0])
    b = float(values[1])
    c = float(values[2])
    d = float(values[3])
    f = float(values[4])

    e_values = []
    i = 5
    while i < len(values):
        e_values.append(values[i])
        i+=1
    if(e_values[0] == 't'):
        tempx =  ((b * a) + (c * a))
        tempy =  ((c * (1-a)) + (b * (1-a)))

        x = tempx + tempy
        y = tempy + tempx
        x = x * d
        y = y * f


        alpha = abs(x) + abs(y)
        x = x/alpha
        y = y/alpha
    else:
        tempx =  ((b * a) + (c * a))
        tempy =  (((1-c) * (1-a)) + ((1-b) * (1-a)))

        xx = tempx + tempy
        yy = tempy + tempx
        x = xx * (1-d)
        y = yy * (1-f)   

        alpha = abs(x) + abs(y)
        x = (1 - x/alpha)
        y = (1 - y/alpha)
    v = 1
    while v < len(e_values):
        if(e_values[v] == 't'):
            tempx = ((x * b) + (y * c))
            tempy = (x * c) + (y * b)

            x = tempx * d
            y = tempy * f 
            alpha = abs(x) + abs(y)
            x = x/alpha
            y = y/alpha
        else:
     
            tempx = (x * c) + (y * b)
            tempy = (y * (1-b)) + (x * (1-c))

            x = tempx * (1-f)
            y = tempy * (1-d) 

            alpha = abs(x) + abs(y)
            x = (1 - x/alpha)
            y = (1 - y/alpha)
        v +=1

    
    alpha = abs(x) + abs(y)
    x = x/alpha
    y = y/alpha

    output = line + "-->" + "<" + str(round(x,4)) + "," + str(round(y,4)) + ">"
    print(output.replace(' ', ''))


