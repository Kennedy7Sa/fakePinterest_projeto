## Bibliotecas 
- flask-login  para login 
- flask-bcrypt para criptografia 
- flask-wtf para trabalhar com formularios 
- email_validator para validações de email 

## Criar chaves secretas com a lib secrets 

```python
import secrets 
print(secrets.token_hex(16))

```

## Criar e carreagr requirements

- Pra salvar o arquivo de requirements  
```cmd
pip freeze > requirements.txt

````
- Pra carregar  o arquivo de requirements  
```cmd
pip install -r requirements.txt

````