from app.db import init_db
from app.repositories.operations import criar_cliente, listar_clientes
# pylint: disable=C0114, C0115

# Inicializa tabelas
init_db()

# Criar alguns clientes
# c1 = criar_cliente("Maria", "tesmariaJOAQUINA@email.com")
# c2 = criar_cliente("João", "jotesaoATRELO@email.com")

# Listar clientes
for cliente in listar_clientes():
    print(cliente["id"], cliente["nome"], cliente["email"])
