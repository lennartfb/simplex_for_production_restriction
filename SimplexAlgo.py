import numpy as np
import copy

#Aufgabe
#db = [200,120]
#nb = [[4,10,1600],[8,4,2400]]

#Aufgabe aus controlling überprüfungsaufgaben Nr1
db = [20,30]
nb = [[3,2,1800],[2,4,1600],[0,1,300]]

#Aufgabe aus Controlling tutorium
#db = [3,2]
#nb = [[2,1,100],[1,1,80],[1,0,40]]


#Aufgabe aus controlling überprüfungsaufgaben Nr2
#db = [20,30,35]
#nb = [[3,2,4,1800],[2,4,4,1600],[0,1,0,300]]




#die simplex methode nimmt als parameter einmal die deckungsbeitragsfunktion in der form [faktor_var_1,faktor_var_2......] und die funktionen der nebenbedingungen [[faktor_var_1,faktor_var_2,....,restriktion],[faktor_var_1,faktor_var_2,....,restriktion],....]
#bei den nb funktionen können die schlupfvariablen vernachlässigt werden und variablen die nicht exitiren werden mit dem faktor 0 eingetragen 
def simplex(db: list,nb: list):
    db_s = np.array(db) * -1 
    breite = len(db)+len(nb)+1  #berechnet die länge einer zeile des simplex tableaus
    print(breite)
    funktionen = [db_s.tolist()]
    funktionen.extend(nb) #fügt an die db funktion die anderes nebenbedingungen dran so da eine liste aus listen entsteht; jede unterliste ist eine nebenbedingung oder eben die db funktion
    
    simplex_tablo = liste_erstellen(breite,funktionen)
    print(simplex_tablo)
    solven = solve_tablo(simplex_tablo)
    print("Solved_tablo",solven)
    solven_with_varaibles = enter_variables(solven)
    print("Solven Tablo with Variables:",solven_with_varaibles)
    print_endtablo(solven_with_varaibles)
    
#erstellt das simplextableau mit den dazugehörigen schlupfvariablen; übergeben wird dafür einmal die länge der zeilen des tableaus (breite) und die liste aus db und nebenbedingungen
    #wiedergeggebn wird eine liste aus listen die aus den db und nb bestehen und um die entsprechenden schlupfvrariablenwerte erweitert wurden
def liste_erstellen(breite,funktionen):
    print(funktionen)
    funktions_liste = [[0] * breite for _ in range(len(funktionen))]
    print(funktions_liste)
    
    for j in range(len(funktionen)):
        if j == 0:
            for i in range(len(funktionen[j])):
                funktions_liste[j][i] = funktionen[j][i]
        
        else:
            for i in range(len(funktionen[0])):
                funktions_liste[j][i] = funktionen[j][i]
            funktions_liste[j][len(funktionen[0])-1+j] = 1
            funktions_liste[j][len(funktions_liste[j])-1] = funktionen[j][len(funktionen[j])-1]
    
    return funktions_liste

#löst das tableau mit dem entsprehcnenden algo für produktionsrestriktionen
def solve_tablo(tablo):
    tab = tablo
    
    while min(tab[0])<0:
        print("/////////////NEU REIHE///////////")
        print(tab)
        #gibt den index des Elements bei dem die db funktion am kleinsten ist: 
        pivot_collum = tab[0].index(min(tab[0]))
        #gibt den index der liste in der das pivoelement ist: 
        pivot_element_index_row = get_pivot_element_index(tab)
        print("Pivot collum:",pivot_collum)
        print("Pivot_element:",pivot_element_index_row)
        
        for i in range(len(tab)):
            print("i:",i,"element in liste i an pivotstelle:",tab[i][pivot_collum])
            if  tab[i][pivot_collum] != 0 and i != pivot_element_index_row  :
                
                abzugs_faktor = tab[i][pivot_collum]/tab[pivot_element_index_row][pivot_collum]
                print("Abzug:",abzugs_faktor)
                tab[i] = [x - (abzugs_faktor)*y for x, y in zip(tab[i], tab[pivot_element_index_row])]
                
            
        

        abzugs_faktor = tab[pivot_element_index_row][pivot_collum]
        print("Abzungsfaktor bei pivor reihe:",abzugs_faktor)
        tab[pivot_element_index_row] = [x/abzugs_faktor for x in tab[pivot_element_index_row]]
    return tab
                
#gibt die unterliste wieder, in der das pivot element liegt, dazu wird ein ungelöstes simplex tableau übergeben 
def get_pivot_element_index(tablo):
    pivot_collum_index = tablo[0].index(min(tablo[0]))
    pivot_collum = []
    pivot_collum = []
    

    for i in range(len(tablo)):
            pivot_collum.append(tablo[i][pivot_collum_index])
    end_collum = []
    for row in tablo:
        end_collum.append(row[-1])
    end_collum.pop(0)
    pivot_collum.pop(0)
    print("pivot collum",pivot_collum)
    print("endcollum",end_collum)
    result_endcollum = []
    for x,y in zip(end_collum, pivot_collum):
        if y <= 0:
            result_endcollum.append(-1)
        else:
            result_endcollum.append(x/y) 
    pivot_element_index_row = result_endcollum.index(min(x for x in result_endcollum if x >= 0))
    print("Changed pivot collum:",result_endcollum)
    
    return pivot_element_index_row+1
    
#gibt die variablen der linken spalte anhand der pivot spalten an     
def enter_variables(s_tablo):
    stablo = copy.deepcopy(s_tablo)
    stab = s_tablo
    
    for i in range(len(stablo[0])):
        current_collum = [sublist[i] for sublist in stablo]
        print("Current",current_collum)
        print("STablo:",stablo)
        
        if current_collum.count(1) == 1 and all(item == 0 or item == 1 for item in current_collum):
            
            index_of_one = current_collum.index(1)
            stab[index_of_one].insert(0,f"var_{i+1}")
            
    


    stab[0].insert(0, "db")
    return stab

#printet das tableau in seiner entsprechenden form und gibt die optimalen lösungen für die variablen an
def print_endtablo(solven_tablo):
    print("////////////////////RESULTS TABLEAU/////////////////////")
    name_list = []
    for i in range(len(solven_tablo[0])-2):
        name_list.append(f"Var{i+1}")
    name_list.append("Optimum")

    print(name_list)
    for i in range(1,len(solven_tablo)):
        print(solven_tablo[i])
    print(solven_tablo[0])
    print("////////////////////////////////////////////////")
    print("//////////////////////OPTIMALE WERTE///////////////////////")
    for i in range(len(solven_tablo)):
        print(solven_tablo[i][0] ," = ",solven_tablo[i][-1])
    print("//////////////////////END///////////////////////")



#die simplex methode nimmt als parameter einmal die deckungsbeitragsfunktion in der form [faktor_var_1,faktor_var_2......] und die funktionen der nebenbedingungen [[faktor_var_1,faktor_var_2,....,restriktion],[faktor_var_1,faktor_var_2,....,restriktion],....]
#bei den nb funktionen können die schlupfvariablen vernachlässigt werden und variablen die nicht exitiren werden mit dem faktor 0 eingetragen 
simplex(db,nb)


        

    
