# python3

def parallel_processing(n, m, data):
    output = []

    a = n*[0]
    time = n*[0]

    for i in range(m):
        time2 = data[i]



        done = float('inf')
        x = 0

        for j in range(n):
            if time[j]<done:
                done = time[j]

                x = j
                

        time1 = max(a[x], time[x])
        time[x] = time1+time2
        a[x] = time1

        output.append((x, time1))

    return output

def main():
    n,m = map(int,input().split())
    data = list(map(int,input().split()))

    result = parallel_processing(n, m, data)

    for both in result:
        print(both[0], both[1])
    
if __name__ == "__main__":
    main()
#
#