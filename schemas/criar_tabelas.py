#from core.database import engine
import core
"""""
async def create_table() -> None:
    import models.__all_models
    print("Criando as tabelas de banco de dados...")

    async with engine.begin() as conn:
        print('Tabelas criadas com sucesso')


    async with engine.begin() as conn:
        await conn.run_sync(core.configs.settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)




if __name__ == 'main' :
    import asyncio

    asyncio.run(create_table())

"""
print("testando")

