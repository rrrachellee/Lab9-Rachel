def decode (passC):
    #already should be an integer at this point
    decoded = []
    for i in range (len(passC)):
        meow = passC[i] - 3
        decoded.append(meow)
    return decoded 
