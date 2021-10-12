# push_front X
# puxh_back X
# pop_front
# pop_back
# size
# empty
# front
# back 

def push_front(queue, Value):
    queue.insert(0, Value)
    print('queue: ',queue)
    return queue

def push_back(queue, Value):
    queue.append(Value)
    print('queue: ',queue)    
    return queue

def pop_front(queue):
    if len(queue) == 0 :
        print(-1)
        print('queue: ',queue)
        return queue
    else: 
        print(queue[0])
        queue.pop(0)
        print('queue: ',queue)       
        return queue
    
def pop_back(queue):
    if len(queue) == 0 :
        print(-1)
        print('queue: ',queue)
        return queue
    else: 
        print(queue[-1])
        queue.pop(-1)
        print('queue: ',queue)
        return queue

def size(queue):
    print(len(queue))
    print('queue: ',queue)
    
def empty(queue):
    if len(queue) == 0:
        print(1)
        print('queue: ',queue)
    else: print(0); print('queue: ',queue)

def front(queue):
    if len(queue) == 0:
        print(-1)
        print('queue: ',queue)
    else:
        print(queue[0])
        print('queue: ',queue)

def back(queue):
    if len(queue) == 0:
        print(-1)
        print('queue: ',queue)
    else:
        print(queue[-1])
        print('queue: ',queue)


N = int(input())

procedure = []
queue = []

for _ in range(N):
    procedure.append(input().split())

for action in procedure:
    if action[0] == 'push_front':
        value = int(action[1])
        push_front(queue, value)

    elif action[0] == 'push_back':
        value = int(action[1])
        push_back(queue, value)
    
    elif action[0] == 'pop_front':
        pop_front(queue)

    elif action[0] == 'pop_back':
        pop_back(queue)

    elif action[0] == 'size':
        size(queue)

    elif action[0] == 'empty':
        empty(queue)

    elif action[0] == 'front':
        front(queue)

    elif action[0] == 'back':
        back(queue)


