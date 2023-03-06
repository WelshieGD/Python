#region foreachlistiteminanotherlist
availableitems = ['apples','forks','books','pens','headphones']
wishlistitems = ['books','headphones','BMW']

for wishlistitem in wishlistitems:
    if wishlistitem in availableitems:
        print(f"Your wish list item {wishlistitem} is available")

    else:
        print(f"Your wish list item {wishlistitem} is not available")

#endregion foreachlistiteminanotherlist