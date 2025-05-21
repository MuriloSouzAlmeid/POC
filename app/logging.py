import logging

logging.basicConfig(filename="./app/logging.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - Mensagem: %(message)s Função: %(funcName)s Arquivo: %(filename)s")