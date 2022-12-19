
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import re
import urllib.request


#Film ID for Toy Story films
ToyStory1_id = "tt0114709"
ToyStory2_id = "tt0120363"
ToyStory3_id = "tt0435761"
ToyStory4_id = "tt1979376"

#Name ID for Toy Story voice actors
allen_id ="nm0000741"
hanks_id = "nm0000158"
cusack_id = "nm0000349"
ratzenberger_id = "nm0001652"
shawn_id = "nm0001728"



def imbdFetchFilm(filmID):
    url = "https://www.imdb.com/title/" + filmID + "/fullcredits"
    
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    time.sleep(1)
    #print(html)
    
    castTable = soup.find_all("table", "cast_list")[0]
    #print(castTable)
    
    tdList = castTable.find_all("td", "primary_photo")
    nameIDs = []
    for td in tdList:
        #print("\n" + str(td) + "\n")
        tag = td.find_all("a")[0]
        #print(aTag.get('href'))
        href = tag.get('href')
        nameID = href.strip("/").split("/")[1]
        #print(nameID)
        nameIDs.append(nameID)
    return(nameIDs)


def imbdFetchPerson(nameID):
    url = "https://www.imdb.com/name/nm4004793"
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
    page = urllib.request.urlopen( req )
   
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    filmIds = []
    #for film in filmList:
    for s in soup.find_all("button",id=re.compile("nm-flmg_cred-act.*-tt.*")):
        filmIds.append(s.get('id').split('-')[-1])
    return filmIds
    
################################################
#Film ID for Toy Story films
ToyStory1_id = "tt0114709"
ToyStory2_id = "tt0120363"
ToyStory3_id = "tt0435761"
ToyStory4_id = "tt1979376"

#Name ID for Toy Story voice actors
allen_id ="nm0000741"
hanks_id = "nm0000158"
cusack_id = "nm0000349"
ratzenberger_id = "nm0001652"
shawn_id = "nm0001728"



#Toy Story 1
toystory1_list = imbdFetchFilm(ToyStory1_id)
print(toystory1_list)

#Toy Story 2
toystory2_list = imbdFetchFilm(ToyStory2_id)
print(toystory2_list)

#Toy Story 3
toystory3_list = imbdFetchFilm(ToyStory3_id)
print(toystory3_list)

#Toy Story 4
toystory4_list = imbdFetchFilm(ToyStory4_id)
print(toystory4_list)

#Tim Allen
buzzLightyear = imbdFetchPerson(allen_id)
print(buzzLightyear)

#Tom Hanks
sheriffWoody = imbdFetchPerson(hanks_id)
print(sheriffWoody)

#Joan Cusack
Jessie = imbdFetchPerson(cusack_id)
print(Jessie)

#John RatzenBerger
Hamm = imbdFetchPerson(ratzenberger_id)
print(Hamm)

#Wallace Shawn
Rex = imbdFetchPerson(shawn_id)
print(Rex)

