# pylint: disable=C0114, C0115
# from app.repositories import cliente_operations, processo_operations

# Criar alguns clientes
# c1 = cliente_operations.criar("Maria", "testemariaJOAQUINA@email.com")
# c2 = cliente_operations.criar("João", "testejotesaoATRELO@email.com")
# p1 = processo_operations.criar("EU", "ELE")
# p2 = processo_operations.criar("EU", "OUTRA PESSOA")

# Listar clientes
# for cliente in cliente_operations.listar():
#     print(cliente.id, cliente.nome, cliente.email)

# for processo in processo_operations.listar():
#     print(processo.nro_processo, processo.polo_ativo, processo.polo_passivo)

from fastapi import FastAPI
from app.routers import cliente_router, processo_router

app = FastAPI(title="Minha API")

# Registrando as rotas
app.include_router(cliente_router.router)
app.include_router(processo_router.router)
