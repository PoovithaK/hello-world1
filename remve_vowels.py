test = 'ReverseMe VowelsRemoved'
rev=test[::-1]
print("Reversed string=")
print rev
for eachLetter in rev: 
        if eachLetter in ['a','e','i','o','u']:
                rev = rev.replace(eachLetter, '')
print("String with vowels removed=")
print rev
