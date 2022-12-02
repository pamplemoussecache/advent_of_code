import sys

if (len(sys.argv) < 2):
    print("I need an input file and a number of elves. Please try again :)")
    exit()

def sumElvesWithMostCalories(input_file, num_elves):
    input_file = open(sys.argv[1], "r")
    elves = input_file.read().split("\n\n")

    calorie_counts = []

    for elf in elves:
        calorie_count = sum([int(snack) for snack in elf.split("\n") if type(snack)== int or snack.isdigit()])
        calorie_counts += [calorie_count]

    calorie_counts.sort(reverse=True)

    total = 0
    for i in range(num_elves):
        total += calorie_counts[i]

    print(total)


print("Puzzle One:")

sumElvesWithMostCalories(sys.argv[1], 1)

print("Puzzle Two:")

sumElvesWithMostCalories(sys.argv[1], int(sys.argv[2]))



