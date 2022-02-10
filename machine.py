def isValid(x):
    if (len(x) != 8):
        return False
    cnt = 7
    while (x[cnt] != '='):
        cnt-=1
        if (cnt < 4):
            return False
    if (cnt == 7):
        return False
    
    expr = x[:cnt] + '=' + x[cnt:]
    try:
        u = eval(expr)
    except:
        return False
    if (isinstance(u,bool)):
        return u
    else:
        return False

def representation(x):
    a = []
    for i in range(8):
        a.append('*')
    for i in range(7,-1,-1):
        b = x//(3**i)
        a[i] = chr(b+48)
        x -= (b*(3**i))
    for i in range(8):
        if (a[i]=='0'):
            a[i]='*'
        elif (a[i]=='1'):
            a[i]='Y'
        else:
            a[i]='G'
    return a

'''
Verification of data correctness


lines_seen = set() # holds lines already seen
with open("validwords.txt", "r+") as f:
    d = f.readlines()
    f.seek(0)
    cnt = 0
    for i in d:
        if (len(i) != 9):
            print(len(i),cnt)
        cnt+=1
        if i not in lines_seen:
            f.write(i)
            lines_seen.add(i)
        else:
            print(i, cnt)
    f.truncate()

cnt = 0
total = 0
for i in ws:
    cnt+=1
    if (not isValid(i)):
        total+=1
        print(i,cnt)
'''

with open("validwords.txt") as file:
    ws = [line.rstrip() for line in file]

depict = []
for i in range(3**8):
    depict.append(''.join(representation(i)))

attempts = 6
while (attempts > 0):
    attempts-=1
    maxrem = 0
    maxremind = 0
    v = []
    remw = []
    for i in range(3**8):
        v.append(0)
        remw.append([])

    print('Your guess: ',end='')
    x = input()

    while (not isValid(x)):
        print('This guess does not compute or is wrong length!\nYour guess: ', end='')
        x = input()

    #calculate for every word in the dictionary the yellow and green spaces. then pick the one with the most
    for i in range(len(ws)):
        y = ws[i]
        #x: the input
        #y: the compared one
        yellow = []
        usedy = []
        green = []
        for j in range(8):
            if (x[j] == y[j]):
                green.append(j)
        for j in range(8):
            if (j in green):
                continue
            for k in range(8):
                if ((k in green) or j == k or (k in usedy)):
                    continue
                if (x[j] == y[k]):
                    yellow.append(j)
                    usedy.append(k)
                    break
        s = 0
        for j in green:
            s += 2 * (3**j)
        for j in yellow:
            s += (3**j)
        
        v[s] += 1
        remw[s].append(i)
        if (v[s] > maxrem):
            maxrem = v[s]
            maxremind = s

    #maxrem has the maximum number of words remaining
    #maxremind has the position of the index
    #v[maxremind] has the number of words
    #remw[maxremind] has the indexes of words in ws

    #print the result
    print(depict[maxremind])

    wsnew = []
    for i in remw[maxremind]:
        wsnew.append(ws[i])
    ws = wsnew
    print(ws)
    print(len(ws))





