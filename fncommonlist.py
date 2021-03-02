def common(a, b): 
    x = set(a) 
    y= set(b) 
    if (x & y): 
        print(x & y) 
    else: 
        print("No common elements")  
a = [9, 6, 3, 4, 5] 
b = [5, 6, 0, 8] 
common(a, b) 
