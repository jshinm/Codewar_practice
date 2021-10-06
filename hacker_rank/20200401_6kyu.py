def longest_consec(strarr, k):
    # your code
    tempchar = ""
    maxchar = ""
    
    if k > 0:
        for i in range(len(strarr)-k+1):
            tempchar = "".join(strarr[i:i+k])

            if len(tempchar) > len(maxchar):
                maxchar = tempchar

    return maxchar

def find_uniq(arr):
    # your code here
    n = list(set(arr))
    
    if arr[0:3].count(n[0]) > 1:
        return n[1]

    return n[0]

if __name__ == "__main__":
    longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)
    find_uniq([ 1, 1, 1, 2, 1, 1 ])