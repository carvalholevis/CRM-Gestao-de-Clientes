# CRM - Gestão de Clientes | CA Design de Interiores 🛋️

Este repositório contém o **CRM (Customer Relationship Management)** desenvolvido como **Projeto de Extensão Universitária**. O sistema foi projetado para atender às necessidades da empresa **CA Design de Interiores**, facilitando a organização, o cadastro e o acompanhamento de clientes de forma centralizada e eficiente.

---

## 📋 Sobre o Projeto

O objetivo principal deste software é substituir planilhas manuais e anotações dispersas por um sistema web robusto e seguro. O CRM permite que o escritório de design gerencie sua base de clientes, mantendo um histórico organizado de contatos e informações essenciais para o atendimento.

**Destaques:**
* Interface intuitiva e amigável.
* Foco em produtividade para o dia a dia do escritório.
* Arquitetura escalável para futuras implementações (como controle de projetos e orçamentos).

---

## 🛠️ Tecnologias Utilizadas

O projeto foi desenvolvido utilizando uma stack moderna e robusta, priorizando a segurança e a rapidez no desenvolvimento:

* **Linguagem:** [Python 3.x](https://www.python.org/) - Escolhida pela sua legibilidade e poder de processamento.
* **Framework Web:** [Django](https://www.djangoproject.com/) - Utilizado pela sua arquitetura "batteries-included", que já fornece autenticação, ORM e segurança nativa.
* **Frontend:** HTML5, CSS3 e Django Templates - Para a criação de uma interface responsiva e dinâmica.
* **Banco de Dados:** SQLite (Desenvolvimento) - Padrão do Django, leve e eficiente para a escala atual do projeto.
* **Controle de Versão:** Git e GitHub.

---

## ✨ Funcionalidades

* **Gestão de Clientes (CRUD):**
    * **C**reate: Cadastro completo de novos clientes (Nome, Telefone, Email, Endereço, etc.).
    * **R**ead: Listagem e visualização detalhada dos dados de cada cliente.
    * **U**pdate: Edição de informações cadastrais.
    * **D**elete: Remoção segura de registros.
* **Interface Administrativa:** Utilização do Django Admin para gestão avançada de dados.
* **Organização Visual:** Layout limpo focado na usabilidade do usuário final.

---

## 📂 Estrutura e Metodologia (Relatório Acadêmico)

### Arquitetura MVT (Model-View-Template)
O projeto segue o padrão arquitetural do Django, garantindo a separação de responsabilidades:

1.  **Models (Modelos):** Definem a estrutura dos dados (Tabelas de Clientes) e as regras de negócio no banco de dados.
2.  **Views (Visões):** Controlam a lógica da aplicação, processando as requisições do usuário e determinando quais dados devem ser exibidos.
3.  **Templates:** Camada de apresentação (HTML/CSS) que exibe os dados ao usuário final de forma formatada.

### Desenvolvimento
O desenvolvimento foi iterativo:
1.  **Levantamento de Requisitos:** Identificação das necessidades da *CA Design de Interiores*.
2.  **Configuração do Ambiente:** Setup do Python, Virtualenv e Django.
3.  **Modelagem de Dados:** Criação das entidades no banco de dados.
4.  **Implementação do Backend:** Criação das Views e rotas (URLs).
5.  **Desenvolvimento do Frontend:** Estilização das páginas e formulários.
6.  **Testes:** Verificação do fluxo de cadastro e edição.

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar o CRM em sua máquina local:

### Pré-requisitos
* Python instalado.
* Git instalado.

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/carvalholevis/CRM-Gestao-de-Clientes.git](https://github.com/carvalholevis/CRM-Gestao-de-Clientes.git)
    ```

2.  **Acesse a pasta do projeto:**
    ```bash
    cd CRM-Gestao-de-Clientes/crm
    ```
    *(Nota: Certifique-se de estar na pasta onde o arquivo `manage.py` se encontra)*

3.  **Crie e ative um ambiente virtual:**
    * No Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    * No Linux/Mac:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Se o arquivo requirements.txt não existir, instale o Django manualmente: `pip install django`)*

5.  **Realize as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

6.  **Inicie o servidor:**
    ```bash
    python manage.py runserver
    ```

7.  **Acesse:** Abra o navegador em `http://127.0.0.1:8000/`.

---

## 👨‍💻 Autor

**Léviton Lima Carvalho**
* Estudante de Engenharia de Software
* Desenvolvedor Full Stack
* [LinkedIn](https://www.linkedin.com/in/leviton-carvalho/) | [GitHub](https://github.com/carvalholevis)

---
*Projeto desenvolvido como requisito de extensão universitária.*
