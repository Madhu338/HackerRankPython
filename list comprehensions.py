if __name__ == '__main__':
    # Read inputs
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # Use list comprehension to generate valid coordinates
    result = [[i, j, k] for i in range(x) for j in range(y) for k in range(z) if i + j + k != n]
    
    # Print the result
    print(result)