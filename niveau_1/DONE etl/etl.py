def transform(legacy_data: dict):
    new_data={}
    for point in legacy_data:
        for letter in range(len(legacy_data[point])):
            new_data[ 
                        legacy_data[point][letter].lower() 
                    ] = point
    return new_data
