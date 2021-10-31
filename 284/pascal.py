from typing import List


def pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    # you code ...
    # return row

    def bounds_val(row, idx):
        if (0 <= idx < len(row)):
            return row[idx]
        else:
            return 0

    if N <= 0: return []
    
    res = [1]

    for row_len in range(2,N+1):
        res_next = [bounds_val(res, i-1) + bounds_val(res, i)
                    for i in range(row_len)]
        res = res_next
    return res

if __name__ == '__main__':
    for i in range(6):
        print(pascal(i))
        
        
