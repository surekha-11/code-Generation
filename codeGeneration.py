def notation(num1, num2, operator):
    if operator == '+' :
        return 'A'
    elif operator == '-' :
        return 'S'
    elif operator == '*' :
        return 'M'
    elif operator == '/' :
        return 'D'

def isAlphabet(i):
    return exp[i].isalpha()

def precedingOperator(i):
    return not (i > 0 and exp[i-1].isalpha())

def succeedingDivisionOperator(i):
    return not (i+1 < len(exp) and (exp[i+1].isalpha() or exp[i+1] == '/'))

def ifAlphabet(a, b, i):
    global no_of_oper, output
    oper = notation(b, a, exp[i])
    output += 'L' + " " + b +'\n' + oper + " " + a + '\n'
    if not succeedingDivisionOperator(i) :
        no_of_oper += 1
        output += "ST" + " " + "$" + str(no_of_oper) + '\n'
    result="$" + str(no_of_oper)
    l.append(result)
    return output

def ifOperator(a, b, i):
    global no_of_oper, output
    oper = notation(b, a, exp[i])
    output += oper + " " + b + '\n'
    if b[0] != '$' :
        result = '$' + str(no_of_oper)
    else :
        result = b  
        no_of_oper = int(b[1])
    l.append(result)
    if not succeedingDivisionOperator(i) :
        output += 'ST' + " " + result + '\n'
    return output
               
def ifNegation(i):
    global no_of_oper, output
    a = l.pop()
    if exp[i-1].isalpha() :
        no_of_oper += 1 
        output += 'L' + " " + a + '\n'
    output += 'N' +'\n'
    if not succeedingDivisionOperator(i) :
        if not isAlphabet(i-1) :
            no_of_oper += 1
            output += 'ST' + " " + '$' + str(no_of_oper) + '\n'
    result = '$' + str(no_of_oper)
    l.append(result)
    return output

def ifSubtract(a, b, i):
    global no_of_oper, output
    oper = notation(b, a, '+')
    output += 'N' + '\n' + oper + " " + b + '\n'
    if b[0] != '$' :
        result = '$' + str(no_of_oper)
    else:
        result = b  
        no_of_oper = int (b[1])
    if not succeedingDivisionOperator(i) :
        output += 'ST' + " " + result +'\n'
    l.append(result)
    return output 

def checkOperator(a, b, i):
    if precedingOperator(i) and exp[i] == '-' :
        ifSubtract(a, b, i)
    elif precedingOperator(i) and exp[i] != '/' :
        ifOperator(a, b, i)
    else:
        ifAlphabet(a, b, i)

def codeGeneration(exp):
   global output
   for i in range(len(exp)):
     if isAlphabet(i) :
        l.append(exp[i])
     elif exp[i] != '@' :
        a = l.pop()
        b = l.pop()
        checkOperator(a, b, i)
     else:
        ifNegation(i)
   return output

expression = ["AB+CD+EF++GH+++", "AB+CD+-"]
l = []
for exp in expression :
	no_of_oper = 0
	output = ""
	print(codeGeneration(exp))

