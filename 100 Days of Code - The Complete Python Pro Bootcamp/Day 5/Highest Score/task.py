student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

max_val = 0

for hold_val in student_scores:
    if hold_val > max_val:
        max_val = hold_val

print(max_val)
