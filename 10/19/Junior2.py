lines = int(input())

msg = ""


for i in range(lines):
    code = input()
    code = code.split(" ")
    number = int(code[0])
    text = code[1]
    msg = msg + (text*number)
    if i != lines-1:
        msg = msg+"\n"
print(msg)
