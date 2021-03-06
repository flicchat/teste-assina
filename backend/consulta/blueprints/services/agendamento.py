from datetime import datetime

from consulta.models import Agendamento
from consulta.ext.database import db


class AgendamentoService:
    @staticmethod
    def agendar_consulta(dados):
        dados['data'] = datetime.strptime(dados['data'], '%Y-%m-%d %H:%M:%S')
        agendamento = Agendamento(**dados)
        db.session.add(agendamento)
        db.session.commit()
        return agendamento.id
    
    @staticmethod
    def buscar_agendamento(id_agendamento):
        agendamento = Agendamento.query.filter(Agendamento.id==id_agendamento).first()
        return agendamento.to_dict()

    @staticmethod
    def listar_agendamentos():
        agendamentos = Agendamento.query.all()
        return {"agendamentos": [agendamento.to_dict() for agendamento in agendamentos]}
        