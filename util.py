import dao
async def rate_addprof(content: str):
    await dao.insert_prof(content.split()[1], content.split()[2])

async def rate_deleteprof(content: str):
    await dao.delete_prof(content.split()[1])

async def rate_delete(content: str):
    await dao.delete_rating(await dao.get_profid(content.split()[2]), content.split()[1])

async def rate(content: str, id: int):
    await dao.insert_rating(await dao.get_profid(content.split()[1]), id, int(content.split()[2]), int(content.split()[3]), int(content.split()[4]))

async def rate_getratings(content: str):
    ratings_list = await dao.get_prof(await dao.get_profid(content.split()[1]))
    quality = difficulty = grade = 0
    rating_count = len(ratings_list)
    for rating in ratings_list:
        quality += rating[0]
        difficulty += rating[1]
        grade += rating[2]

    quality /= rating_count
    difficulty /= rating_count
    grade /= rating_count
    return {"quality": quality, "difficulty": difficulty, "grade": grade}
