import matplotlib.pyplot as plt
import random

xo = 50.00
yo = 50.00

x = [xo]
y = [yo]
fixed_distance = 2


n = 0
while (n <= 100):
    randx = random.uniform (0.00, 50.00)
    randy = random.uniform (0.00, 50.00)
    min_distance = ((randx - x[0]) ** 2 + (randy - y[0]) ** 2) ** (1 / 2) # closest to the node
    min_index = 0  # index of the node which is at the minimum distance from random point
    
    for i in range (len (x)):
        curr_distance = ((randx - x[i]) ** 2 + (randy - y[i]) ** 2) ** (1 / 2)

        if (curr_distance < min_distance):
            min_distance = curr_distance
            min_index = i
    if (min_distance <= fixed_distance) :
        plt.plot ([x[min_index], randx], [y[min_index], randy],"k-")
        plt.plot ([x[min_index], randx], [y[min_index], randy], "bo")
        x.append (randx)
        y.append (randy)

    else:
        xnew = ((randx-x[min_index]) * (fixed_distance/min_distance) )+ x[min_index]
        ynew = ((randy- y[min_index]) * (fixed_distance/min_distance) ) + y[min_index]
        x.append (xnew)
        y.append (ynew)
        plt.plot ([x[min_index], xnew], [y[min_index], ynew], "k-")
        plt.plot ([x[min_index], xnew], [y[min_index], ynew], "bo")

    n = n + 1

    # is minimum distance less than fixed distance

    # if it is less than fixed distance plot points and connect the points (x[min_index], y[min_index]) and (randx, randy)

    # if it is greater than fixed distance
    # find slope
    # find another point in the same direction as random point which is at a distance fixed_distance
    # plot and connect this point with (x[min_index], y[min_index])
plt.show ()