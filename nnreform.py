def nnreform(CVResults):
    global gameElement
    gameElement = []
    if len(CVResults) > 0 and len(CVResults) < 20:
        obj = CVResults[0::4]
        for x in obj:
            gameElement.extend(x)
        extraVal = 10 - len(gameElement)
        for i in range(extraVal):
            gameElement.extend([0])
        
    elif len(CVResults) == 0:
        for i in range(5):
            gameElement.extend([0,0])
    return gameElement


