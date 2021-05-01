# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 23:04:15 2021

@author: khodk
"""
def littleEndian(data, start, length, size_bin):
    print("Little Endian")
    print("Before logic = ", data)
    val = ""
    inv = ""
    i = 0
    while i <= size_bin:                  #This
        if i % 8 == 0:                    #code 
            inv = inv[::-1]               #creates
            val = val + inv               #mirror
            inv = ""                      #images
            if i == size_bin:             #of
                break;                    #each
        inv = inv + data[i]               #byte
        i = i + 1                         #
    print("After Logic = ", val)
    byte_no = start // 8
    rem_bytes = byte_no
    bit_no = start % 8
    rem_bits = 7 - bit_no
    total_rem = rem_bits + (rem_bytes * 8) #total number of bits to be removed
    val = val[total_rem: total_rem + length -1] #remove unneeded part
    print("Value =", val) #Final output
    return val
    
def bigEndian(data, start, length, size_bin):
    print("Big Endian")
    byte_no = start // 8
    rem_bytes = 7 - byte_no
    bit_no = start % 8
    rem_bits = start % 8
    total_rem = rem_bits + (rem_bytes * 8)
    data = data[0:(size_bin-1)-total_rem]
    data = data[::-1] #invert the binary data for big endian
    val = data[0:length-1] #get substring with start and end
    print("Value =", val)
    return val

def getBinaryEq(hexaCode):
    size_bin = len(hexaCode) * 4 #this will be total size of the message in bits
    bindata = bin(int(hexaCode, 16))[2:] 
    i = 0
    emp = ""
    while i < size_bin - len(bindata):
        emp = emp + "0"
        i = i + 1
    data = emp + str(bindata) #binary form of the Hexadecimal
    return data, size_bin
    
#Program starts here
#These three values are derived from log file and dbc   
hexaCode = "00B411204510C101"
bit_number = 51
length = 12
#

data, size_bin = getBinaryEq(hexaCode) #get binary equivalent of the hexadecimal log and it's size

value_le = littleEndian(data, bit_number, length, size_bin)
print("")
value_be = bigEndian(data, bit_number, length, size_bin)