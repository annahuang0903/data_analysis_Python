##
## File: week01a.py (STAT 3250)
##

#%%  This is the start of a cell.  It's
##   frequently handy to split your code 
##   into cells.  It also makes the 
##   keyboard shortcuts work correctly.

#%%  Each #%% ends the preceding cell and
##   starts the next.

####   Arithmetic with Python

2+5  # The sum of 2 and 5

#%%  

-3*7  # The product of -3 and 7

#%% 

15/7  # 15 divided by 7; 

#%%

2**5  # 2 to the power 5; ^ is not exponentiation!!

#%% The "%" operator gives the remainder.  

19 % 4
1234567 % 100

#%%  Python only displays the last calculated value
##   in the iPython console

2**5
7-4

#%%  Using "print" will display multple values (and other
##   stuff too, as we'll see later.)

print(2**5)
print(7-4)

#%%

####  Defining variables

x = 13
print(x)  # Good, but not clear this is x
print('x = %d.' % x)  # Displays x with label as a decimal

7*x  # Arithmetic can be performed on variables

y = 93
x**y  # Integers can be big!

#%%
####  New Variables From Old

x = 10   # Set x equal to 10
y = x    # Set y equal to x
print(y) # Display y; we see that y is value of x

x = 29   # Change x to 29
print(x) # The new value of x
print(y) # y does not change

#%%

####  Lists

list01 = [2,5,1,7,4,6,3]
print(list01)

#%%  List elements

list01[0]  # The 1st entry -- counting starts at 0

list01[3]  # The 4th entry

list01[4] = -8  # Redefine 5th entry to be -8
print(list01)

#%%  Adding and removing list elements

list01.append(12)  # Append 12 to end of mylist
print(list01)

list01.insert(2, 13)  # Insert 13 in the 3rd position
print(list01)

list01.pop(5)  # Remove the 6th entry from mylist
print(list01)

list01.remove(7)  # Removes first occurence of 7
print(list01)

#%% Slicing -- Extracting and replacing sublists

list01 = [2,5,1,7,4,6,3]  # Reset definition for list01
print(list01)

## Note that none of these below changes list01

list01[2:5] # The 3rd, 4th, and 5th entries

list01[:4]  # Entries first to 4  

list01[2:]  # Entries 3 to end

list01[-5:]  # Last 5 entries

list01[:-2] # Entries up to 2nd from end

list01[::2] # Every other entry

list01[::3] # Every third entry

list01[::-1] # Every entry, but in reverse

# If we want to actually change list01:
list01 = list01[::-1]
print(list01)

#%%   Other list operations

print(list01)
list02 = [5,7,-3,2]  # Define a new list

biglist = list01+list02 # Concatenate lists
print(biglist)

biglist.sort()  # Sort list from smallest to largest
print(biglist)  # Note that this command changed biglist

biglist.reverse()  # Reverse the order of the sorted list
print(biglist)     # This command also changed biglist

biglist.count(5)  # Count the number of times 5 appears

biglist.index(2)  # Location of first 2 in list 

#%%  A list caution

x = [1,2,3] # Set x to a list
y = x       # Set y equal to x
print(x)
print(y)

x[1] = 37
print(x)
print(y)  # y change too!

y[1] = -23
print(y)
print(x)  # x is changed

# To prevent above behavior:
x = [1,2,3] # Reset x to a [1,2,3]
y = list(x)  # Set y equal to x
print(y)
x[1] = 19   # Change 2nd entry of x
print(x)   # x is changed
print(y)   # This time y is not changed

#%%










