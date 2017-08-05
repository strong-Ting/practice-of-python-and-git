def lowercase0(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


def lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def lowercase2(s):
    for c in s:
        flag = c.islower()
    return flag

def lowercase3(s):
    flag = False
    for c in s:
        flag = flag or c.islower() 
    return flag

def lowercase4(s):
    for c in s:
        if not c.islower():
            return False
    return True

s = input('str:')
for i in range (5):
    function = globals() ['lowercase'+ str(i)]
    print(function(s))
