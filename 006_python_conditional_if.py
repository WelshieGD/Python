
# region simpleif
# Simple if

myfavband = "The Jam"
bandplaying = "Boys Zone"

if bandplaying != myfavband:
    print("Not going")

# Case sensitivity - returns not going
myfavband = "The Jam"
bandplaying = "the jam"

if bandplaying != myfavband:
    print("Not going")

# Switch everything to lower case to check .. 

myfavband = "The Jam"
bandplaying = "the jam"

if bandplaying.lower() != myfavband.lower():
    print("Not going")

else:
    print("Going")

#endregion simpleif


#region ifinwithlist
bandsplayingtoday = ['The Jam', 'The Clash', 'Oasis']
myfavband2 = 'The Clash'

if myfavband2 in bandsplayingtoday:
    print(f"\nI'm going out tonight\n")
else:
    print(f"\nI'm staying in tonight\n")

#endregion ifinwithlist

#region elseelseelse
# Use when only one correct answer \ only one condition can ever evaluate to true as this will stop once a match is made. 
month = "june"
winter = ['December','January','February']
spring = ['March','April','May']
summer = ['June','July','August']
autumn = ['September','October','November']

print (month.title())

if month.title() in winter:
    print ("It is winter time; let's go play in the snow")
elif month.title() in spring:
    print ("It is spring time; everythings gone green")
elif month.title() in summer:
    print ("It is summer time!; let's go party\n")
else:
    print ("It must be autumn\n")

#endregion elseelseelse

#region checkiflistisempty
anemptylist = []

# Returns true if contains one or more items
if anemptylist:
    print("This is not an empty list")
else:
        print("This is an empty list")

        

#endregion checkiflistisempty