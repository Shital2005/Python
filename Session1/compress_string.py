#input= "aaabbbcccc"
#outout= "a3b3c4"
def compress_String(input):
    count=1
    output=""
    for i in range(1,len(input)):
        if input[i]==input[i-1]:
            count+=1
        else:
            output+=input[i-1]+str(count)
            count=1
    output+=input[i]+str(count)
    return output

a = compress_String("aaabb")
print(a)