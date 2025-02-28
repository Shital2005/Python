# input : 578378923
# output: 3

# def repeated_digits_count():

#     n = "578378923"
#     count = 0
#     repeatcount = 0
#     for i in n:
#         count += 1
#         if count > 1:
#             repeatcount += 1

#         if repeatcount > 1:
#             print("repeated digits count:",repeatcount)
#             break    
#     print(repeatcount)

# repeated_digits_count()

def repeated_digits_count():
    n = "578378923"
    repeatcount = 0
    for i in n:
        count = 0 
        for j in n:
            if i == j:
                count += 1
    
        if count > 1:
            repeatcount += 1
            n = n.replace(i, "") 
    
    print("Repeated digits count:", repeatcount)

repeated_digits_count()






