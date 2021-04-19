import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt

# importing the dataset
print("reading the cardiovascular disease dataset using pandas")
cardiovascular_disease_dataset = pd.read_excel("E:\\VIT UNIVERSITY  ACADEMICS\\vit assignment\\WINTER SEMESTER\\Nosql Database J component Review\\Heart Disease Data.xlsx")
print("data is : \n")
print(cardiovascular_disease_dataset)