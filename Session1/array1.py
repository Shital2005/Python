#input = [1,2,3,4]
#output = [24,12,8,6]

def product_array(input):
    output=[]
    for i in range(len(input)):
        product=1
        for j in range(len(input)):
            if i!=j:
                product*=input[j]
        output.append(product)
    return output
