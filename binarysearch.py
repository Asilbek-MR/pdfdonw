
w = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

def test_binarsearch(list, test):
    low = 0
    hight = len(list) - 1
    while low <= hight:
        mid = (low + hight) // 2
        mid_val = list[mid]
        if mid_val == test:
            return mid
        elif mid_val > test:
            hight = mid_val - 1
        else:
            low = mid_val + 1
    return None
            
            
print(test_binarsearch(w,15))          


























