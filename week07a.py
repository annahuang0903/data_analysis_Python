##
## File: week7a.py (STAT 3250)
## Topic: String operations and reading text files
##

#### Introduction to String operations

teststr = "There    are two ways   of constructing a software design." 

# Extract substrings in specific positions
teststr[10:30] # Characters from positions indexed by 10-29
teststr[10:30:2] # Every other character
teststr[:20] # The first 20 characters
teststr[50:] # From the position indexed by 50 to the end
teststr[:-20] # All but the last 20 characters

teststr[5:10]+teststr[15:20] # Concatenate strings

teststr.upper() # Shout!
teststr.lower() # Whisper?

teststr.index("o") # Index for first "o".
teststr.count("o") # Number of "o"s in str.
teststr.find("o") # Same as index
teststr.replace("are", "were") # Replace a substring

teststr.startswith("Hello")
teststr.startswith("The")
teststr.endswith("ign")
teststr.endswith("ign.")

testspl = teststr.split(" ")
testspl.replace("are", "were") # Replace a substring

teststr.split(" ")
teststr.split("s")
teststr.split() # The default is spaces; extra spaces discarded
"ABCD".join(teststr.split("s")) # Splice strings together, with "ABCD"
"".join(teststr.split("s")) # Splice strings together, with no space
"s".join(teststr.split("s")) # Splice strings together, with s back in place

#%%

#### Reading text files

# The code below will read a text file, and put
# each line from the text file into a list
# element.
lines = open('transactions.txt').read().splitlines()
lines[0:10]

# Here are the first 10 lines of the file.
for i in range(10):
    print("Line",i+1) # Print line number
    print(lines[i]) # Print contents of line
    print("") # Add an extra line for space

# We can iterate through "lines" to pick out
# items of interest.

# This loop will print every line that contains
# the substring "AnSwEr" and the number found.
ct = 0
for aline in lines:
    if aline.count("AnSwEr") > 0:
        print(aline)
        ct += 1
print("Number found:",ct)

# This loop will print the date and time 
# for any line starting with such an expression.
# It will also count how many there are.

ct = 0
for aline in lines:
    if aline.count(' 2014 ') > 0:
        sub = aline.split('2014')[0]+'2014'
        print(sub)
        ct += 1
print("Number found:",ct)





