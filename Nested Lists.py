#Nested Lists
if __name__ == '__main__':
    dict = {}
    points = []
    names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dict[name] = score
    for elems in dict:
        points.append(dict[elems])
        
    points.sort()
    p = set(points)
    p1 = list(p)
        
    for elem in dict:
        if dict[elem] == p1[1]:
            names.append(elem)
        
    names.sort()
    print('\n'.join(names))    
    
