x = float(input("Enter X value: "))
y = float(input("Enter Y value: "))
z = float(input("Enter Z value: "))

def m_func(x, y, z):
    m = (((x**2)*y) - z) / (5 + y)
    return m

def s_func(x, y, z, m):
    s = ((x*m)**3 - (y*m)**2 + (z/2)**2 + (y/2)**2 + (x/2)**2)**0.5
    return s

m = m_func(x, y, z)
print(f"m: {m:.2f}")
print(f"s: {s_func(x, y, z, m):.2f}")

