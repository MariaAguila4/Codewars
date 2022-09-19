def seats_in_theater(tot_cols, tot_rows, col, row):
    return ((tot_cols -(col -1)) * (tot_rows - row))

tot_cols = 16
tot_rows = 11
col = 5
row = 3
print(seats_in_theater(tot_cols, tot_rows, col, row))
print(seats_in_theater(1,1,1,1))
print(seats_in_theater(13,6,8,3))