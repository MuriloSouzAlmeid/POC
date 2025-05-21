from app.crud import NcmEntries, Session, engine, select, HTTPException
import uuid
from app.logging import logging

def create_ncm_entrie(user: str, ipi: str, ncm: str, description: str, created_at):
    ncm_entrie = NcmEntries(
        user=user, 
        ipi=ipi,
        ncm=ncm,
        description=description,
        created_at=created_at
    )

    with Session(engine) as session:
        try:
            session.add(ncm_entrie)
            session.commit()
        except:
            logging.error("Ocorreu um erro ao tentar cadastrar o ncm na tabela ncm_entries")
            raise HTTPException(status_code=500, detail="Erro interno de banco de dados")

    return ncm_entrie

def get_ncms_by_page(offset, limit):
    with Session(engine) as session:
        try:
            query_by_limit = select(NcmEntries).order_by(NcmEntries.created_at.desc()).offset(offset).limit(limit)
            ncms_list =  session.exec(query_by_limit).all()

            return ncms_list
        except:
            logging.error("Ocorreu um erro ao tentar buscar os ncms a partir do offset e limit informados")
            raise HTTPException(status_code=500, detail="Erro interno de banco de dados")
            

def get_ncm_by_id(id_ncm : uuid.UUID):
    with Session(engine) as session:
        try:
            ncm_by_id = session.get(NcmEntries, id_ncm)

            return ncm_by_id
        except:
            logging.error("Ocorreu um erro ao tentar buscar o ncm com o ID informado")
            raise HTTPException(status_code=500, detail="Erro interno de banco de dados")
    
def delete_ncm(id_ncm : uuid.UUID):
    with Session(engine) as session:
        try:
            ncm_buscado = get_ncm_by_id(id_ncm)
            session.delete(ncm_buscado)
            session.commit()
        except:
            logging.error("Ocorreu um erro ao tentar deletar o ncm com o ID informado da tabela ncm_entries")
            raise HTTPException(status_code=500, detail="Erro interno de banco de dados")


    