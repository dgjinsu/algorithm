def solution(s, skip, index):
    # 알파벳 리스트를 만듭니다. (a ~ z)
    alphabet = [chr(i) for i in range(97, 123)]
    
    # skip에 있는 알파벳을 알파벳 리스트에서 제거합니다.
    for char in skip:
        if char in alphabet:
            alphabet.remove(char)
    
    answer = ''
    
    # 각 문자에 대해 변환 작업을 수행합니다.
    for char in s:
        current_index = alphabet.index(char)
        new_index = (current_index + index) % len(alphabet)
        answer += alphabet[new_index]
    
    return answer