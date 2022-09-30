lim_num = str(input())
N_M = lim_num.split(" ")
N = int(N_M[0])
M = int(N_M[1])
string = ".|."

# Upper Half
for i in range(int((N-1)/2)):
    i = (i*2) + 1
    print((string*i).center(M,"-"))

# Middle
print("WELCOME".center(M,"-"))

# Lower Half
for i in range(int((N-1)/2),0,-1):  
    i = ((i-1)*2) +1
    print((string*i).center(M,"-"))
