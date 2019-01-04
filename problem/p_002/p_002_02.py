"""
두 개의 정수 n, m이 주어집니다.
반복문을 사용하지 않고 가로가 n, 세로가 m인 *로 이루어진 사각형을 출력해주세요

- 예시
    - n : 5 / m : 4
    
    *****
    *****
    *****
    *****

"""
#직관적 풀이
n = input("n의 값을 지정합니다. 숫자를 입력해주세요 : ")
m = input("m의 값을 지정합니다. 숫자를 입력해주세요 : ")

width = "*"*int(n)
total = (f"{width}\n")*int(m)

print(total)


# #다른 풀이방법
# n, m = input("숫자를 입력해주세요").split()
# print((("*"*int(n))+"\n")*int(m))