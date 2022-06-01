from getCurriculos import get_curriculos
from createCourse import createcourse

def criar_turmas(n):
    i = 1
    while i <= n:
        idcurso = createcourse("NOVA SALA")
        get_curriculos(idcurso)
        i=i+1
