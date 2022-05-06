import csv 
import numpy as np
import random


    
    
def convert_monk_csv(filename,destname):
    fieldnames = ['class', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6']
    # Reading train data
    train_data = []
    with open(destname, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        
        with open(filename) as infile:
            reader = csv.reader(infile, delimiter=" ")
            for row in reader:
                writer.writerow({'class':row[1],'a1':row[2],'a2':row[3],'a3':row[4],'a4':row[5],'a5':row[6],'a6':row[7]})

filename = 'monks-3.test'
destname = 'monks-3_test.csv'
convert_monk_csv(filename, destname)