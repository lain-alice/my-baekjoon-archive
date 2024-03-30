import problem
import sys
sys.stdin=open("data.txt","r")
input=sys.stdin.readline


def cont():
    while(True):
        try:
            problem.main0()
        except Exception as e:  
            print('예외가 발생했습니다.', e)
            return


if __name__ == "__main__":
    problem.main0()
    cont()

print(input)