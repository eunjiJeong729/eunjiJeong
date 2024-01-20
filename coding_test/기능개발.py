def solution(progresses, speeds):
    answer = []
    add_progress = []
    count = []
    for i,j in zip(progresses,speeds) :
        add_arg = i+j
        count_arg = 1
        while not add_arg >= 100 :
            add_arg += j
            count_arg += 1
        count.append(str(count_arg))
        add_progress.append(add_arg)

    point = 0
    for i in range(len(count)):
        if count[i] > count[point]:
            answer.append(i - point)
            point = i
    answer.append(len(count) - point)

    return answer

if __name__ == '__main__':
    progresses1 = [93, 30, 55]
    speeds1 = [1, 30, 5]
    print(solution(progresses1, speeds1))
