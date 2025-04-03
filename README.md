# Gerador de Projetos HTML com Tkinter

Este projeto é um aplicativo desenvolvido em Python com Tkinter e ttkbootstrap para criar rapidamente a estrutura básica de um projeto HTML, incluindo pastas e arquivos essenciais.

## 📌 Funcionalidades
- Criação automática de um projeto HTML com estrutura organizada
- Opção para incluir suporte a jQuery, Bootstrap ou Bootstrap + jQuery
- Interface gráfica moderna com `ttkbootstrap`
- Escolha do diretório de salvamento
- Abertura automática do projeto no VS Code após a criação

## 🛠 Tecnologias Utilizadas
- **Python 3**
- **Tkinter** (para interface gráfica)
- **ttkbootstrap** (para um design moderno)
- **OS e subprocess** (para manipulação de arquivos e abertura no VS Code)

## 📂 Estrutura do Projeto Criado
Após a execução do programa, será gerado um projeto com a seguinte estrutura:
```
📂 NomeDoProjeto
 ├── 📂 css
 │   └── style.css
 ├── 📂 js
 │   └── script.js
 ├── 📂 img
 ├── 📂 doc
 ├── 📂 pages
 └── index.html
```

O arquivo `index.html` conterá os links CDN das bibliotecas escolhidas pelo usuário:
- **JavaScript puro:** Apenas um arquivo `script.js`
- **jQuery:** Link CDN do jQuery
- **Bootstrap:** Link CDN do Bootstrap
- **Bootstrap + jQuery:** Links CDN do Bootstrap e jQuery

## 🚀 Como Executar
### 1️⃣ Instale as dependências
Antes de rodar o programa, instale a biblioteca `ttkbootstrap` (se ainda não tiver instalada):
```sh
pip install ttkbootstrap
```

### 2️⃣ Execute o programa
Salve o código em um arquivo `.py` e execute:
```sh
python nome_do_arquivo.py
```

## 🎨 Personalização
- O tema pode ser alterado modificando a linha:
  ```python
  app = tb.Window(themename="superhero")
  ```
  Para ver todos os temas disponíveis, consulte a documentação do `ttkbootstrap`.
- O nome do projeto e seu diretório podem ser escolhidos na interface gráfica.

## 🖥️ Compatibilidade
✅ Windows  
✅ Linux  
✅ macOS  

## 📝 Notas
- Certifique-se de que o arquivo `cafe.ico` esteja no mesmo diretório do script para evitar erros ao definir o ícone.
- Se desejar abrir o projeto em outro editor, altere:
  ```python
  subprocess.Popen(["code", caminho_projeto], shell=True)
  ```
  Para, por exemplo, abrir no Sublime Text:
  ```python
  subprocess.Popen(["subl", caminho_projeto], shell=True)
  ```

## 📢 Créditos
Criado por **Prof-Café ☕**

