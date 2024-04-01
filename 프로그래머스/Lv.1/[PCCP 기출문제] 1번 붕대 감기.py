def solution(bandage, health, attacks):
    max_health = health # 최대 체력
    time = 0
    success = 0
    index = 0
    while (True):
        if attacks[index][0] == time:
            health -= attacks[index][1]
            print(f'{time} 에 공격 성공. 체력 {attacks[index][1]} 까짐, health: {health}')
            success = 0
            time += 1
            index += 1
            if (health <= 0): return -1
            if index == len(attacks): return health
            continue
            
        # 공격 x
        time += 1
        health += bandage[1]
        success += 1
        
        # 체력 회복 (붕대 성공)
        if success == bandage[0]:
            health += bandage[2]
            success = 0
            
        if health > max_health:
            health = max_health
            
    return 0