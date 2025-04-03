import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
import sys
import ttkbootstrap as tb  # Biblioteca para estilo moderno no Tkinter

def criar_projeto():
    nome_projeto = entry_nome.get().strip()
    pasta_destino = entry_local.get().strip()
    tipo_projeto = var_tipo.get()
    
    if not nome_projeto:
        messagebox.showerror("Erro", "Digite um nome para o projeto!")
        return
    
    if not pasta_destino:
        messagebox.showerror("Erro", "Selecione um local para salvar o projeto!")
        return
    
    caminho_projeto = os.path.join(pasta_destino, nome_projeto)
    try:
        os.makedirs(caminho_projeto, exist_ok=True)
        os.makedirs(os.path.join(caminho_projeto, "css"), exist_ok=True)
        os.makedirs(os.path.join(caminho_projeto, "js"), exist_ok=True)
        os.makedirs(os.path.join(caminho_projeto, "img"), exist_ok=True)
        os.makedirs(os.path.join(caminho_projeto, "doc"), exist_ok=True)
        os.makedirs(os.path.join(caminho_projeto, "pages"), exist_ok=True)
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível criar as pastas: {e}")
        return
    
    script_jquery = '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js" crossorigin="anonymous"></script>'
    script_bootstrap = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>'
    css_bootstrap = '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">'
    
    script_include = ""
    if tipo_projeto == "jquery":
        script_include = script_jquery
    elif tipo_projeto == "bootstrap":
        script_include = css_bootstrap + "\n" + script_bootstrap
    elif tipo_projeto == "bootstrap_jquery":
        script_include = css_bootstrap + "\n" + script_bootstrap + "\n" + script_jquery
    
    index_html = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{nome_projeto}</title>
    <link rel="stylesheet" href="css/style.css">
    {script_include}
</head>
<body>
    <h1>Projeto {nome_projeto}</h1>
    <script src="js/script.js"></script>
</body>
</html>"""
    
    try:
        with open(os.path.join(caminho_projeto, "index.html"), "w", encoding="utf-8") as f:
            f.write(index_html)
        
        with open(os.path.join(caminho_projeto, "css", "style.css"), "w", encoding="utf-8") as f:
            f.write("""* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}""")
        
        with open(os.path.join(caminho_projeto, "js", "script.js"), "w", encoding="utf-8") as f:
            f.write("// Escreva seu script aqui")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao criar os arquivos do projeto: {e}")
        return

    messagebox.showinfo("Sucesso", f"Projeto '{nome_projeto}' criado com sucesso em {caminho_projeto}!")
    
    try:
        subprocess.Popen(["code", caminho_projeto], shell=True)
    except Exception as e:
        messagebox.showwarning("Aviso", f"Projeto criado, mas não foi possível abrir no VS Code: {e}")
    
    app.quit()
    sys.exit()

def escolher_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        entry_local.delete(0, tk.END)
        entry_local.insert(0, pasta)

app = tb.Window(themename="superhero")
app.title("Gerador de Projetos")
app.geometry("500x400")
try:
    app.iconbitmap("professor.ico")
except Exception as e:
    print("Ícone não encontrado:", e)

frame = tb.Frame(app)
frame.pack(expand=True, fill="both", padx=20, pady=20)

frame.columnconfigure(0, weight=0)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=0)

titulo = tb.Label(frame, text="Gerador de Projeto HTML", font=("Arial", 16, "bold"))
titulo.grid(row=0, column=0, columnspan=3, pady=(0, 15))

tb.Label(frame, text="Nome do Projeto:", font=("Arial", 11)).grid(row=1, column=0, sticky='e', padx=10, pady=5)
entry_nome = tb.Entry(frame, width=35)
entry_nome.grid(row=1, column=1, columnspan=2, pady=5, sticky="we")

tb.Label(frame, text="Local de Salvamento:", font=("Arial", 11)).grid(row=2, column=0, sticky='e', padx=10, pady=5)
entry_local = tb.Entry(frame, width=28)
entry_local.grid(row=2, column=1, pady=5, sticky="we")
btn_pasta = tb.Button(frame, text="Selecionar", command=escolher_pasta, bootstyle="primary")
btn_pasta.grid(row=2, column=2, padx=5, pady=5)

tb.Label(frame, text="Tipo de Projeto:", font=("Arial", 11)).grid(row=3, column=0, sticky='e', padx=10, pady=5)
var_tipo = tk.StringVar(value="javascript")
radio_js = tb.Radiobutton(frame, text="JavaScript", variable=var_tipo, value="javascript", bootstyle="info")
radio_jquery = tb.Radiobutton(frame, text="jQuery", variable=var_tipo, value="jquery", bootstyle="info")
radio_bootstrap = tb.Radiobutton(frame, text="Bootstrap", variable=var_tipo, value="bootstrap", bootstyle="info")
radio_bootstrap_jquery = tb.Radiobutton(frame, text="Bootstrap + jQuery", variable=var_tipo, value="bootstrap_jquery", bootstyle="info")
radio_js.grid(row=3, column=1, sticky='w', pady=5)
radio_jquery.grid(row=4, column=1, sticky='w', pady=5)
radio_bootstrap.grid(row=5, column=1, sticky='w', pady=5)
radio_bootstrap_jquery.grid(row=6, column=1, sticky='w', pady=5)

btn_criar = tb.Button(frame, text="Criar Projeto", command=criar_projeto, bootstyle="success", width=20)
btn_criar.grid(row=7, column=0, columnspan=3, pady=15)

label_rodape = tb.Label(app, text="by Prof-Café ☕", font=("Arial", 10, "italic"), foreground="gray")
label_rodape.pack(side="bottom", pady=3)

app.mainloop()
