""" 
G2_Assignment
5/29/25
"""

key = "SuperSecret!"

def key_scheduling(key):
    
    # key string converted to ascii in an array of length 256
    key_to_ascii = [ord(i) for i in key]
    k = []
    for i in range(256):
        k.append(key_to_ascii[i%len(key_to_ascii)])

   # s-box array 
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + k[i]) % 256
        s[i], s[j] = s[j], s[i]
    return s
    