def is_prime(num):
    is_true = True  # ← Changed this line
    for i in range(2, num):
        if num % i == 0:
            is_true = False
            break
    print(is_true)


is_prime(73)
