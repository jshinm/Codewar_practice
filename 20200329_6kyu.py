def digital_root(n):
    s = 0

    for i in str(n):
        s += int(i)
    if s > 9:
        s = digital_root(s)
    return s

if __name__ == "__main__":
    print (digital_root(9283))