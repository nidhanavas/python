def half_pyramid(rows):
    for i in range(1, rows + 1):
        print("* " * i)
def upside_down_half_pyramid(rows):
    for i in range(rows, 0, -1):
        print("* " * i)
rows = 5
half_pyramid(rows)
upside_down_half_pyramid(rows)