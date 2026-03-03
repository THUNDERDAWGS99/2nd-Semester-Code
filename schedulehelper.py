import random

def find_avalible_times(people_times):
    # Start with the first person's times
    common = people_times[0]
    # Intersect with each additional person's times
    for times in people_times[1:]:
        common = common.intersection(times)
    return common


# All possible hours someone *might* be available
Random_hours = ["9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm"]

# Randomly generate each person's schedule
people = {
    "Dontavious Williams XI": set(random.sample(Random_hours, random.randint(3, 6))),
    "Deshawn Dequarius": set(random.sample(Random_hours, random.randint(3, 6))),
    "Bob": set(random.sample(Random_hours, random.randint(3, 6)))
}

# Shows the people's available times
print("avaliable hours:")
for name, times in people.items():
    print(f"  {name}: {sorted(times)}")

# Sees what available times are shared
all_time_sets = list(people.values())
shared_times = find_avalible_times(all_time_sets)

print("\nshared time:")
if shared_times:
    print("  Times everyone can meet around:", sorted(shared_times))
else:
    print("  There is no hour that everyone can meet.")
