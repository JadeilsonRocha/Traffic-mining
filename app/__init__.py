from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db) #Cuida das migrações (CRUD)

manager = Manager(app) # Cuida dos comando que inicia a aplicação
manager.add_command('db', MigrateCommand)

lm = LoginManager()
lm.init_app(app)

from app.api import Login, Cadastro, Sair, Pagamento, Base, Contato, TelaPrincipal, LouderUser, MapaAcidentes \
    , GraficosAcidentes, MapaSemaforos,MapaEquipamentos, MapaPontoAcidentes, GerenteDeCorrelacoes\
    ,MapaAcidentesFiltro, RelatorioAcidentes

