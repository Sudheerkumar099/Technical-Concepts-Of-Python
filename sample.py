d = {"name":"sudheer","age":22,"branch":"cse"}
def fun(*d):
    for j in d:
        d1 ={print (i,j[i]) for i in j}

fun({"name":"sudheer","age":22,"branch":"cse"},{"name":"vilas","age":22,"branch":"cse"},{"name":"abc","age":22,"branch":"cse"})
