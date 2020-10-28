import tkinter as tk

root = tk.Tk()
# --------------------------------------
# main window creating
root.title('test')
root.geometry('400x500')
root.resizable(width=False, height=False)
# --------------------------------------
# menu
main_menu = tk.Menu(root)

file_menu = tk.Menu(root)
file_menu.add_command(label='novo')
file_menu.add_command(label='salvar como')
file_menu.add_command(label='sair')

main_menu.add_cascade(label='arquivo', menu=file_menu)
main_menu.add_command(label='editar')
main_menu.add_command(label='sair')
root.config(menu=main_menu)

# --------------------------------------
# conversation window
chatWindow = tk.Text(root, bd=1, bg='black', width='50', height='8', font=('Arial', 23), foreground='#00ffff')
chatWindow.place(x=6, y=6, height=385, width=370)
# --------------------------------------
# msg window
msg_window = tk.Text(root, bd=0, bg='black', width='30', height='4', font=('Arial', 23), foreground='#00ffff')
msg_window.place(x=128, y=400, height=88, width=270)
# --------------------------------------
# scroll bar
scroll = tk.Scrollbar(root, command=chatWindow.yview, cursor='star')
scroll.place(x=375, y=5, height=385)
# --------------------------------------
# buttons
button = tk.Button(root, text='enviar', width='12', height='5', bd=0, bg='#0080ff',
                   activebackground='#00bfff', foreground='#ffffff', font=('Arial', 12))
button.place(x=6, y=400, height=88)
# --------------------------------------
root.mainloop()
