 # Read Cycle 
 
#  🚀 https://read-cycle.azurewebsites.net/

O Read Cycle é uma plataforma que conecta usuários interessados em trocar livros físicos já lidos por novos títulos. Para facilitar essa troca, é possível filtrar os livros disponíveis com base na localização do usuário e em suas preferências literárias. Além disso, o site oferece diversas outras funcionalidades para os usuário, como por exemplo:

- Cadastro de livros com Google Books API
- Filtro de livros por proximidade (menor custo de frete e maior   viabilidade de troca)
- Notificações a cada atualização na troca.
- Tipos de troca por pontos ou por outro livro.
- Gerenciamnento de suas solicitações e também solicitações que foram feitas para seus livrso.
- Gerenciamento de seus livros.



<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=Desenvolvimento&color=GREEN&style=for-the-badge">
</p>

# 🔨 FERRAMENTAS:
## Front-end:
- HTML/CSS/BOOTSTRAP
- JS
- HTMX

## Back-end:
- Django
- Azure WebJobs
- PostgresSQL
- Redis
- Celery/CeleryBeat
- Docker


## DEPLOY: https://read-cycle.azurewebsites.net/


Funcionalidades da aplicação:

- Cadastro, edição e login de usuários.
- Agendamento de Tasks assíncronas com Celery Beat
- Filtros personalizados com localização de usuário, categorias e títulos.
- Avaliação e comentário de livros.
- Tasks assíncronas para notificações por e-mail com Celery e Azure WebJobs.
- Cálculo de frete com API MelhorEnvio.



### Arquitetura do app.
![arquitetura](micro-architecture.png)

### Para ilustrar o fluxo de dados das funcionalidades e suas funções, fiz um diagrama de exemplo:

![diagram-example](rc-architecture-flow-dat.png)

cada funcionalidade descrita do projeto segue esse fluxo com pequenas mudanças. 

### 1. Request Trade
- Exemplifica a implmentação e controle de 
solitação por uma troca de livro

- Implementei o pattern Strategy para dar escalabilidade nos métodos de troca  e separação de como cada método processa e valida a troca.

- Como a troca por outro livro requer 2 postagens, uma para cada usuário, esse método de troca faz com que a Instância Trade fique pendente até o segunda postagem do envio.

### 2. Search Book
- Implementei um sistema de filtro utilizando o DjangoFilter para que eu filtre as querys com os parâmetros que o client pede. 

- Além disso, com o geoconding do usuário owner do book, consigo filtrar os que possuem menor distância do usuário que está filtrando.


### 3. Registro de Book

- Criei o registro de livros que busca na API do Google Book os parâmetros passados pelo usuário como: Título, Autor e versão.

- Com o resutlado, retorno para o usuário os dados para confirmação ou reescrita, assim, caso o livro não seja encontrado na API, o usuário pode preencher manualmente todos os fields.



Eu ainda estou desenvolvendo algumas features novas e atulizando o projeto, então sinta-se à vontade para sugestão.




<img loading="lazy" src="https://avatars.githubusercontent.com/u/88624922?v=4" width=115><br><sub>João Pedro</sub>
