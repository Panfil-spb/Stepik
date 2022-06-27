n = int(input())
l = {i: 0 for i in range(n)}
for i in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        l[0] += 1
    elif x < 0 and y > 0:
        l[1] += 1
    elif x < 0 and y < 0:
        l[2] += 1
    elif x > 0 and y < 0:
        l[3] += 1

print("Первая четверть: " + str(l[0]) + "\n" +
"Вторая четверть: " + str(l[1]) + "\n" +
"Третья четверть: " + str(l[2]) + "\n" +
"Четвертая четверть: " + str(l[3]) + "\n" )


