# Guia de `reduce`

Pelo que apareceu na q35, sua maior dificuldade foi **definir o que o acumulador representa e manter esse formato durante todo o `reduce`**. A partir disso surgiram os problemas com listas dentro de listas, comparações e o caso inicial.

Vou organizar o guia em torno desses pontos.

**1. Entenda o que o `reduce` entrega à sua função**

A estrutura é:

```python
reduce(passo, entrada, valor_inicial)
```

A função `passo` recebe:

```python
def passo(acumulador, atual):
    return novo_acumulador
```

- `acumulador`: o resultado construído até aquele momento.
- `atual`: o próximo elemento da entrada.
- O retorno se torna o acumulador da próxima chamada.

Por exemplo:

```python
def somar(acumulador, atual):
    return acumulador + atual

reduce(somar, [2, 3, 4], 0)
```

As chamadas são equivalentes a:

```text
somar(0, 2) → 2
somar(2, 3) → 5
somar(5, 4) → 9
```

Você escreve **como fazer um passo**. O `reduce` organiza a sequência de chamadas.

**2. Antes de escrever a função, decida o formato do acumulador**

Na soma, o acumulador é um número.

Na sua `pack`, ele é **uma lista contendo os grupos já construídos**:

```python
[[1], [2, 2], [3]]
```

Como você aplicou um `map` que transforma cada elemento em uma lista, o elemento atual também é uma lista:

```python
[3]
```

Portanto, o acordo da sua função é:

```text
Recebe:
    acumulador → lista de grupos
    atual      → lista com um elemento

Retorna:
    nova lista de grupos
```

Esse formato precisa ser mantido em **todos os caminhos** da função.

A demonstração interativa da mensagem está representada abaixo em texto. A entrada após o `map` é `[[1], [2], [3], [3], [3], [4]]`, e o acumulador inicial é `[]`.

| Passo | Acumulador recebido | Elemento recebido | Valores comparados | Novo acumulador |
| --- | --- | --- | --- | --- |
| 1 | `[]` | `[1]` | Não há grupo anterior | `[[1]]` |
| 2 | `[[1]]` | `[2]` | `1` e `2` | `[[1], [2]]` |
| 3 | `[[1], [2]]` | `[3]` | `2` e `3` | `[[1], [2], [3]]` |
| 4 | `[[1], [2], [3]]` | `[3]` | `3` e `3` | `[[1], [2], [3, 3]]` |
| 5 | `[[1], [2], [3, 3]]` | `[3]` | `3` e `3` | `[[1], [2], [3, 3, 3]]` |
| 6 | `[[1], [2], [3, 3, 3]]` | `[4]` | `3` e `4` | `[[1], [2], [3, 3, 3], [4]]` |

No primeiro passo, cria-se o primeiro grupo. Quando o valor recebido é igual ao do último grupo, esse grupo é ampliado. Quando é diferente, acrescenta-se um novo grupo.

**3. O valor inicial determina como a primeira chamada começa**

Você encontrou um problema importante: sem valor inicial, o `reduce` usa o primeiro elemento da entrada como acumulador.

Se a entrada for:

```python
[[1], [2], [3]]
```

Ele começa com:

```python
acumulador = [1]
atual = [2]
```

Mas `[1]` ainda não tem o formato de uma lista de grupos.

Com `[]` como valor inicial, começa assim:

```python
acumulador = []
atual = [1]
```

Agora você controla a criação do primeiro grupo. Por isso, precisa tratar esse caso **antes de chamar `head` ou `last`**:

```python
if not acumulador:
    return [atual]
```

Se `atual` é `[1]`, então `[atual]` é `[[1]]`.

O acumulador vazio é um caso que sua função precisa saber processar.

**4. Separe mentalmente elemento, grupo e lista de grupos**

Essa foi uma das confusões mais frequentes no seu código.

Considere:

```python
acumulador = [[1], [3, 3]]
atual = [3]
```

Observe os níveis:

```python
last(acumulador)        # [3, 3] → último grupo
head(last(acumulador)) # 3      → elemento desse grupo
head(atual)            # 3      → elemento recebido
```

Comparar os grupos inteiros:

```python
[3, 3] == [3]  # False
```

não responde se o próximo elemento pertence ao mesmo grupo.

Para essa decisão, você precisa comparar **os valores dos elementos**.

Uma prática útil é anotar ao lado de cada expressão:

```text
Isso é um número?
Uma lista de elementos?
Uma lista de grupos?
```

**5. Os colchetes mudam a estrutura do resultado**

Você usou expressões parecidas que produzem resultados diferentes:

```python
a = [1]
b = [2]

a + b        # [1, 2]
[a] + [b]    # [[1], [2]]
[a + b]      # [[1, 2]]
```

- `a + b`: junta os conteúdos das listas.
- `[a] + [b]`: mantém cada lista como um grupo separado.
- `[a + b]`: junta os conteúdos e envolve o resultado em um grupo.

Na `pack`, existem duas operações diferentes:

- **Criar um novo grupo:** acrescentar uma sublista ao acumulador.
- **Ampliar o último grupo:** preservar os grupos anteriores e reconstruir o último.

Antes de escolher uma expressão, escreva um exemplo concreto do resultado que você quer produzir.

**6. O retorno precisa preservar o trabalho anterior**

No seu primeiro código, o trecho:

```python
else y
```

descartava o acumulador inteiro quando encontrava um elemento diferente.

Pergunte em cada caso:

> Onde ficaram os grupos que eu já tinha construído?

Eles precisam aparecer no retorno, com a atualização necessária.

Também diferencie:

```python
print(resultado)  # Exibe o resultado
return resultado # Entrega o resultado a quem chamou
```

Dentro da função passada ao `reduce`, retornar o novo acumulador é essencial: ele será usado na próxima chamada.

**7. Use uma função nomeada antes de tentar uma lambda**

Para aprender, recomendo começar com:

```python
def passo(acumulador, atual):
    ...
```

Assim você consegue separar os casos:

- Acumulador vazio.
- Elemento igual ao do último grupo.
- Elemento diferente.

Depois que essa função estiver funcionando, você pode decidir se uma lambda deixa o código mais claro. **Não é obrigatório usar lambda com `reduce`.**

**8. Escolha entre `map`, `filter` e `reduce` pelo trabalho necessário**

- **`map`:** transformar cada elemento independentemente. Exemplo: transformar cada grupo em `(quantidade, elemento)` na questão 36.
- **`filter`:** selecionar os elementos que atendem a uma condição.
- **`reduce`:** construir um resultado em que cada passo depende do que já foi acumulado. Exemplo: decidir se um elemento amplia o último grupo da `pack`.

Para seus próximos exercícios com `reduce`, siga esta ordem:

1. Escreva um exemplo de entrada e saída.
2. Defina o formato do acumulador.
3. Escolha o valor inicial.
4. Simule duas ou três chamadas no papel.
5. Escreva a função de um passo.
6. Teste lista vazia, um elemento, três repetições e valores iguais separados.

Para praticar, tente prever o acumulador da `pack` após cada elemento de:

```python
[2, 2, 2, 5, 2]
```

As três repetições verificam se você compara os elementos corretamente; o último `2` verifica se você preserva a separação entre grupos.
