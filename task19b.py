def half_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1,i+1):
            print(j, end=" ")

        print("\r")


rows = 5
half_pyramid(rows)