<h1 align="center">Oficina Mecânica</h1>

- No começo você terá que escolher, qual das dos dois bancos irá querer utilizar (carros ou pessoa).

<img src="https://github.com/glauber2k2/workshopFabrica/blob/desafio/tela1.png" >

- Escolhendo Pessoa, você terá duas informações de cadastro (CPF = (chave primaria), e o Nome).
- Você pode repetir o nome, porem não o CPF, até pelo fato de apenas 1 pessoa possuir o CPF indicado.
- Você so conseguirá cadastrar a informação no banco no formato correto (xxx-xxx-xxx-xx), caso contrario não será feito o cadastro.

<img src="https://github.com/glauber2k2/workshopFabrica/blob/desafio/tela2.png">

- Na hora de cadastrar o carro/serviço, você tem a opção de ligar o serviço com algum cliente pre-cadastrado no sistema.
- Será gerado um protocolo unico (id_carro) a cada serviço cadastrado no sistema, pois assim você conseguirá acessar o dado pelo protocolo gerado.
- Um cliente poderá ter seu CPF ligado com varios carros na oficina, porem cada carro só é ligado com um unico cliente.

<img src="https://github.com/glauber2k2/workshopFabrica/blob/desafio/tela3.png">

- Caso queira acessar um dado especifico, você terá que utilizar a chave primaria: </br>
cliente = CPF </br>
serviço = protocolo/id
- Com a chave, você irá colocar após o link na sua URL de busca.
- Fazendo isso será redirecionado para o painel de controle do dado.

<img src="https://github.com/glauber2k2/workshopFabrica/blob/desafio/tela4.png">

- Agora, que você ja está com o painel do dado escolhido aberto, terá a opção de excluir ou editar.
- Para editar basta alterar o dado, e clicar em PUT.
- Para excluir basta clicar em DELETE.

<img src="https://github.com/glauber2k2/workshopFabrica/blob/desafio/tela5.png">

## Como abrir o sistema no seu pc:

- Você terá que instalar as dependencias, para isso execute o seguinte comando:
```
$ git clone https://github.com/glauber2k2/workshopFabrica.git
```
- Logo após instale o ambiente virtual no seu projeto:
```
$ python -m venv venv
```
- Agora crie um banco de dados no postgresql, e coloque o nome desejado.
- Abra o arquivo CRUD/oficina/settings.py.
- Altere o seguinte trecho:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<nome_escolhido>',
        'USER': 'postgres',
        'PASSWORD': '<senha_do_seu_servidor>',
        'HOST': 'localhost'
    }
}
```
- Agora terá que instalar as dependencias no projeto, execute:
```
$ pip install -r requirements.txt
```
- Agora execute:
```
$python manage.py makemigrations

$python manage.py migrate
```
- E por fim, para abrir a aplicação, execute:
```
$ python manage.py runserver
```
- Segure CTRL + Clique no link.
- Pronto, servidor iniciado!

## Sobre:

- Projeto feito como etapa de seleção da empresa "Fabrica de Softwares", para a área de Back-end.
- Projeto feito utilizando o Djangorestframework.
- Para entrar em contato, me mande um <a href="mailto:devglaubermonteiro@gmail.com">Email</a>.
