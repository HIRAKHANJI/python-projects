import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

name_picker = random.randint(0, 4)

print(friends[name_picker])
print(random.choice(friends))

