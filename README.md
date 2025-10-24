# 🏪 Sistema de Gerenciamento de Supermercado

## 📖 Visão Geral

O **Sistema de Gerenciamento de Supermercado** é uma aplicação modular desenvolvida em **Python + Flask**, voltada para automação operacional no varejo.  
O sistema recebe informações de dispositivos **ESP (crachás inteligentes)** e processa-as para gerar **ações corretivas automáticas**, como notificações para equipes, medições de tempo de resposta e análise de produtividade.

A comunicação é **event-driven**, com serviços desacoplados em múltiplas camadas, permitindo fácil manutenção e expansão.

---

## ⚙️ Arquitetura Geral

O sistema é estruturado em uma **arquitetura N-Tier + Event-Driven**, composta por módulos independentes conectados pela camada principal (`main`), que injeta dependências entre os serviços.  
Cada camada tem responsabilidades bem definidas — entrada, orquestração, persistência, interface e análise.

### 🧩 Estrutura de Pastas

```
project_root/
│
├── src/
│   │
│   ├── ingest/                # Entrada e validação dos dados (ponto de entrada)
│   │   ├── api/               # Ponto de entrada (porta que vai escutar as ESPs)
│   │   ├── ingest_controller/ # Controla todo o fluxo dependendo do tipo de evento
│   │   ├── ingest_dispatcher/ # Contém lógica para envio das requisições ao Orchestrator
│   │   ├── validation/        # Camada para autenticação da ESP e validação do seu conteúdo
│   │   └── errors/            # Camada para lidar com erros e emitir mensagens ou retrys
│   │
│   ├── orchestrator/          # Núcleo de processamento e decisão
│   │   ├── controller/        # Coordena as regras conforme o tipo de evento
│   │   ├── service/           # Armazena a lógica para realizar o processamento das requisições do controller
│   │   ├── dispatcher/        # Contém lógica para envio das respostas para as ESPs
│   │   └── repository/        # Conexão, fallback de dados e persistência e logs de eventos
│   │
│   ├── admin_ui/              # Interface administrativa (gerenciamento e logs)
│   │
│   ├── logs/                  # Registro de eventos e métricas do sistema
│   │
│   ├── core/                  # Configurações, utilitários e variáveis de ambiente
│   │
│   └── dashboards/            # Transformação de logs em métricas e visualizações
│
└── test/                      # Testes unitários e de integração
```

---

## 🧑‍💻 Tecnologias Principais

- **Linguagem:** Python 3.11+
- **Framework Web:** Flask
- **Banco de Dados:** SQLite / PostgreSQL
- **Gerenciador de Pacotes:** uv
- **Protocolo de Comunicação:** MQTT
- **Interface de Admin:** React ou Streamlit (em desenvolvimento)
- **Arquitetura:** N-Tier + Event-Driven

---

## 🧰 Boas Práticas

- Evitar dependências diretas entre módulos (usar injeção na `main`)
- Logar cada decisão crítica com `event_id` e `timestamp`
- Separar arquivos de configuração por ambiente
- Manter funções puras dentro dos serviços
- Simular dados de entrada (ESPs) para testes locais

---

## 🔄 Pipeline de Eventos

O fluxo principal do sistema segue as etapas abaixo:

```mermaid

ESP = A[1️⃣ Recebimento de Evento - (Áudio + Imagem?)]
A --> B[2️⃣ Ingest_Service - Valida e formata dados]
B --> C[3️⃣ Media_Service - STT: Áudio → Texto]
C --> D[4️⃣ Orchestrator/Controller - Decide a ação a tomar]
D --> E[5️⃣ Orchestrator/Service - Gera JSON: {event, action}]
E --> F[6️⃣ Repository - Valida e persiste dados]
F --> G[7️⃣ Dispatcher - Envia ação para o colaborador correto]
G --> H[8️⃣ Logging - Registra tudo: event_id, actor, result]
H --> I[9️⃣ Dashboard - Converte logs em métricas de performance]

```

⚠️ Casos excepcionais:
- O evento pode **não conter imagem**.
- O áudio pode falhar; o sistema salva a ocorrência como **incompleta** e marca para retry.
- Se o dispositivo de destino estiver offline, o `dispatcher` faz reenvios com `retry` e `timeout`.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

- **uv** (gerenciador de pacotes e ambiente)
- Banco de dados: **SQLite** (desenvolvimento) / **PostgreSQL** (produção)

### Instalação

```bash
# 1. Clonar o repositório
git clone <link_do_projeto>
cd Market_Manager

# 2. Criar ambiente com uv
uv venv
source .venv/bin/activate  # (Linux/Mac)
# ou
.venv\Scripts\activate     # (Windows)

# 3. Instalar dependências
uv sync
```

### Configuração do Ambiente

Crie um arquivo `.env` na pasta `core/` com os parâmetros:

```
DB_URL=sqlite:///./database/dev.db
BROKER_URL=mqtt://localhost:1883
MAX_FILE_SIZE_MB=10
AUDIO_FOLDER=./data/audio
IMAGE_FOLDER=./data/images
```

### Execução

```bash
uv run flask run
```

Ou, se preferir usar diretamente:

```bash
python main.py
```

---

## 📊 Próximos Passos e Visão Futura

O projeto será expandido para abranger mais áreas operacionais:
- **Compras**, **Recebimento**, **Operadores de Caixa**
- Integração de **IA leve** para análise inteligente de logs e geração de *insights automáticos*
- **Câmeras de monitoramento** com visão computacional
- **Checklists automatizados** integrados à rotina dos crachás
- **Métricas justas e personalizadas** de desempenho operacional

> A meta é criar um **ecossistema inteligente e transparente** para medir eficiência, reduzir desperdícios e aprimorar a gestão da operação.

---