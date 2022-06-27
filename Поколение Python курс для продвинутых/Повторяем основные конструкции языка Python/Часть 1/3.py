s = input()

cost = len(s) * 60

print(str(cost // 100) + "р. " + str(cost % 100) + " коп.")