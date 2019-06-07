Ao correr este projeto num novo dispositivo, é necessário instalar as bibliotecas que este utiliza.
Para tal, a maneira mais fácil é instalar o Pipenv (pip install pipenv) e, na diretoria do projeto "TC_Project", correr o comando "pipenv install".
Depois deste passo, para ativar o ambiente virtual criado, utiliza-se o comando "pipenv shell", ainda na diretoria "TC_Project.
Depois, para correr o projeto, basta utilizar o comando "python run.py".

Caso o projeto não corra, é porque este utiliza variáveis de ambiente para a SECRET_KEY, DATABASE_URI,
e para as informações da conta gmail de onde irá enviar os emails.

Os campos EMAIL_USERNAME e EMAIL_PASSWORD não se encontram disponíveis por razões óbvias,
mas são preenchidos com o username e password da conta gmail de onde serão enviados os emails aos utilizadores.