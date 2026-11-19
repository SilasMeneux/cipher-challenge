import ciphertext_cleanup

def IoC(text):
    text = ciphertext_cleanup.clean_ciphertext(text)
    ioc=0
    N=len(text)
    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        n=text.count(letters[i])
        ioc+=(n*(n-1))/(N*(N-1))
    ioc*=26
    return ioc