x = 1

while x<=5:
    print("Test", end="")
    j = 1
# end is used to print the next value in same line, it will not go in new line
# in while loop first will start from outer loop and until inner loop will not complete
# it will not come in outer loop
    while j<=4:
        print("Rocks", end="")
        j=j+1
    x = x + 1
    print()
