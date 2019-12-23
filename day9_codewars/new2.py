def valid_parentheses(string):
    str = ""
    for i in string:
        if i == "(" or i == ")": str += i
    while True:
        if "()" in str:
            str = str.replace("()","")
            continue
        elif len(str) == 0:
            return True
        else:
            return False

string =  " e()miae)e)kwxvcebppq(ylaazr(" # False (() ()) ((  ABBBAA (( ))
print(valid_parentheses(string))