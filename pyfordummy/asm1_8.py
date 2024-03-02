import math
n = int(input())

def factors_of(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def remove_duplicates(lst):
    return list(set(lst))

def find_pairs(c):
    list_of_pairs = []
    for k in factors_of(c):
        s = c / k
        for n in range(int(math.sqrt(s / 2)) + 1):  # Local optimization, we know that m >= n
            m_square = s - n**2
            m = math.floor(math.sqrt(m_square))
            if m * m == m_square:
                a = m**2 - n**2
                b = 2 * m * n
                list_of_pairs.append((k * a, k * b))
                list_of_pairs.append((k * b, k * a))
    return remove_duplicates(list_of_pairs)

print(len(find_pairs(n))//2-1)

#https://www.quora.com/Trigonometry-mathematics-How-can-I-get-a-Pythagorean-triple-from-a-given-hypotenuse-if-it-exists
