import sys

def ler_conjunto(arquivo):
    with open(arquivo, 'r') as f:
        conteudo = f.read().strip()
        conteudo = conteudo.strip('{}')
        elementos = conteudo.split(',')
        return set(elementos)

def uniao(conjuntoA, conjuntoB):
    return conjuntoA.union(conjuntoB)

def interseccao(conjuntoA, conjuntoB):
    return conjuntoA.intersection(conjuntoB)

def diferenca(conjuntoA, conjuntoB):
    return conjuntoA.difference(conjuntoB)

def main(conjuntoA_arquivo, conjuntoB_arquivo):
    conjuntoA = ler_conjunto(conjuntoA_arquivo)
    conjuntoB = ler_conjunto(conjuntoB_arquivo)

    print(f"Conjunto A: {conjuntoA}")
    print(f"Conjunto B: {conjuntoB}")
    
    uniao_ab = uniao(conjuntoA, conjuntoB)
    interseccao_ab = interseccao(conjuntoA, conjuntoB)
    diferenca_ab = diferenca(conjuntoA, conjuntoB)
    
    print(f"União A u B = {uniao_ab}")
    print(f"Intersecção A ∩ B = {interseccao_ab}")
    print(f"Diferença A – B = {diferenca_ab}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python main.py conjuntoA.txt conjuntoB.txt")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
