# Srcooky_site
#  SR COOKY — Confeitaria Artesanal

<p align="center">
  <strong>Pequenos doces, grandes momentos.</strong>
</p>

<p align="center">
  Um site de confeitaria desenvolvido com Django, com uma vitrine de doces artesanais e uma identidade visual acolhedora e moderna.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
</p>

---

##  Sobre o projeto

A **SR COOKY** é um projeto de desenvolvimento web que busca transformar a experiência de conhecer e escolher doces artesanais em algo visualmente agradável e intuitivo.

Inspirado em designs modernos de confeitarias, o site combina cores suaves, tipografia marcante, fotografias de doces e uma organização visual pensada para destacar cada produto.

O projeto também é uma oportunidade de aprender, na prática, conceitos importantes de desenvolvimento web com Python e Django.

##  Identidade visual

-  **Paleta acolhedora:** tons de bege, marrom, terracota e lilás.
-  **Vitrine de produtos:** cartões com imagens, nomes, descrições e preços.
-  **Design artesanal:** elementos visuais que remetem ao cuidado e à produção de doces.
-  **Layout responsivo:** adaptações para diferentes tamanhos de tela.

##  Funcionalidades

- [x] Página inicial com banner de apresentação.
- [x] Seção de diferenciais da confeitaria.
- [x] Vitrine dinâmica de produtos.
- [x] Cadastro e gerenciamento de produtos pelo Django Admin.
- [x] Armazenamento de produtos no banco de dados SQLite.
- [x] Exibição de nome, descrição, preço e disponibilidade.
- [x] Uso de templates e herança de HTML com Django.
- [ ] Carrinho de compras funcional.
- [ ] Finalização de pedidos.
- [ ] Upload de imagens diretamente pelo painel administrativo.
- [ ] Autenticação de clientes.

> **Status:** em desenvolvimento. As funcionalidades listadas como pendentes fazem parte dos próximos passos do projeto.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| Python | Linguagem principal do projeto |
| Django | Framework web e lógica da aplicação |
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização e responsividade |
| SQLite | Banco de dados |
| Django Admin | Gerenciamento dos produtos |

## 📂 Estrutura do projeto

```text
SR-COOKY/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── produtos/
│   ├── migrations/
│   ├── templates/
│   │   └── produtos/
│   │       └── inicio.html
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── tests.py
├── static/
│   └── css/
│       └── style.css
├── templates/
│   └── base.html
├── manage.py
└── README.md
```

##  Como executar o projeto

### 1. Pré-requisitos

Antes de começar, instale:

- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads/)

### 2. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd NOME_DA_PASTA
```

Substitua `URL_DO_SEU_REPOSITORIO` pelo endereço real do repositório e `NOME_DA_PASTA` pelo nome da pasta criada.

### 3. Crie e ative um ambiente virtual

Crie o ambiente:

```bash
python -m venv venv
```

No Windows, ative-o com:

```powershell
.\venv\Scripts\Activate.ps1
```

Se estiver usando o Prompt de Comando (CMD), utilize:

```bat
venv\Scripts\activate.bat
```

### 4. Instale o Django

```bash
python -m pip install django
```

> Se o projeto tiver um arquivo `requirements.txt`, prefira instalar as dependências com `python -m pip install -r requirements.txt`.

### 5. Execute as migrações

```bash
python manage.py migrate
```

### 6. Crie um usuário administrador

```bash
python manage.py createsuperuser
```

Siga as instruções do terminal para cadastrar suas credenciais.

### 7. Inicie o servidor

```bash
python manage.py runserver
```

Acesse o site:

- **Página inicial:** http://127.0.0.1:8000/
- **Painel administrativo:** http://127.0.0.1:8000/admin/

No painel administrativo, você poderá cadastrar e gerenciar os doces disponíveis na vitrine.

##  O que estou aprendendo com este projeto?

O desenvolvimento da SR COOKY envolve a aplicação prática de conceitos como:

- Organização de projetos Django.
- Models e estruturação de dados.
- Views e comunicação com templates.
- Herança de templates HTML.
- Consultas ao banco de dados com o ORM do Django.
- Migrações de banco de dados.
- Arquivos estáticos e estilização com CSS.
- Versionamento de código com Git e GitHub.

##  Próximos passos

1. Aprimorar a experiência visual em diferentes dispositivos.
2. Implementar um carrinho de compras funcional.
3. Desenvolver o fluxo de criação e acompanhamento de pedidos.
4. Permitir o envio de imagens pelo painel administrativo.
5. Adicionar testes e preparar o projeto para implantação.

##  Desenvolvimento

Projeto desenvolvido como parte de uma jornada de aprendizado em programação e desenvolvimento web.

Construído com curiosidade, prática e muitos doces. 

---

<p align="center">
  <strong>SR COOKY</strong><br>
  <em>Pequenos doces, grandes momentos.</em>
</p>
