def data():
    data = []
    return data

def size(data):
    data_size = len(data)
    return data_size

def empty(data_size):
    if data_size == 0 :
        return 1
    else:
        return 0

def push(data, X):
    data.append(X)

def pop(data, data_exi):
    if data_exi == 1 : return -1
    else: return data.pop()

def top(data):
    return data[-1]

a = data()
push(a, '1')
push(a, '2')
print(top(a))
print(size(a))
print(empty(size(a)))
print(pop(a, empty(size(a))))
print(pop(a, empty(size(a))))
print(pop(a, empty(size(a))))
print(size(a))
print(empty(size(a)))
print(pop(a, empty(size(a))))
push(a, '3')
print(empty(size(a)))
print(top(a))