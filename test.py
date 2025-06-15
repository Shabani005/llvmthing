from llvmlite import ir

# Create a module
module = ir.Module(name="my_module")

def easy_function(module, name, return_type, arg_types, arg_names=None):
    func_type = ir.FunctionType(return_type, arg_types)
    func = ir.Function(module, func_type, name=name)
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    if arg_names:
        for arg, name in zip(func.args, arg_names):
            arg.name = name
    return func, builder, func.args

# Use the easy_function helper
func, builder, args = easy_function(
    module,
    name="add",
    return_type=ir.IntType(32),
    arg_types=[ir.IntType(32), ir.IntType(32)],
    arg_names=["a", "b"]
)

# Build the function body
result = builder.add(args[0], args[1], name="sum")
builder.ret(result)

# Print the LLVM IR
print(module)