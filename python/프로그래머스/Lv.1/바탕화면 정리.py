def solution(wallpaper):
    file_x = []
    file_y = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                file_x.append(i)
                file_y.append(j)
    min_x, max_x = min(file_x), max(file_x) + 1
    min_y, max_y = min(file_y), max(file_y) + 1
    
    answer = [min_x, min_y, max_x, max_y]
                
    return answer