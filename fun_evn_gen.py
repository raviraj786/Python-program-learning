def evn_gen(limt):
    li = []
    for i in range(2, limt + 1 , 2):
        yield i
  

    

for num in  evn_gen(10):
    print(num)  