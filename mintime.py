

def minTime(machines, goal):
    lg = goal*machines[0]
    l = [0 for _ in range(lg)]
    for i in machines:
        for j in range(1, int(lg/i)):
            if(i*j < lg):
                l[i*j] += 1
    t = 0

    for i in range(lg):
        if(t >= goal):
            return (i-1)
            break
        t += l[i]


if __name__ == '__main__':

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)
