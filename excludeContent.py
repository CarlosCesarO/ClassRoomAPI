from listTopic import listtopic
from listMaterials import listMaterials
from deleteTopic import deletetopic
from deleteMaterials import deleteMaterials


def excludecontent(courseId):

    listtop = listtopic(courseId)
    listmat = listMaterials(courseId)

    for i in listtop:
        deletetopic(courseId,i)

    for i in listmat:
        deleteMaterials(courseId,i)


excludecontent(480591135349)