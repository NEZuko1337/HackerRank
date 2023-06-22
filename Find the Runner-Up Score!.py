# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr1 = set(arr)
    finarr = list(arr1)
    print(finarr[-2])
