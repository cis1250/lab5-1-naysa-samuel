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
  sequence = [] #in Python this is a list, in C this would be an array
  a,b= 0,1
  for _ in range(n):
    sequence.append(a)
    a, b= b, a+b
  return sequence

def print_fibonacci(sequence):
  print("Fibonacci Sequence:")
  for num in sequence:
    print(num, end=" ")
  print()

def main():
  n = get_num_terms()
  sequence = generate_fibonacci(n)
  print_fibonacci(sequence)

if __name__ == "__main__": #module guard, for running main only when executed as a script
  main()
   
# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
