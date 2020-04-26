def init_rows():
    rows = [[]]
    for i in range (1,82):
        rows[int(i/9)].append(i)
    print( rows)

init_rows()