
# AVOID GLOBALS
a = 123   # global variable (file global)

def spam(b):  # b and c are LOCAL variables
    c = "wombat"
#    print(x)  # search local->nonlocal->global->builtin

spam(22)



