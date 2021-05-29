import dao
async def rate_addprof(content: str):
    await dao.insert_prof(content.split()[1], content.split()[2])

async def rate_deleteprof(content: str):
    await dao.delete_prof(content.split()[1])

async def rate_delete(content: str):
    await dao.delete_rating(await dao.get_profid(content.split()[2]), content.split()[1])

async def rate(content: str, id: int):
    await dao.insert_rating(await dao.get_profid(content.split()[1]), id, int(content.split()[2]), int(content.split()[3]), int(content.split()[4]))