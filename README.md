## API DEMO em Flask com model de classificação Iris

O modelo iris é um porblema de calssficação classico onde o classificador determina a especie da Flor (Íris) com base nos paramêtros passados.

veja mais em [Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris)

## Para rodar o ambiente

### Configurando o ambiente

O ambiente de execução é base no python virtualenv. Certifique-se de tê-lo instalado.

rode o comando

`bash setup_enviroment.sh`

Isso irá configurar o ambiente virtual do python no seu projeto

### Ativante o Ambiente virtual de execução

rode o comando

`source bin/activate`

### Atualizando libs do projeto

`pip3 install -r requeriments.txt`

### Rodando o projeto

`bash start_api.sh`

---
(TODO) Configuarar ambiente para rodar no docker


## Fazendo requisiçõos para a API

#### CURL

```
curl --location --request POST 'http://127.0.0.1:5000/predict?Content-Type=application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sepal_lenght":0.5,
    "sepal_width": 0.2,
    "petal_length": 0.5,
    "petal_width": 0.4
}'
```

Resultado esperado

```
{
    "prediction": "Iris-setosa"
}
```

(TODO) Receber resquisições em JSON
