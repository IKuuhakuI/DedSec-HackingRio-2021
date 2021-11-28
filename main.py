from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
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

usuario_logado = ""

# Funções das telas
class TelaRegistro(Screen):
    nome= ObjectProperty(None)
    usuario = ObjectProperty(None)
    email = ObjectProperty(None)
    senha = ObjectProperty(None)
    confirmar = ObjectProperty(None)

    # Obs: faça self.usuario.text para acessar o texto do objeto!
    def registrar(self,db):
        global usuario_logado
        if self.nome.text!="" and self.senha.text!="" and self.usuario.text!="" and self.email.text!="" and self.senha.text == self.confirmar.text:
            print(db)
            retorno = registrarAluno(db,self.usuario.text,self.nome.text,self.email.text,self.senha.text)
            usuario_logado = self.usuario.text
            self.reset()
            if True:
                sm.current = "avatar"
            #exibirPopup("Debug","Passou")
        else:
            exibirPopup("Formulário inválido","Preecnha os campos com informações válidas")
            self.senha.text = ""
            self.confirmar.text = ""
    
    def registrarHandle(self):
        self.registrar(db)

    def voltar(self):
        self.reset()
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
        if validarAluno(db,self.usuario.text,self.senha.text):
            usuario_logado = self.usuario.text
            self.reset()
            if True:
                sm.current = "avatar"
            #else: self.current = "areas"
        else:
            exibirPopup("Login inválido","Usuário ou senha incorretos.")
            self.reset()

    def logarHandle(self):
        self.logar(db)
    
    def registrar(self,db):
        self.reset()
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
        if True:
            #confirmarAvatar(db,username)
            #sm.current = "areas"
            print(usuario_logado)
            exibirPopup("Debug",usuario_logado)

    def confirmarHandler(self):
        self.confirmar(db)

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
        #TelaStatus(name="status"),\
        TelaAvatar(name="avatar")\
        #TelaAreas(name="areas"),\
        #TelaMarketing(name="marketing"),\
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