msg = "Hello world"
print(msg)

name = "Jeff"
print("my name %s " % name)
age = 42
word = 'egg' #i don't think double or single quotes matter
"""
multi line comment!
wahoo
i am so excited everyone
"""
#s = string, %d = int, %f = float, %.<dig>f = float w/<dig> digits, %x = hex int
price = 53.44
print("%s is %d years old. He pays %.2f for his %s" % (name, age, price, word))

if age <= 21:
    print("goodness me how young")
else:
    print ("you are mildly old")
testarray = ['a', 'b', 'c']
print (testarray is ['a', 'b', 'c'], testarray == ['a', 'b', 'c']) #is checks reference, == checks value
#there's no ! for false, it's the word 'not'