from itertools import product

def implies(a, b):
    return (not a) or b

def is_kb_true(P, Q, R):
    sentence1 = implies(Q, P)
    sentence2 = implies(P, not Q)
    sentence3 = Q or R
    return sentence1 and sentence2 and sentence3

def entails(query):
    for P, Q, R in product([False, True], repeat=3):
        if is_kb_true(P, Q, R):
            if not query(P, Q, R):
                return False
    return True

print("P Q R | Q->P | P->not Q | Q or R | KB")
print("-" * 45)
for P, Q, R in product([True, False], repeat=3):
    s1 = implies(Q, P)
    s2 = implies(P, not Q)
    s3 = Q or R
    kb = s1 and s2 and s3
    def tf(value):
        return "T" if value else "F"
    print(
        tf(P), tf(Q), tf(R), "|",
        tf(s1), "  |", tf(s2), "       |",
        tf(s3), "     |", tf(kb)
    )
print("\nModels where KB is true:")
for P, Q, R in product([True, False], repeat=3):
    if is_kb_true(P, Q, R):
        print(f"P={P}, Q={Q}, R={R}")
queries = [
    ("R", lambda P, Q, R: R),
    ("R -> P", lambda P, Q, R: implies(R, P)),
    ("Q -> R", lambda P, Q, R: implies(Q, R))
]
print("\nEntailment results:")
for name, query in queries:
    result = entails(query)
    print(f"KB entails {name}: {result}")
