"""
predictor.py
author: Steve
finish date: 2022.1.11
email: apesc1116@outlook.com
This is just a simple program.
If you want to learn more about Neural Network, 
you can read the book "Make Your Own Neural Network" written by Tariq Rashid.
"""
import csv
import random
import math

# Set some primary variables.
L = 0.3
A = 0.1
writer = None


def iteration(x, m, iY, Layer, pLayer, detail=True):
    global A, L, writer

    # Calculate and update the variables.
    rY = L*(A*x+m)
    E = iY-rY
    try:
        dA = E/x
    except ZeroDivisionError:
        dA = 0
        m = iY
    A += dA
    writer.writerow([iY, rY, E])

    # Iteration
    if Layer>=pLayer:
        if detail == True: print("The value of A after training:{}".format(A))
        if detail == True: print("iY={}, rY={}, x={}, A={}, dA={}, L={}, m={}, E={}".format(iY, rY, x, A, dA, L, m, E))
        # here is where the truly return value defined
        back = A
    else:
        back = iteration(x, m, iY, Layer+1, pLayer, detail)
    return back


def main(detail=True):
    global L, A, writer

    # Get the data.
    with open(r".\data_gen.csv", "r", encoding="utf-8") as source_data:
        source_data = csv.reader(source_data)
        temp = []
        for x in source_data:
            temp.append(x)
    source_data = temp
    del temp

    # Training.
    print("Training.")
    write_file = open(r".\data_per.csv", "w", encoding="utf-8")
    writer = csv.writer(write_file)
    writer.writerow(["iY", "rY", "E"])
    As = []
    for aline in source_data:
        x = float(aline[0])
        iY = float(aline[-1])
        As.append(iteration(x, 0, iY, 0, int(math.ceil(69/L*0.5)), detail))

    # Calculate the average.
    temp = 0
    counter = 0
    for A_ in As:
        temp+=A_
        counter +=1
    average_of_A = temp/counter
    if detail == True: print("average_of_A: "+str(average_of_A))
    print("A: "+str(average_of_A*L))
    write_file.close()
    return average_of_A*L

if __name__ == "__main__":
    main() 