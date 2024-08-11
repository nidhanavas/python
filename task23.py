def half_triangle(rows):
    start_num = 1
    for i in range(rows):
        for j in range(i + 1):
            print(start_num, end=" ")
            start_num += 2
        print()

rows = 5
half_triangle(rows)