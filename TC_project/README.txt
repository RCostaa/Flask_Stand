Ao correr este projeto num novo dispositivo, � necess�rio instalar as bibliotecas que este utiliza.
Para tal, a maneira mais f�cil � instalar o Pipenv (pip install pipenv) e, na diretoria do projeto "TC_Project", correr o comando "pipenv install".
Depois deste passo, para ativar o ambiente virtual criado, utiliza-se o comando "pipenv shell", ainda na diretoria "TC_Project.
Depois, para correr o projeto, basta utilizar o comando "python run.py".

Caso o projeto n�o corra, � porque este utiliza vari�veis de ambiente para a SECRET_KEY, DATABASE_URI,
e para as informa��es da conta gmail de onde ir� enviar os emails.

Os campos EMAIL_USERNAME e EMAIL_PASSWORD n�o se encontram dispon�veis por raz�es �bvias,
mas s�o preenchidos com o username e password da conta gmail de onde ser�o enviados os emails aos utilizadores.