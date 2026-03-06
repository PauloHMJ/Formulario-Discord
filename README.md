<h1 align="center">🤖 Formulário com Integração Discord</h1>

<p align="center">
Sistema web para envio de formulários de candidatura para staff de servidor Discord, com armazenamento em banco de dados e painel de visualização das respostas.
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask"/>
<img src="https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql"/>
<img src="https://img.shields.io/badge/HTML-5-orange?style=for-the-badge&logo=html5"/>
<img src="https://img.shields.io/badge/CSS-3-blue?style=for-the-badge&logo=css3"/>
<img src="https://img.shields.io/badge/JavaScript-ES6-yellow?style=for-the-badge&logo=javascript"/>
<img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-green?style=for-the-badge"/>
</p>

---

# 📖 Sobre o Projeto

Este projeto consiste em um **sistema de formulário web para candidatura de staff em servidores Discord**.

Os dados enviados pelos usuários são processados por um servidor **Flask (Python)** e armazenados em um **banco de dados MySQL**, permitindo que administradores visualizem todas as candidaturas enviadas.

O sistema foi desenvolvido com foco em **organização de processos de recrutamento dentro de comunidades Discord**.

---

# 🚀 Funcionalidades

✔ Formulário web para envio de candidatura  
✔ Validação de nick do Discord duplicado  
✔ Armazenamento das respostas em banco de dados MySQL  
✔ Registro automático da data e horário da candidatura  
✔ Página administrativa para visualização das respostas enviadas  
✔ API interna para listagem das candidaturas

---

# 🛠 Tecnologias Utilizadas

- Python
- Flask
- MySQL
- HTML5
- CSS3
- JavaScript
- Git
- GitHub

---

# 📂 Estrutura do Projeto

```
Formulario-Discord
│
├── static/
│
├── templates/
│   ├── index.html
│   └── dados.html
│
├── app.py
├── requirements.txt
└── render.yaml
```

### 📌 Descrição dos Arquivos

**app.py**  
Servidor Flask responsável por processar os dados enviados pelo formulário e armazená-los no banco de dados.

**templates/index.html**  
Página contendo o formulário de candidatura.

**templates/dados.html**  
Página para visualização das respostas enviadas.

**static/**  
Arquivos de estilo e recursos visuais do site.

---

# ▶ Como Executar o Projeto

### 1️⃣ Clone o repositório

```
git clone https://github.com/PauloHMJ/Formulario-Discord
```

### 2️⃣ Entre na pasta do projeto

```
cd Formulario-Discord
```

### 3️⃣ Instale as dependências

```
pip install -r requirements.txt
```

### 4️⃣ Execute o servidor

```
python app.py
```

### 5️⃣ Acesse no navegador

```
http://localhost:5000
```

---

# 🎯 Objetivo do Projeto

O objetivo deste projeto é criar um **sistema simples e funcional de recrutamento de staff para servidores Discord**, centralizando as candidaturas e facilitando a análise dos candidatos pelos administradores.

---

# 🔮 Melhorias Futuras

Algumas melhorias planejadas para evoluir o sistema:

### 🤖 Integração com Bot do Discord

Criação de um **bot do Discord** para coletar automaticamente informações sobre o candidato no servidor, como:

- 📅 Data de entrada no servidor
- 📊 Quantidade de denúncias realizadas
- ⚠ Quantidade de denúncias recebidas
- 🎧 Tempo total em chamadas de voz
- 📈 Estatísticas de atividade no servidor

Esses dados poderão ser usados para **avaliar automaticamente o perfil do candidato antes da aprovação**.

---

### 🔐 Sistema Administrativo

- Painel de administração com login
- Aprovação ou rejeição de candidatos
- Histórico de candidaturas
- Filtros e busca de candidatos

---

### 🌐 Melhorias na Interface

- Layout responsivo
- Melhor experiência visual
- Dashboard com estatísticas

---

# 👨‍💻 Autor

**Paulo Henrique Manoel Junior**

GitHub  
https://github.com/PauloHMJ
