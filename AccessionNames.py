#!/usr/bin/python

from __future__ import division
from __future__ import print_function
import re

print("\n")
print("Tyler McCraney")
print("February 11, 2015")
print("EEB C234")

# Accession names
# Here is a list of made up gene accession names:

accs = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

# Write a program that will print only the accession names that satisfy the following criteria - treat each criterion separately:
# contain the number 5

print("\n")
print("PFB Ch7 exercises")
print ("Write a program that will print only the accession names that satisfy the following criteria - treat each criterion separately:")
print("\n")
print ("-contain the number 5")
for accession in accs:
    if re.search(r"5", accession):
        print(accession)
        
print("\n")
print("-contain the letter d or e")
for accession in accs:
    if re.search(r"(d|e)", accession):
        print(accession)    

print("\n")
print("-contain the letter d and e in that order")
for accession in accs:
    if re.search(r"de", accession):
        print(accession)    
    
print("\n")
print("-contain the letter d and e in that order with a single letter between them")
for accession in accs:
    if re.search(r"d(\w)e", accession):
        print(accession)    
    
print("\n")
print("-contain both the letters d and e in any order")
for accession in accs:
    if re.search(r"d", accession) and re.search(r"e", accession):
        print(accession)    

print("\n")
print("-start with x or y")
for accession in accs:
    if re.search(r"^x", accession) or re.search(r"^y", accession):
        print(accession)    

print("\n")
print("-start with x or y and end with e")
for accession in accs:
    if re.search(r"^x", accession) and re.search(r"e$", accession) or re.search(r"^y", accession) and re.search(r"e$", accession): 
        print(accession)    

print("\n")
print("-contain three or more numbers in a row")
for accession in accs:
    if re.search(r"\d{3}", accession):
        print(accession)    

print("\n")
print("-end with d followed by either a, r, or p")
for accession in accs:
    if re.search(r"d[arp]$", accession):
        print(accession)    
