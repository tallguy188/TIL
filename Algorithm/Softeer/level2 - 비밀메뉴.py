import sys
input = sys.stdin.readline

m,n,k = map(int,input().split())

if m > n :
    print("normal")
    exit()  # 그냥 프로그램을 끝내버림

secret_key = "".join(list(map(str,input().split())))
user_input = "".join(list(map(str,input().split())))

if secret_key in user_input:
    print("secret")
else:
    print("normal")