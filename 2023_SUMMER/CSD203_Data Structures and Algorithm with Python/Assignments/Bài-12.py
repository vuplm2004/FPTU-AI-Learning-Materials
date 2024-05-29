def bucket_sort(arr):
    buckets = [[] for _ in range(10)]
    for num in arr:
        index = int(num * 10)
        buckets[index].append(num)
    for i in range(len(buckets)):
        buckets[i] = sorted(buckets[i])
    return [num for bucket in buckets for num in bucket]

with open("data.txt", "r") as f:
    data = [float(line.strip()) for line in f.readlines()]

sorted_data = bucket_sort(data)

print(sorted_data)