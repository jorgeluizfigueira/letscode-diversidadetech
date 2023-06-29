# <p align="center"> <b> Consumindo dados do Spotify e armazenando com o Postgresql </b> 
 
##  💻 Sobre o projeto

Este repositório trata do projeto do Módulo V (Banco de Dados) do programa DiversidadeTech. Foi escolhida a proposta 2, no qual o objetivo era criar um código Python que consuma dados de uma API pública, e armazene os dados em um banco de dados PostgreSQL.
    
Para atingir esse objetivo, teve-se a ideia simples de utilizar os dados de algumas músicas do spotify dos participantes e armazená-las no banco.

As seguintes etapas foram consideradas: modelagem do banco (*figura banco_dados_modelo_fisico.png*), criação do banco e tabelas, escrita dos códigos de conexão e manipulação do banco, códigos de obtenção dos dados da músicas e persitência no banco, e por fim escrita de algumas consultas para obter uma análise simples dos dados (*arquivo consultas.sql*).  

    
## 🛠 Tecnologias

Esse projeto foi desenvolvido na linguagem Python, utilizando as bibliotecas: *spotipy*, como cliente API do Spotify; *psycopg2* como  adaptador de banco de dados; e o *PostgreSQL* sendo o banco de dados.
    
Também serviram como tecnologias auxiliares o *SQL Power Architect*, usado durante a modelagem do banco, e o cliente SQL *DBeaver* que ajudou durante a escrita das instruções SQL de consulta e manipulação. 

## 📲 Requerimentos

- **Instale as bibliotecas necessárias a partir do PyPI:**
  ```shell
  pip install -r requirements.txt
  ```
- **Obtenha as credenciais do Spotify**
(1)Acesse <a href="https://developer.spotify.com/dashboard/"> Spotify Dashboard </a>, faça login normalmente com sua conta Spotify. (2) Clique em "Create An App", e preencha com um nome de aplicativo e sua descrição. (3) Após criado, guarde os dados de **CLIENT ID** e **CLIENT SECRET** no arquivo *spotify_credentials.txt* . 

- **Banco de Dados**
Crie o banco de dados e suas tabelas a partir do arquivo **database.sql**. Altere o arquivo **database.ini** com as devidas configurações de acesso do banco criado.
    
- **Utilização**
    
A partir do arquivo **musicas.py** é possivel obter os dados das músicas dado um id de usuário e id da playlist. Essas informações são facilmente obtidas por meio dos links de compartilhamento de perfil e playlist do próprio Spotify.
    
## 🗒️ Dados
    
Os dados obtidos neste projeto educativo foram exportados e salvos na pasta *data*.