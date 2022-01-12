"""
author: Steve
finish date: 2022.1.11
email: apesc1116@outlook.com
This is just a simple program.
If you want to learn more about Neural Network, 
you can read the book "Make Your Own Neural Network" written by Tariq Rashid.
"""
import random
def main(times, detail=True):
    with open(r".\data_gen.csv", "w", encoding="utf-8") as data_resource:
        weight = random.randint(1, random.randint(10, 20))
        err = random.random()
        for i in range(times):
            temp = random.randint(0, 10)
            coefficient_of_weight = random.randint(-1, 1)
            if detail == True:
                print(str(temp)+", "+str(temp*(weight+coefficient_of_weight*err)))
            data_resource.write(str(temp)+", "+str(temp*(weight+coefficient_of_weight*err))+"\n")
    return weight

if __name__ == "__main__":
    times = int(input("Input the pair of the number of the data.\n"))
    main(times)