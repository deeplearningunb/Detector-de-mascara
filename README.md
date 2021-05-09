# Detector-de-mascara
Projeto com o intuito de criar um detector de mascaras utilizando técnicas de Deep Learning 

## Funcionalidade dos scripts

Uma breve explicação de cada script do projeto

* **dect_faces.py** [Script principal]

    Abre a webcam, carrega os dois modelos usados e os utiliza para fazer o reconhecimento em tempo real

* **mask_identifier.py**

    Realiza o treinamento do modelo, com as imagens contidas em ``data/training_images`` e ``data/test_images``

* **data/scrapping_persons.py**

    Coleta os dados de pessoas que não existem

* **data/add_masks.py**

    Adiciona máscaras nas imagens já coletadas pelo `scrapping_persons.py`

* **mask_detector_model**

    Modelo obtido com o treinamento

![Funcionamento do modelo](./assets/casoexemplo.gif)