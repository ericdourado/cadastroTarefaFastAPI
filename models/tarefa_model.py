from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from core.configs import settings
import datetime

class TarefaModel(settings.DBBaseModel):
    __tablename__ = 'tarefas' 
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id: int = Column(Integer, ForeignKey('usuarios.id'))
    nome: str = Column(String(255), nullable= True)
    descricao: str = Column(String(255), nullable= True)
    concluido: str = Column(Boolean, nullable=False)
    criado_em: str = Column(DateTime, nullable= True)
    atualizado_em: str = Column(DateTime, nullable= True)
