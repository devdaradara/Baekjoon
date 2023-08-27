def solution(brown, yellow):
    answer = []
    total = brown + yellow 
    for height in range(1, total + 1):
        if (total / height) % 1 == 0:
            width = total / height
            if width >= height: 
                if 2*width + 2*height == brown + 4: 
                    return [width, height]
            
    return answer