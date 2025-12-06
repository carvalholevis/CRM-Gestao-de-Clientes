# CRM - Gestão de Clientes | CA Design de Interiores 🛋️ PT-PT

Este repositório documenta o **Sistema de Gestão de Clientes (CRM)** desenvolvido como **Projeto de Extensão Universitária**. O software foi criado sob medida para atender uma demanda real de organização e produtividade de uma empresa de Design de Interiores sediada em Portugal.

---

## 🏢 Contexto do Cliente e Justificativa

Este projeto não é apenas um exercício acadêmico, mas uma solução prática desenvolvida para um cliente real.

* **Cliente:** CA Design de Interiores.
* **Localização:** Portugal.
* **Propósito:** O projeto foi solicitado pelo proprietário da empresa para resolver problemas de organização de dados, substituindo anotações manuais por um sistema digital centralizado.

### ⚠️ Nota sobre Identificação Jurídica (CNPJ)
Como a empresa beneficiária está localizada e opera em **Portugal**, ela **não possui CNPJ** (Cadastro Nacional da Pessoa Jurídica), que é um registro exclusivo para empresas brasileiras. A empresa opera sob as normas e registros fiscais portugueses. Portanto, para fins de relatório de extensão, considera-se este um projeto internacional de suporte a uma microempresa ativa.

---

## 📋 Sobre o Projeto

O objetivo principal foi criar uma ferramenta acessível e segura para que o escritório possa cadastrar, consultar e gerenciar o histórico de seus clientes.

**Problema Solucionado:**
Antes do sistema, os dados dos clientes estavam dispersos, dificultando o acesso rápido a contatos e endereços para visitas técnicas.

**Solução Entregue:**
Um sistema web intuitivo onde é possível registrar novos clientes, editar informações desatualizadas e manter uma base de dados unificada, facilitando o dia a dia operacional do designer.

---

## 🛠️ Tecnologias Utilizadas

A escolha tecnológica focou em **segurança**, **rapidez de desenvolvimento** e **preparo para nuvem (deploy)**:

* **Linguagem:** [Python 3.x](https://www.python.org/)
* **Framework:** [Django](https://www.djangoproject.com/) - Arquitetura robusta e segura.
* **Servidor de Aplicação:** Gunicorn - Para execução em ambiente de produção.
* **Frontend:** HTML5, CSS3 e Django Templates.
* **Banco de Dados:** SQLite (Desenvolvimento).
* **Infraestrutura:** Configurado para deploy em plataformas PaaS (como Heroku), incluindo arquivos `Procfile` e `requirements.txt`.

---

## ✨ Funcionalidades (O que foi feito)

O sistema implementa o ciclo completo de gestão de dados (CRUD):

1.  **Cadastro de Clientes:** Formulário para inserção de Nome, Telefone, Email e Endereço.
2.  **Listagem Inteligente:** Visualização rápida de todos os clientes cadastrados.
3.  **Edição de Dados:** Atualização de contatos e endereços.
4.  **Remoção de Registros:** Limpeza de dados de clientes inativos.
5.  **Área Administrativa:** Painel seguro (Django Admin) para gestão total do sistema.

---

## 📂 Metodologia de Desenvolvimento

O projeto seguiu etapas de engenharia de software:

1.  **Levantamento de Requisitos:** Reuniões com o cliente para entender o fluxo de trabalho.
2.  **Reestruturação e Organização:** O projeto foi estruturado seguindo as melhores práticas do Django, mantendo a raiz do repositório limpa e configurada para integração contínua.
3.  **Implementação MVT:** Desenvolvimento focado na separação de responsabilidades (Modelos, Visualizações e Templates).

---

## 🚀 Como Executar o Projeto

Instruções para rodar a aplicação em ambiente local:

1.  **Clonar o repositório:**
    ```bash
    git clone [https://github.com/carvalholevis/CRM-Gestao-de-Clientes.git](https://github.com/carvalholevis/CRM-Gestao-de-Clientes.git)
    ```

2.  **Entrar na pasta do projeto:**
    ```bash
    cd CRM-Gestao-de-Clientes
    ```

3.  **Criar ambiente virtual e instalar dependências:**
    ```bash
    python -m venv venv
    # Ativar venv (Windows: venv\Scripts\activate | Linux/Mac: source venv/bin/activate)
    pip install -r requirements.txt
    ```

4.  **Executar Migrações e Servidor:**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

5.  **Acesse:** Abra o navegador em `http://127.0.0.1:8000/`

---

## 👨‍💻 Autor

**Léviton Lima Carvalho**
* Estudante de Engenharia de Software
* Desenvolvedor Full Stack
* [GitHub](https://github.com/carvalholevis)

---
*Projeto de Extensão Universitária - Apoio à Gestão de Microempresa Internacional.*
