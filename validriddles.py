f = open("validwords.txt","a")

#POSITIVE NUMBERS

#addition (single)
for i in range(0,10):
    for j in range(91,100):
        k = i+j
        res = str(i) + '+' + str(j) + '=' + str(k)
        if (len(res) == 8):
            f.write(res + '\n')
for i in range(10,100):
    for j in range(0,100):
        k = i+j
        res = str(i) + '+' + str(j) + '=' + str(k)
        if (len(res) == 8):
            f.write(res + '\n')
            
#subtraction (single)
for i in range(10,100):
    for j in range(10,100):
        k = i-j
        if (k<0):
            continue
        res = str(i) + '-' + str(j) + '=' + str(k)
        if (len(res) == 8):
            f.write(res + '\n')
for i in range(100,1000):
    for j in range(0,100):
        k = i-j
        res = str(i) + '-' + str(j) + '=' + str(k)
        if (len(res) == 8):
            f.write(res + '\n')

#multiplication (single)
for i in range(10000):

    res = str(0) + '*' + str(i) + '=' + str(0)
    if (len(res) == 8):
        f.write(res + '\n')
    res = str(i) + '*' + str(0) + '=' + str(0)
    if (len(res) == 8):
        f.write(res + '\n')
for i in range(1,10):
    for j in range(10,100):
        k = i*j
        res = str(i) + '*' + str(j) + '=' + str(k)
        if (len(res) == 8):
            f.write(res + '\n')
for i in range(10,100):
    for j in range(1,10):
        k = i*j
        res = str(i) + '*' + str(j) + '=' + str(k)
        if (len(res) == 8):
            f.write(res + '\n')

#division (single)
for i in range(100,1000):
    for j in range(1,100):
        if (i%j != 0):
            continue
        k = i//j
        res = str(i) + '/' + str(j) + '=' + str(k)
        if (len(res) == 8):
            f.write(res + '\n')


#addition (double)
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            l = i+j+k
            res = str(i) + '+' + str(j) + '+' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#subtraction (double)
for i in range(10,100):
    for j in range(0,10):
        for k in range(0,10):
            l = i-j-k
            if (l < 0):
                continue
            res = str(i) + '-' + str(j) + '-' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#addition then subtraction (double)
for i in range(0,100):
    for j in range(0,100):
        for k in range(0,10):
            l = i+j-k
            if (l < 0):
                continue
            res = str(i) + '+' + str(j) + '-' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#subtraction then addition (double)
for i in range(0,100):
    for j in range(0,10):
        for k in range(0,100):
            l = i-j+k
            if (l < 0):
                continue
            res = str(i) + '-' + str(j) + '+' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#multiplication (double)
for i in range(0,100):
    for j in range(0,100):
        for k in range(0,100):
            l = i*j*k
            res = str(i) + '*' + str(j) + '*' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#addition then multiplication (double)
for i in range(0,100):
    for j in range(0,100):
        for k in range(0,100):
            l = i+j*k
            res = str(i) + '+' + str(j) + '*' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#multiplication then addition (double)
for i in range(0,100):
    for j in range(0,100):
        for k in range(0,100):
            l = i*j+k
            res = str(i) + '*' + str(j) + '+' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#subtraction then multiplication (double)
for i in range(0,100):
    for j in range(0,100):
        for k in range(0,100):
            l = i-j*k
            if (l < 0):
                continue
            res = str(i) + '-' + str(j) + '*' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#multiplication then subtraction (double)
for i in range(0,100):
    for j in range(0,100):
        for k in range(0,100):
            l = i*j-k
            if (l < 0):
                continue
            res = str(i) + '*' + str(j) + '-' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#division (double)
for i in range(10,100):
    for j in range(1,10):
        for k in range(1,10):
            if (i%j != 0):
                continue
            else:
                u = i//j
                if (u%k != 0):
                    continue
            l = (i//j)//k
            res = str(i) + '/' + str(j) + '/' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')
for i in range(10000):
    res = str(0) + '/' + str(i) + '=' + str(0)
    if (len(res) == 8):
        f.write(res + '\n')
for i in range(1,100):
    for j in range(1,100):
        res = str(0) + '/' + str(i) + '/' + str(j) + '=' + str(0)
        if (len(res) == 8):
            f.write(res + '\n')
    for j in range(0,100):
        res = str(0) + '/' + str(i) + '+' + str(j) + '=' + str(j)
        if (len(res) == 8):
            f.write(res + '\n')
    res = str(0) + '/' + str(i) + '-0=0'
    if (len(res) == 8):
        f.write(res + '\n')
    for j in range(0,100):
        res = str(0) + '/' + str(i) + '*' + str(j) + '=' + str(0)
        if (len(res) == 8):
            f.write(res + '\n')
for i in range(1,100):
    for j in range(0,100):
        res = str(j) + '+' + str(0) + '/' + str(i) + '=' + str(j)
        if (len(res) == 8):
            f.write(res + '\n')
    for j in range(0,100):
        res = str(j) + '-' + str(0) + '/' + str(i) + '=' + str(j)
        if (len(res) == 8):
            f.write(res + '\n')
    for j in range(0,100):
        res = str(j) + '*' + str(0) + '/' + str(i) + '=' + str(0)
        if (len(res) == 8):
            f.write(res + '\n')

#addition then division (double)
for i in range(0,100):
    for j in range(1,100):
        for k in range(1,10):
            if (j%k != 0):
                continue
            l = i+(j//k)
            res = str(i) + '+' + str(j) + '/' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#division then addition (double)
for i in range(1,100):
    for j in range(1,100):
        for k in range(0,100):
            if (i%j != 0):
                continue
            l = (i//j)+k
            res = str(i) + '/' + str(j) + '+' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#subtraction then division (double)
for i in range(0,100):
    for j in range(1,100):
        for k in range(1,100):
            if (j%k != 0):
                continue
            l = i - (j//k)
            if (l < 0):
                continue
            res = str(i) + '-' + str(j) + '/' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#division then subtraction (double)
for i in range(1,100):
    for j in range(1,100):
        for k in range(0,100):
            if (i%j != 0):
                continue
            l = (i//j) - k
            if (l < 0):
                continue
            res = str(i) + '/' + str(j) + '-' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#multiplication then division (double)
for i in range(0,100):
    for j in range(1,100):
        for k in range(1,100):
            u = i*j
            if (u%k != 0):
                continue
            l = (i*j)//k
            res = str(i) + '*' + str(j) + '/' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#division then multiplication (double)
for i in range(1,100):
    for j in range(1,100):
        for k in range(0,100):
            if (i%j != 0):
                continue
            l = (i//j)*k
            res = str(i) + '/' + str(j) + '*' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')
























# NEGATIVE NUMBERS AS RESULT ONLY

#subtraction (single)
for i in range(-9,100):
    for j in range(-9,1000):
        k = i-j
        if (k >= 0):
            continue
        res = str(i) + '-' + str(j) + '=' + str(k)
        if (len(res) == 8):
            f.write(res + '\n')

#subtraction then addition (double)
for i in range(0,100):
    for j in range(0,100):
        for k in range(0,100):
            l = i-j+k
            if (l>=0):
                continue
            res = str(i) + '-' + str(j) + '+' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#addition then subtraction (double)
for i in range(0,100):
    for j in range(0,100):
        for k in range(0,100):
            l = i+j-k
            if (l>=0):
                continue
            res = str(i) + '+' + str(j) + '-' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#subtraction then multiplication (double)
for i in range(0,100):
    for j in range(0,100):
        for k in range(0,100):
            l = i-j*k
            if (l>=0):
                continue
            res = str(i) + '-' + str(j) + '*' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#multiplication then subtraction (double)
for i in range(0,100):
    for j in range(0,100):
        for k in range(0,100):
            l = i*j-k
            if (l>=0):
                continue
            res = str(i) + '*' + str(j) + '-' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')
                
#subtraction then division (double)
for i in range(0,100):
    for j in range(0,100):
        for k in range(1,100):
            if (j%k != 0):
                continue
            l = i-(j//k)
            if (l>=0):
                continue
            res = str(i) + '-' + str(j) + '/' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#division then subtraction (double)
for i in range(0,100):
    for j in range(1,100):
        for k in range(0,100):
            if (i%j != 0):
                continue
            l = (i//j)+k
            if (l>=0):
                continue
            res = str(i) + '/' + str(j) + '-' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')



















# FIRST NUMBER IS NEGATIVE

#addition (single)
for i in range(-99,0):
    for j in range(0,100):
        k = i+j
        res = str(i) + '+' + str(j) + '=' + str(k)
        if (len(res) == 8):
            f.write(res + '\n')

#subtraction (single)
for i in range(-9,0):
    for j in range(1,10):
        k = i-j
        res = str(i) + '-' + str(j) + '=' + str(k)
        if (len(res) == 8):
            f.write(res + '\n')

#multiplication (single)
for i in range(-999,-99):
    res = str(i) + '*0=0'
    if (len(res) == 8):
        f.write(res + '\n')
for i in range(-9,0):
    for j in range(1,10):
        k = i*j
        res = str(i) + '*' + str(j) + '=' + str(k)
        if (len(res) == 8):
            f.write(res + '\n')

#division (single)
for i in range(-99,-9):
    for j in range(1,10):
        u = i*-1
        if (u%j != 0):
            continue
        k = i//j
        res = str(i) + '/' + str(j) + '=' + str(k)
        if (len(res) == 8):
            f.write(res + '\n')

#addition (double)
for i in range(-9,0):
    for j in range(0,10):
        for k in range(0,10):
            l = i+j+k
            res = str(i) + '+' + str(j) + '+' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#addition then subtraction (double)
for i in range(-9,0):
    for j in range(0,10):
        for k in range(0,10):
            l = i+j-k
            res = str(i) + '+' + str(j) + '-' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#addition then multiplication (double)
for i in range(-9,0):
    for j in range(0,10):
        for k in range(0,10):
            l = i+j*k
            res = str(i) + '+' + str(j) + '*' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#addition then division (double)
for i in range(-9,0):
    for j in range(0,10):
        for k in range(1,10):
            if (j%k != 0):
                continue
            l = i+(j//k)
            res = str(i) + '+' + str(j) + '/' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#subtraction then addition (double)
for i in range(-9,0):
    for j in range(0,10):
        for k in range(0,10):
            l = i-j+k
            res = str(i) + '-' + str(j) + '+' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#multiplication then addition (double)
for i in range(-9,0):
    for j in range(0,10):
        for k in range(0,10):
            l = i*j+k
            res = str(i) + '*' + str(j) + '+' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')

#division then addition (double)
for i in range(-9,0):
    for j in range(1,10):
        for k in range(0,10):
            if (i%j != 0):
                continue
            l = (i//j) + k
            res = str(i) + '/' + str(j) + '+' + str(k) + '=' + str(l)
            if (len(res) == 8):
                f.write(res + '\n')