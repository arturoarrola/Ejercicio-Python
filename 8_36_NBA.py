def nba_extrap(ppg, mpg):
    if mpg == 0:
        return 0
    xgame=ppg/mpg
    total = xgame * 48
    total=round(total,1)
    return total
