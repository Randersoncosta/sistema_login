import customtkinter as ctk
from tkinter import *
import database
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as msgbox
import sqlite3

janela = ctk.CTk()

class application():
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def showMessage(message, timeout=1000):
        root = tk.Tk()
        root.withdraw()
        root.after(timeout, root.destroy)
        msgbox.showinfo('Info', message, master=root)

    def tela(self):
        janela.geometry("700x400")
        janela.title("Sistema de login")
        janela.resizable(False,False)
        janela.iconbitmap("icon.ico")

    def tela_login(self):
        img = PhotoImage(file="img.png")
        Label_img = ctk.CTkLabel(master=janela, image=img ,text="")
        Label_img.place(x=5 , y=65)

        label_text = ctk.CTkLabel(master=janela , text="Entre com Sua conta e tenha \na Platafoma", 
        font=("Roboto",18),text_color="#00B0F0").place(x=65,y=10)

        login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=RIGHT)

        label = ctk.CTkLabel(master=login_frame, text="Sistema de Login" , font=("Roboto", 20))
        label.place(x=100 , y = 5)

        Username_Entry= ctk.CTkEntry(master=login_frame , placeholder_text="Nome do Usuario", width=300, font=("roboto", 14))
        Username_Entry.place(x=25 , y=105)
       

        password_Entry= ctk.CTkEntry(master=login_frame , placeholder_text="Senha do Usuario", width=300, font=("roboto", 14),show="*")
        password_Entry.place(x=25 , y=175)
        

        checkbox = ctk.CTkCheckBox(master=login_frame, text="Lembra-se de mim Sempre!!!").place(x=25 , y=235)
        
        def limpar_labels():
                for widget in login_frame.winfo_children():
                     if isinstance(widget, ctk.CTkLabel):
                        if widget.cget("text") != "Faça o seu Cadastro" and widget.cget("text") != "Prencha todos os Campos Corretamente.":
                           widget.destroy()
        def resultados():
            
            resultados_frame = ctk.CTkFrame(master=janela, width=350, height=396)
            resultados_frame.pack(side=RIGHT)

            titulo_label = ctk.CTkLabel(master=resultados_frame, text="Resultados dos Cadastros", font=("Roboto", 22))
            titulo_label.place(x=25, y=6)

            tree = ttk.Treeview(master=resultados_frame, columns=("ID", "Nome", "Email","password"), show="headings")  # Adicione outras colunas conforme necessário
            tree.heading("#1", text="ID")
            tree.heading("#2", text="Nome")
            tree.heading("#3", text="Email")
            tree.heading("#4", text="Password")
            tree.place(x=25, y=60, width=300, height=260)

            database.conn = sqlite3.connect("Sistema.db")
            database.conn
            database.cursor.execute(""" SELECT * FROM users """)
            database.conn.commit()
            dados = database.cursor.fetchall() 
            database.conn.close()
            
            for row in dados:
                tree.insert("", "end", values=row)

            tree.update()
            
            def back():
                resultados_frame.pack_forget()
                login_frame.pack(side=RIGHT)

            back_button = ctk.CTkButton(master=resultados_frame, text="Logout", width=150, fg_color="gray", 
            hover_color="#014B05",command=back).place(x=177 , y=330)
                
            

        def login():
            limpar_labels()

            msg = []
            
            if Username_Entry.get() == "":
                Username_label= ctk.CTkLabel(master=login_frame, text="* O Campo nome de usuario e de carater é Obrigatorio!!!", text_color="green", 
                font=("roboto", 8)).place(x=25 , y= 135)
                msg.append(Username_label)
            if password_Entry.get() == "":
                password_label= ctk.CTkLabel(master=login_frame, text="*Campo senha do Usuario e de carater é Obrigatorio!!!", text_color="green", 
                font=("roboto", 8)).place(x=25 , y=205)
                msg.append(password_label)


            if len(msg) == 0:
                    database.conn = sqlite3.connect("Sistema.db")
                    database.cursor.execute(""" select * from users where username = ? and password = ?  """,
                    (Username_Entry.get(),password_Entry.get()))
                    database.conn.commit()
                    database.conn.close()                    
                    login_frame.pack_forget()
                    resultados()
                    
            return msg

        botão = ctk.CTkButton(master=login_frame, text="LOGIN" , width=300, command=login).place(x=25 , y=285)
        
        def tela_cadastro():            
            login_frame.pack_forget()
                     

            #Tela de frame
            cadastro_frame = ctk.CTkFrame(master=janela, width=350, height=396)
            cadastro_frame.pack(side=RIGHT)

            label = ctk.CTkLabel(master=cadastro_frame, text="Faça o seu Cadastro" , font=("Roboto", 22)).place(x=25 , y = 6)

            label = ctk.CTkLabel(master=cadastro_frame, text="Prencha todos os Campos Corretamente." , font=("Roboto", 11)).place(x=25 , y = 30)
            
            name_user= ctk.CTkEntry(master=cadastro_frame , placeholder_text="Nome do Usuario", width=300, font=("roboto", 14))
            name_user.place(x=25 , y=60)
                        
            email_usuario= ctk.CTkEntry(master=cadastro_frame , placeholder_text="E-mail de Usuario", width=300, font=("roboto", 14))
            email_usuario.place(x=25 , y=120)

            password_user= ctk.CTkEntry(master=cadastro_frame , placeholder_text="Senha do Usuario", width=300, font=("roboto", 14),show="*")
            password_user.place(x=25 , y=180)
                                 
            conf_password= ctk.CTkEntry(master=cadastro_frame , placeholder_text="Confirma Senha", width=300, font=("roboto", 14),show="*")
            conf_password.place(x=25 , y=240)

            checkbox = ctk.CTkCheckBox(master=cadastro_frame, text="Aceito os Termos e Politicas").place(x=25 , y=310)

            def back():
                cadastro_frame.pack_forget()
                login_frame.pack(side=RIGHT)

            back_button = ctk.CTkButton(master=cadastro_frame, text="Voltar", width=150, fg_color="gray", 
            hover_color="#014B05",command=back).place(x=23 , y=350)

            def limpar_labels():
                for widget in cadastro_frame.winfo_children():
                     if isinstance(widget, ctk.CTkLabel):
                        if widget.cget("text") != "Faça o seu Cadastro" and widget.cget("text") != "Prencha todos os Campos Corretamente.":
                           widget.destroy()

            def salvar(): 
            
                limpar_labels()
                msg_erro = []

                if name_user.get() == "" :
                    msg_label= ctk.CTkLabel(master=cadastro_frame, text="* O Campo é Obrigatorio!!!", text_color="green", 
                    font=("roboto", 8)).place(x=25 , y = 90)
                    msg_erro.append(msg_label)
                
                    
                if email_usuario.get() == "" :
                    msg_label= ctk.CTkLabel(master=cadastro_frame, text="* O Campo é Obrigatorio!!!", text_color="green", 
                    font=("roboto", 8)).place(x=25 , y = 150)
                    msg_erro.append(msg_label)

                if password_user.get() == "" :
                    msg_label= ctk.CTkLabel(master=cadastro_frame, text="* O Campo é Obrigatorio!!!", text_color="green", 
                    font=("roboto", 8)).place(x=25 , y = 210)
                    msg_erro.append(msg_label)
                
                if conf_password.get() == "":
                   msg_label= ctk.CTkLabel(master=cadastro_frame, text="* O Campo é Obrigatorio!!!", text_color="green", 
                   font=("roboto", 8)).place(x=25 , y = 270)
                   msg_erro.append(msg_label)
                elif conf_password.get() != password_user.get():
                    msg_label= ctk.CTkLabel(master=cadastro_frame, text="* A senha deve ser igual!!!", text_color="green", 
                    font=("roboto", 8)).place(x=25 , y =270)
                    msg_erro.append(msg_label)
                
                
                if len(msg_erro) == 0:
                    database.conn = sqlite3.connect("Sistema.db")
                    database.cursor.execute(""" INSERT INTO users (username,email,password) VALUES 
                    (?,?,?) """,(name_user.get(),email_usuario.get(),password_user.get()))
                    database.conn.commit()
                    
                    
                    def showMessage(message, timeout=2000):
                        root = tk.Tk()
                        root.withdraw()
                        root.after(timeout, root.destroy)
                        msgbox.showinfo('Info', message, master=root)

                    showMessage('Usuario cadastrado com sucesso!!!')
                    database.conn.close()
                    cadastro_frame.pack_forget()
                    self.tela_login()
                
                return msg_erro
            
            cadastrar_button = ctk.CTkButton(master=cadastro_frame, text="Cadastrar", width=150, fg_color="green", 
            hover_color="#014B05",command=salvar).place(x=177 , y=350)
       
    
        register_span = ctk.CTkLabel(master=login_frame, text="Se não tem uma Conta").place(x=25, y=325)
        register_button = ctk.CTkButton(master=login_frame, text="Cadastra-se", width=150, fg_color="green", 
        hover_color="#2D9334",command=tela_cadastro).place(x=175 , y=325)

application()