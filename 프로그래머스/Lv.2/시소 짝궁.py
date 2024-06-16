def solution(weights):
    # 각 무게의 개수를 센다.
    weight_count = {}
    for weight in weights:
        if weight in weight_count:
            weight_count[weight] += 1
        else:
            weight_count[weight] = 1

    
    # 가능한 거리 비율
    ratios = [1/1, 2/3, 3/2, 3/4, 4/3, 1/2, 2]
    
    # 짝꿍의 수를 센다.
    pair_count = 0
    
    for weight in weights:
        weight_count[weight] -= 1
        for ratio in ratios:
            if weight * ratio in weight_count:
                pair_count += weight_count[weight * ratio]
    
    return pair_count