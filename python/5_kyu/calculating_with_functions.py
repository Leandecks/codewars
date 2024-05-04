import operator

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '//': operator.floordiv}

def zero(o=""): return ops[o[0]](0, o[1]) if o else 0
def one(o=""): return ops[o[0]](1, o[1]) if o else 1
def two(o=""): return ops[o[0]](2, o[1]) if o else 2
def three(o=""): return ops[o[0]](3, o[1]) if o else 3
def four(o=""): return ops[o[0]](4, o[1]) if o else 4
def five(o=""): return ops[o[0]](5, o[1]) if o else 5
def six(o=""): return ops[o[0]](6, o[1]) if o else 6
def seven(o=""): return ops[o[0]](7, o[1]) if o else 7
def eight(o=""): return ops[o[0]](8, o[1]) if o else 8
def nine(o=""): return ops[o[0]](9, o[1]) if o else 9

def plus(n): return ["+", n]
def minus(n): return ["-", n]
def times(n): return ["*", n]
def divided_by(n): return ["//", n]

print(three(times(five())))


