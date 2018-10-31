a = []

with open("c:\\dd\\ss.txt", 'r') as f:
	for i in range(10):
		a.append(f.readline().split())

for i in range(len(a)):
	for j in range(1,4):
		a[i][j] = int(a[i][j])
	a[i].append(sum(a[i][1:4]))
	a[i].append(round((a[i][4] / 3), 2))

korT = 0
engT = 0
matT = 0

for i in range(len(a)):
	korT += a[i][1]
	engT += a[i][2]
	matT += a[i][3]

korA = korT / len(a)
engA = engT / len(a)
matA = matT / len(a)

everyT = korT + engT + matT
everyA = everyT / (3 * len(a))


print(" *************** 성 적 표 ************** ")
print(" *************************************** ")
print("  이 름  국어  영어  수학  총점    평균  ")
print(" *************************************** ")

for i in range(len(a)):
	print(" {} {:5d} {:5d} {:5d} {:5d} {:7.2f} "
              .format(a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], a[i][5]))

print(" ************************************** ")
print(" 총평균 {:5.1f} {:5.1f} {:5.1f} {:5d} {:7.2f} "
      .format(korA, engA, matA, everyT, everyA))
