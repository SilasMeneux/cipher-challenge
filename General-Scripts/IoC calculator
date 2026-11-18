def IoC(text):
    text=(text.replace(" ","")).lower()
    ioc=0
    N=len(text)
    letters="abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        n=text.count(letters[i])
        ioc+=(n*(n-1))/(N*(N-1))
    ioc*=26
    return ioc