def to_camel_case(text):
    #your code here
    from string import punctuation

    newstring = ""

    for i in range(len(text)):
        if text[i] in set(punctuation):
            #text[i+1] = text[i+1].upper()
            newstring = newstring + text[i+1].upper()
        elif text[i-1] in set(punctuation):
            continue
        else: newstring = newstring + text[i]

    return newstring

def countBits(n):
    return bin(n).replace("0b", "").count("1")

def max_sequence(arr):
	
    maxseq = []
    maxscore = 0

    for i in range(len(arr)):

        tempscore = 0
        tempseq = []

        for j in arr[i:]:
            
            tempscore += j
            tempseq.append(j)

            if tempscore > maxscore:
                maxscore = tempscore
                maxseq = tempseq

    return maxscore


if __name__ == "__main__":
    to_camel_case("the_stealth_warrior")
    countBits(1234)
    max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])