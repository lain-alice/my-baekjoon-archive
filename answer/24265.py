# 24265 알고리즘 수업 - 알고리즘의 수행 시간 4

n = int(input())
print((n - 1) * n // 2)
print(2)

# def MenOfPassion(A, n) :
#     sum = 0
#     for i in range(n):        
#         for j in range(i+1):
#             sum += A[i] * A[j]
#     return sum

# 리스트 A에서 나올 수 있는 모든 숫자 쌍을 서로 곱하고 다 합친다
# 이중반복문의 시간복잡도 O(n^2)