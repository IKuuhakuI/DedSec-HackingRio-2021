from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import banco
from banco.banco import conectar
from banco.banco import configurarTabelas
from banco.alunos import registrarAluno
from banco.alunos import validarAluno

# Funções das telas
class TelaRegistro(Screen):
    nome= ObjectProperty(None)
    usuario = ObjectProperty(None)
    email = ObjectProperty(None)
    senha = ObjectProperty(None)
    confirmar = ObjectProperty(None)

    # Obs: faça self.usuario.text para acessar o texto do objeto!
    def registrar(self,db):
        if self.nome.text!="" and self.senha.text!="" and self.usuario.text!="" and self.email.text!="":
            if self.senha.text == self.confirmar.text:
                registrarAluno(db,self.usuario.text,self.nome.text,self.email.text,self.senha.text)
                self.reset()
                #sm.current = "status"
                exibirPopup("Debug","Passou")
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
        if validarAluno(db,self.usuario.text,self.senha.text):
            self.reset()
            #self.current("areas")
            exibirPopup("Debug","Passou")
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

#class 

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

telas = [TelaLogin(name="login"),\
        TelaRegistro(name="registro")\
        #TelaStatus(name="status"),\
        #TelaStatus(name="avatar"),\
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