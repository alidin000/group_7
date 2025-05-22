def summa(l:list[int]) -> int:
    def helper(index: int, l:list[int]):
        if index >= len(l):
            return 0
        print(f"uchurdagy index={index}, {l[index]}")
        return l[index] + helper(index + 1, l)
    
    summa_2 = helper(0, l)
    return summa_2


# print(f"summa = {summa([1,2,3,4,5])}")
# [1,2,3,4,5]
# [0,1,2,3,4]

def temp():
    print("Bul temp function")