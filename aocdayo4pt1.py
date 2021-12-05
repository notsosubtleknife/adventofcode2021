def bingo(srch: list, brd: list) -> list:
    for row in brd:
        intr = [n for n in row if n in srch]
        if len(intr) == 5:
            return intr
        
    brd_t = list(map(list, zip(*brd)))
    
    for col in brd_t:
        intc = [n for n in srch if n in col]
        if len(intc) == 5:
            return intc
        
    return list()


fh = open("aocdayo4_input", mode='r')
itxt = fh.read()
fh.close()

itxt = list(itxt.strip().split("\n\n"))

nbrs = list(map(int, itxt[0].split(',')))
itxt = [i.split('\n') for i in itxt[1:]]

"""can you read this? i cant."""
brds = [[[int(k) for k in j.split(' ') if k != ''] for j in i] for i in itxt]

try:
    for i in range(len(nbrs)):
        for brd in brds:
            if len(bingo(nbrs[0:i], brd)) == 5:
                raise StopIteration
            #another way to break 2 in python
except StopIteration:
    pass

brd = [j for sub in brd for j in sub]
brd = [j for j in brd if j not in nbrs[0:i]]
print(sum(brd) * nbrs[i-1])
