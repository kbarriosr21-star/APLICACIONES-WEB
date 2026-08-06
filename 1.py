vector_texto = ["a", "b", "c", "d", "e"]
vector_num = [1, 2, 3, 4, 5]

for num, letra in zip(vector_num, vector_texto):
    print(f"{num}{letra}")
