def cartesian_product(set_A, set_B, index_A=0, index_B=0):
    # Recursive function to calculate the Cartesian product of two sets

    if index_A == len(set_A) or index_B == len(set_B):
        # Base case: if either set is fully processed, return an empty list
        return []

    # List to store the Cartesian product
    product = []

    for i in range(index_B, len(set_B)):
        # Create a tuple with the pair (set_A[index_A], set_B[i])
        pair = (set_A[index_A], set_B[i])
        # Check for duplicates before appending to the product list
        if pair not in product:
            product.append(pair)

    # Recursively calculate the Cartesian product of the remaining elements in set_A with set_B
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

# Test with user input
product, cardinality = get_cartesian_product()
print("Cartesian product of set A and set B:", product)
print("Total cardinality of the Cartesian product:", cardinality)