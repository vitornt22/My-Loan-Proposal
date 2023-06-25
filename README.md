# MLP- My Loan Proposal

Sistema para a solicitação de propostas de empréstimo

## 🚀 Starting

Instruções para rodar o sistema na sua máquina


### 📋 1- Rode os seguintes comandos 


Primeiramente certifique-se de ter um ambiente docker integrado ao seu sistema.

```
docker-compose build
docker-compose up -d
```

ou

```
docker-compose up --build
```

Se por acaso obtiver algum erro ou problema como a utilização das portas definidas, utilize os seguintes comandos.

```
sudo lsof -i:PORT
sudo kill PID 
```

### 🔧 2- Acesse o link abaixo para ter acesso a interface

[Local host para aplicação MLP](http://localhost:8082/)


Se por acaso quiser acessar os dados da API, acessar o link abaixo

[Local host para aplicação MLP](http://localhost:8000/)


### ⚙️ 3- Admin do Django

Para fazer login na área do admin do django, utilize as credenciais abaixo

acesse o link :

[Admin do Django ](http://localhost:8000/admin/login/?next=/admin/)

```
username: DigitalsysTecnologia
password: 123
```

### 4- Testes

Para realização de vários cadastros ao mesmo tempo, facilitando assim a visualização das funcionalidades da APLICAÇÃO,
siga os passos na sua máquina local.

Acesse o ambiente virtual 

```
python -m venv venv
source venv/bin/activate
```

Instale as ferramentas necessárias

```
pip install requirements.txt
```

Inicie o celery

```
celery -A myLoanProposal worker --loglevel=info
```

Em outra bash do terminal rode o shell

```
python manage.py shell
```

Com shell em execução, faça

```
from model_bakery import baker
baker.make('loan.Loan', _quantity=30)
```

obs: você pode alterar a quantidade de 30 para mais ou menos, conforme as suas necessidades




