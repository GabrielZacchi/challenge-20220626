# Use uma imagem base Python com o Poetry instalado
FROM python:3.9

# Define a variável de ambiente para evitar problemas de codificação
ENV LANG C.UTF-8

# Instale as dependências do sistema necessárias
RUN apt-get update && \
    apt-get install -y netcat

# Crie e defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie apenas os arquivos de dependência e o arquivo pyproject.toml para o contêiner
COPY poetry.lock pyproject.toml /app/

# Instale as dependências do projeto usando o Poetry
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copie o restante do código-fonte para o contêiner
COPY . /app/

# Comando para executar o servidor
CMD ["poetry", "run", "python", "core/manage.py", "runserver"]
