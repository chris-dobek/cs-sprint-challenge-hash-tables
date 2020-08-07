def get_indices_of_item_weights(weights, length, limit):
    # Set up a dictionary to store the values
    d = dict()

    # Use enumerate to keep track of iterations with key value pairs
    for i, weight in enumerate(weights):
        d[weight] = i
    
    # Now iterate through the table checking weights that meet  the limit
    for i, weight in enumerate(weights):
        if limit - weight in d:
            j = d[limit - weight]
            if i > j:
                return (i, j)
            else:
                return (j, i)

    return None
