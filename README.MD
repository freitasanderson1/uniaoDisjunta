# Operações com Conjuntos (União Disjunta)

Este projeto em Python realiza operações de união, intersecção e diferença entre dois conjuntos lidos a partir de arquivos de texto.

## Estrutura do Projeto

- `main.py`: Script Python que realiza as operações com conjuntos.
- `run`: Script shell para executar o `main.py` com arquivos predefinidos.
- `conjuntoA.txt`: Arquivo contendo os elementos do conjunto A.
- `conjuntoB.txt`: Arquivo contendo os elementos do conjunto B.

## Como Usar

### Pré-requisitos

- Python 3 instalado.
- Sistema operacional Unix-like (Linux, macOS) para o script shell.

### Passos para Executar

1. **Clone o repositório**:

   ```sh
   git clone https://github.com/freitasanderson/uniaoDisjunta.git
   cd uniaoDisjunta
   ```

2. **Prepare os arquivos de entrada**:

   Certifique-se de que os arquivos `conjuntoA.txt` e `conjuntoB.txt` estão no mesmo diretório do projeto. O formato dos arquivos deve ser:

   **conjuntoA.txt**:
   ```
   {1,a,b,c,d,10,11}
   ```

   **conjuntoB.txt**:
   ```
   {1,2,3,4,e,f}
   ```

3. **Dê permissão de execução ao script `run`**:

   ```sh
   chmod +x run
   ```

4. **Execute o script**:

   ```sh
   ./run
   ```

### Exemplo de Saída

```
Conjunto A: {'10', 'c', 'a', '11', '1', 'd', 'b'}
Conjunto B: {'4', '3', '1', '2', 'f', 'e'}
União A u B = {'10', 'c', '4', 'a', '3', '11', '1', '2', 'd', 'f', 'b', 'e'}
Intersecção A ∩ B = {'1'}
Diferença A – B = {'10', 'c', 'a', '11', 'd', 'b'}
```

## Explicação dos Scripts

### `main.py`

Este script lê os elementos dos conjuntos a partir dos arquivos especificados, realiza as operações de união, intersecção e diferença, e imprime os resultados.

- **Funções**:
  - `ler_conjunto(arquivo)`: Lê os elementos de um arquivo e retorna um conjunto.
  - `uniao(conjuntoA, conjuntoB)`: Retorna a união dos conjuntos A e B.
  - `interseccao(conjuntoA, conjuntoB)`: Retorna a intersecção dos conjuntos A e B.
  - `diferenca(conjuntoA, conjuntoB)`: Retorna a diferença do conjunto A em relação ao conjunto B.

### `run`

Este script shell executa o `main.py` com os arquivos `conjuntoA.txt` e `conjuntoB.txt` predefinidos.

- **Passos**:
  - Verifica se os arquivos de entrada existem.
  - Executa o script Python passando os arquivos de entrada como argumentos.