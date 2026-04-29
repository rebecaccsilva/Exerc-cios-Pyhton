# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


def notas(*n, sit=False):
    bo = dict()
    bo["maior"] = max(n)
    bo["menor"] = min(n)
    bo["total"] = len(n)
    bo["media"] = sum(n) / len(n)
    if sit == True:
        if bo["media"] >= 7:
            bo["media"] = "BOA"
        elif 5 <= bo["media"] < 7:
            bo["media"] = "RAZOAVEL"
        else:
            bo["media"] = "REPROVADO"
    return bo


resp = notas(1, 8, 5, 7, 9, 2.1, sit=True)
print(resp)
