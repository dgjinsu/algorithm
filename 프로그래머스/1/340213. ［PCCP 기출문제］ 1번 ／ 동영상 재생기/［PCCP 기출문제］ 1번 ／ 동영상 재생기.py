def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    m_video_len = int(video_len.split(":")[0]) * 60 + int(video_len.split(":")[1])
    m_pos = int(pos.split(":")[0]) * 60 + int(pos.split(":")[1])
    m_op_start = int(op_start.split(":")[0]) * 60 + int(op_start.split(":")[1])
    m_op_end = int(op_end.split(":")[0]) * 60 + int(op_end.split(":")[1])
    
    for com in commands:
        # 오프닝 시간 체크
        if m_pos >= m_op_start and m_pos <= m_op_end:
            m_pos = m_op_end

        if com == "next":
            m_pos += 10
            if m_pos > m_video_len:
                m_pos = m_video_len
                
        if com == "prev":
            m_pos -= 10
            if m_pos < 0:
                m_pos = 0
                
        # 오프닝 시간 체크
        if m_pos >= m_op_start and m_pos <= m_op_end:
            m_pos = m_op_end
        
    hour = str(m_pos // 60)
    minuite = str(m_pos % 60)
    
    if len(hour) == 1:
        hour = "0" + hour
    if len(minuite) == 1:
        minuite = "0" + minuite
        
    return f'{hour}:{minuite}'