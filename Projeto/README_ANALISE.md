
# 📚 Análise de Desempenho Acadêmico com Python e SQLite

Este projeto realiza a análise do desempenho dos alunos de uma universidade com base em um banco de dados SQLite (`universidade.db`). Ele calcula a média de notas por aluno e gera um gráfico para facilitar a visualização dos resultados.

---

## 📦 Estrutura do Projeto

```
/UniversidadeProjeto
├── universidade.db             # Banco de dados SQLite
├── analise_com_grafico.py      # Script Python para análise e gráfico
├── medias_por_aluno.csv        # Arquivo gerado com as médias
├── grafico_medias.png          # Gráfico de barras gerado
└── script_banco_universidade.sql # Script SQL para criar e popular o banco
```

---

## ⚙️ Pré-requisitos

- Python 3.10+
- Bibliotecas:
  - `pandas`
  - `matplotlib`
  - `sqlite3` (padrão do Python)

Para instalar os pacotes:

```bash
pip install pandas matplotlib
```

---

## ▶️ Como Usar

1. Certifique-se de que o banco `universidade.db` está na mesma pasta.
2. Execute o script de análise:

```bash
python analise_com_grafico.py
```

3. Os seguintes arquivos serão gerados:
   - `medias_por_aluno.csv`
   - `grafico_medias.png`

---

## 📊 Saída Esperada

- Tabela de médias no terminal
- Arquivo `.csv` com nome e média de cada aluno
- Gráfico de barras com os nomes e as respectivas médias

---

## 💡 Observação

Caso ainda não tenha criado o banco, execute o script `script_banco_universidade.sql` no VSCode com SQLTools para criar todas as tabelas e popular os dados.

