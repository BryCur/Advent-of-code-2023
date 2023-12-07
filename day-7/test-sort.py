

def test(i: int):
    return "case 1" if i  == 1 else ("case 2" if i == 2 else "case 3")

for i in range(5):
    print(test(i))