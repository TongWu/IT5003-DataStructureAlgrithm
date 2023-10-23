# Student ID: A0255954R
# Full Name: Wu Tong
# Lab Group: B5
# TA: Steven Halim
import sys

def solution():
    printed_star = 0
    for line in sys.stdin:
        if line == "\n":
            # If the line is empty, start over for a new log file
            printed_star = 0
            print()
        else:
            # Count the number of star
            star_num = line.count("*")
            # We just need to calculate how many * in each row, and push these * to the far right but not excess the previous line's first star location
            print('.' * (len(line)-1 - star_num - printed_star), end='') # The number of first part of '.' is the rest
            print('*' * star_num, end='') # The number of star is counted before
            print('.' * printed_star,  end='') # The number of second part of '.' is printed star number
            print()
            printed_star += star_num

solution()