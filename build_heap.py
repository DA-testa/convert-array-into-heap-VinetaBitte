# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range(n//2-1, -1, -1):
        min_heapify(data, i, n,swaps)
#    print(data)
    
    return swaps

def min_heapify(data, i, n, swaps):
    minimal = i
    leftchild = 2*i+1
    rigthchild = 2*i+2

    if (leftchild <= n-1 and data[leftchild] < data[minimal]):
        minimal = leftchild
    if (rigthchild <= n-1 and data[rigthchild] < data[minimal]):
        minimal = rigthchild
    if (minimal != i):
        data[i], data[minimal] = data[minimal], data[i]
        swaps.append((i, minimal))
        min_heapify(data, minimal, n,swaps)


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    text = input()
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))
    else:
        if "F" in text:
            filename = input()
            with open("./tests/" + filename, mode = "r") as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
   # print("end")


if __name__ == "__main__":
    main()
