def get_multiples(base, limit):
    curr = base
    multiples = []
    while curr < limit:
        multiples.append(curr)
        curr += base
    return set(multiples)

def get_union_sum(set1, set2):
    return sum(set1 | set2)

if __name__ == "__main__":
    multiples_3 = get_multiples(3, 1000)
    multiples_5 = get_multiples(5, 1000)
    print(get_union_sum(multiples_3, multiples_5))
