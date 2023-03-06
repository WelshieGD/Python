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






