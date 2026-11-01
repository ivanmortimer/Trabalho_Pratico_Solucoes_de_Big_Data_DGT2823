# DGT2823 - Tecnologias para Desenvolvimento de Soluções de Big Data

Repositório dedicado à entrega das **Microatividades (1 a 5)** e do **Trabalho Prático** da disciplina **DGT2823**, utilizando a linguagem **Python** e a biblioteca **Pandas**.

## Estrutura do Repositório

- `.gitignore`: Configuração do Git para ignorar caches de bytecode do Python, arquivos temporários de checkpoint do Jupyter Notebook, e ambientes virtuais do Python.
- `requirements.txt`: Lista de bibliotecas e dependências necessárias para reproduzir o ambiente do projeto.
- `conjunto_de_dados_trabalho_pratico_contextualizacao_atividade_pico_web.csv`: Conjunto de dados estruturado em formato CSV (separado por `;`).
- `microatividades.py`: Script contendo a resolução das 5 microatividades exploratórias.
- `trabalho_pratico.py`: Script contendo o pipeline de limpeza e transformação de dados em 13 etapas.
- `DGT2823_Microatividades_e_Trabalho_Pratico.ipynb`: Jupyter Notebook interativo combinando explicações, código e saídas de execução.
- `DGT2823_Microatividades_e_Trabalho_Pratico.pdf`: Versão exportada em PDF do Jupyter Notebook (via `jupyter nbconvert --to webpdf`) para leitura rápida e visualização direta no GitHub.
- `DGT2823_Microatividades_e_Trabalho_Pratico.html`: Versão exportada em HTML do Jupyter Notebook (via `jupyter nbconvert --to html`) para visualização estática em qualquer navegador web.

## Como Executar e Visualizar

1. **Visualização Rápida (Sem necessidade de execução):**
   - Os resultados completos da execução das microatividades e do trabalho prático podem ser consultados diretamente nos arquivos `DGT2823_Microatividades_e_Trabalho_Pratico.pdf`, `DGT2823_Microatividades_e_Trabalho_Pratico.html` ou `DGT2823_Microatividades_e_Trabalho_Pratico.ipynb`.

2. **Instalação das Dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execução dos Scripts via Terminal ou Jupyter Notebook:**
   ```bash
   python microatividades.py
   python trabalho_pratico.py
   ```
   