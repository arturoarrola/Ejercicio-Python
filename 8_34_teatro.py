def seats_in_theater(tot_cols, tot_rows, col, row):
    total_cols = tot_cols - col+1 
    total_row = tot_rows - row
    total = total_cols * total_row 
    return total
