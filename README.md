# 🥛 Milk Production Dashboard

Dashboard interativo de análise de produção de leite nos EUA por estado, com visualizações de renda anual, soma acumulada, análise Year-over-Year e percentual por ano.

---

## 📁 Estrutura do Projeto

```
informacoes_milk/
│
├── analise.py            # Aplicação principal Streamlit
├── informacoes_milk.csv  # Dataset exportado do SQL
├── requirements.txt      # Dependências Python
└── .gitignore
```

---


## 🗄️ SQL — Origem dos Dados

Os dados utilizados no dashboard foram extraídos via SQL a partir de duas tabelas: `milk_production` e `state_lookup`. A query é composta por **três camadas aninhadas**, cada uma com uma responsabilidade específica.

### Query Completa

```sql
SELECT *,
    ROUND(CAST(soma_ano AS FLOAT) / CAST(Soma_total AS FLOAT), 3) * 100 AS percentual,
    soma_ano - qtd_ano_anterior AS diferenca
FROM (
    SELECT *,
        SUM(soma_ano) OVER (PARTITION BY State_ANSI) AS Soma_total,
        SUM(soma_ano) OVER (PARTITION BY State_ANSI ORDER BY Year) AS Soma_ac,
        LAG(soma_ano, 1) OVER (PARTITION BY State_ANSI) AS qtd_ano_anterior
    FROM (
        SELECT
            Year,
            mp.State_ANSI,
            sl.State,
            SUM(mp.Value) AS soma_ano
        FROM milk_production mp
        JOIN state_lookup sl ON mp.State_ANSI = sl.State_ANSI
        GROUP BY mp.Year, mp.State_ANSI
        HAVING mp.Year >= 2020
        ORDER BY mp.State_ANSI
    )
)
```

---

### 📐 Camada 1 — Subquery Interna: Agregação Base

```sql
SELECT
    Year,
    mp.State_ANSI,
    sl.State,
    SUM(mp.Value) AS soma_ano
FROM milk_production mp
JOIN state_lookup sl ON mp.State_ANSI = sl.State_ANSI
GROUP BY mp.Year, mp.State_ANSI
HAVING mp.Year >= 2020
ORDER BY mp.State_ANSI
```

Aqui é feita a **agregação base**: soma de toda a produção (`Value`) por estado e por ano. O `JOIN` com `state_lookup` traz o nome legível do estado. O `HAVING` filtra apenas anos a partir de 2020.

> ⚠️ Nota: o `HAVING` aqui filtra após o `GROUP BY`, o que funciona neste caso. Em outras situações, filtrar com `WHERE` antes do agrupamento é mais eficiente.

---

### 📐 Camada 2 — Subquery Intermediária: Window Functions

```sql
SELECT *,
    SUM(soma_ano) OVER (PARTITION BY State_ANSI) AS Soma_total,
    SUM(soma_ano) OVER (PARTITION BY State_ANSI ORDER BY Year) AS Soma_ac,
    LAG(soma_ano, 1) OVER (PARTITION BY State_ANSI) AS qtd_ano_anterior
FROM (...)
```

Esta camada aplica **Window Functions** sobre o resultado da camada anterior. Ao contrário do `GROUP BY`, as Window Functions **não colapsam as linhas** — elas calculam valores agregados mantendo cada linha individual visível.

#### O que é uma Window Function?

Uma Window Function opera sobre uma "janela" de linhas relacionadas à linha atual. A sintaxe geral é:

```sql
FUNÇÃO() OVER (
    PARTITION BY coluna   -- divide os dados em grupos
    ORDER BY coluna       -- define a ordem dentro de cada grupo
)
```

#### As três funções usadas:

**`SUM() OVER (PARTITION BY State_ANSI)`** → `Soma_total`
- Soma **todos os anos** de cada estado numa única linha, sem quebrar os dados.
- Como não tem `ORDER BY`, soma o total completo do estado em todas as linhas desse estado.
- Resultado: todas as linhas do mesmo estado terão o mesmo `Soma_total`.

**`SUM() OVER (PARTITION BY State_ANSI ORDER BY Year)`** → `Soma_ac`
- Soma **acumulada** ano a ano, dentro de cada estado.
- O `ORDER BY Year` faz com que o SQL some progressivamente: ano 1 + ano 2 + ano 3...
- Resultado: a última linha de cada estado terá o valor igual ao `Soma_total`.

**`LAG(soma_ano, 1) OVER (PARTITION BY State_ANSI)`** → `qtd_ano_anterior`
- Retorna o valor de `soma_ano` da **linha anterior** dentro do mesmo estado.
- O `1` indica quantas posições "olhar para trás".
- A primeira linha de cada estado terá `NULL` (não há ano anterior).
- Permite comparar o ano atual com o anterior sem fazer um `self JOIN`.

---

### 📐 Camada 3 — Query Externa: Cálculos Finais

```sql
SELECT *,
    ROUND(CAST(soma_ano AS FLOAT) / CAST(Soma_total AS FLOAT), 3) * 100 AS percentual,
    soma_ano - qtd_ano_anterior AS diferenca
FROM (...)
```

Com todos os dados calculados nas camadas anteriores, a query externa faz dois cálculos finais:

**`percentual`**
- Divide a produção do ano pelo total histórico do estado.
- O `CAST AS FLOAT` é necessário para forçar divisão decimal (sem ele, a divisão de inteiros resultaria em 0 ou 1).
- Multiplicado por 100 e arredondado a 3 casas com `ROUND`.

**`diferenca`**
- Subtrai o valor do ano anterior (`qtd_ano_anterior`) do valor atual (`soma_ano`).
- Equivalente ao que a análise **Year-over-Year (YoY)** representa: quanto cresceu ou caiu em relação ao período anterior.

---

## 📊 Gráficos Disponíveis no Dashboard

| Gráfico | Coluna SQL | Descrição |
|---|---|---|
| Renda Total por Ano | `soma_ano` | Produção agregada por ano |
| Soma Acumulada dos Anos | `Soma_ac` | Crescimento acumulado ano a ano |
| Análise YoY | `diferenca` | Variação em relação ao ano anterior |
| Percentual por Ano | `percentual` | Peso de cada ano sobre o total do estado |

---

## 🌐 Dashboard Online

Acesse o dashboard em produção aqui:
👉 **[Link do Dashboard](http://localhost:8501/)**

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.13**
- **Pandas** — manipulação de dados
- **Streamlit** — interface web interativa
- **Plotly Express** — visualizações gráficas
- **SQLite / SQL** — extração e transformação dos dados