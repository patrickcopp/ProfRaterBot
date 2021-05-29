import dao
async def rate_addprof(content: str):
    await dao.insert_prof(content.split()[1], content.split()[2])
    return

async def rate_deleteprof(content: str):
    await dao.delete_prof(content.split()[1])

async def rate_delete(content: str):
    return

async def rate(content: str):
    return

async def rate_remove(content: str):
    return