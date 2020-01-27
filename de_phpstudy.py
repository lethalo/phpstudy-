# coding:utf-8


# import bytes




def decode1(data):
    data = data.strip()
    # data = bytes.fromhex(data)
    data = data.decode("hex")
    length = ord(data[1])
    print length
    if len(data)%4 !=0:
        return "decode fail"
        
    # print (len(data))
    ret = ""
    for i in range(0, len(data), 4):
        # ret += chr(data[i + 0] ^ data[i +2]) + chr(data[i +1] ^ data[i +3])
        # ret += chr(ord(data[i + 0]) ^ ord(data[i +2])) + chr(ord(data[i +1]) ^ ord(data[i +3]))
        ret +=  chr(ord(data[i +1]) ^ ord(data[i +3])) + chr(ord(data[i + 0]) ^ ord(data[i +2]))
    print len(ret[:length * 2])
    return ret[:length * 2]
 
 
data = "00035DF1002991644823374D18BE6A1067840ED64AE115713D6C2B252CD64127"
# print (unicode(decode(data)).decode("unicode_escape"))
s = decode1(data)
print s.decode("unicode-escape")
fp = open("dd.txt", "wb")
fp.write(decode1(data))
fp.close()