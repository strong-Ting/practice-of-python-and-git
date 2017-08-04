def eval_loop():
    x = None
    while x != 'done':
        x = input('>>')
        eval("print(x)")

eval_loop()

