# 채팅방에 누군가 들어온다면 -> "[닉네임]님이 들어왔습니다." 출력
# 채팅방에 누군가 나갔다면 -> "[닉네임]님이 나갔습니다."
# 채팅바은 중복 닉네임을 허용한다.

# 채팅방에서 닉네임을 변경하는 방법은 2가지가 있다.
    # 1. 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
    # 2. 채팅방에서 닉네임을 변경한다.
        # 닉네임을 변경하면 기존 메세지의 닉네임도 변경된다.

# 모든 record가 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메세지를 return

record = ["Enter uid1234 Muzi",
          "Enter uid4567 Prodo",
          "Leave uid1234",
          "Enter uid1234 Prodo",
          "Change uid4567 Ryan"]

# result
# #["Prodo님이 들어왔습니다.",
# "Ryan님이 들어왔습니다.",
# "Prodo님이 나갔습니다.",
# "Prodo님이 들어왔습니다."]

def solution(record):
    answer = []
    store = {}

    for data in record:
        data_split = data.split()
        if 'Leave' not in data_split:
            store[data_split[1]] = data_split[2]

    for data in record:
        data_split = data.split()
        if data_split[0] == 'Enter':
            answer.append("%s님이 들어왔습니다." %store[data_split[1]])
        elif data_split[0] == 'Leave':
            answer.append("%s님이 나갔습니다." %store[data_split[1]])
    return answer

print(solution(record))