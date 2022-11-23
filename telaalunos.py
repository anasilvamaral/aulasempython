import glob
import os
from tkinter import filedialog, font
import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import askyesno
from tkinter.tix import *

# Variáveis globais
global hostX, userX, passwordX, databaseX, cursorX
global comando_sql_criar_database, comando_sql_criar_table,  comando_sql_inserir, comando_sql_select, comando_sql_seguranca, comando_sql_deletar
global caixa_combo_diasX, caixa_combo_mesesX, caixa_combo_anosX

global fonte_tela, fonte_label
global path_foto, img_bt_inserir, img_bt_excluir
 
# Dados para conexão com o banco de dados
hostX = 'localhost'
userX = 'root'
passwordX = 'acesso123'
databaseX = 'academico'

fonte_tela = 'cambria'
fonte_label = 'cambria'

# Instruções SQL (não mexer)
comando_sql_criar_database = "CREATE DATABASE IF NOT EXISTS academico"

# Alterar conforme dados do banco de dados
comando_sql_criar_table = "CREATE TABLE IF NOT EXISTS `alunos` (`id_aluno` INT NOT NULL AUTO_INCREMENT,`cpf_aluno` VARCHAR(11) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NOT NULL,`nome_aluno` VARCHAR(50) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NOT NULL,`cep_aluno` VARCHAR(10) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NOT NULL DEFAULT CURRENT_TIMESTAMP,`endereco_aluno` VARCHAR(30) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NOT NULL,`complemento_aluno` VARCHAR(30) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL,`bairro_aluno` VARCHAR(30) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NOT NULL,`cidade_aluno` INT NOT NULL,`email_aluno` VARCHAR(40) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL,`telefone_aluno` VARCHAR(14) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NOT NULL,`data_nascimento` DATE NOT NULL,`foto_aluno` VARCHAR(200) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NOT NULL,`sexo_aluno` CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NOT NULL,`sexo_aluno_outro` VARCHAR(20) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL,PRIMARY KEY (`id_aluno`), INDEX `fk_cidade_idx` (`cidade_aluno` ASC) VISIBLE, INDEX `fk_telefone_idx` (`telefone_aluno` ASC) VISIBLE, CONSTRAINT `fk_cidade` FOREIGN KEY (`cidade_aluno`) REFERENCES `acadêmico`.`cidade` (`id_cidade`) ON DELETE NO ACTION ON UPDATE NO ACTION, CONSTRAINT `fk_telefone` FOREIGN KEY (`telefone_aluno`) REFERENCES `acadêmico`.`telefone` (`id_telefone`) ON DELETE NO ACTION ON UPDATE NO ACTION)"


# Alterar conforme dados do banco de dados
comando_sql_inserir = "INSERT INTO alunos (cpf_aluno, nome_aluno, cep_aluno, endereco_aluno, complemento_aluno, bairro_aluno, cidade_aluno, email_aluno, telefone_aluno, data_nascimento, foto_aluno, sexo_aluno, sexo_aluno_outro   ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
comando_sql_select = "SELECT * FROM alunos;"
comando_sql_seguranca = "SET SQL_SAFE_UPDATES = 0;"
comando_sql_deletar = "DELETE FROM alunos WHERE id_user = %s;"

caixa_combo_diasX = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
caixa_combo_mesesX = ['01','02','03','04','05','06','07','08','09','10','11','12']
caixa_combo_anosX = ["1900","1901","1902","1903","1904","1905","1906","1907","1908","1909","1910","1911","1912","1913","1914","1915","1916","1917","1918","1919","1920","1921","1922","1923","1924","1925","1926","1927","1928","1929","1930","1931","1932","1933","1934","1935","1936","1937","1938","1939","1940","1941","1942","1943","1944","1945","1946","1947","1948","1949","1950","1951","1952","1953","1954","1955","1956","1957","1958","1959","1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006"]

# Lista de mensagens
mensagem_bd = ['Erro de Conexão ao banco de dados.',
               'Erro ao criar banco de dados.',
               'Erro ao criar tabela no banco de dados.',
               'Registro cadastrado com sucesso',
               'Erro ao cadastrar o registro',
               'Erro ao deletar o cadastro',
               'Deseja deletar o registro selecionado?']

lista_sexo = ['Masculino',
              'Feminino',
              'Outro',
              'Prefiro não informar']

#Função mostrar foto
def mostrarfoto():
    global foto, foto_label, foto_sel
    foto_sel = filedialog.askopenfilename(initialdir= "./", title=
     "Abrir Arquivo", filetypes= (("PNG", ".png"),("JPG", ".jpg")))
    print(foto_sel,type(foto_sel))
    entry_fotoaluno.insert(0, foto_sel)

# Função para conectar o banco de dados.
def conectar():
    global banco
    try:
        banco = mysql.connector.connect(
            host = hostX, 
            user = userX,
            password = passwordX)
        #print('Conexão 0: ', banco)
    except Error as erro:
        print(mensagem_bd[0])
            
# Função para criar o banco de dados
def criar_database():
    global banco
    try:
        conectar()
        cursorX = banco.cursor()
        cursorX.execute(comando_sql_criar_database)        
    except Error as erro:
        print(mensagem_bd[1])
        
    if banco.is_connected():
        cursorX.close()

# Função para criar tabela
def criar_tabela():
    global banco
    try:
        banco = mysql.connector.connect(
            host = hostX,
            user = userX,
            password = passwordX,
            database = databaseX
        )

        cursorX = banco.cursor()
        cursorX.execute(comando_sql_criar_table)
        print(banco)
    except Error as erro:
        print(mensagem_bd[2])
        
    if banco.is_connected():
            banco.close()
    
# Inserir novo registro
def inserir_novo_registro():
    global banco
    entry_01['state'] = 'normal'
    entry_01.delete(0,'end')
    entry_01['state'] = 'disabled'
    
    banco = mysql.connector.connect(
        host=hostX,
        user=userX,
        password=passwordX,
        database=databaseX
    )
    
    cursorX = banco.cursor()
    cursorX.execute(comando_sql_criar_table)
    try:
        if banco.is_connected():
            agrupa_data = str(caixa_combo_anos.get() + '-' + caixa_combo_meses.get() + '-'+ caixa_combo_dias.get())
            # Alterar os nomes das caixas
            dados = (str(entry_cpf.get()), str(entry_nomedoaluno.get()), str(entry_cep.get()), str(entry_endereco.get()), str(entry_comple.get()), str(entry_bairro.get()))
            (str(entry_cidade.get()), str(entry_email.get()), str(entry_telefone.get()),str(agrupa_data.get()),  str(entry_fotoaluno.get()), str(caixa_combo_sexo.get()), str(entry_outro.get()))
            cursorX.execute(comando_sql_inserir, dados)
            banco.commit()
            messagebox.showinfo('AVISO', mensagem_bd[3])
    except:
        messagebox.showerror('ERRO', mensagem_bd[4])
    
    # Para apagar o conteúdo das caixa
    
# Exibe os registros do banco de dados
def mostrar_todos_registros():
    banco = mysql.connector.connect(
        host=hostX,
        user=userX,
        password=passwordX,
        database=databaseX
    )
 
    if banco.is_connected():
        grid_reg.delete(*grid_reg.get_children(None))
        cursorX = banco.cursor()
        cursorX.execute(comando_sql_select)
        dados_tabela = cursorX.fetchall()
        #print(dados_tabela)
        for i in range(0, len(dados_tabela)):
            grid_reg.insert(parent='', index=i, values=dados_tabela[i])

# Deletar o registro selecionado no Grid            
def deletar_registro():
    deletar_reg = messagebox.askyesno('ATENÇÃO', mensagem_bd[6])

    curItem = grid_reg.focus()
    valor = grid_reg.item(curItem)
    lista_valores = valor['values']
    
    try:
        if deletar_reg:
            banco = mysql.connector.connect(
                host=hostX,
                user=userX,
                password=passwordX,
                database=databaseX
            )
            if banco.is_connected():
                grid_reg.delete(curItem)
                cursorX = banco.cursor()
                dados = [(lista_valores[0])]
                cursorX.execute(comando_sql_seguranca)
                cursorX.execute(comando_sql_deletar, dados)
                banco.commit()
    except:
        messagebox.showerror('ERRO', mensagem_bd[5])
        
# Mostrar o registro selecionado no Grid           
def mostrar_registro_selecionado(event):
    curItem = grid_reg.focus()
    valor = grid_reg.item(curItem)
    lista_valores = valor['values']
    print('Lista: ', lista_valores)
    
# Desconecta banco
def desconecta_banco():
    if banco.is_connected():
        banco.close()
 

# Mostrar a foto do usuário - Não está funcionando
'''
def mostra_foto(path_foto):
    #  Imagem
    print(path_foto)
    foto=PhotoImage(file=path_foto)
    Label(frame2,image=foto,bg='grey',).pack()
    
def carrega_foto(event):
    path_foto = entry_foto.get()
    foto=PhotoImage(file=path_foto)
    Label(janela,image=foto,).place(x=0,y=0)
'''
      
# Janela principal
janela = Tk()
janela.title('Sistema acadêmico')
janela.geometry('1000x750') #Define o tamanho da tela

janela.configure(bg='#FFB6C1')
janela.resizable(width=FALSE, height=FALSE)

frame1 = Frame(janela, bg='#FFB6C1', width=1000, height=750)
frame1.place(x=0, y=0)
frame2= Frame(janela, bg='#FFB6C1', width=50, height=50)
frame2.place(x=910, y=30)
frame3 = Frame(janela, bg='#FFB6C1', width=295, height=220)
frame3.place(x=700,y=190)
frame4 = Frame(janela, bg= '#FFB6C1', width=150, height=100)
frame4.place(x=800,y=500)

#frame4 = Frame(janela, bg='white', width=1000, height=60)
#frame4.place(x=0,y=325)

#Sexo Radiobuton
varSexo = IntVar()
r1 = Radiobutton(frame4, text= 'Masculino', variable=varSexo,
value=1, bg='#FFB6C1', font=(fonte_label,'10'))
r1.place(x=10, y=5)
r1 = Radiobutton(frame4, text= 'Feminino', variable=varSexo,
value=2, bg='#FFB6C1', font=(fonte_label,'10'))
r1.place(x=10, y=25)
r1 = Radiobutton(frame4, text= 'Outro', variable=varSexo,
value=3, bg='#FFB6C1', font=(fonte_label,'10'))
r1.place(x=10, y=45)
r1 = Radiobutton(frame4, text= 'Prefiro não informar', variable=varSexo,
value=1, bg='#FFB6C1', font=(fonte_label,'10'))
r1.place(x=10, y=65)


# JANELA 
# ToolBar
toolbar = Frame(janela)
toolbar.pack(side=TOP, fill=X)
b1 = Button(
    toolbar,
    background='#F08080',
    relief=FLAT,
    compound = LEFT,
    text="Mostrar  registros                                                                                                                                                                                                                                                                                                           ",
    command=mostrar_todos_registros,
    #image=imgs["notepad"]
    )

b1.pack(side=LEFT, padx=0, pady=0)

# Menubar
menubar = tk.Menu(janela)
filemenu = tk.Menu(menubar)
filemenu.add_command(label="Mostrar reistros", command=mostrar_todos_registros)
filemenu.add_command(label="Sair", command=janela.quit)
menubar.add_cascade(label="Arquivos", menu=filemenu)
janela.config(menu=menubar)

# StatusBar
barrastatus = tk.Label(janela, text="alunos", bd=1, relief=tk.SUNKEN, anchor=tk.W, fg='#FFB6C1')
barrastatus.pack(side=tk.BOTTOM, fill=tk.X)

# Começa a tela - deve ser alterada conforme modelo do banco de dados
label_cadastro = Label(janela, text='alunos', fg='#DC143C', bg='#FFB6C1', font=(fonte_tela,'30'), justify='center')
label_cadastro.pack(side=TOP)

# FRAME 1
label_01 = Label(frame1, text='id aluno', fg='#DC143C', bg='#FFB6C1', font=(fonte_label,'12'))
label_01.place(x=110,y=80)
entry_01 = Entry(frame1, font=(fonte_label,'12'), relief='solid')
entry_01.place(x=175, y=80, height=28)
entry_01['state'] = 'disable'

label_cpf = Label(frame1, text='cpf', fg='#DC143C', bg='#FFB6C1', font=(fonte_label,'12'))
label_cpf.place(x=140,y=120)
entry_cpf = Entry(frame1, font=(fonte_label,'12'), relief='solid')
entry_cpf.place(x=175, y=120, height=28)

label_nomedoaluno = Label(frame1, text='nome do aluno', fg='#DC143C', bg='#FFB6C1', font=(fonte_tela,'12'))
label_nomedoaluno.place(x=60, y=160)
entry_nomedoaluno = Entry(frame1, font=(fonte_label,'12'), relief='solid')
entry_nomedoaluno.place(x=175,y=160,height=20, width=500)

label_cep = Label(frame1, text='cep', fg='#DC143C', bg='#FFB6C1', font=(fonte_label,'12'))
label_cep.place(x=135,y=200)
entry_cep = Entry(frame1, font=(fonte_label,'12'), relief='solid')
entry_cep.place(x=175,y=200,height=20, width=500)

label_endereco = Label(frame1, text='endereço', fg='#DC143C', bg='#FFB6C1', font=(fonte_label,'12'))
label_endereco.place(x=100,y=240)
entry_endereco = Entry(frame1, font=(fonte_label,'12'), relief='solid')
entry_endereco.place(x=175,y=240,height=20, width=500)

label_comple = Label(frame1, text='complemento', fg='#DC143C', bg='#FFB6C1', font=(fonte_label,'12'))
label_comple.place(x=70,y=280)
entry_comple = Entry(frame1, font=(fonte_label,'12'), relief='solid')
entry_comple.place(x=175,y=280,height=20, width=500)

label_bairro = Label(frame1, text='bairro', fg='#DC143C', bg='#FFB6C1', font=(fonte_label,'12'))
label_bairro.place(x=125,y=320)
entry_bairro = Entry(frame1, font=(fonte_label,'12'), relief='solid')
entry_bairro.place(x=175,y=320,height=20, width=500)

label_cidade = Label(frame1, text='cidade', fg='#DC143C', bg='#FFB6C1', font=(fonte_label,'12'))
label_cidade.place(x=120,y=360)
entry_cidade = Entry(frame1, font=(fonte_label,'12'), relief='solid')
entry_cidade.place(x=175,y=360,height=20, width=500)

label_email = Label(frame1, text='e-mail', fg='#DC143C', bg='#FFB6C1', font=(fonte_label,'12'))
label_email.place(x=120,y=400)
entry_email = Entry(frame1, font=(fonte_label,'12'), relief='solid')
entry_email.place(x=175,y=400,height=20, width=500)

label_telefone = Label(frame1, text='telefone', fg='#DC143C', bg='#FFB6C1', font=(fonte_label,'12'))
label_telefone.place(x=110,y=480)
entry_telefone = Entry(frame1, font=(fonte_label,'12'), relief='solid')
entry_telefone.place(x=175,y=480,height=20, width=500)

label_fotoaluno = Label(frame1, text='foto do aluno', fg='#DC143C', bg='#FFB6C1', font=(fonte_label,'12'))
label_fotoaluno.place(x=75,y=520)
entry_fotoaluno = Entry(frame1, font=(fonte_label,'12'), relief='solid')
entry_fotoaluno.place(x=175,y=520,height=20, width=500)

escolher_sexo = StringVar()
label_sexo = Label(frame1, text='sexo aluno', fg='#DC143C', bg='#FFB6C1', 
font=(fonte_label,'12'))
label_sexo.place(x=90,y=560)
caixa_combo_sexo = ttk.Combobox(frame1, textvariable=escolher_sexo)
caixa_combo_sexo['values']= lista_sexo
caixa_combo_sexo.place(x=175, y=560, width=150,height=20)

label_outro = Label(frame1, text='sexo outro', fg='#DC143C', bg='#FFB6C1', font=(fonte_label,'12'))
label_outro.place(x=90,y=600)
entry_outro = Entry(frame1, font=(fonte_label,'12'), relief='solid') 
entry_outro.place(x=175,y=600,height=20, width=500)




#entry_foto.bind("<FocusOut>",carrega_foto)

imagem = tk.PhotoImage(file="gost.png")
w = tk.Label(frame2, image=imagem)
w.imagem = imagem
w.pack()

#foto=PhotoImage('img.png')
#Label(frame2, image=foto)

label_data = Label(frame1, text='data de nascimento', fg='#DC143C', bg='#FFB6C1', font=(fonte_label,'12'))
label_data.place(x=30,y=440)

escolher_dia = StringVar()
caixa_combo_dias = ttk.Combobox(frame1, textvariable=escolher_dia)
caixa_combo_dias['values']=caixa_combo_diasX
caixa_combo_dias.place(x=175, y=440, width=45, height=20)

escolher_meses = StringVar()
caixa_combo_meses = ttk.Combobox(frame1, textvariable=escolher_meses)
caixa_combo_meses['values']=caixa_combo_mesesX
caixa_combo_meses.place(x=222, y=440, width=45, height=20)

escolher_anos = StringVar()
caixa_combo_anos = ttk.Combobox(frame1, textvariable=escolher_anos)
caixa_combo_anos['values']=caixa_combo_anosX
caixa_combo_anos.place(x=269, y=440, width=55, height=20)



# Grid de registros do banco
colunas_grid = ('Cod','Usuário')
grid_reg = ttk.Treeview(frame3, columns=colunas_grid, show='headings')

grid_reg.column("Cod", width=55, anchor=CENTER, minwidth=55, stretch=NO)
grid_reg.column("Usuário", width=230, anchor=CENTER, minwidth=150, stretch=NO)

grid_reg.heading('Cod', text='Cod')
grid_reg.heading('Usuário', text='Usuario')
grid_reg.place(x=0, y=0, width=295, height=220)

grid_reg.bind("<Button>", mostrar_registro_selecionado)

#scrollbar_x = ttk.Scrollbar(frame3, orient='horizontal', command=grid_reg.xview)
#grid_reg.configure(xscrollcommand=scrollbar_x.set)
#scrollbar_x.place(x=0,y=200,width=300)

scrollbar_y = ttk.Scrollbar(frame3,orient='vertical', command=grid_reg.yview)
grid_reg.configure(yscrollcommand=scrollbar_y.set)
scrollbar_y.place(x=396,y=71,height=240)

# Botões
img_bt_inserir=PhotoImage(file = r"Salvar.png") 
img_bt_excluir=PhotoImage(file = r"Excluir.png")

tip = Balloon(janela)

botao_inserir = Button(frame1,text='', image=img_bt_inserir, compound = LEFT,relief='groove', command=inserir_novo_registro, font=(fonte_label,'14'), fg='#FFB6C1', activeforeground='orange')
botao_inserir.place(x=10,y=680,width=80,height=30)
tip.bind_widget(botao_inserir, balloonmsg="Salvar o registro na base de dados")

botao_excluir = Button(frame1,text='', image=img_bt_excluir, compound = LEFT, command=deletar_registro,font=(fonte_label,'14'), relief='groove', fg='#FFB6C1', activeforeground='orange')
botao_excluir.place(x=100,y=680,width=80,height=30)
tip.bind_widget(botao_excluir, balloonmsg="Excluir o registro selecionado da base de dados")

botao_sel_foto = Button(frame1,text='Busca',command=mostrarfoto,
font= (fonte_label,'7'), relief='raised', fg='black',
activeforeground='orange')
botao_sel_foto.place(x=680,y=520,height=20,width=30)

#botao_mostrar_grid = Button(frame1, text='Registros',command=mostrar_todos_registros,font=(fonte_label,#'14'),relief='groove',fg='black', activeforeground='orange')
#botao_mostrar_grid.place(x=700,y=345,width=100,height=30)


# Incio do programa. As funções serão chamadas e executadas
#conectar()
#criar_database()
#criar_tabela()
 
janela.mainloop()