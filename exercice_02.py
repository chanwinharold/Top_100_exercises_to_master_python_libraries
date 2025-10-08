
s = "3.14"

s_float = float(s)
s_int = int(round(s_float, 0))

s_float *= 2
s_int *= 2

print(f"{s_float} -> type {type(s_float)}")
print(f"{s_int} -> type {type(s_int)}")