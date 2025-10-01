# 🏥 Clínica Vida+ API

API REST completa para gerenciamento de clínica médica, desenvolvida com FastAPI, SQLAlchemy e PostgreSQL. Sistema robusto para gestão de pacientes, médicos, consultas e autenticação de usuários.

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Executando a Aplicação](#executando-a-aplicação)
- [Documentação Interativa](#documentação-interativa)
- [Endpoints da API](#endpoints-da-api)
- [Exemplos de Uso](#exemplos-de-uso)
- [Testes](#testes)
- [Migrações de Banco de Dados](#migrações-de-banco-de-dados)

---

## 🎯 Sobre o Projeto

A **Clínica Vida+ API** é um sistema backend completo desenvolvido para facilitar a gestão de clínicas médicas. O sistema oferece:

- ✅ Autenticação e autorização segura com JWT
- ✅ Gerenciamento completo de pacientes
- ✅ Cadastro e controle de médicos
- ✅ Agendamento e controle de consultas
- ✅ Sistema de roles (paciente, médico, admin)
- ✅ Validação de dados com Pydantic
- ✅ Migrações de banco de dados com Alembic
- ✅ Documentação interativa automática (Swagger/ReDoc)

---

## 🚀 Tecnologias Utilizadas

### Backend
- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno e de alta performance
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - ORM para Python
- **[Alembic](https://alembic.sqlalchemy.org/)** - Gerenciamento de migrações de banco
- **[Pydantic](https://docs.pydantic.dev/)** - Validação de dados e schemas

### Segurança
- **[python-jose](https://python-jose.readthedocs.io/)** - Geração e validação de tokens JWT
- **[passlib](https://passlib.readthedocs.io/)** - Hash de senhas com bcrypt

### Banco de Dados
- **PostgreSQL** (recomendado para produção)
- **SQLite** (suportado para desenvolvimento)

### Outras Bibliotecas
- **[Uvicorn](https://www.uvicorn.org/)** - Servidor ASGI
- **[ReportLab](https://www.reportlab.com/)** - Geração de PDFs
- **[FastAPI-Mail](https://sabuhish.github.io/fastapi-mail/)** - Envio de emails
- **[Pytest](https://docs.pytest.org/)** - Framework de testes

---

## ⚡ Funcionalidades

### Autenticação (`/auth`)
- Registro de novos usuários com diferentes roles
- Login com geração de token JWT
- Autenticação via OAuth2 Password Flow

### Pacientes (`/api/patients`)
- Listar todos os pacientes
- Buscar paciente por ID
- Criar novo paciente
- Atualizar dados do paciente

### Consultas (`/api/consultations`)
- Listar todas as consultas
- Buscar consulta por ID
- Agendar nova consulta
- Atualizar status da consulta (pendente, confirmada, concluída, cancelada)
- Atualizar dados da consulta

---

## 📁 Estrutura do Projeto

```
Clinica+Vida/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Ponto de entrada da aplicação
│   ├── config.py               # Configurações e variáveis de ambiente
│   ├── database.py             # Configuração do banco de dados
│   │
│   ├── models/                 # Modelos SQLAlchemy
│   │   ├── __init__.py
│   │   ├── user.py             # Modelo de usuários
│   │   ├── patient.py          # Modelo de pacientes
│   │   ├── doctor.py           # Modelo de médicos
│   │   └── consulta.py         # Modelo de consultas
│   │
│   ├── schemas/                # Schemas Pydantic
│   │   ├── __init__.py
│   │   ├── user_schema.py
│   │   ├── patient_schema.py
│   │   └── consultation_schema.py
│   │
│   ├── routes/                 # Rotas/Endpoints
│   │   ├── __init__.py
│   │   ├── auth_routes.py      # Rotas de autenticação
│   │   ├── paciente_routes.py  # Rotas de pacientes
│   │   └── consulta_routes.py  # Rotas de consultas
│   │
│   ├── services/               # Lógica de negócio
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── patient_service.py
│   │   └── consultation_service.py
│   │
│   └── utils/                  # Utilitários
│       ├── __init__.py
│       ├── jwt_handler.py      # Manipulação de tokens JWT
│       ├── security.py         # Funções de segurança
│       ├── exceptions.py       # Exceções personalizadas
│       └── pdf_generator.py    # Geração de PDFs
│
├── alembic/                    # Migrações do banco de dados
│   ├── versions/
│   └── env.py
│
├── tests/                      # Testes automatizados
│   └── test_auth.py
│
├── .env                        # Variáveis de ambiente (NÃO versionar)
├── .env.example                # Exemplo de variáveis de ambiente
├── alembic.ini                 # Configuração do Alembic
├── requirements.txt            # Dependências do projeto
└── README.md                   # Este arquivo
```

---

## 📋 Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:

- **Python 3.9+** - [Download](https://www.python.org/downloads/)
- **PostgreSQL 12+** (ou SQLite para desenvolvimento) - [Download](https://www.postgresql.org/download/)
- **pip** (gerenciador de pacotes Python)
- **Git** - [Download](https://git-scm.com/)

### Verificar instalações:

```bash
python --version
pip --version
psql --version
git --version
```

---

## 🔧 Instalação

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd Clinica+Vida
```

### 2. Crie um ambiente virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuração

### 1. Configure o Banco de Dados

**PostgreSQL (Recomendado para produção):**

Crie um banco de dados no PostgreSQL:

```sql
CREATE DATABASE clinica_vida;
CREATE USER clinica_user WITH PASSWORD 'sua_senha_segura';
GRANT ALL PRIVILEGES ON DATABASE clinica_vida TO clinica_user;
```

### 2. Configure as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
# Database
DATABASE_URL=postgresql://clinica_user:sua_senha_segura@localhost:5432/clinica_vida

# Para SQLite (desenvolvimento):
# DATABASE_URL=sqlite:///./clinica_vida.db

# Security
SECRET_KEY=sua_chave_secreta_super_segura_aqui_gere_com_openssl
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Email (Opcional)
MAIL_USERNAME=seu_email@gmail.com
MAIL_PASSWORD=sua_senha_app
MAIL_FROM=seu_email@gmail.com
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
```

**Gerar SECRET_KEY segura:**

```bash
# No terminal Python:
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 3. Execute as Migrações do Banco

```bash
alembic upgrade head
```

Este comando criará todas as tabelas necessárias no banco de dados.

---

## ▶️ Executando a Aplicação

Há duas formas de executar a aplicação:

### Opção 1: Usando Uvicorn (Recomendado)

```bash
uvicorn app.main:app --reload
```

### Opção 2: Executando diretamente

```bash
python -m app.main
```

### Flags úteis do Uvicorn:

```bash
# Com reload automático (desenvolvimento)
uvicorn app.main:app --reload

# Especificar host e porta
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Modo de produção (sem reload)
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

A aplicação estará rodando em: **http://localhost:8000**

---

## 📚 Documentação Interativa

### 🌟 Por que usar a Documentação Interativa?

A documentação interativa é uma das maiores vantagens do FastAPI. Ela é gerada **automaticamente** e oferece:

#### ✅ Benefícios da Documentação Swagger UI

1. **Teste de Endpoints em Tempo Real**
   - Não precisa de Postman ou Insomnia
   - Teste todos os endpoints diretamente no navegador
   - Visualize respostas em tempo real

2. **Exploração da API**
   - Veja todos os endpoints disponíveis
   - Entenda os parâmetros necessários
   - Visualize os schemas de request/response
   - Conheça os códigos de status HTTP

3. **Autenticação Integrada**
   - Botão "Authorize" para inserir seu token JWT
   - Uma vez autenticado, todas as requisições incluem o token
   - Teste endpoints protegidos facilmente

4. **Documentação Sempre Atualizada**
   - Sincronizada automaticamente com o código
   - Sem necessidade de manutenção manual
   - Reflete mudanças instantaneamente

5. **Validação Visual**
   - Veja exemplos de dados válidos
   - Entenda as validações aplicadas
   - Identifique campos obrigatórios e opcionais

### Acesse a Documentação:

#### 📘 Swagger UI (Interativa)
```
http://localhost:8000/docs
```
- Interface visual moderna
- Melhor para testes e exploração
- Permite executar requisições diretamente

#### 📗 ReDoc (Alternativa)
```
http://localhost:8000/redoc
```
- Documentação mais limpa e organizada
- Melhor para leitura e apresentações
- Foco na visualização dos schemas

### 🔐 Como usar a autenticação na documentação:

1. Acesse http://localhost:8000/docs
2. Primeiro, registre um usuário no endpoint `/auth/register`
3. Faça login no endpoint `/auth/login` e copie o `access_token`
4. Clique no botão **"Authorize"** 🔒 (canto superior direito)
5. Cole o token no campo (formato: `Bearer seu_token_aqui` ou apenas `seu_token_aqui`)
6. Clique em "Authorize" e depois em "Close"
7. Agora você pode testar todos os endpoints protegidos! 🎉

---

## 🔌 Endpoints da API

### Autenticação

| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| POST | `/auth/register` | Registrar novo usuário | ❌ |
| POST | `/auth/login` | Login e obtenção de token | ❌ |

### Pacientes

| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| GET | `/api/patients` | Listar todos os pacientes | ✅ |
| GET | `/api/patients/{id}` | Buscar paciente por ID | ✅ |
| POST | `/api/patients` | Criar novo paciente | ✅ |
| PUT | `/api/patients/{id}` | Atualizar paciente | ✅ |

### Consultas

| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| GET | `/api/consultations` | Listar todas as consultas | ✅ |
| GET | `/api/consultations/{id}` | Buscar consulta por ID | ✅ |
| POST | `/api/consultations` | Criar nova consulta | ✅ |
| PATCH | `/api/consultations/{id}/status` | Atualizar status | ✅ |
| PUT | `/api/consultations/{id}` | Atualizar consulta | ✅ |

---

## 💡 Exemplos de Uso

### 1. Registrar um novo usuário

```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "medico@clinica.com",
    "password": "senha123",
    "role": "doctor"
  }'
```

### 2. Fazer login

```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=medico@clinica.com&password=senha123"
```

**Resposta:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### 3. Criar um paciente (com autenticação)

```bash
curl -X POST "http://localhost:8000/api/patients" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "João Silva",
    "birth_date": "1990-05-15",
    "phone": "(11) 98765-4321",
    "address": "Rua das Flores, 123",
    "user_id": 1
  }'
```

### 4. Agendar uma consulta

```bash
curl -X POST "http://localhost:8000/api/consultations" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
    "patient_id": 1,
    "doctor_id": 1,
    "start_datetime": "2024-12-20T14:30:00",
    "price": 250.00
  }'
```

### 5. Atualizar status de uma consulta

```bash
curl -X PATCH "http://localhost:8000/api/consultations/1/status" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
    "status": "confirmed"
  }'
```

---

## 🧪 Testes

Execute os testes automatizados:

```bash
pytest
```

Execute com cobertura:

```bash
pytest --cov=app tests/
```

Execute um arquivo específico:

```bash
pytest tests/test_auth.py -v
```

---

## 🗄️ Migrações de Banco de Dados

### Criar uma nova migração

```bash
alembic revision --autogenerate -m "Descrição da alteração"
```

### Aplicar migrações

```bash
alembic upgrade head
```

### Reverter última migração

```bash
alembic downgrade -1
```

### Ver histórico de migrações

```bash
alembic history
```

### Ver status atual

```bash
alembic current
```

---

## 🔒 Segurança

### Boas Práticas Implementadas

- ✅ Senhas hasheadas com bcrypt
- ✅ Tokens JWT com expiração configurável
- ✅ Validação de dados com Pydantic
- ✅ Proteção contra SQL Injection (SQLAlchemy ORM)
- ✅ Configurações sensíveis em variáveis de ambiente
- ✅ CORS configurável
- ✅ OAuth2 Password Flow

### Recomendações

- 🔐 Nunca compartilhe seu arquivo `.env`
- 🔐 Use senhas fortes para o SECRET_KEY
- 🔐 Configure HTTPS em produção
- 🔐 Implemente rate limiting
- 🔐 Monitore logs de acesso

---

## 📝 Modelos de Dados

### User (Usuário)
- `id`: Integer (PK)
- `email`: String (Único)
- `hashed_password`: String
- `role`: String (patient, doctor, admin)
- `is_active`: Boolean
- `created_at`: DateTime
- `updated_at`: DateTime

### Patient (Paciente)
- `id`: Integer (PK)
- `user_id`: Integer (FK)
- `name`: String
- `birth_date`: Date
- `phone`: String
- `address`: String
- `created_at`: DateTime
- `updated_at`: DateTime

### Doctor (Médico)
- `id`: Integer (PK)
- `user_id`: Integer (FK)
- `name`: String
- `specialty`: String
- `license_number`: String (Único)
- `phone`: String
- `created_at`: DateTime
- `updated_at`: DateTime

### Consultation (Consulta)
- `id`: Integer (PK)
- `patient_id`: Integer (FK)
- `doctor_id`: Integer (FK)
- `start_datetime`: DateTime
- `end_datetime`: DateTime
- `price`: Decimal
- `status`: String (pending, confirmed, completed, cancelled)
- `notes`: Text
- `consultation_type`: String
- `created_at`: DateTime
- `updated_at`: DateTime

---

## 🛠️ Tecnologias e Padrões

### Arquitetura
- **Layered Architecture** (Routes → Services → Models)
- **Repository Pattern** (via SQLAlchemy)
- **Dependency Injection** (FastAPI Depends)

### Padrões de Código
- **PEP 8** - Style Guide for Python Code
- **Type Hints** - Tipagem estática
- **Async/Await** - Programação assíncrona

---

## 🚧 Roadmap

- [ ] Implementar sistema de notificações
- [ ] Adicionar relatórios em PDF
- [ ] Criar dashboard administrativo
- [ ] Implementar upload de documentos
- [ ] Sistema de lembretes de consultas
- [ ] Integração com calendário
- [ ] API de pagamentos
- [ ] Prontuário eletrônico

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

## 👨‍💻 Desenvolvedor

Desenvolvido com ❤️ para facilitar a gestão de clínicas médicas.

---

## 📞 Suporte

Para dúvidas ou problemas:
- Consulte a [documentação interativa](http://localhost:8000/docs)
- Verifique os logs da aplicação
- Revise as configurações do arquivo `.env`

---

**🎉 Pronto! Sua API está configurada e funcionando!**

Acesse http://localhost:8000/docs e comece a explorar todos os recursos da Clínica Vida+ API.
