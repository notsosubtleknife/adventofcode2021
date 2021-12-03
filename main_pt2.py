report_str = open('day1aocinput.txt', 'r').readlines()
report = list(map(int, report_str))

count = 0
for x in range(len(report)-3):
    if report[x+3] > report[x]:
        count += 1

print(count)
