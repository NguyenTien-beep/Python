mytuple = ("apple", "banana", "cherry")
myit= iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
# myit = iter(mystr)
# 
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
for x in mytuple:
    print(x)

class Number:
    
    def __iter__(self): # tra ve gia tri chinh no
        self.a=1
        return self
    def __next__(self): # tra ve gia tri tiep theo
        if self.a<5:
            x=self.a
            self.a +=1
            return x
        else:
            raise StopIteration # thong bao cho python la het du lieu
myclass=Number()
myiter=iter(myclass) # chuyen ve iterator
# print(next(myiter))
# print(next(myiter))
for x in myiter:
    print(x)