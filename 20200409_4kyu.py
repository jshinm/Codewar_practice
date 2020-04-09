def snail(snail_map):
    
    snail_output = []
    dirc =1
 
    while snail_map:
        if dirc == 1:
            snail_output.extend(snail_map.pop(0))
            dirc = 2
        elif dirc == 2:
            for i in range(len(snail_map)):
                snail_output.append(snail_map[i].pop(len(snail_map[i])-1))
            dirc = 3
        elif dirc == 3:
            rvslist = snail_map.pop(len(snail_map)-1)
            snail_output.extend(rvslist[::-1])
            dirc = 4
        elif dirc == 4:
            for i in range(len(snail_map)-1,0,-1):
                snail_output.append(snail_map[i].pop(0))        
            dirc = 1

    return(snail_output)

if __name__ == "__main__":
    array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
    expected = [1,2,3,6,9,8,7,4,5]
    print (snail(array), expected)
