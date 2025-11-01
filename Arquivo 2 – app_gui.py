# app_gui.py
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from crypto_utils import encode_message, decode_message


def process_mode():
    """Executa a criptografia ou descriptografia conforme o modo selecionado."""
    text = message_text.get()
    key = private_key.get()
    operation = mode.get().lower()

    try:
        if operation == "e":
            result_text.set(encode_message(key, text))
        elif operation == "d":
            result_text.set(decode_message(key, text))
        else:
            messagebox.showerror("Erro", "Modo inválido! Use 'e' para codificar ou 'd' para decodificar.")
    except ValueError as ve:
        messagebox.showwarning("Aviso", str(ve))
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")


def reset_fields():
    """Limpa todos os campos de entrada."""
    message_text.set("")
    private_key.set("")
    mode.set("")
    result_text.set("")


def exit_app():
    """Fecha a aplicação."""
    root.destroy()


# Inicialização da janela principal
root = Tk()
root.geometry("500x300")
root.resizable(0, 0)
root.title("Cryptography World")

# Variáveis
message_text = StringVar()
private_key = StringVar()
mode = StringVar()
result_text = StringVar()

# Cabeçalhos e campos
Label(root, text="ENCODE / DECODE", font="Arial 20 bold").pack()
Label(root, text="By Felipe Teixeira Batista", font="Arial 10").pack(side="bottom")

Label(root, text="Mensagem:", font="Arial 12 bold").place(x=60, y=60)
Entry(root, font="Arial 10", textvariable=message_text, bg="ghost white").place(x=290, y=60)

Label(root, text="Chave:", font="Arial 12 bold").place(x=60, y=90)
Entry(root, font="Arial 10", textvariable=private_key, bg="ghost white").place(x=290, y=90)

Label(root, text="Modo (e - encode / d - decode):", font="Arial 12 bold").place(x=60, y=120)
Entry(root, font="Arial 10", textvariable=mode, bg="ghost white").place(x=290, y=120)

Entry(root, font="Arial 10 bold", textvariable=result_text, bg="ghost white").place(x=290, y=150)
Button(root, text="RESULT", font="Arial 10 bold", bg="lightgray", command=process_mode).place(x=60, y=150)

Button(root, text="RESET", font="Arial 10 bold", bg="green", fg="white", width=8, command=reset_fields).place(x=80, y=190)
Button(root, text="EXIT", font="Arial 10 bold", bg="red", fg="white", width=8, command=exit_app).place(x=180, y=190)

root.mainloop()
