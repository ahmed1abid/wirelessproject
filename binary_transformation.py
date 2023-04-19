""" Apply the Cesar transformation to the ASCII input to perform (trivial) decoding 
""" 
def cesarDecode(userIdent,messEnc): 
    cesarKey = getCesarKey(userIdent)
    mess = []
    for elem in messEnc:
        rr = (elem - cesarKey)%(0xFF)
        mess.append(rr)
    return mess 


""" Convert a binary array into a Byte arrays 
"""
def bitToByte(array):
    mess = []
    nbWord = math.floor(len(array) / 8)
    for n in range(nbWord):
        w = 0
        for k in range(8):
            w += array[ n * 8 + k ] * 2**k
        mess.append(w)
    return mess 

""" Convert a byte array into a comprehensive string """
def toASCII(mess):
    word = []
    for x in mess:
        word.append(chr(int(x)))
    return word 


def getCesarKey(userId):
    # We have hard coded an interleaver between 1 and 26 and then we modulo 
	# Not using Cesar key system 
    cesarVect =   [5,
                   6,
                   10,
                   23,
                   18,
                   3,
                   9,
                   14,
                   2,
                   13,
                   8,
                   17,
                   0,
                   12,
                   4,
                   22,
                   11,
                   7,
                   20,
                   25,
                   15,
                   19,
                   24,
                   21,
                   1,
                   16];
    return cesarVect[(userId-1)%26] 


""" Unit testing for bit to byte transform 
"""
def test_bitToByte():
    seq = np.array([ 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0])
    mess = bitToByte(seq)
    assert mess == [22,96,82,54]
    assert bitToByte(np.array([1,0,1,0,1,0,1,1])) == [213]
    assert bitToByte(np.array([1,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0])) == [89, 5]
    assert bitToByte(np.array([0,1,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,1,1,0,0,0,1,0,0,1,0,0,0])) == [62, 176, 61, 18]
    assert bitToByte(np.array([1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,0,0,0,0,1,1,1,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,1,0,0,1,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,1,1])) == [113, 121, 56, 253, 101, 22, 18, 232]

test_bitToByte()
