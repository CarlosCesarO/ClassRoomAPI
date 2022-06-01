# -*- coding: utf-8 -*-

def create_lesson(numberlessons,name,intro, panoram,curriculo):
    lessons = []
    i = 0
    while i <= numberlessons:
        if i == 0 and intro == True:
            nametopic = "Introdução "+name+" "+str(i)
            lessons.append(dict({'title': nametopic,'state':'PUBLISHED'}))
            i=i+1
        if i > 0 and curriculo == False:
            nametopic = "Linha do Tempo "+name+" "+str(i) #MUDE O NOME PARA O QUE FOR NECESSÁRIO
            lessons.append(dict({'title': nametopic,'state':'PUBLISHED'}))
            i=i+1
        if i > 0 and curriculo == True:
            nametopic = "Sala de Aula "+name+" "+str(i)
            lessons.append(dict({'title': nametopic,'state':'PUBLISHED'}))

            nametopic = "Roteiro e Atividades "+name+" "+str(i)
            lessons.append(dict({'title': nametopic,'state':'PUBLISHED'}))

            nametopic = "Videoaula "+name+" "+str(numberlessons)
            lessons.append(dict({'title': nametopic,'state':'PUBLISHED'}))

            nametopic = "Devocionais "+name+" "+str(numberlessons)
            lessons.append(dict({'title': nametopic,'state':'PUBLISHED'}))

            nametopic = "Imagens de Apoio "+name+" "+str(numberlessons)
            lessons.append(dict({'title': nametopic,'state':'PUBLISHED'}))

            if panoram == True:
                nametopic = "Panorama "+name+" "+str(numberlessons)
                lessons.append(dict({'title': nametopic,'state':'PUBLISHED'}))
        i=i+1
        
    return (lessons)
