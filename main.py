from maxMinSelect import max_min_select

if __name__ == "__main__":
    entrada = input("Digite os números separados por espaço: ")
    
    if not entrada.strip():
        print("Erro: Nenhum número foi digitado. O array está vazio!")
        exit()
    
    sequencia = list(map(int, entrada.split()))
    
    print(f"\nArray da Sequência digitada: {sequencia}")

    menor, maior = max_min_select(sequencia)

    print(f"Menor elemento do Array: {menor}")
    print(f"Maior elemento do Array: {maior}")