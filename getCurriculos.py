# -*- coding: utf-8 -*-
from curriculos import list
from materiais import create_lesson
from createTopic import create_topic
from createMaterials import create_roteiroativ, create_devocionais,create_imagensdeapoio,create_videoaula, create_intro, create_panoram,create_noncurriculum, create_saladeaula

def get_curriculos(idcurso):
    
    for i in list:
        n = 0
        while n <= i.get('topicos'): 
 
            lessons = create_lesson(n,i.get('nome'),i.get('intro'),i.get('panoram'),i.get('curriculo'))

            if n == 0:
                if i.get('intro') == True:
                    nomeTopico = i.get('nome')+" Introdução "+ str(n)
                    topicid = create_topic(idcurso,nomeTopico,)            
                    create_intro(lessons,idcurso, n ,topicid , i.get('nome'))
            else:
                if i.get('curriculo') == False:
                    nomeTopico = i.get('nome')+" Linha do Tempo "+ str(n) #MUDE O NOME QUANDO QUISER
                    topicid = create_topic(idcurso,nomeTopico,)            
                    create_noncurriculum(lessons,idcurso, n ,topicid , i.get('nome'))
                # else:
                if n == 1:#USAR ISSO COMO EXCESSÃO PARA UPAR APENAS UMA LIÇÃO
                    nomeTopico = i.get('nome')+" Lição "+ str(n)
                    topicid = create_topic(idcurso,nomeTopico)
                    create_devocionais(lessons,idcurso, n , topicid , i.get('nome'))
                    # create_imagensdeapoio(lessons,idcurso, n , topicid , i.get('nome'))
                    create_videoaula(lessons,idcurso, n , topicid , i.get('nome'))
                    create_saladeaula(lessons,idcurso, n , topicid , i.get('nome'))
                    # create_roteiroativ(lessons,idcurso, n , topicid , i.get('nome'))
                    if i.get('panoram') == True:
                        create_panoram(lessons,idcurso, n , topicid , i.get('nome'))

            n=n+1




