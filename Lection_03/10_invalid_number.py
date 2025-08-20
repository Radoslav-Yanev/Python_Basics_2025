num = int(input())
isvalid = (100 <= num <= 200) or (num == 0)

if not isvalid:
    print("invalid" )