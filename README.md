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
 curl -X POST -F 'sepal_lenght=0.5' -F 'sepal_width=0.2' -F 'petal_length=0.5' -F 'petal_width=0.4' http://127.0.0.1:5000/predict
```

Resultado esperado

```
{
    "prediction": "Iris-setosa"
}
```

(TODO) Receber resquisições em JSON
