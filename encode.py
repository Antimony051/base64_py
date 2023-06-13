base64_="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

string_input=input()
arr=[]
for x in string_input:
    val=ord(x)
    arr.append(val)

bytes_=""
for x in arr:
    bytes_+='{0:08b}'.format(x)

if len(bytes_)%6!=0:
    bytes_+="0"*(6-len(bytes_)%6)
for x in range(0,len(bytes_),6):
    print(base64_[int(bytes_[x:x+6],2)],end="")

if len(arr)%3 !=0:
    if len(arr)%3 ==1:
        print("==")
    else:
        print("=")
else: print()
