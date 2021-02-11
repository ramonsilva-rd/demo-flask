## API DEMO em Flask com model de Predição

O modelo iris é um porblema de calssficação classico onde o classificador determina a especie da Flor (Íris) com base nos paramêtros passados.

veja mais em [Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris)

## Rodando o ambiente

O projeto roda dentro de um container docker, certifique-se de ter o docker instalado

Para rodar, basta executar o comando:
`make build && make run`

## Fazendo requisiçõos para a API

#### CURL

```
curl --location --request POST 'http://127.0.0.1:5000/predict \
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
