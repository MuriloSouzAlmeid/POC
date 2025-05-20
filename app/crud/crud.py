from app.crud import NcmEntries, Session, engine, select
import uuid

def create_ncm_rentrie(user: str, ipi: str, ncm: str, description: str, created_at):
    ncm_entrie = NcmEntries(
        user=user, 
        ipi=ipi,
        ncm=ncm,
        description=description,
        created_at=created_at
    )

    with Session(engine) as session:
        session.add(ncm_entrie)
        session.commit()

def get_ncms_by_page(offset, limit):
    with Session(engine) as session:
        query_by_limit = select(NcmEntries).offset(offset).limit(limit).order_by(NcmEntries.id)
        ncms_list =  session.exec(query_by_limit).all()
        return ncms_list

def get_ncm_by_id(id_ncm : uuid.UUID):
    with Session(engine) as session:
        ncm_by_id = session.get(NcmEntries, id_ncm)
        return ncm_by_id
    
def delete_ncm(id_ncm : uuid.UUID):
    with Session(engine) as session:
        ncm_buscado = get_ncm_by_id(id_ncm)

        if ncm_buscado != None:
            session.delete(ncm_buscado)
        session.commit()


    