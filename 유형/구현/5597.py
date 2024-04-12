import sys
input = sys.stdin.readline

students = [i + 1 for i in range(30)]
passed = [int(input()) for i in range(28)]
failed = []

for i in students:
    if i not in passed:
        failed.append(i)

print(min(failed))
print(max(failed))