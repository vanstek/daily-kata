#Data Reverse
#Level: 6 kyu
'''
A stream of data is received and needs to be reversed.

Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)

should become:

10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)
'''


def data_reverse(data):
    i = 0
    rvr = []
    while i < len(data):
        back = len(data) - i
        back2 = back - 8
        rvr += data[back2:back]
        i += 8
    return rvr
