import sys
import datetime

input = sys.stdin.readline

x, y = map(int, input().split())

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

a = datetime.date(2007, x, y).weekday()

print(days[a])