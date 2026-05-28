import math

def gen_seq_a(x):
    k = 1
    term = x
    while True:
        yield term
        k += 1
        term = term * x * (k - 1) / k

def solve_a(x, target_k):
    generator = gen_seq_a(x)
    result = 0
    for _ in range(target_k):
        result = next(generator)
    return result

def gen_seq_b():
    i = 1
    term = 1 / 2
    while True:
        yield term
        i += 1
        term = term / (i + 1)

def solve_b(n):
    generator = gen_seq_b()
    product = 1
    for _ in range(n):
        product *= next(generator)
    return product

def gen_seq_c():
    d_prev = 2
    yield d_prev
    d_curr = 1
    yield d_curr
    while True:
        d_next = 2 * d_curr - 3 * d_prev
        yield d_next
        d_prev, d_curr = d_curr, d_next

def solve_c(n):
    generator = gen_seq_c()
    result = 0
    for _ in range(n):
        result = next(generator)
    return result

def gen_seq_d():
    k = 1
    a_prev2 = 0
    yield (2**k) * a_prev2
    
    k = 2
    a_prev1 = 1
    yield (2**k) * a_prev1
    
    while True:
        k += 1
        a_curr = a_prev1 + k * a_prev2
        yield (2**k) * a_curr
        a_prev2, a_prev1 = a_prev1, a_curr

def solve_d(n):
    generator = gen_seq_d()
    total_sum = 0
    for _ in range(n):
        total_sum += next(generator)
    return total_sum

def gen_seq_e(x):
    i = 1
    term = x
    while True:
        yield term
        i += 1
        term = -term * (x**2) / ((2*i - 2) * (2*i - 1))

def solve_e(x, epsilon):
    generator = gen_seq_e(x)
    total_sum = 0
    while True:
        term = next(generator)
        total_sum += term
        if abs(term) < epsilon:
            break
    return total_sum

if __name__ == "__main__":
    x_val, k_val = 2.0, 5
    print(f"a) x_{k_val} для x={x_val}: {solve_a(x_val, k_val)}")
    
    n_val = 5
    print(f"b) P_{n_val}: {solve_b(n_val)}")
    
    n_det = 4
    print(f"c) D_{n_det}: {solve_c(n_det)}")
    
    n_sum = 5
    print(f"d) S_{n_sum}: {solve_d(n_sum)}")
    
    x_angle = math.pi / 4
    eps = 1e-6
    calc_sin = solve_e(x_angle, eps)
    math_sin = math.sin(x_angle)
    print(f"e) sin({x_angle:.4f}) через Тейлора: {calc_sin:.6f}")
    print(f"   sin({x_angle:.4f}) через math:    {math_sin:.6f}")
    print(f"   Різниця: {abs(calc_sin - math_sin):.2e}")