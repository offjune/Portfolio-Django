<h1 align="center" style="color:#f5f5f5;background-color:#0d1117;padding:10px;border-radius:8px;">📝 To-Do List Django</h1>

<p align="center">
  Um aplicativo simples, elegante e funcional para gerenciar suas tarefas, desenvolvido com <strong>Django</strong>.
</p>

---

## ✨ Funcionalidades

- ✅ Criar novas tarefas com título e prazo  
- 📋 Listar todas as tarefas  
- ✏ Editar tarefas existentes  
- ❌ Excluir tarefas  
- ☑ Marcar tarefas como concluídas  
- ⏳ Ordenação automática por prazo

---

## 🛠 Tecnologias Utilizadas

<div align="center" style="background-color:#0d1117;padding:10px;border-radius:8px;">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="Python"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" height="40" alt="Django"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" height="40" alt="HTML"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height="40" alt="CSS"/>
</div>

---

## 📂 Estrutura do Projeto

```bash
📦 To-Do-List-Django
 ┣ 📂 setup/            # Configurações do projeto
 ┣ 📂 todos/            # Aplicação principal
 ┃ ┣ 📜 models.py       # Modelo da tarefa
 ┃ ┣ 📜 views.py        # Lógica da aplicação
 ┃ ┗ 📂 templates/      # Templates HTML
 ┣ 📜 manage.py
 ┣ 📜 db.sqlite3
 ┗ 📜 requirements.txt
```
##🌐 Rotas Principais

| Rota              | Método     | Descrição              |
| ----------------- | ---------- | ---------------------- |
| `/`               | `GET`      | Lista todas as tarefas |
| `/create`         | `GET/POST` | Cria uma nova tarefa   |
| `/update/<id>`    | `GET/POST` | Atualiza uma tarefa    |
| `/delete/<id>`    | `POST`     | Exclui uma tarefa      |
| `/completed/<id>` | `GET`      | Marca como concluída   |


🚀 Como Executar
```bash
# Clone o repositório
git clone https://github.com/offjune/To-Do-List-Django.git

# Acesse a pasta do projeto
cd To-Do-List-Django

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Aplique as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
```
Acesse em: http://127.0.0.1:8000/

🗄 Diagrama do Banco de Dados
```mermaid
erDiagram
    TODO {
        int id PK
        string title
        datetime created_at
        date deadline
        date finished_at
    }
````
📜 Licença
Este projeto está sob a licença MIT. Sinta-se livre para utilizar e modificar.
💡 Desenvolvido por offjune com ❤️
