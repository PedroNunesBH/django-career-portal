# Sistema Web de Anúncios de Ofertas de Emprego com Django

Esse projeto é uma plataforma de anúncios de ofertas de emprego desenvolvido com o framework Django.
O foco do projeto é o backend do sistema.

# Funcionalidades

1. **Cadastro de Usuários** : Permite o cadastro dos usuários na plataforma.
2. **Sistema de Autenticação** : Sistema de autenticação simples e eficiente.
3. **Sistema De Recuperação de Senha** : Sistema para recuperação de senha do usuário integrado ao email.Basta fornecer o email de cadastro na página de recuperação e o usuário recebe as instruções e um email com o link para redefinir sua senha.
4. **Anúncio de Ofertas** : Os usuários devidamente cadastrados no sistema podem publicar suas ofertas de forma rápida e prática.
5. **CRUD Completo** : Os usuários responsáveis pela oferta podem visualizar,editar e excluir a mesma caso necessário.
6. **Controle de Ofertas** : Os administradores da plataforma conseguem verificar o número de ofertas cadastradas no momento e a cada adição/exclusão.

# Tecnologias Utilizadas

    -Django
    -HTML
    -CSS

## Pré-requisitos

Certifique-se de ter os seguintes pré-requisitos instalados em sua máquina:

- **Python**
- **Pip** (gerenciador de pacotes do Python)

## Instalação das Dependências do Projeto

Para instalar todas as dependências necessárias para o funcionamento correto do projeto(especificadas no requirements.txt) utilize o comando:

```bash
pip install -r requirements.txt
```
### Configuração do Ambiente

Este projeto utiliza variáveis de ambiente para configuração. Para configurar seu ambiente local:

1. Renomeie o arquivo `.env-example` para `.env` executando o seguinte comando no terminal :
   ```sh
   cp .env-example .env

2. Abra o arquivo .env e substitua as variáveis de exemplo pelos valores reais, seguindo as instruções fornecidas no próprio arquivo.

| Variável  | Descrição                                        | Exemplo                    |
|-----------|--------------------------------------------------|----------------------------|
| `EMAIL`   | O endereço de email usado para envio de emails.  | `meu_email@dominio.com`    |
| `SENHA`   | A senha do endereço de email especificado.       | `minha_senha_segura`       |

## Criando um Super Usuário(Administrador)

Para configurar um administrador no Django,no terminal,utilize o seguinte comando:

```bash
python manage.py createsuperuser
```

Após isso siga os passos descritos no terminal para configurar o mesmo.

## Configuração do Banco de Dados 

Para configurar o banco de dados do projeto são necessários dois comandos na seguinte ordem:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

## Rodando o Servidor Local

Para iniciar o servidor de desenvolvimento do Django em sua máquina utilize o seguinte comando:

```bash
python manage.py runserver
```

## Docker

O projeto contém os arquivos `Dockerfile` e `docker-compose.yml`  para a conteinerização da aplicação. Neste projeto, utilizaremos o Docker Compose para rodar a aplicação containerizada e conectá-la a um banco de dados PostgreSQL, também em um container.

**Passos para realizar o processo de conteinerização:**

1. **Instalar o Docker:**
   - Certifique-se de ter o Docker instalado e funcionando corretamente em sua máquina. Siga as instruções oficiais para [instalar o Docker](https://docs.docker.com/get-docker/).

2. **Configurar o Banco de Dados no Django:**
   - No arquivo `settings.py` da aplicação Django, substitua a configuração padrão da variável `DATABASES` pela seguinte configuração:
     

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT'),
        }
    }
    ```

3. **Subir os Containers:**
   - Abra o terminal e, no diretório da aplicação, execute o seguinte comando:

 ```bash
docker compose -p nomedoprojeto up
```

## Observações Adicionais:

Comando para parar e remover os containers:

```bash
docker compose down
```



