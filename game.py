import os
complete = []

for i in range(3):
    drawing = []
    os.system("clear")

    if len(complete) > 0:
        print("\n".join(complete[-1][-1:]))
    while True:
        line = input("")
        if not line:
            break
        else:
            drawing.append("     "+line if i ==0 else line)
    complete.append(drawing)

os.system("clear")
print("\n".join(["\n".join(i) for i in complete]))