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

Para instalar todas as dependências necessárias para o funcionamento correto do projeto(especificadas no requirements.txt) utilize o comando :

**pip install -r requirements.txt**

## Configuração do Banco de Dados 

Para configurar o banco de dados do projeto são necessários dois comandos na seguinte ordem:

**1 - python manage.py makemigrations**
**2 - python manage.py migrate**

## Rodando o Servidor Local

Para iniciar o servidor de desenvolvimento do Django em sua máquina utilize o seguinte comando:

**python manage.py runserver**
