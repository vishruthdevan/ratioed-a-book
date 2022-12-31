def code_gen(characters):
    code = {}
    number = 0
    for i in characters:
        code[i] = str(number).zfill(3)
        number += 1
    return code
