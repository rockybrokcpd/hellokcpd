def KMPSearch(pat, txt):
    a = len(pat)
    b = len(txt)
    lps = [0] * a #pi table for pattern
    j = 0
    calcLPSArray(pat, a, lps) #calculating pi t
    i = 0
    while i < b: #check patrn match
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == a:
            print("Found pattern at index " + str(i - j))
            j = lps[j - 1]
        elif i < b and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

def calcLPSArray(pat, a, lps):
    len = 0
    lps[0]
    i = 1
    while i < a:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1
txt = input("enter the string:")
pat = input("enter the pattern:")
KMPSearch(pat,txt)