#Complementary DNA
#Level: 7 kyu
'''
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. 
DNA strand is never empty or there is no DNA at all (again, except for Haskell).
'''
def DNA_strand(dna):
    dict = {
        'A':'T',
        'T':'A',
        'C':'G',
        'G':'C'
    }
    return ''.join(dict[x] for x in dna)
