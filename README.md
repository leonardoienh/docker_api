1.Como executar
<br>
-Clonar o repositório do GitHub, use o comando anexado no seu terminal:
  git clone https://github.com/leonardoienh/docker_api.git

-Entrar na pasta do repositório
<br>
-Entrar na pasta 'meu-projeto'
<br>
-Acessar o cmd via pasta: Digitando 'cmd' na barra de diretório da pasta
<br>
-Digitar esse comando: docker-compose up --build


2-Aplicação e seu USO

Método 1: Criar a tabela produtos
Rota: GET /criar_tabela
Objetivo: Cria a tabela no banco (caso ainda não exista).
Como usar: Acesse a URL no navegador ou utilize curl:
http://localhost:5000/criar_tabela
ou via terminal com o comando:
bash curl http://localhost:5000/criar_tabela

Método 2: Limpar todos os dados da tabela
Rota: GET /limpar
Objetivo: Apaga todos os registros da tabela produtos.
Como usar: Acesse a URL no navegador ou utilize curl:
http://localhost:5000/limpar
ou via terminal com o comando:
bash curl http://localhost:5000/limpar

Método 3: Cadastrar dados na tabela
Rota: POST /formulario
Objetivo: Cadastrar registro na tabela produtos.
Como usar: Acesse a URL no navegador ou utilize curl:
http://localhost:5000/formulario

Método 4: Listar todos os produtos
Rota: GET /getdados
Objetivo: Retorna todos os produtos em formato JSON.
Como usar: Acesse a URL no navegador ou utilize curl:
http://localhost:5000/getdados
ou via terminal com o comando:
bash curl http://localhost:5000/getdados

3-Finalizar
-No cmd de execução do Docker aperte CTRL + C para dar stop na execução;
