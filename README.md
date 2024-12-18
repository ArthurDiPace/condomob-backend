# Condomob Backend

Este é o backend do projeto Condomob, desenvolvido em Django REST Framework.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados antes de prosseguir:
- Python (versão 3.8)
- Pip (gerenciador de pacotes do Python)
- Ambiente virtual (recomendado)

## Instalação

1. Clone o repositório:
git clone https://github.com/seu-usuario/condomob-backend.git
cd condomob-backend

2. Configurar Ambiente Virtual (opcional, mas recomendado):
python -m venv env
source env/bin/activate # no Windows use venv\Scripts\activate

3. Instalar Dependências:
pip install -r requirements.txt

## Configuração

1. Configurar Variáveis de Ambiente:
(Já subi com o .env para facilitar)

2. Aplicar Migrações do Banco de Dados:
python manage.py migrate

## Executando o Servidor de Desenvolvimento

Para iniciar o servidor de desenvolvimento do Django:
python manage.py runserver

OBS.: A anexação do arquivo depende do front-end que esta em outro repositorio
