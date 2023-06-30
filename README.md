# Nome dos itegrantes:
Daniel Pereira, Daniel Cavalcanti, João Victor Do Nascimento Ribeiro, Flávio França

# TinocoFrut 
A TinocoFrut é uma API desenvolvida em Django, projetada para gerenciar o cadastro de usuários, produtos e estoque de uma empresa fictícia chamada TinocoFrut. Este documento fornece informações sobre o projeto e explica como instalar as dependências necessárias para executar a API em seu ambiente local.

# Funcionalidades Principais
A TinocoFrut API oferece as seguintes funcionalidades principais:

Cadastro de usuários: permite registrar novos usuários fornecendo informações como nome, idade, e-mail e senha.
Cadastro de produtos: possibilita cadastrar produtos com detalhes como nome, quantidade, descrição, preço, categoria e tipo.
Gerenciamento de estoque: fornece uma página de estoque que exibe informações gerais sobre o estoque da TinocoFrut.
Login: permite que os usuários façam login usando suas credenciais de usuário.

# Requisitos do Sistema
Antes de prosseguir com a instalação da API, certifique-se de que o seguinte esteja instalado em seu sistema:

Python (versão 3.6 ou superior)
Django (versão 3.0 ou superior)
Django REST Framework (versão 3.12 ou superior)
Banco de dados suportado pelo Django (por exemplo, SQLite, MySQL, PostgreSQL)

# Instalação
Siga as etapas abaixo para configurar e executar a TinocoFrut API em seu ambiente local:

Clone o repositório do projeto:
git clone https://github.com/seu-usuario/nomedomeuprojeto.git

Acesse o diretório do projeto:
cd nomedomeuprojeto

Crie e ative um ambiente virtual (opcional, mas recomendado):
python3 -m venv env
source env/bin/activate

Instale as dependências do projeto:
pip install -r requirements.txt

Execute as migrações do banco de dados:
python manage.py migrate

Crie um superusuário (opcional, necessário para acessar a área de administração):
python manage.py createsuperuser

Inicie o servidor de desenvolvimento:
python manage.py runserver

Agora a API TinocoFrut estará em execução em http://localhost:8000/.

# Uso da API
A API possui várias rotas para realizar operações de cadastro, login, consulta e outras funcionalidades. Você pode consultar a documentação da API para obter mais detalhes sobre as rotas disponíveis e seus parâmetros.

Para acessar a documentação da API, acesse http://localhost:8000/swagger/ ou http://localhost:8000/redoc/ no seu navegador.

# Contribuição
Se você quiser contribuir com o projeto da TinocoFrut API, siga as etapas abaixo:

Faça um fork do repositório.
Clone o fork do repositório em seu ambiente local.
Crie um branch para sua nova feature ou correção de bug.
Implemente as alterações desejadas.
Execute os testes e verifique se tudo está funcionando corretamente.
Envie um pull request para o repositório principal.

# Conclusão
A TinocoFrut API é uma API desenvolvida em Django que oferece recursos para gerenciamento de usuários, produtos e estoque. Com este guia, você poderá configurar a API em seu ambiente local e começar a explorar suas funcionalidades. Se tiver alguma dúvida ou encontrar algum problema, sinta-se à vontade para abrir uma nova issue no repositório do projeto. Aproveite a TinocoFrut API e boa codificação!
