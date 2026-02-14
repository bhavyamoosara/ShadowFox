import random
# Task 1: Dice Rolling Simulation
print("Task 1: Dice Rolling Simulation")

rolls = []
num_rolls = 20

for _ in range(num_rolls):
    roll = random.randint(1, 6)
    rolls.append(roll)

print("All rolls:", rolls)

count_6 = rolls.count(6)
count_1 = rolls.count(1)

two_sixes_in_a_row = 0
for i in range(len(rolls) - 1):
    if rolls[i] == 6 and rolls[i + 1] == 6:
        two_sixes_in_a_row += 1

print("Number of times rolled 6:", count_6)
print("Number of times rolled 1:", count_1)
print("Number of times rolled two 6s in a row:", two_sixes_in_a_row)

# Task 2: Jumping Jacks Workout
print("\nTask 2: Jumping Jacks Workout")

total_jumps = 100
completed = 0
set_size = 10

while completed < total_jumps:
    completed += set_size
    remaining = total_jumps - completed

    if remaining <= 0:
        print("Congratulations! You completed the workout.")
        break

    answer = input(f"You completed {completed} jumping jacks. Are you tired? (yes/y or no/n): ").strip().lower()

    if answer in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed} jumping jacks.")
            break
        else:
            print(f"{remaining} jumping jacks remaining. Keep going! 💪")
    else:
        print(f"{remaining} jumping jacks remaining. Keep going! 💪")
