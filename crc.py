""" Check the CRC polynom. Returns 1 if the CRC is correct and 0 otherwise """
def crc_decode(data,poly):
    data2 = np.copy(data)       # Copy of working vector 
    lenR  = len(data);           # length of the received codeword
    lenGW = len(poly);          # length of the generator
    for i in range(lenR - lenGW + 1):
        if data2[i] == 1:
            data2[i:i+lenGW:1] = np.logical_xor(data2[i:i+lenGW:1],poly);
	# syndrome is now equal to the remainder of xor division
    syndrome = data2[ lenR - lenGW + 1: lenR : 1];
    print(syndrome)
    if all(syndrome == 0x00):
        err = 1
    else: 
        err = 0;
    print(err)
    return err


""" Create the CRC polynom of size crcSize, based on the positions of the 1 in the CRC polynoms """
def create_g(crcSize,positions):
    gx = np.zeros(1+crcSize)
    gx[0] = 1
    for k in positions:
        gx[k] = 1
    return gx 

""" Returns the generated CRC polynoms for the given size """
def get_crc_poly(crcSize):
    if crcSize == 8:
        gx = create_g(crcSize,[1,2,8])
    elif crcSize == 16:
        gx = create_g(crcSize,[2,15,16])
    elif crcSize == 24:
        gx = create_g(crcSize,[1,3,6,7,8,10,11,13,14,16,18,19,20,22,24])
    elif crcSize == 32:
        gx = create_g(crcSize,[1,2,4,5,7,8,10,11,12,16,22,23,26,32])
    return gx


def test_crcGen():
    gx = get_crc_poly(8)
    assert len(gx) == 9 
    assert gx[0] == 1 
    assert sum(gx) == 4
    print(gx)

def test_crcDecode():
    sizeCRC = 8
    gx = get_crc_poly(sizeCRC)
    seq = np.array([0,1,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1])
    crc = crc_decode(seq,gx)
    assert crc == 1
    seq = np.array([1,1,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1])
    crc = crc_decode(seq,gx)
    assert crc == 0



test_crcGen()
test_crcDecode()
