import llvmlite.ir as ir

i8 = ir.IntType(8)
i16 = ir.IntType(16)
i32 = ir.IntType(32)
i64 = ir.IntType(64)
i128 = ir.IntType(128)

f16 = ir.HalfType()
f32 = ir.FloatType()
f64 = ir.DoubleType()

def vec(element, count):
    return ir.VectorType(element, count)

def arr(element, count):
    return ir.ArrayType(element, count)

