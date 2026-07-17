<div align="center">

<img src="static/og-image.png" alt="BI Data Generator PRO" width="100%">

<br><br>

# BI Data Generator PRO

**Gere bases de dados profissionais em Star Schema — em segundos.**

[![Streamlit App](https://img.shields.io/badge/🚀_Acessar_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://ai-bidatagenerator.streamlit.app)
[![GitHub Stars](https://img.shields.io/github/stars/RodrigoAiosa/bi_data_generator?style=for-the-badge&color=a78bfa&logo=github)](https://github.com/RodrigoAiosa/bi_data_generator/stargazers)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/Licença-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Open Source](https://img.shields.io/badge/Open_Source-❤️-a78bfa?style=for-the-badge)](https://github.com/RodrigoAiosa/bi_data_generator)

<br>

> 52 setores · Star Schema · Scripts SQL · Dashboards · Dicionário de Dados · PT 🇧🇷 / EN 🇺🇸

</div>

---

## 🎯 O Problema

Você tem o Power BI. Você tem o Tableau. Você tem a ferramenta.

**Mas não tem dados.**

Pede pro DBA criar as tabelas, espera semanas, recebe um Excel mal formatado com dados sensíveis que não pode usar em portfólio, e ainda passa horas limpando antes de começar de verdade.

**O BI Data Generator PRO resolve isso com um clique.**

---

## ✨ O que você recebe

<table>
<tr>
<td width="50%">

### 📊 Dados Realistas
Bases profissionais com dados sintéticos contextualmente corretos — vocabulário, métricas e dimensões específicos de cada setor. Nomes brasileiros, CNPJs, CPFs, datas e valores reais.

</td>
<td width="50%">

### 📐 Star Schema Pronto
Tabelas **Fato** com métricas e chaves estrangeiras + Tabelas **Dimensão** com atributos descritivos + **dCalendario** compatível com Power Query. Relacionamentos íntegros e sem ambiguidade.

</td>
</tr>
<tr>
<td width="50%">

### 🗄️ Scripts SQL Completos
Gere **DDL** (CREATE TABLE com tipos inferidos), **INSERT INTO** (dados reais em blocos) ou o **script completo** — tudo em ordem que respeita as chaves estrangeiras. SQL Server, PostgreSQL ou MySQL.

</td>
<td width="50%">

### 📖 Dicionário de Dados
Cada geração exporta documentação completa: tipo, descrição e exemplo de cada coluna, tabela por tabela. Pronto para anexar no seu projeto profissional.

</td>
</tr>
<tr>
<td width="50%">

### 📊 Dashboards por Setor
Preview interativo em Plotly com KPIs, gráficos de tendência e distribuições específicos de cada negócio — disponível antes mesmo de gerar os dados.

</td>
<td width="50%">

### 🧪 Modo Anomalia
Injeta problemas reais nos dados: spike de churn, margem negativa, queda de 70% num trimestre e outliers extremos. Ideal para praticar **análise de causa raiz**.

</td>
</tr>
<tr>
<td width="50%">

### 🌍 Bilíngue PT 🇧🇷 / EN 🇺🇸
Toggle na sidebar traduz toda a interface e os dados instantaneamente — labels, dashboards, dicionário e meses do calendário.

</td>
<td width="50%">

### 🔍 Pesquisa Inteligente
Campo de busca filtra setores em tempo real por nome ou descrição. Digite "saúde", "MRR", "combustível" ou qualquer palavra-chave.

</td>
</tr>
</table>

---

## 🚀 Como Usar

```
1. Escolha o setor      →   52 opções com dados contextualmente corretos
2. Defina o período     →   dCalendario gerada automaticamente
3. Ajuste o volume      →   100 até 100.000 linhas na tabela fato
4. Clique em Gerar      →   Base completa em segundos
5. Baixe o .zip         →   CSVs + Dicionário prontos para uso
```

> **Bônus:** Gere o script SQL antes mesmo de gerar os dados — sem precisar clicar em "Gerar base".

---

## 🏭 52 Setores Disponíveis

<details>
<summary><b>Ver todos os setores</b></summary>

<br>

| | Setor | Tabelas Fato | Destaques |
|---|---|---|---|
| 🌾 | Agronegócio | FatoSafra | Culturas, propriedades, insumos |
| 🍔 | Alimentos & Bebidas | FatoProducao | Conformidade ANVISA, refugo |
| 🏛️ | Arquitetura & Design | FatoServico | Honorários por m², retrabalho |
| 🎬 | Audiovisual & Produtora | FatoProducao | ROI, views, custo por departamento |
| ✈️ | Aviação Civil | FatoVoo | Aeronaves, aeroportos, passageiros |
| 💄 | Beleza & Estética | FatoVenda, FatoAgenda | Serviços, salões, recorrência |
| 🤝 | CRM | FatoOportunidade, FatoAtividade | Funil, win rate, ciclo de vendas |
| 🏢 | Condomínio & Facilities | FatoCota, FatoOcorrencia | Inadimplência, despesas |
| 🏗️ | Construção Civil | FatoObra | Materiais, fornecedores, custos |
| 🏪 | E-commerce | FatoPedido | Fretes, devoluções, pagamentos |
| 📚 | Educação | FatoMatricula | Alunos, cursos, instrutores |
| ⚡ | Energia | FatoConsumo | Medidores, subestações, tarifas |
| 🚀 | Espacial & Aeroespacial | FatoOperacao | Missões, TRL, anomalias, GB coletados |
| 🏟️ | Esportes | FatoPartida | Atletas, clubes, bilheteria |
| 🎉 | Eventos & Entretenimento | FatoEvento | Ingressos, NPS, fornecedores |
| 💊 | Farmacêutico | FatoVenda, FatoEstoque | Classe terapêutica, ANVISA |
| 💰 | Financeiro | FatoTransacao | Contas, agências, transações |
| 🏦 | Fintech | FatoTransacao | Cartões, cashback, antifraude |
| 🌲 | Florestal & Papel | FatoProducao | MAP, carbono, FSC |
| 🏷️ | Franquias | FatoDesempenho, FatoTaxa | Royalties, NPS por unidade |
| 🎮 | Games & eSports | FatoPartida | Jogadores, monetização in-game |
| 🏛️ | Governo & Setor Público | FatoDespesa, FatoReceita, FatoLicitacao | Empenho, liquidação |
| 🏨 | Hotelaria | FatoReserva | Hóspedes, canais, diárias |
| 🏠 | Imobiliário | FatoTransacao | Vendas, aluguéis, corretores |
| 🏭 | Indústria | FatoProducao | Máquinas, OEE, operadores |
| ⚖️ | Jurídico | FatoProcesso | Advogados, tribunais, êxito |
| 🔬 | Laboratório & Diagnóstico | FatoExame | Laudos, SLA, convênios |
| 🚚 | Logística | FatoEntrega | Transportadoras, rotas, SLA |
| 🚴 | Logística Urbana | FatoEntrega | Last mile, entregadores, falhas |
| 📣 | Marketing Digital | FatoPerformance, FatoConversao | CTR, ROAS, CPA |
| 📲 | Migração Claro (Portabilidade) | FatoMigracao | IN/OUT, motivos, operadoras |
| ⛏️ | Mineração | FatoExtracao | Minas, minerais, segurança |
| 🚗 | Mobilidade | FatoViagem | Motoristas, rotas, avaliações |
| 👗 | Moda & Vestuário | FatoVenda, FatoEstoque | Coleções, tamanhos, ruptura |
| 🐟 | Pesca & Aquicultura | FatoProducao | FCR, mortalidade, biomassa |
| 🐾 | Pet & Veterinária | FatoAtendimento | Pets, tutores, veterinários |
| 🛢️ | Petróleo & Gás | FatoProducao, FatoCusto | Poços, lifting cost, BSW |
| 🏢 | Recursos Humanos | FatoHorasTrabalhadas | Projetos, cargos, produtividade |
| ☁️ | SaaS B2B | FatoAssinatura | MRR, ARR, churn, NPS, LTV |
| 💧 | Saneamento & Água | FatoConsumo | Ligações, estações, tarifas |
| 🏥 | Saúde | FatoAtendimento | Pacientes, médicos, procedimentos |
| 🧠 | Saúde Mental | FatoSessao | Diagnósticos, modalidades, sessões |
| 🛡️ | Seguros | FatoApolice | Sinistros, corretores, loss ratio |
| 🦄 | Startups & Venture Capital | FatoRodada, FatoMetrica | Valuation, runway, burn rate |
| 🎬 | Streaming | FatoPlay | Assinantes, conteúdo, artistas |
| 💻 | Tecnologia | FatoContrato | SaaS, clientes, planos |
| 📡 | Telecom | FatoChamada | Assinantes, torres, planos |
| 🚛 | Transporte | FatoViagem, FatoAbastecimento, FatoManutencao | Frota, rentabilidade |
| ✈️ | Turismo | FatoViagem | Pacotes, agências, destinos |
| 🧵 | Têxtil & Confecção | FatoProducao | Fibras, eficiência, refugo |
| 🛒 | Varejo | FatoVenda | Produtos, filiais, devoluções |
| ✈️ | Viagens Corporativas | FatoViagem | Política de viagem, custo por dept. |

</details>

---

## 🗄️ Scripts SQL

Gere scripts SQL prontos para executar diretamente no seu banco — **sem digitar uma linha de código**.

```sql
-- Exemplo gerado automaticamente para o setor CRM (PostgreSQL)
-- Ordem de inserção respeita chaves estrangeiras:
--    1. dCalendario        [Calendário]  (365 linhas)
--    2. DimVendedor        [Dimensão]    ( 20 linhas)
--    3. DimProduto         [Dimensão]    ( 10 linhas)
--    4. DimConta           [Dimensão]    (200 linhas)
--    5. DimContato         [Dimensão]    (400 linhas)
--    6. FatoOportunidade   [Fato]        (500 linhas)
--    7. FatoAtividade      [Fato]        (750 linhas)

CREATE TABLE dCalendario (
    Data      DATE        NOT NULL,
    Ano       INTEGER     NOT NULL,
    Mes       INTEGER     NOT NULL,
    MesAno    VARCHAR(255) NULL,
    IdMesAno  INTEGER     NOT NULL,
    CONSTRAINT pk_dcalendario PRIMARY KEY (Data)
);
```

| Opção | Conteúdo | Uso ideal |
|---|---|---|
| **CREATE TABLE (DDL)** | Estrutura, tipos, PKs e índices | Criar o banco do zero |
| **INSERT INTO (dados)** | Dados reais em blocos de 500 linhas | Popular um banco existente |
| **Completo (DDL + INSERT)** | Os dois num único arquivo `.sql` | Setup completo em um clique |

**3 dialetos:** SQL Server · PostgreSQL · MySQL

---

## 📐 Arquitetura Star Schema

```
                    ┌─────────────┐
                    │ dCalendario │
                    │  (Calendário)│
                    └──────┬──────┘
                           │ id_data
          ┌────────────────┼────────────────┐
          │                │                │
   ┌──────┴──────┐  ┌──────┴──────┐  ┌──────┴──────┐
   │  DimCliente │  │  DimProduto │  │  DimFilial  │
   │  (Dimensão) │  │  (Dimensão) │  │  (Dimensão) │
   └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
          │                │                │
          └────────────────┼────────────────┘
                           │
                    ┌──────┴──────┐
                    │  FatoVenda  │
                    │    (Fato)   │
                    │  métricas   │
                    │  receita    │
                    │  quantidade │
                    └─────────────┘
```

| Componente | Descrição |
|---|---|
| **Tabela Fato** | Chaves estrangeiras (`id_*`) + métricas de negócio |
| **Tabelas Dimensão** | Chave primária + atributos descritivos |
| **dCalendario** | Data, Ano, Mês, MesAno, IdMesAno — Power Query ready |

---

## 🛠 Stack Tecnológica

| | Tecnologia | Função |
|---|---|---|
| 🐍 | **Python 3.8+** | Linguagem principal |
| 🌊 | **Streamlit ≥ 1.32** | Interface web interativa |
| 🐼 | **Pandas ≥ 2.0** | Geração e manipulação de dados |
| 🔢 | **NumPy ≥ 1.26** | Computação numérica vetorizada |
| 🎭 | **Faker ≥ 24.0** | Dados sintéticos realistas (PT-BR / EN-US) |
| 📈 | **Plotly ≥ 5.18** | Dashboards interativos por setor |

---

## 💻 Instalação Local

```bash
# Clone
git clone https://github.com/RodrigoAiosa/bi_data_generator.git
cd bi_data_generator

# Ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows

# Dependências
pip install -r requirements.txt

# Executar
streamlit run app.py
```

Acesse em `http://localhost:8501` 🎉

---

## 🔧 Adicionando um Novo Setor

**3 arquivos, 3 passos:**

**1.** Crie `generators/meu_setor.py`

```python
from datetime import date
import pandas as pd
from .helpers import new_ids, dcalendario, rand_dates, rng

def gerar_meu_setor(n: int, start: date, end: date) -> dict:
    dim = pd.DataFrame({
        "id_dim": new_ids(100),
        "nome":   [f"Item {i}" for i in range(1, 101)],
    })
    fato = pd.DataFrame({
        "id_fato":  new_ids(n),
        "id_dim":   rng.choice(dim["id_dim"].tolist(), n),
        "id_data":  rand_dates(start, end, n),
        "valor":    rng.uniform(100, 5000, n).round(2),
    })
    return {"DimItem": dim, "FatoMeuSetor": fato,
            "dCalendario": dcalendario(start, end)}
```

**2.** Exporte em `generators/__init__.py`

```python
from .meu_setor import gerar_meu_setor
__all__ = [..., "gerar_meu_setor"]
```

**3.** Registre em `config.py`

```python
from generators import gerar_meu_setor

SETORES = {
    ...,
    "🆕 Meu Setor": gerar_meu_setor,   # ordem alfabética
}
SETORES_INFO = [
    ...,
    ("🆕", "Meu Setor", "Descrição do setor"),
]
```

> O setor aparece automaticamente na interface, no contador do hero, nos flip-cards e na pesquisa inteligente.

---

## 🎯 Para Quem É

<table>
<tr>
<td align="center" width="25%">

**📊 Analistas de BI**<br><br>
Teste dashboards sem esperar dados reais

</td>
<td align="center" width="25%">

**🎓 Estudantes**<br><br>
Monte portfólio com dados realistas documentados

</td>
<td align="center" width="25%">

**👨‍💻 Desenvolvedores**<br><br>
Valide pipelines ETL com volumes conhecidos

</td>
<td align="center" width="25%">

**🏫 Professores**<br><br>
Dados para aula sem a tabela Northwind de 1997

</td>
</tr>
</table>

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Especialmente novos setores.

```bash
# Fork → Branch → Commit → PR
git checkout -b feature/setor-saas-marketplace
git commit -m 'feat: adiciona setor SaaS Marketplace'
git push origin feature/setor-saas-marketplace
```

Abra um **Pull Request** descrevendo o setor e as tabelas criadas.

---

## 📄 Licença

Distribuído sob a licença **MIT**. Veja [`LICENSE`](LICENSE) para detalhes.

---

<div align="center">

**Desenvolvido com ❤️ para a comunidade de BI e Data Analytics**

[![GitHub](https://img.shields.io/badge/GitHub-RodrigoAiosa-181717?style=flat-square&logo=github)](https://github.com/RodrigoAiosa)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rodrigo_Aiosa-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com/in/rodrigoaiosa)
[![App](https://img.shields.io/badge/App-ai--bidatagenerator.streamlit.app-FF4B4B?style=flat-square&logo=streamlit)](https://ai-bidatagenerator.streamlit.app)

<br>

⭐ **Se este projeto te ajudou, deixe uma estrela no GitHub!** ⭐

</div>
