def kampResultat(scoringerLagA, scoringerLagB):
    if(scoringerLagA > scoringerLagB):
        return "hjemme"
    elif(scoringerLagA < scoringerLagB):
        return "borte"
    return "uavgjort"
