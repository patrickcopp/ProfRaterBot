from codes import ResponseCodes
import dao

async def add_prof_val(content: str):
    if len(content.split()) != 3:
        return ResponseCodes.WRONG_NUMBER_ARGS
    if await dao.get_profid(content.split()[2]) != -1:
        return ResponseCodes.PROF_EXISTS
    return ResponseCodes.OK

def remove_prof_val(content: str):
    if len(content.split()) != 2:
        return ResponseCodes.WRONG_NUMBER_ARGS
    return ResponseCodes.OK

async def remove_rating_val(content: str):
    if len(content.split()) != 3:
        return ResponseCodes.WRONG_NUMBER_ARGS
    if content.split()[1][0] != '<' or content.split()[1][-1] != '>':
        return ResponseCodes.ARGS_MESSED_UP
    profid = await dao.get_profid(content.split()[2])
    if profid == -1:
        return ResponseCodes.PROF_DOESNT_EXIST
    if await dao.get_rating(profid, content.split()[1]) == -1:
        return ResponseCodes.RATING_DOESNT_EXIST
    return ResponseCodes.OK

async def rate_val(content: str):
    if len(content.split()) != 5:
        return ResponseCodes.WRONG_NUMBER_ARGS
    try:
        if int(content.split()[2]) > 10 or int(content.split()[2]) < -1:
            return ResponseCodes.NUMBERS_MESSED_UP
        if int(content.split()[3]) > 10 or int(content.split()[3]) < -1:
            return ResponseCodes.NUMBERS_MESSED_UP
        if int(content.split()[4]) > 100 or int(content.split()[4]) < -1:
            return ResponseCodes.NUMBERS_MESSED_UP
    except:
        return ResponseCodes.ARGS_MESSED_UP
    if await dao.get_profid(content.split()[1]) == -1:
        return ResponseCodes.PROF_DOESNT_EXIST
    return ResponseCodes.OK

async def get_rate_val(content: str):
    if await dao.get_profid(content.split()[1]) == -1:
        return ResponseCodes.PROF_DOESNT_EXIST
    return ResponseCodes.OK
