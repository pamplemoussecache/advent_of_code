# argv.py
import sys

if (len(sys.argv) < 1):
    print("I need an input file. Please try again :)")
    exit()

print("Puzzle One:")


input_file = open(sys.argv[1], "r")
elves = input_file.read().split("\n\n")

max_snack = -1

for elf in elves:
    calorie_count = sum([int(snack) for snack in elf.split("\n") if type(snack)== int or snack.isdigit()])
    if calorie_count > max_snack:
        max_snack = calorie_count

print(max_snack)

print("Puzzle Two:")



