import math

def dot_product(V1: list[float], V2: list[float]) -> float | str:
    if len(V1) == len(V2):
        dot_product = 0
        for i in range(len(V1)):
            dot_product = dot_product + (V1[i] * V2[i])
        return dot_product
    else:
        return "Error"

def cos_angle_between_vectors(V1: list[float], V2: list[float]) -> float | str:
    if len(V1) == len(V2):
        return dot_product(V1, V2)/math.sqrt((dot_product(V1, V1)) * dot_product(V2, V2))
    else:
        return "Error"

def monogram_fitness_with_angle(english_monogram_freq: list[float], text_monogram_freq: list[float]) -> float:
    return cos_angle_between_vectors(english_monogram_freq, text_monogram_freq)

# test vectors
vector1 = [1,5]
vector2 = [1,3]

print(dot_product(vector1, vector2))
print(cos_angle_between_vectors(vector1, vector2))
print(monogram_fitness_with_angle(vector1, vector2))