import itertools
size = 5    
def show(table):
    print()
    print("%" * 8)
    for n, val in enumerate(table):
        if n % size == 0:
            print("\n", val, end="")
        else:
            print(val, end="")
    print()

def count_spots(table):
    spots = 0
    for i in range(len(table)):
        if table[i] == "B":
            if (i >= size and table[i - size] == "R") or ( i % size != 0 and table[i - 1] == "R"):
                spots +=1
                if spots > 1: return False
    if spots == 1: return True
    return False

def count_tables(*args):
    count= 0
    for i in itertools.product(["R", "B"], repeat=(size ** 2)): # generates tables as lists
        if count_spots(i):
            count += 1
            if args: show(i)
    print("Number of tables with one spot:", count)

count_tables()
