# String Concatenation
str1 = "Hello"
str2 = "World"
str3 = str1 + str2
print(str3)

name = "pramod"
age = 23
#r = name + age #TypeError: can only concatenate str(not 'int') to str
r = name + str(age)
print(r)

g = "Hello"
g += "World"
print(g)

# Increment and Decrement ++, --
x = 5
x += 1
print(x)

y = 6
y -= 3
print(y)