N = int(input())

countries = []
for i in range(N):
    country = input()
    countries.append(country) 

countries = set(countries)
print(len(countries))
