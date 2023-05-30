# SISAR

Sistema de Antecipação e Reposição de Aulas do IFPI CACOR


## Criando o ambiente virtual

```python
mkdir sisar
```

cd sisar

Atualizar o sistema

```python
sudo apt update 
```


```python
sudo apt -y upgrade
```

Instalar o pip3

```python
sudo apt install python3-pip
```

Instalar ferramentas adicionais


```python
sudo apt install build-essential libssl-dev libffi-dev python3-dev
```

Instalando o env e virtualenv


```python
sudo apt install -y python3-venv
```

```python
sudo apt install python3-virtualenv
```

Instalando no MacOS

```python
sudo pip uninstall virtualenv

sudo -H pip install virtualenv
```

Criando seu ambiente virtual. Vamos chamá-lo de generic env


```python
virtualenv venv
```

Criando o seu ambiente virtual no Windows 

```python
python -m virtualenv venv
```

Criando seu ambiente virtual no MacOS

```python
virtualenv -p python3 <desired-path>

virtualenv -p python3 venv

```

Ative o ambiente virtual 

```python
. venv/bin/activate
```

Caso queira desativar o ambiente virtual, na pasta

```python
deactivate 
```

```python
quit()
```

## Instalando as dependências ao sistema

```python
pip install -r requirements.txt
```

## Criando um banco de dados 

Para criar um banco de dados para o nossa livraria, vamos executar o seguinte comando no console (precisamos estar no diretório que contém o arquivo manage.py).

```python
python manage.py makemigrations sisar 
```

```python
python manage.py migrate 
```

## Povoando o banco de dados 


```python
python povoando_banco.py
```
