## Desafio: Medicar
# Teste Técnico Backend [REMOTO]

### Como executar o projeto

 01 - Faça um fork desse projeto para a sua conta GitHub clicando no botão Fork.

 02 - Clone essa cópia do reposítorio para a sua maquina.
 ```
 git clone https://github.com/[seuNomeDeUsuarioDoGitHub]/Medicar.git
 ```

 03 - Instale o [Python 3.9+](https://www.python.org/downloads/).

 04 - Crie um ambiente virtual.

 05 - Inicie o ambiente virtual.

 06 - Instale os [Requerimentos](requeriments.txt)

 ```
 pip install -r requeriments.txt
 ```

 07 - copie e cole o arquivo local_settings_example.py que se encontra dentro da pasta medicar e renomeie esse novo arquivo para local_settings.py
 
 08 - Faça a migração do banco de dados do projeto
 ```
 python manage.py migrate
 ```

 09 - Rode os testes para verificar se esta tudo certo
 ```
 python manage.py test
 ```

 10 - Crie um superusuario
 ```
 python manage.py createsuperuser
 ```

 11 - inicie o servidor de desenvolvimento
 ```
 python manage.py runserver
 ```