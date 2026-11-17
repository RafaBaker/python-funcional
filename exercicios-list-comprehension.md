# Exercícios de list comprehension

Oito exercícios em dificuldade crescente, no estilo das questões 29, 30 e 31 da Lista Python Funcional — Parte 2.

Em todos, use **list comprehension para construir as listas**. Quando precisar somar elementos, você pode usar `reduce`.

## 1. Quadrados dos pares

Defina `quadradosPares(n)`, que retorna os quadrados dos números pares entre `1` e `n`, incluindo os limites.

```python
quadradosPares(8)
# [4, 16, 36, 64]
```

## 2. Seleção de palavras

Defina `palavrasLongas(palavras, tamanho)`, que retorna as palavras com pelo menos a quantidade de caracteres indicada.

Preserve a ordem original.

```python
palavrasLongas(["sol", "casa", "mar", "python"], 4)
# ["casa", "python"]
```

## 3. Divisores de um número

Defina `divisores(n)`, que retorna todos os divisores positivos de um inteiro positivo `n`, em ordem crescente.

```python
divisores(12)
# [1, 2, 3, 4, 6, 12]
```

## 4. Operações entre posições correspondentes

Defina `diferencasQuadradas(v, w)`, que recebe duas listas numéricas de mesmo tamanho e retorna o quadrado da diferença entre os elementos de cada posição.

```python
diferencasQuadradas([1, 2, 3], [3, 2, 1])
# [4, 0, 4]
```

Por exemplo, o primeiro resultado vem de `(1 - 3)²`.

## 5. Pares com uma soma determinada

Defina `paresSoma(n, soma)`, que retorna todos os pares `(x, y)` em que ambos os valores estão entre `1` e `n` e `x + y` é igual à soma recebida.

Considere pares em ordens diferentes como resultados diferentes.

```python
paresSoma(4, 5)
# [(1, 4), (2, 3), (3, 2), (4, 1)]
```

## 6. Concatenação de sublistas

Defina `achata(listas)`, que recebe uma lista de listas e retorna uma única lista com seus elementos, preservando a ordem.

```python
achata([[1, 2], [], [3], [4, 5]])
# [1, 2, 3, 4, 5]
```

## 7. Transposição de uma matriz

Defina `transposta(matriz)`, que transforma as linhas de uma matriz em colunas.

Considere uma matriz não vazia, com todas as linhas do mesmo tamanho. Use list comprehensions aninhadas.

```python
transposta([[1, 2, 3], [4, 5, 6]])
# [[1, 4], [2, 5], [3, 6]]
```

## 8. Números abundantes

Um inteiro positivo é abundante quando a soma de seus divisores positivos, excluindo ele próprio, é maior que ele.

Defina `abundantes(n)`, que retorna todos os números abundantes entre `1` e `n`.

```python
abundantes(25)
# [12, 18, 20, 24]
```

Por exemplo, os divisores próprios de `12` são `1, 2, 3, 4, 6`. A soma é `16`, portanto `12` é abundante.

Sugestão de início: exercícios **1, 3 e 5**. Eles praticam, respectivamente, transformação com filtro, seleção por condição e combinação de duas sequências.
