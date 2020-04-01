def duplicate_count(text):
    # Your code goes here
    
    allcount = 0
    b = (list(set(text.lower())))
    
    for i in b:
        
        count = 0
        
        for j in text.lower():

            if i == j:
                count += 1
        
            if count == 2:
                allcount +=1
                break    
        
    return allcount 

def likes(names):
    if names == []:
        return "no one likes this"
    elif len(names) == 1:
        return "{} likes this".format(names[0])
    elif len(names) == 2:
        return "{0} and {1} like this".format(names[0], names[1])
    elif len(names) == 3:
        return "{0}, {1} and {2} like this".format(names[0], names[1], names[2])
    elif len(names) > 3:
        return "{0}, {1} and {2} others like this".format(names[0], names[1], len(names)-2)

def main():
    print (duplicate_count("1abcbccc"))
    print (likes(["a", "b", "c","d"]))

if __name__ == "__main__": main()
    #a("aaa")