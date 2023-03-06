# Dictionary is a colelction of key \ value pairs
# A value can be a string, a number, a list or even another dictionary

#region bassguitarmodels
# Dictionary with 2 key \ value pairs
bassguitar = {'Make':'Yamaha','Model':'BB434'}
print(bassguitar['Make'] + ' ' + bassguitar['Model'])

bassguitar['strings'] = 'roundwound'

print(bassguitar)
#Returns the dictionary (key \ value pairs) in the order the key value pairs were added
#{'Make': 'Yamaha', 'Model': 'BB434','strings': 'roundwound'}

print(bassguitar['Make'] + ' ' + bassguitar['Model'] + ' with ' + bassguitar['strings'] + ' strings')
#Returns Yamaha BB434 with roundwound strings

#endregion bassguitarmodels

#region emptydictionary

mycars={}

# Add a value
mycars['Make']= 'VW'
print(f"I own a {mycars['Make']}")

#endregion emptydictionary

#region changevalue in dictionary

mycars['Make']= 'BMW'
print(f"I now own a {mycars['Make']}")

#endregion changevalue in dictionary

#region deleteakey
del mycars['Make']
print(mycars)

#endregion deleteakey

#region verticallayout

employees = {
    'Bob':'IT',
    'Kevin':'Sales',
    'Graham':'Boss',
    'Tanja':'Real Boss'
}

print(f"Bob works in {employees['Bob']}")

tanjasjob = employees['Tanja']
print(f"Tanja is the {tanjasjob}")


#endregion verticallayout

#region setadefaultvalue
# Set a default value if the key doesn't exist
# Following on from previous example

Jennysjob = employees.get('Jenny','Jenny doesnt work here anymore')
print(Jennysjob)

# If don't have a second aruement then returns None
Anilsjob = employees.get('Anil')
print(Anilsjob)
#endregion setadefaultvalue

