# Detector-de-mascara
Projeto da disciplina de Deep Learning (2/2020) que tem como intuito de criar um detector de mascaras utilizando técnicas de Deep Learning.

![Funcionamento do modelo](./assets/casoexemplo.gif)

## Membros

|Nome|Matricula|Github|
|--|--|--|
|Ana Carolina Carvalho da Silva|190063441|[AnaCarolcs](https://github.com/AnaCarolcs)|
|Lucas da Cunha Andrade|180105256|[nYCSTs](https://github.com/nYCSTs)|
|Matheus Gabriel Alves Rodrigues|180106970|[Matheus73](https://github.com/Matheus73)|

## Funcionalidade dos scripts

Uma breve explicação de cada script do projeto

* **dect_faces.py** [Script principal]

    Abre a webcam, carrega o modelo usado e o utiliza para fazer classificação em tempo real

* **mask_identifier.py**

    Realiza o treinamento do modelo, com as imagens contidas em ``data/training_images`` e ``data/test_images`` e salva o modelo

* **data/scrapping_persons.py**

    Coleta os dados de pessoas que não existem, utilizando para isso o site [thispersondoesnotexist.com](https://thispersondoesnotexist.com/)

* **data/add_masks.py**

    Adiciona máscaras nas imagens já coletadas pelo `scrapping_persons.py`

* **mask_detector_model**

    Modelo obtido com o treinamento

