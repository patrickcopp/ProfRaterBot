from codes import ResponseCodes
import dao

def add_prof_val(content: str):
    if len(content.split()) != 3:
        return ResponseCodes.WRONG_NUMBER_ARGS
    return ResponseCodes.OK

def remove_prof_val(content: str):
    if len(content.split()) != 2:
        return ResponseCodes.WRONG_NUMBER_ARGS
    return ResponseCodes.OK

def remove_rating_val(content: str):
    if len(content.split()) != 3:
        return ResponseCodes.WRONG_NUMBER_ARGS
    if content.split()[1][0] != '<' or content.split()[1][-1] != '>':
        return ResponseCodes.ARGS_MESSED_UP

def rate_val(content: str):
    if len(content.split()) != 5:
        return ResponseCodes.WRONG_NUMBER_ARGS
    try:
        if int(content.split()[2]) > 10 or int(content.split()[2]) < -1:
            return ResponseCodes.NUMBERS_MESSED_UP
        if int(content.split()[3]) > 10 or int(content.split()[2]) < -1:
            return ResponseCodes.NUMBERS_MESSED_UP
        if int(content.split()[4]) > 10 or int(content.split()[2]) < -1:
            return ResponseCodes.NUMBERS_MESSED_UP
    except:
        return ResponseCodes.ARGS_MESSED_UP
    return ResponseCodes.OK

def remove_val(content: str):
    if len(content.split()) != 3:
        return ResponseCodes.WRONG_NUMBER_ARGS
    return ResponseCodes.OK
