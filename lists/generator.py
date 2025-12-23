def my_generator():
    yield 1
    print("this is a generator")
    yield 2
    yield 3
    yield 4

for i in my_generator():
    print(i)
    
def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

# for  i in gen:
#     print(next(gen)) #this will not work next is used for manual traversing
for  i in gen:
    print(i)
