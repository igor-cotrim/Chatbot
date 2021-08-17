# Um Robô de atendimento para um vendedor de alimentos, vulgo senhor Alex

OBS: Se estiver no Windows, importante está com um Python 3.6.8 e rodar `python -m pip install -r requirements.txt` e `python -m spacy download en` e no arquivo requirements.txt
certifique que tem esses arquivos:
```
spacy==2.1.9
chatterbot==1.0.4
chatterbot_corpus==1.2.0
pytz
flask
```

Se estiver no Linux certifique de instalar as seguintes dependências:
```
chatterbot
chatterbot_corpus
flask
```

Depois que baixar as dependências vá ao arquivo `treinamento.py` e mude as CONFIGURACOES_CONVERSAS para as pastas que estão na sua maquina.
```
Copia o caminho do arquivo informacoes.json e saudacoes.json e coloque onde está o meu caminho.
```

Após isso execute o arquivo `treinamento.py` para treinar o robô e execute o arquivo `robo.py` para inicializa-lo.

As conversas disponiveis estão nos arquivos `informacoes.json` e `saudacoes.json` dentro da pasta de conversas
