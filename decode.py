def strinp():
    return(input().split())

base64_="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

input_string=strinp()[0]
NoOfEquals=input_string.count("=")

bytes_=""
last_24_bytes=""
for x in range(len(input_string)-4):
    cur_chr=input_string[x]
    bytes_+='{0:06b}'.format(base64_.index(cur_chr))

for x in range(len(input_string)-4,len(input_string)): # handel the last 4 chars xxxx or xxx= or xx==
    cur_chr=input_string[x]
    if input_string[x]!="=":
        last_24_bytes+='{0:06b}'.format(base64_.index(cur_chr))
    else:
        if NoOfEquals==1:
            bytes_+=last_24_bytes[:16]
        else:
            bytes_+=last_24_bytes[:8]
        break
for x in range(0,len(bytes_),8):
    print(chr(int(bytes_[x:x+8],2)),end="")
