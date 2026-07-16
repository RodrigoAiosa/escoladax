# 📊 Escola DAX

Plataforma gamificada para aprender **boas práticas de DAX** (Power BI) — na prática, escrevendo e corrigindo fórmulas, não só lendo teoria.

🔗 **Demo:** _adicione aqui o link do Streamlit Community Cloud depois do deploy_

## ✨ O que tem na plataforma

- **📚 Práticas** — 30 boas práticas de DAX organizadas por categoria (Fundamentos, Contexto de Filtro, Iteradoras, Time Intelligence, Modelagem, Performance) e nível (Iniciante, Intermediário, Avançado). Cada uma compara o jeito **❌ Evitar** com o jeito **✅ Preferir**, com explicação.
- **🧩 Simulador de Fórmulas** — exercícios de múltipla escolha: dado um cenário de negócio, escolha a fórmula DAX correta.
- **✍️ Escreva sua Fórmula** — um mini-modelo de dados de exemplo (`Fato_Vendas` + dimensões `Dim_Produto`, `Dim_Cliente`, `Dim_Calendario`) para praticar. Inclui:
  - **Destaque de sintaxe** (funções, tabelas/colunas, strings, números coloridos)
  - **Corretor** com exercícios guiados e validação por padrões
  - **Modo livre** para escrever e receber avisos gerais de boas práticas (parênteses desbalanceados, uso de `/` em vez de `DIVIDE`, sugestão de correção para nomes de função digitados errado)
- **🎯 Desafios semanais**, **🏆 Badges** e **📊 Perfil** — sistema de XP, níveis e conquistas para manter o engajamento.

> ⚠️ Importante: como o DAX depende do motor do Power BI/Analysis Services, este projeto **não executa DAX de verdade**. A correção é baseada em reconhecimento de padrões de texto (a lógica esperada precisa aparecer na fórmula), não em cálculo real sobre dados.

## 🚀 Como rodar localmente

```bash
git clone https://github.com/SEU_USUARIO/escoladax.git
cd escoladax
pip install -r requirements.txt
streamlit run app.py
```

Acesse em `http://localhost:8501`.

## ☁️ Deploy no Streamlit Community Cloud

1. Suba este repositório para o GitHub (público ou privado).
2. Acesse [share.streamlit.io](https://share.streamlit.io).
3. Clique em **New app**, selecione o repositório e o arquivo `app.py`.
4. Deploy — pronto, sem configuração adicional (não usa banco de dados nem segredos).

## 🗂️ Estrutura do projeto

```
escoladax/
├── app.py              # aplicação Streamlit completa
├── requirements.txt     # dependências (streamlit, pandas)
├── README.md
├── LICENSE
└── .gitignore
```

## 🛠️ Stack

- [Streamlit](https://streamlit.io) — interface e estado da aplicação
- [pandas](https://pandas.pydata.org) — tabelas de exemplo (fato/dimensões)
- Python padrão (`re`, `difflib`, `html`) — destaque de sintaxe e correção de fórmulas

## 📄 Licença

Este projeto é de uso livre para fins educacionais. Sinta-se à vontade para adaptar as práticas e exercícios ao seu próprio conteúdo.

---

Criado por **Rodrigo Aiosa**.
