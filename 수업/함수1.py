# N개의 정수를 입력 받아 오름 차순으로 정렬

N = 5 # 입력 정수 갯수

inputValuelist = [] # 입력 값 리스트

# 키보드로 부터 N개의 정수를 입력 받아 리스트에 저장
for index in range(N):
    inputValue = input(str(index +  1) + "번째 입력 값")
    inputValuelist.append(int(inputValue))

# 리스트에 저장된 정수 값을 오름 차순으로 정렬
for iCount in range(N - 1):
    for jCount in range( N - iCount - 1):
        if inputValuelist[jCount] > inputValuelist[jCount + 1]:
            temp = inputValuelist[jCount + 1]
            inputValuelist[jCount + 1] = inputValuelist[jCount]
            inputValuelist[jCount] = temp

# 리스트 값 출력
print(inputValuelist)