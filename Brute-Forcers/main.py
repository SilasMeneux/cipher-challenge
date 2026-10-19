import Caesar

mode = input("Enter the mode for brute forcing:\n1. Number Key\n2. Word Key")
cipherType = input("Enter the mode for brute forcing:\n1. Caesar Cipher") #add more later

cipherText = "Jg if ibe bozuijoh dpogjefoujbm up tbz, if xspuf ju jo djqifs, uibu jt, cz tp dibohjoh uif psefs pg uif mfuufst pg uif bmqibcfu, uibu opu b xpse dpvme cf nbef pvu."

NUMERICALBRUTEFORCELIMIT = 100

def AttemptDecodeAlphabeticKey(keyLength, cipherType, cipherText):
    pass

def AttemptDecodeNumericKey(cipherText):
    for i in range(NUMERICALBRUTEFORCELIMIT):
        if(("If" in(Caesar.decode(i, cipherText))) and ("anything" in (Caesar.decode(i, cipherText)))):
            print((Caesar.decode(i, cipherText)))


if mode == "1":
    AttemptDecodeNumericKey(cipherText)



