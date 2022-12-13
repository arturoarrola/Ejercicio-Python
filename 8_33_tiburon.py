def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin == True:
        shark_speed/=2
    sharktime = shark_distance/shark_speed
    mytime = pontoon_distance/you_speed
    if  sharktime < mytime:
        return "Shark Bait!"
    else:
        return "Alive!"
