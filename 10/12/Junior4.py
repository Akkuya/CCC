offset = int(input())
encoded = input().lower()

decoded = ""
letters = ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']

for i in range(len(encoded)):
    s = 3*(i+1) + offset
    decodedletter = letters.index(encoded[i]) - s
    if decodedletter < 0:
        decodedletter+=26
    decoded += letters[decodedletter]

print(decoded.upper())
