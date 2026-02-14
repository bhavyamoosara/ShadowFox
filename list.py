# Initial Justice League list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

print("Initial Justice League:")
print(justice_league)

# 1. Number of members
print("\n1. Number of members in Justice League:")
print(len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")

print("\n2. After adding Batgirl and Nightwing:")
print(justice_league)

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

print("\n3. After making Wonder Woman the leader:")
print(justice_league)

# 4. Separate Aquaman and Flash by moving Green Lantern between them
justice_league.remove("Green Lantern")

# Find positions of Flash and Aquaman
flash_index = justice_league.index("Flash")
aquaman_index = justice_league.index("Aquaman")

# Insert Green Lantern between them
insert_position = min(flash_index, aquaman_index) + 1
justice_league.insert(insert_position, "Green Lantern")

print("\n4. After separating Aquaman and Flash with Green Lantern in between:")
print(justice_league)

# 5. Replace entire list with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]

print("\n5. New Justice League formed by Superman:")
print(justice_league)

# 6. Sort alphabetically and set new leader
justice_league.sort()

print("\n6. Justice League sorted alphabetically:")
print(justice_league)

print("\nNew leader (0th index):", justice_league[0])
