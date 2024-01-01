str_doc = {
    "-" :  0,
    "\\":  1,
    "(" :  2,
    "@" :  3,
    "?" :  4,
    ">" :  5,
    "&" :  6,
    "%" :  7,
    "/" : -1
}

while True:
    string = input()
    if string == "#":
        break
    else:
        n_int = 0
        for i in range(len(string)):
            n_int += str_doc[string[i]]*(8**(len(string)-(i+1)))
        print(n_int)