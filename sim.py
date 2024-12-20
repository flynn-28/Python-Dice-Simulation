import random
import csv

def sim(rolls, dice, sides):
    data = []
    sides = dice * sides
    for i in range(rolls):
        data.append([i + 1,random.randint(1, sides)])
    return data

def save(data):
    with open("data.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['index', 'value'])        
        for row in data:
            writer.writerow(row)


rolls = int(input("How many rolls?: "))
dice = int(input("How many dice?: "))
sides = int(input("How many sides?: "))
data = sim(rolls, dice, sides)
save(data)
