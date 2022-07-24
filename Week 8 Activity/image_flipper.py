def flip_image(image):
    result = []
    for row in image:
        result.append(list(map(lambda x: 0 if x == 1 else 1, row[::-1])))
    return result
