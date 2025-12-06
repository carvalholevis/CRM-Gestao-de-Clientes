# CRM - Gestão de Clientes | CA Design de Interiores 🛋️ PT-PT

Este repositório documenta o **Sistema de Gestão de Clientes (CRM)** desenvolvido como **Projeto de Extensão Universitária**. O software foi criado sob medida para atender uma demanda real de organização e produtividade de uma empresa de Design de Interiores sediada em Portugal.

---

## 🏢 Contexto do Cliente e Justificativa

Este projeto não é apenas um exercício acadêmico, mas uma solução prática desenvolvida para um cliente real.

* **Cliente:** CA Design de Interiores.
* **Localização:** Portugal.
* **Propósito:** O projeto foi solicitado pelo proprietário da empresa (meu noivo) para resolver problemas de organização de dados, substituindo anotações manuais por um sistema digital centralizado.

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

A escolha tecnológica focou em **segurança**, **rapidez de desenvolvimento** e **escalabilidade**, utilizando padrões de mercado:

* **Linguagem:** [Python 3.x](https://www.python.org/) - Pela robustez e facilidade de manutenção.
* **Framework:** [Django](https://www.djangoproject.com/) - Escolhido pela arquitetura segura e completa ("batteries-included"), ideal para sistemas de gestão.
* **Frontend:** HTML5, CSS3 e Django Templates - Interface limpa e responsiva.
* **Banco de Dados:** SQLite - Eficiente para a demanda atual da empresa.

---

## ✨ Funcionalidades (O que foi feito)

O sistema implementa o ciclo completo de gestão de dados (CRUD):

1.  **Cadastro de Clientes:** Formulário para inserção de Nome, Telefone, Email e Endereço.
2.  **Listagem Inteligente:** Visualização rápida de todos os clientes cadastrados.
3.  **Edição de Dados:** Permite atualizar informações de contato conforme os clientes mudam de endereço ou telefone.
4.  **Remoção de Registros:** Funcionalidade para limpar o banco de dados de clientes inativos.
5.  **Área Administrativa:** Painel seguro (Django Admin) para controle total do sistema pelo proprietário.

---

## 📂 Metodologia de Desenvolvimento

O projeto seguiu etapas de engenharia de software para garantir a qualidade da entrega:

1.  **Levantamento de Requisitos:** Reuniões com o cliente (proprietário da CA Design) para entender as dificuldades na gestão atual.
2.  **Arquitetura MVT (Model-View-Template):**
    * *Model:* Definição da estrutura de dados dos clientes.
    * *View:* Lógica de processamento e regras de negócio.
    * *Template:* Desenvolvimento das telas de interação.
3.  **Implementação e Testes:** Codificação em Python/Django e validação das funcionalidades junto ao usuário final.

---

## 🚀 Como Executar o Projeto

Instruções para rodar a aplicação em ambiente local para fins de avaliação:

1.  **Clonar o repositório:**
    ```bash
    git clone [https://github.com/carvalholevis/CRM-Gestao-de-Clientes.git](https://github.com/carvalholevis/CRM-Gestao-de-Clientes.git)
    ```
2.  **Entrar na pasta do projeto:**
    ```bash
    cd CRM-Gestao-de-Clientes/crm
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
5.  Acesse: `http://127.0.0.1:8000/`

---

## 👨‍💻 Autor

**Léviton Lima Carvalho**
* Estudante de Engenharia de Software
* Desenvolvedor Full Stack
* [GitHub](https://github.com/carvalholevis)

---
*Projeto de Extensão Universitária - Apoio à Gestão de Microempresa Internacional.*
