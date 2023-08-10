def cartesian_product(set_A, set_B, index_A=0, index_B=0):

    if index_A == len(set_A) or index_B == len(set_B):
        return []

    product = []

    for i in range(index_B, len(set_B)):
        pair = (set_A[index_A], set_B[i])
        if pair not in product:
            product.append(pair)


    remaining_product = cartesian_product(set_A, set_B, index_A + 1, index_B)
    product.extend(remaining_product)

    return product

def get_cartesian_product():
    # Main function to take user input for sets A and B, calculate the Cartesian product, and find total cardinality
    set_A = input("Enter elements for set A separated by commas: ").split(',')
    set_B = input("Enter elements for set B separated by commas: ").split(',')
    product = cartesian_product(set_A, set_B)
    cardinality = len(product)
    return product, cardinality


product, cardinality = get_cartesian_product()
print("Cartesian product of set A and set B:", product)
print("Total cardinality of the Cartesian product:", cardinality)