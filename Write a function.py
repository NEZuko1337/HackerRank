#Write a function
def is_leap(year):
    flag = True
    if year%4==0 and year%100!=0:
        flag = True
    if year%400:
        flag = True
    if year%4!=0:
        flag = False
    if year%100 == 0 and year%400!=0:
        flag = False
    return flag

year = int(input())
print(is_leap(year))
