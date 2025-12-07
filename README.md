# 🏠 CRM - Gestão de Clientes (Design de Interiores)

Este repositório contém o código-fonte de um sistema de CRM (Customer Relationship Management) desenvolvido como **Projeto de Extensão** para o curso de Engenharia de Software da **Descomplica Faculdade Digital**.

## 📖 Sobre o Projeto

O objetivo deste projeto foi desenvolver uma solução tecnológica real para otimizar os processos de gestão de uma **empresa de Design de Interiores**. O sistema visa centralizar o cadastro de clientes, gerenciar atendimentos e facilitar a organização de dados para projetos de decoração e reforma.

O projeto foi concebido para resolver dores reais de organização e relacionamento com o cliente no nicho de interiores, oferecendo uma interface amigável e funcional.

## 🛠 Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Framework Web:** Django
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Bibliotecas Auxiliares:**
    * `django-crispy-forms` (Estilização de formulários)
    * `crispy-bootstrap5` (Integração do Crispy com Bootstrap 5)

---

## 🚀 Como rodar o projeto localmente

Siga os passos abaixo para clonar e executar a aplicação na sua máquina.

### 1. Pré-requisitos
Certifique-se de ter o [Python](https://www.python.org/downloads/) instalado em sua máquina.

### 2. Clonar o repositório
Abra o terminal e execute:

```bash
git clone [https://github.com/carvalholevis/CRM-Gestao-de-Clientes.git](https://github.com/carvalholevis/CRM-Gestao-de-Clientes.git)
cd CRM-Gestao-de-Clientes
```

### 3. Criar e ativar o Ambiente Virtual (Virtualenv)
É recomendável criar um ambiente isolado para as dependências do projeto.

**No Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**No macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar as Dependências
Com o ambiente virtual ativado, instale o Django e as bibliotecas necessárias.

*Caso o arquivo `requirements.txt` não esteja disponível, instale manualmente:*
```bash
pip install django django-crispy-forms crispy-bootstrap5
```

*Se o arquivo `requirements.txt` já existir no projeto, use apenas:*
```bash
pip install -r requirements.txt
```

### 5. Configurar o Banco de Dados
Crie as tabelas necessárias no banco de dados SQLite local:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Criar um Superusuário (Admin)
Para acessar o painel administrativo do Django, crie um usuário com acesso total:

```bash
python manage.py createsuperuser
```
*Siga as instruções no terminal para definir nome de usuário, e-mail e senha.*

### 7. Iniciar o Servidor
Por fim, inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

### 8. Acessar a Aplicação
O projeto estará acessível em:
* **Aplicação Principal:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Painel Admin:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 👨‍💻 Autor

**Léviton Lima Carvalho**
* Estudante de Engenharia de Software - Descomplica Faculdade Digital
* [Perfil no GitHub](https://github.com/carvalholevis)

---

### 📝 Dica para manutenção
Para gerar ou atualizar o arquivo de dependências deste projeto após instalar novas bibliotecas, execute:
```bash
pip freeze > requirements.txt
