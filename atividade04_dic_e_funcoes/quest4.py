def main():
    n = int(input("Digite o valor de n:\n"))
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    print(f"O valor de fatorial eh {n} = {fat}")
main()
