def mutate_string(string, position, character):
    a = []
    for i in string:
        a += i
    
    a[position] = character
    new_word = "".join(a[:])
    return new_word

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
