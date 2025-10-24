#!/usr/bin/env python3
def get_num_terms():
  while True:
    try:
      n = int(input("How many terms of the Fibonacci sequence do you want? "))
      if n>0:
        return n
      else:
        print("Error: Please enter a positive integer.")
    except ValueError:
      print("Error: Invalid input. Please enter a positive integer. ")

def generate_fibonacci(n):
  sequence = []
  a,b= 0,1
  for _ in range(n):
    #this....is a bit confusing. I'm going to watch a tutorial on append and how for loops work.
# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
