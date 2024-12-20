import csv
import statistics as s

def analyze(csv_file):
    rolls = 0
    average = 0
    total = 0
    data = []
    
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        
        next(reader) 
        
        for row in reader:
            value = int(row[1]) 
            rolls += 1
            total += value
            data.append(value)
    average = total / rolls
    mode = s.mode(data)
    std = s.stdev(data)
    variance = s.variance(data)

    return average, mode, std, variance

average, mode, std, variance = analyze("data.csv")

print(f'''
Results
---------- 
Average: {average}
Mode: {mode} 
Standard Deviation: {std} 
Variance: {variance}
    ''')