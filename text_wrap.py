import textwrap

lines = []
def wrap(string, max_width):
    for i,y in enumerate(string):
        y = (i+1)*max_width
        i = i*max_width
        print(string[i:y])
        if y > len(string):
            break 

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
