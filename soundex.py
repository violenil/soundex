'''
Soundex is an algorithm for phonetic hashing. It can be used for equivalence
classing: for normalizing words to find matches, ie. to map all corresponding
spellings to one (phonetic equivalence).
'''
def convSoundex(w):
    soundex = w[:1]
    for c in w:
        if c in 'AEIOUHWY':
            soundex += '0'
        elif c in 'BFPV':
            soundex += '1'
        elif c in 'CGJKQSXZ':
            soundex += '2'
        elif c in 'DT':
            soundex += '3'
        elif c == 'L':
            soundex += '4'
        elif c in 'MN':
            soundex += '5'
        elif c == 'R':
            soundex += '6'
    newSoundex = soundex[:1]
    for s in range(1, len(soundex)):
        if soundex[s] != soundex[s-1] and soundex[s] != '0':
            newSoundex += soundex[s]
    newSoundex += '000'
    return(newSoundex[:4])

word = input("Please enter word to convert to soundex: ")
print("This is the corresponding soundex: " + convSoundex(word.upper()))
