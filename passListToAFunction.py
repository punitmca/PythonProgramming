def count(lst):
    even =0
    odd =0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd


lst=[2,33,4,5,6,7,9,11,21]
even,odd = count(lst)
print('Even: {} and Odd: {}'.format(even,odd))



