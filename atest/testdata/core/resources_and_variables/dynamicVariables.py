def getVariables(*args):
    return {
        'dyn_multi_args_getVar': 'Dyn var got with multiple args from getVariables',
        'dyn_multi_args_getVar_x': ' '.join([str(a) for a in args]),
    }