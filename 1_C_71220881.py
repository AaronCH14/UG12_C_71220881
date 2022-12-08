kata =str(input("Masukkan kata atau angka:"))
def reserve (kata):
    str=""
    for i in kata:
        str = i + str
    return str
print (reserve(kata))


        
