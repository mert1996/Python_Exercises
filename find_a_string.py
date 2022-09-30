def count_substring(string, sub_string):
    length_ss = len(sub_string)
    count = 0

    for i,s in enumerate(string):
        sub = string[i:i+length_ss]        
        if sub_string == sub:
            count +=1
    return count
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
