from logging import root
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import NoTransition, ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
import banco
from banco.banco import conectar
from banco.banco import configurarTabelas
from banco.alunos import registrarAluno
from banco.alunos import validarAluno
from banco.alunos import verificarAvatar
from banco.alunos import confirmarAvatar
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

usuario_logado = ""
ultima_tela = "login"
quantidade_cursos = "7"

class ImageButtonMarketing (ButtonBehavior, Image):
    def on_release(self):
        global ultima_tela
        ultima_tela = "marketing"

        sm.current = "status"

class BtnTerra (ButtonBehavior, Image):
    def on_release(self):
        print ("Terra")

class BtnAjuda (ButtonBehavior, Image):
    def on_release(self):
        print ("Help")

# Funções das telas
class TelaRegistro(Screen):
    nome= ObjectProperty(None)
    usuario = ObjectProperty(None)
    email = ObjectProperty(None)
    senha = ObjectProperty(None)
    confirmar = ObjectProperty(None)

    def registrar(self,db):
        global usuario_logado
        global ultima_tela
        if self.nome.text!="" and self.senha.text!="" and self.usuario.text!="" and self.email.text!="" and self.senha.text == self.confirmar.text:
            print(db)
            retorno = registrarAluno(db,self.usuario.text,self.nome.text,self.email.text,self.senha.text)
            usuario_logado = self.usuario.text
            self.reset()
            ultima_tela = "registro"
            sm.current = "avatar"
        else:
            exibirPopup("Formulário inválido","Preecnha os campos com informações válidas")
            self.senha.text = ""
            self.confirmar.text = ""
    
    def registrarHandle(self):
        self.registrar(db)

    def voltar(self):
        global ultima_tela
        self.reset()
        ultima_tela = "registro"
        sm.current = "login"

    def reset(self):
        self.nome.text = ""
        self.usuario.text = ""
        self.email.text = ""
        self.senha.text = ""
        self.confirmar.text = ""

class TelaLogin(Screen):
    usuario = ObjectProperty(None)
    senha = ObjectProperty(None)

    def logar(self,db):
        global usuario_logado
        global ultima_tela
        if (validarAluno(db,self.usuario.text,self.senha.text)):
            usuario_logado = self.usuario.text
            self.reset()
            if (not(verificarAvatar(db,usuario_logado))):
                ultima_tela = "login"
                sm.current = "avatar"
            else:
                ultima_tela = "login"
                sm.current = "areas"
        else:
            exibirPopup("Login inválido","Usuário ou senha incorretos.")
            self.reset()

    def logarHandle(self):
        self.logar(db)
    
    def registrar(self,db):
        self.reset()
        global ultima_tela
        ultima_tela = "login"
        sm.current = "registro"

    def registrarHandle(self):
        self.registrar(db)

    def reset(self):
        self.usuario.text = ""
        self.senha.text = ""

class TelaAvatar(Screen):

    def desenharCanvas(self):
        with self.canvas:
            Color(1,0,0,.5,mode="rgba")
            x = self.size[0] * 0.5
            y = self.size[1] * 0.8
            size_x = self.size[0] * 0.1
            size_y = self.size[1] * 0.1
            print(x,y,size_x,size_y)
            self.rect = Rectangle(pos=(x,y),size=(size_x,size_y))

    def confirmar(self,db):
        global usuario_logado
        global ultima_tela
        confirmarAvatar(db,usuario_logado)
        if (ultima_tela == "registro" or ultima_tela == "login"):
            sm.current = "areas"
        else:
            sm.current = ultima_tela

    def voltar(self):
        global usuario_logado
        global ultima_tela
        if(ultima_tela == "registro" or ultima_tela == "login"):
            exit()
        else:
            sm.current = ultima_tela

    def confirmarHandler(self):
        self.confirmar(db)

class TelaAreas(Screen):

    def pressionouImagem(self):
        global ultima_tela
        ultima_tela = "areas"
        sm.current = "status"

    def irStatus(self):
        global ultima_tela
        ultima_tela = "areas"
        sm.current = "status"

    def irMarketing(self):
        global ultima_tela
        ultima_tela = "areas"
        sm.current = "marketing"
        # exibirPopup("Debug","Passou")

    def voltar(self):
        exit ()
        #global usuario_logado
        #global ultima_tela
        #if (ultima_tela == "login" or ultima_tela == "registro"):
        #    exit()
        #else:
        #    sm.current = ultima_tela    

class TelaStatus(Screen):

    def quantidadeCursos(self):
        global quantidade_cursos
        return quantidade_cursos
    
    def voltar(self):
        sm.current = ultima_tela

class TelaMarketing(Screen):
    def voltar(self):
        sm.current = "areas"

class TelaAjuda(Screen):
    def voltar (self):
        sm.current = ultima_tela

class WindowManager(ScreenManager):
    pass

# Funções auxiliares
def exibirPopup(titulo, texto):
    pop = Popup(title=titulo,
                content=Label(text=texto),
                size_hint=(None,None), size=(400,400))
    pop.open()

# Configurações
kv = Builder.load_file("my.kv")

sm = WindowManager()
db = conectar()
print(db)

telas = [TelaLogin(name="login"),\
        TelaRegistro(name="registro"),\
        TelaAvatar(name="avatar"),\
        TelaAreas(name="areas"),\
        TelaStatus(name="status"),\
        TelaMarketing(name="marketing"),\
        TelaAjuda(name="ajuda"),\
        #TelaInventario(name="inventario"),\
        ]
for tela in telas:
    sm.add_widget(tela)

sm.current = "login"

# Inicialização do app
class MyMainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MyMainApp().run()