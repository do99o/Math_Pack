        # Parameters
        print("What is the maximum size for the a, b, and c values? [a.e. 60]")
        int_max = int(input())
        print("What is the minimum size for the a, b, and c values? [a.e. -45]")
        int_min = int(input())
        while True:
            # generate a, b, c values
            a = random.randint(int_min, int_max)
            b = random.randint(int_min, int_max)
            c = random.randint(int_min, int_max)
            neg = b ** 2 - 4 * a * c
            if neg > 0:
                ans1 = ((b * -1) + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
                ans2 = ((b * -1) - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        if neg < 0:
            break