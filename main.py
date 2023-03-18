# python3


def parallel_processing(n, m, data):
    output = []


    threads = [0] * n
    finish_times = [0] * n
    
  
    for i in range(m):
        job_time = data[i]
        
      
        min_finish_time = float('inf')
        thread_index = 0
        for j in range(n):
            if finish_times[j] < min_finish_time:
                min_finish_time = finish_times[j]
                thread_index = j
        
        
        start_time = max(threads[thread_index], finish_times[thread_index])
        finish_times[thread_index] = start_time + job_time
        threads[thread_index] = start_time
        
        
        output.append((thread_index, start_time))
    
    return output


def main():
    

    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)
    
    for pair in result:
        print(pair[0], pair[1])


if __name__ == "__main__":
    main()
