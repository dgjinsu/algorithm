def solution(players, callings):
    m = dict()
    for idx, player in enumerate(players):
        m[player] = idx
    
    for call in callings:
        call_idx = m[call]
        players[call_idx - 1], players[call_idx] = players[call_idx], players[call_idx - 1]
        m[call] = m[call] - 1
        m[players[call_idx]] = m[players[call_idx]] + 1
    
    return players