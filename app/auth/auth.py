from app.auth import (datetime, timedelta, timezone, BaseModel, HTTPBearer, 
                      Depends, HTTPException, Annotated, status, InvalidTokenError)
import jwt
from app.config import settings
from app.logging import logging

class User(BaseModel):
    sub: str

class Token(BaseModel):
    access_token: str
    token_type: str

bearer_scheme = HTTPBearer()

def gerar_token(username : str):
    # cria as claims
    claims = {
                "sub": username,
                "exp" : datetime.now(timezone.utc) + timedelta(minutes=settings.poc_expiration_token_time),
                "iat": datetime.now(timezone.utc)
            }

    logging.info("Inicio-se da criacao do JWT token")
    try:
        token = jwt.encode(claims, settings.poc_secret_key_token, settings.poc_algorithm_jwt_token)
    except:
        logging.error("Ocorreu um erro ao criar o JWT token")
        raise HTTPException(status_code=500, detail="Erro ao criar um JWT Token")

    logging.info("Finalizou-se da criacao do JWT token")
    return Token(access_token=token, token_type="bearer")


def descriptografar_token(token : str):
    token_descriptografado = jwt.decode(jwt=token, key=settings.poc_secret_key_token, algorithms=[settings.poc_algorithm_jwt_token])

    return token_descriptografado


async def get_current_user(token: Annotated[str, Depends(bearer_scheme)]):
    token_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido ou expirado",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        token_descriptografado = descriptografar_token(token.credentials)
        if token_descriptografado.get("sub") is None:
            logging.error("Ocorreu um erro ao descriptografar o token, as claims do token estao vindo vazias")
            raise token_exception
    except InvalidTokenError:
        logging.error("Ocorreu um erro ao validar o JWT token, o token informado esta expirado ou em formato invalido")
        raise token_exception

    return User(sub=token_descriptografado.get("sub"))