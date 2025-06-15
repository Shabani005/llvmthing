# in the documentation there is something called var_arg may need to revisit
def funct(*args, return_type=ir.VoidType(), name=""):
    return ir.FunctionType(return_type, args)


# documentation has module,typ,name,addrspace, it could be made into a constant check later
def global_var(name, type, init=None):
    return ir.GlobalVariable(name)

def global_const(name, type, init=None):
    return ir.GlobalVariable(name, type, init)

def func(name):
    return ir.Function(name)