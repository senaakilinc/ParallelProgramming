def calculate_pyramid_height(number_of_blocks):
    height = 0
    current_layer = 1  # We start from the first layer

    while number_of_blocks >= current_layer:
        number_of_blocks -= current_layer  # Remove used blocks
        height += 1  # increase height
        current_layer += 1  # move on to the next layer
    
    return height
