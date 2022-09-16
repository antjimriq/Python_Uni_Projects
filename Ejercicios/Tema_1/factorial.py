def factoriales(n):
    i,f = 1,1
    while i<=n:
        f=f*i
        i= i+1
    return f
a= int(input("De que valor quieres calcular el factorial: "))
print("El factorial de", a, "es", factoriales(a))

