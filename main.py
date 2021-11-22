def pangkat(a, b):
    hasil = a
    
    if b < 0:
        
        b = abs(b)
        
        return 1 / (hitungPow(a, b))
    else:
        for i in range(b - 1) :
            hasil *= a    

        return hasil

a = int(input('Please enter the numbers : '))
b = int(input('Please enter the rank number : '))

print(f'pangkat of {a} and {b} is {pangkat(a, b)}')
