def add(*nums):
    result=0
    val= 25
    for x in nums:
        result +=x
    return result, val
numsum, z =add(20, 30, 10, 25, 36)
print(numsum, z)