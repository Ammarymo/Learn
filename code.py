def artho(x):
    new =""
    if "+" in x:
        y = x.split("+")
        z = "+"
    elif "-" in x:
        y = x.split("-")
        z = "-"

    len_1 = 6 - len(y[0].strip())
    len_str = len_1* " "

    len_3 = 4 - len(y[1].strip())
    len_sec = len_3 * " "

    if z == "+":
        arth = str(int(y[0].strip()) + int(y[1].strip()))
    elif z == "-":
        arth = str(int(y[0].strip()) - int(y[1].strip()))

    len_2 = 6- len(arth)
    len_arth = len_2 * " "
    new += f"{len_str}{y[0]}\n{z}{len_sec}{y[1]}\n------\n{len_arth}{arth}"
    return new

def arithmetic_arranger(list_arth):
    final = []
    for i in list_arth:
        x = artho(i)
        final.append(x)
    f0 = final[0]
    if final[1] in final:
        f1 = final[1]
    else:
        f1 =""
    if final[2] in final:
        f2 = final[2]
    else:
        f2 =""
    if final[3]  in final:
        f3 = final[3]
    else:
        f3 =""
    # if final[4] is True:
    #     f4 = final[4]
    # else:
    #     f4 =""
    print(f0,f1,f2,f3)
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
