
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
    print ("It is summer time!; let's go party")
else:
    print ("It must be autumn")

#endregion elseelseelse