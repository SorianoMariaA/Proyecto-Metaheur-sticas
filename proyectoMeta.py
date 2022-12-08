import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta
import random
import time

start=time.time()

asignados = 0
disponible1 = True
disponible2 = True
disponible3 = True
disponible4 = True
disponible5 = True
disponible6 = True
disponible7 = True
disponible8 = True
disponible9 = True
disponible10 = True
disponible11 = True
disponible12 = True
disponible13 = True

#Muestra representativa seleccionada aleatoriamente
Muestras = [338, 	30, 	335, 	195, 	266, 	139, 	212, 	70, 	200, 	240, 	131, 	315, 	97, 	270, 	34, 	156, 	78, 	278, 	119, 	173, 	252, 	235, 	52, 	337, 	154, 	246, 	327, 	60, 	67, 	62, 	165, 	302, 	20, 	51, 	1, 	234, 	313, 	16, 	258, 	116, 	35, 	75, 	138, 	316, 	207, 	251, 	5, 	329, 	28, 	54, 	325, 	170, 	294, 	223, 	341, 	137,   57,	103, 	108, 	175, 	296, 	285, 	203, 	209, 	85, 	299, 	222, 	132, 	253, 	241, 	263, 	64, 	33, 	10, 	40, 	254] 

columnas = ['A','B','C','D','E','F']

valorEsperado = {
'1A': 0.316468794248992,
'1F': 0.303725084413463,
'1B': 0.25737937043895,
'1E': 0.24441781940965,
'1D': 0.210271212286243,
'1C': 0.199651454089968,
'2A': 0.381439930290818,
'2C': 0.34255527720292,
'2D': 0.335148676614748,
'2F': 0.288857422938678,
'2B': 0.232164252260102,
'2E': 0.210053371092474,
'3A': 0.288857422938678,
'3F': 0.249972769850779,
'3B': 0.173728352031369,
'3D': 0.203681516174709,
'3E': 0.172149003376539,
'3C': 0.183313364557238,
'4A': 0.251824419997822,
'4B': 0.183204443960353,
'4C': 0.15183531205751,
'4F': 0.149983661910467,
'4E': 0.121609846421958,
'4D': 0.0999891079403117,
'5B': 0.0963402679446682,
'5E': 0.0789674327415313,
'5A': 0.087027556911012,
'5C': 0.0759176560287549,
'5F': 0.0629561049994555,
'5D': 0.0592528047053696,
'6A': 0.279381331009693,
'6F': 0.273499618777911,
'6B': 0.203681516174709,
'6E': 0.192898377083106,
'6C': 0.15586537414225,
'6D': 0.13527938133101,
'7A': 0.216152924518026,
'7B': 0.158152706676833,
'7F': 0.189685219475003,
'7E': 0.118614530007624,
'7C': 0.116163816577715,
'7D': 0.0823439712449625,
'8A': 0.216152924518026,
'8B': 0.159350833242566,
'8E': 0.104237011218822,
'8F': 0.122045528809498,
'8C': 0.0882256834767455,
'8D': 0.0705805467813963,
'9A': 0.152924518026359,
'9B': 0.116218276876157,
'9F': 0.114693388519769,
'9E': 0.0670950876810806,
'9D': 0.0764622590131793,
'9C': 0.0691101187234507,
'10B': 0.0826707330356171,
'10A': 0.0985186798823659,
'10F': 0.079403115129071,
'10E': 0.0587082017209455,
'10C': 0.0558762662019389,
'10D': 0.0249972769850779,
'11B': 0.068293214246814,
'11A': 0.0823439712449625,
'11E': 0.0587082017209455,
'11F': 0.0646988345496133,
'11D': 0.0220564208691864,
'11C': 0.0191155647532948,
'12F': 0.104237011218821,
'12A': 0.097919616599499,
'12E': 0.0771157825944886,
'12B': 0.0745016882692517,
'12C': 0.0394837163707658,
'12D': 0.0363250190611046,
'13F': 0.0663326435028864,
'13E': 0.0509748393421195,
'13B': 0.0431325563664089,
'13A': 0.0458011109900883,
'13C': 0.0442217623352575,
'13D': 0.0236902298224594,
'14B': 0.0960679664524561,
'14A': 0.130377954471191,
'14E': 0.0758087354318701,
'14C': 0.09704825182442,
'14F': 0.0931271103365647,
'14D': 0.0627382638056857,
'15B': 0.0973750136150746,
'15A': 0.120575100751552,
'15E': 0.0797298769197256,
'15F': 0.106851105544058,
'15C': 0.0843045419888901,
'15D': 0.072541117525324,
'16A': 0.154885088770286,
'16B': 0.0986820607776931,
'16F': 0.0882256834767454,
'16C': 0.0784228297571071,
'16E': 0.0516283629234288,
'16D': 0.042152270994445,
'17B': 0.0718875939440148,
'17A': 0.103910249428167,
'17E': 0.0503213157608104,
'17F': 0.0617579784337217,
'17C': 0.042152270994445,
'17D': 0.0323494172748067,
'18F': 0.118614530007624,
'18E': 0.0777693061757978,
'18A': 0.0803834005010348,
'18B': 0.0522818865047381,
'18D': 0.0617579784337217,
'18C': 0.0431325563664089,
'19B': 0.0758087354318701,
'19E': 0.0686199760374686,
'19A': 0.091166539592637,
'19F': 0.0794031151290709,
'19C': 0.0754819736412155,
'19D': 0.0637185491776496,
'20B': 0.0758087354318701,
'20A': 0.105870820172095,
'20E': 0.0692734996187779,
'20F': 0.100969393312275,
'20D': 0.0558762662019388,
'20C': 0.0480339832262281,
'21B': 0.0895327306393639,
'21A': 0.129397669099227,
'21E': 0.0620847402243764,
'21F': 0.091166539592637,
'21C': 0.0352902733906982,
'21D': 0.0313691319028427,
'22B': 0.103910249428167,
'22A': 0.14802309116654,
'22C': 0.0921468249646007,
'22E': 0.0496677921795012,
'22D': 0.0627382638056857,
'22F': 0.0490142685981919,
'23A': 0.104890534800131,
'23B': 0.0679664524561595,
'23E': 0.0568565515739027,
'23F': 0.066659405293541,
'23D': 0.0597974076897941,
'23C': 0.054895980829975,
'24B': 0.102929964056203,
'24A': 0.16011327742076,
'24E': 0.0965581091384382,
'24F': 0.14715172639146,
'24C': 0.0770068619976037,
'24D': 0.070907308572051,
'25E': 0.0970482518244198,
'25F': 0.14715172639146,
'25B': 0.0887158261627274,
'25A': 0.118178847620085,
'25C': 0.0831064154231566,
'25D': 0.0792941945321861,
'26A': 0.116653959263697,
'26E': 0.0715608321533602,
'26B': 0.0671495479795229,
'26F': 0.0998801873434267,
'26D': 0.0792941945321861,
'26C': 0.0655701993246923,
'27B': 0.0838143993029082,
'27A': 0.12656573358022,
'27F': 0.107504629125368,
'27E': 0.0681298333514868,
'27C': 0.0792941945321861,
'27D': 0.0747195294630215,
'28E': 0.0514649820281015,
'28B': 0.0504846966561377,
'28A': 0.0701448643938568,
'28F': 0.0663326435028865,
'28C': 0.0533710924735867,
'28D': 0.0526086482953927,
'29E': 0.0887158261627274,
'29F': 0.132665287005773,
'29A': 0.105979740768979,
'29B': 0.066659405293541,
'29D': 0.0770068619976037,
'29C': 0.0625204226119159,
'30E': 0.0622481211197037,
'30B': 0.0573466942598845,
'30F': 0.0884435246705151,
'30A': 0.0853937479577388,
'30D': 0.0670950876810805,
'30C': 0.0564208691863631,
'31B': 0.042642413680427,
'31E': 0.0387212721925716,
'31F': 0.0556584250081691,
'31A': 0.0518462041171985,
'31C': 0.0510837599390045,
'31D': 0.039647097266093,
'32B': 0.018625422067313,
'32C': 0.0221108811676288
}

FOs_F=[]
FOs_IMA=[]
FOs_LS=[]
for sample in Muestras:
    sillas = [
    '1A',
    '1F',
    '1B',
    '1E',
    '1D',
    '1C',
    '2A',
    '2C',
    '2D',
    '2F',
    '2B',
    '2E',
    '3A',
    '3F',
    '3B',
    '3D',
    '3E',
    '3C',
    '4A',
    '4B',
    '4C',
    '4F',
    '4E',
    '4D',
    '5B',
    '5E',
    '5A',
    '5C',
    '5F',
    '5D',
    '6A',
    '6F',
    '6B',
    '6E',
    '6C',
    '6D',
    '7A',
    '7B',
    '7F',
    '7E',
    '7C',
    '7D',
    '8A',
    '8B',
    '8E',
    '8F',
    '8C',
    '8D',
    '9A',
    '9B',
    '9F',
    '9E',
    '9D',
    '9C',
    '10B',
    '10A',
    '10F',
    '10E',
    '10C',
    '10D',
    '11B',
    '11A',
    '11E',
    '11F',
    '11D',
    '11C',
    '12F',
    '12A',
    '12E',
    '12B',
    '12C',
    '12D',
    '13F',
    '13E',
    '13B',
    '13A',
    '13C',
    '13D',
    '14B',
    '14A',
    '14E',
    '14C',
    '14F',
    '14D',
    '15B',
    '15A',
    '15E',
    '15F',
    '15C',
    '15D',
    '16A',
    '16B',
    '16F',
    '16C',
    '16E',
    '16D',
    '17B',
    '17A',
    '17E',
    '17F',
    '17C',
    '17D',
    '18F',
    '18E',
    '18A',
    '18B',
    '18D',
    '18C',
    '19B',
    '19E',
    '19A',
    '19F',
    '19C',
    '19D',
    '20B',
    '20A',
    '20E',
    '20F',
    '20D',
    '20C',
    '21B',
    '21A',
    '21E',
    '21F',
    '21C',
    '21D',
    '22B',
    '22A',
    '22C',
    '22E',
    '22D',
    '22F',
    '23A',
    '23B',
    '23E',
    '23F',
    '23D',
    '23C',
    '24B',
    '24A',
    '24E',
    '24F',
    '24C',
    '24D',
    '25E',
    '25F',
    '25B',
    '25A',
    '25C',
    '25D',
    '26A',
    '26E',
    '26B',
    '26F',
    '26D',
    '26C',
    '27B',
    '27A',
    '27F',
    '27E',
    '27C',
    '27D',
    '28E',
    '28B',
    '28A',
    '28F',
    '28C',
    '28D',
    '29E',
    '29F',
    '29A',
    '29B',
    '29D',
    '29C',
    '30E',
    '30B',
    '30F',
    '30A',
    '30D',
    '30C',
    '31B',
    '31E',
    '31F',
    '31A',
    '31C',
    '31D',
    '32B',
    '32C']
    baseDatos=pd.read_csv("ima_"+str(sample).zfill(3)+".txt", sep="	")
    
    asientos = pd.DataFrame(columns = ["A","B","C","D","E","F"],index=range(32))
    iDs = pd.DataFrame(columns = ["A","B","C","D","E","F"],index=range(32))
    vueloFecha = baseDatos.iloc[0]["DepartureDate"]
    Fidelina = pd.DataFrame(columns = ["A","B","C","D","E","F"],index=range(32))
    iDsF = pd.DataFrame(columns = ["A","B","C","D","E","F"],index=range(32))
    
    #Puestos no disponibles----------------------------------------------------
    asientos.iloc[31][0] = "X"
    iDs.iloc[31][0] = "X"
    Fidelina.iloc[31][0] = "X"
    iDsF.iloc[31][0] = "X"
    for i in range(3,6):
        asientos.iloc[31][i] = "X"
        iDs.iloc[31][i] = "X"
        Fidelina.iloc[31][i] = "X"
        iDsF.iloc[31][i] = "X"
      
    #Funcion objetivo de Fidelina----------------------------------------------
    for i in range(len(baseDatos)):
    #Ocupar las sillas que Fidelina asignó------------------------------------
        string = baseDatos.iloc[i]["UnitDesignator"]
        columna = string[-1]
        fila = string[0:-1]
        Fidelina.iloc[int(fila)-1][columna] = 0
        iDsF.iloc[int(fila)-1][columna] = "CC - " + baseDatos.iloc[i]["RecordLocator"]
    cuantasvacias=0
    F0_Fidelina=0 
    for i in range(len(Fidelina)):
        for j in columnas:
            if pd.isna(Fidelina.iloc[i][j]):
                cuantasvacias+=1
                F0_Fidelina+=valorEsperado[str(i+1)+j]
    FOs_F.append(F0_Fidelina)
    #--------------------------------------------------------------------------  
    #Algoritmo propuesto:------------------------------------------------------
    indices = []
    count = 0
    # Ocupar/bloquear las sillas que fueron compradas--------------------------
    for i in range(len(baseDatos)):  
        compra = baseDatos.iloc[i]["SeatBookDate"]
        if pd.isna(compra)==False:
            if datetime.strptime(compra, '%m/%d/%Y') <= datetime.strptime(vueloFecha, '%m/%d/%Y')-timedelta(1):
                count += 1
                string = baseDatos.iloc[i]["UnitDesignator"]
                columna = string[-1]
                fila = string[0:-1]
                asientos.iloc[int(fila)-1][columna] = count
                iDs.iloc[int(fila)-1][columna] = "CC - " + baseDatos.iloc[i]["RecordLocator"]
                indices.append(i) #Guarda la posición de las personas que ya compraron asiento
                if count == 99:
                    count = 0
                sillas.remove(str(fila)+columna)
    #--------------------------------------------------------------------------
    listaFamiliares = {}
    for i in range(len(baseDatos)):
        # Borrar a los que no compraron y viajan en grupo
        if i not in indices:
            contador = 0
            for j in range(i+1,len(baseDatos)):      
                if j not in indices:
                    if baseDatos.iloc[i]["RecordLocator"] == baseDatos.iloc[j]["RecordLocator"] and pd.isna(baseDatos.iloc[j]["SeatBookDate"]):
                        contador += 1
                        indices.append(j) #Guarda la posición de los integrantes de un grupo que no compraron asiento
            if contador > 0:
                listaFamiliares[baseDatos.iloc[i]["RecordLocator"]] = contador
   
    for i in indices:
        baseDatos = baseDatos.drop(i,axis = 0) # Borrar los que ya compraron y a los familiares
        # La base de datos queda con las cabeza de familia que no compraron
        #----------------------------------------------------------------------

    iteracionesss = 0
    # Condiciones para la asignación
    for i in range(len(baseDatos)): 
        iteracionesss +=1
        # Si el pasajero viene en grupo, se ubica por primera vez a TODOS los integrantes aleatoriamente
        if baseDatos.iloc[i]["RecordLocator"] in listaFamiliares:
            cantidadPorAsignar = listaFamiliares[baseDatos.iloc[i]["RecordLocator"]]
            familiaresAsignados = []
            familiaresAnteriores = []
            for j in range(cantidadPorAsignar+1):
                silla = random.choice(sillas)
                columna = silla[-1]
                fila = silla[0:-1]
                count += 1
                asientos.iloc[int(fila)-1][columna] = count
                iDs.iloc[int(fila)-1][columna] = baseDatos.iloc[i]["RecordLocator"]
                if count == 99:
                    count = 0
                sillas.remove(silla)
                familiaresAsignados.append(silla)
                familiaresAnteriores.append(silla)
                
            # Calcular distancia con la asignacion inicial
            distanciaMejor = 0
            for chair in familiaresAsignados:
                col = ord(chair[-1])-65
                fil = chair[0:-1]
                for chair2 in familiaresAsignados:
                    col2 = ord(chair[-1])-65
                    fil2 = chair[0:-1]
                    distanciaMejor = distanciaMejor + abs(int(fil)-int(fil2)) + abs(col-col2)
                    
            # ILS lo repite-------------------------------------------------------------------------------------------------------
            
            for c in range(cantidadPorAsignar+1): 
                familiaresAsignados = []
                for j in range(cantidadPorAsignar+1):
                    silla = random.choice(sillas)
                    columna = silla[-1]
                    fila = silla[0:-1]
                    familiaresAsignados.append(silla)
                # Calcular distancia de la solucion temporal 
                distancia = 0
                for chair in familiaresAsignados:
                    col = ord(chair[-1])-65
                    fil = chair[0:-1]
                    for chair2 in familiaresAsignados:
                        col2 = ord(chair[-1])-65
                        fil2 = chair[0:-1]
                        distancia = distancia + abs(int(fil)-int(fil2)) + abs(col-col2)
                # Actualiza la mejor distribución
                # Permite degradación una vez
                perturbacion = 0               
                if distancia < distanciaMejor:
                    perturbacion +=1
                if distancia > distanciaMejor or perturbacion==1:
                    aceptar = True
                    distanciaMejor = distancia
                    if count - cantidadPorAsignar+1 < 0:
                        count = 99+count-cantidadPorAsignar+1
                    for w in familiaresAnteriores:
                        sillas.append(w)
                        asientos.iloc[int(w[0:-1])-1][w[-1]] = np.nan
                        iDs.iloc[int(w[0:-1])-1][w[-1]] = np.nan
                    
                    for x in familiaresAsignados:
                        count += 1
                        columna = x[-1]
                        fila = x[0:-1]
                        asientos.iloc[int(fila)-1][columna] = count
                        iDs.iloc[int(fila)-1][columna] = baseDatos.iloc[i]["RecordLocator"]
                        if count == 99:
                            count = 0
                        sillas.remove(x)
                        familiaresAnteriores=familiaresAsignados[:]
            
                #------------------------------------------------------------------------------------------------------------------
        #Si los pasajeros viajan solos se agregan inicialmente por medio del constructivo
        else:  
            
            if pd.isna(baseDatos.iloc[i]["SeatBookDate"]):
                booleana = False
                asignados = 0
                # Columnas B y E en centro y posterior
                if disponible1 == True:
                    for x in range(14,29):
                        for w in ["B","E"]:
                            booleana = False
                            asignados += 1 
                            if asignados == 30:
                                disponible1 = False
                            if pd.isna(asientos.iloc[x-1][w]):
                                count += 1
                                asientos.iloc[x-1][w] = count
                                iDs.iloc[x-1][w] = baseDatos.iloc[i]["RecordLocator"] 
                                sillaAsignada = str(x) + w
                                valorActualF0 = valorEsperado[str(x) + w]
                                booleana = True
                                if count == 99:
                                    count = 0
                                sillas.remove(str(x) + w)
                                break
                        else:
                              continue
                        break 
                # Busqueda local primera mejora
                if booleana == True:                
                    for benito in sillas:
                        if valorEsperado[benito] < valorActualF0:
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            sillas.append(sillaAsignada)
                            sillaAsignada = benito
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = count
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = baseDatos.iloc[i]["RecordLocator"] 
                            sillas.remove(sillaAsignada)
                            
                    continue
                # Columnas A, C, D y F filas 24 a 28
                if booleana == False and disponible2==True:
                    for x in range(24,29):
                        for w in ["A","C","D","F"]:
                            booleana = False
                            asignados += 1
                            if asignados == 20:
                                disponible2 = False
                            if pd.isna(asientos.iloc[x-1][w]):
                                count += 1
                                asientos.iloc[x-1][w] = count
                                iDs.iloc[x-1][w] = baseDatos.iloc[i]["RecordLocator"]
                                booleana = True
                                if count == 99:
                                    count = 0
                                sillas.remove(str(x) + w)
                                
                                break
                        else:
                              continue
                        break
                if booleana == True:
                    for benito in sillas:
                        if valorEsperado[benito] < valorActualF0:
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            sillas.append(sillaAsignada)
                            sillaAsignada = benito
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = count
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = baseDatos.iloc[i]["RecordLocator"] 
                            sillas.remove(sillaAsignada)
                    continue
                # Columnas A, C, D y F en centro
                if booleana == False and disponible3 == True:
                    for x in range(14,24):
                        for w in ["A","C","D","F"]:
                            booleana = False
                            asignados += 1
                            if asignados == 40:
                                disponible3 = False
                            if pd.isna(asientos.iloc[x-1][w]):
                                count += 1
                                asientos.iloc[x-1][w] = count
                                iDs.iloc[x-1][w] = baseDatos.iloc[i]["RecordLocator"]
                                booleana = True
                                if count == 99:
                                    count = 0
                                sillas.remove(str(x) + w)
                                break
                        else:
                              continue
                        break
                if booleana == True:
                    for benito in sillas:
                        if valorEsperado[benito] < valorActualF0:
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            sillas.append(sillaAsignada)
                            sillaAsignada = benito
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = count
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = baseDatos.iloc[i]["RecordLocator"] 
                            sillas.remove(sillaAsignada)
                    continue
                # Columnas B y E en salida rápida 
                if booleana == False and disponible4 == True:
                    for x in range(6,12):
                        for w in ["B","E"]:
                            booleana = False
                            asignados += 1
                            if asignados == 12:
                                disponible4 = False
                            if pd.isna(asientos.iloc[x-1][w]):
                                count += 1
                                asientos.iloc[x-1][w] = count
                                iDs.iloc[x-1][w] = baseDatos.iloc[i]["RecordLocator"]
                                booleana = True
                                if count == 99:
                                    count = 0
                                sillas.remove(str(x) + w)
                                break
                        else:
                              continue
                        break
                if booleana == True:
                    for benito in sillas:
                        if valorEsperado[benito] < valorActualF0:
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            sillas.append(sillaAsignada)
                            sillaAsignada = benito
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = count
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = baseDatos.iloc[i]["RecordLocator"] 
                            sillas.remove(sillaAsignada)
                    continue
                # Columnas B y E en salida emergencia
                if booleana == False and disponible5 == True:
                    for x in range(12,14):
                        for w in ["B","E"]:
                            booleana = False
                            asignados += 1
                            if asignados == 4:
                                disponible5 = False
                            if pd.isna(asientos.iloc[x-1][w]):
                                count += 1
                                asientos.iloc[x-1][w] = count
                                iDs.iloc[x-1][w] = baseDatos.iloc[i]["RecordLocator"]
                                booleana = True
                                if count == 99:
                                    count = 0
                                sillas.remove(str(x) + w)
                                break
                        else:
                              continue
                        break
                if booleana == True:
                    for benito in sillas:
                        if valorEsperado[benito] < valorActualF0:
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            sillas.append(sillaAsignada)
                            sillaAsignada = benito
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = count
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = baseDatos.iloc[i]["RecordLocator"] 
                            sillas.remove(sillaAsignada)
                    continue
                # Columnas A, C, D y F en salida rápida    
                if booleana == False and disponible6 == True: # Hay 24 sillas
                    for x in range(6,12):
                        for w in ["A","C","D","F"]:
                            booleana = False
                            asignados += 1
                            if asignados == 24:
                                disponible6 = False
                            if pd.isna(asientos.iloc[x-1][w]):
                                count += 1
                                asientos.iloc[x-1][w] = count
                                iDs.iloc[x-1][w] = baseDatos.iloc[i]["RecordLocator"]
                                booleana = True
                                if count == 99:
                                    count = 0
                                sillas.remove(str(x) + w)
                                break
                        else:
                              continue
                        break
                if booleana == True:
                    for benito in sillas:
                        if valorEsperado[benito] < valorActualF0:
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            sillas.append(sillaAsignada)
                            sillaAsignada = benito
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = count
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = baseDatos.iloc[i]["RecordLocator"] 
                            sillas.remove(sillaAsignada)
                    continue
                # Columnas B, E en adelante
                if booleana == False and disponible7 == True: # Hay 8 sillas
                    for x in range(2,6):
                        for w in ["B","E"]:
                            booleana = False
                            asignados += 1
                            if asignados == 8:
                                disponible7 = False
                            if pd.isna(asientos.iloc[x-1][w]):
                                count += 1
                                asientos.iloc[x-1][w] = count
                                iDs.iloc[x-1][w] = baseDatos.iloc[i]["RecordLocator"]
                                booleana = True
                                if count == 99:
                                    count = 0
                                sillas.remove(str(x) + w)
                                break
                        else:
                              continue
                        break
                if booleana == True:
                    for benito in sillas:
                        if valorEsperado[benito] < valorActualF0:
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            sillas.append(sillaAsignada)
                            sillaAsignada = benito
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = count
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = baseDatos.iloc[i]["RecordLocator"] 
                            sillas.remove(sillaAsignada)
                    continue
                # Columnas A,C,D y F en fila de emergencia
                if booleana == False and disponible8 == True: # Hay 8 sillas
                    for x in range(12,14):
                        for w in ["A","C","D","F"]:
                            booleana = False
                            asignados += 1
                            if asignados == 8:
                                disponible8 = False
                            if pd.isna(asientos.iloc[x-1][w]):
                                count += 1
                                asientos.iloc[x-1][w] = count
                                iDs.iloc[x-1][w] = baseDatos.iloc[i]["RecordLocator"]
                                booleana = True
                                if count == 99:
                                    count = 0
                                sillas.remove(str(x) + w)
                                break
                        else:
                              continue
                        break
                if booleana == True:
                    for benito in sillas:
                        if valorEsperado[benito] < valorActualF0:
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            sillas.append(sillaAsignada)
                            sillaAsignada = benito
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = count
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = baseDatos.iloc[i]["RecordLocator"] 
                            sillas.remove(sillaAsignada)
                    continue
                # Columnas A, C, D y F en adelante
                if booleana == False and disponible9 == True: # Hay 16 sillas
                    for x in range(2,6):
                        for w in ["A","C","D","F"]:
                            booleana = False
                            asignados += 1
                            if asignados == 16:
                                disponible9 = False
                            if pd.isna(asientos.iloc[x-1][w]):
                                count += 1
                                asientos.iloc[x-1][w] = count
                                iDs.iloc[x-1][w] = baseDatos.iloc[i]["RecordLocator"]
                                asignados += 1
                                booleana = True
                                if count == 99:
                                    count = 0
                                sillas.remove(str(x) + w)
                                break
                        else:
                              continue
                        break
                if booleana == True:
                    for benito in sillas:
                        if valorEsperado[benito] < valorActualF0:
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            sillas.append(sillaAsignada)
                            sillaAsignada = benito
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = count
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = baseDatos.iloc[i]["RecordLocator"] 
                            sillas.remove(sillaAsignada)
                    continue
                # Columnas B y E en primera fila   
                if booleana == False and disponible10 == True: # Hay 2 sillas
                    for x in range(1,2):
                        for w in ["B","E"]:
                            booleana = False
                            asignados += 1
                            if asignados == 2:
                                disponible10 = False
                            if pd.isna(asientos.iloc[x-1][w]):
                                count += 1
                                asientos.iloc[x-1][w] = count
                                iDs.iloc[x-1][w] = baseDatos.iloc[i]["RecordLocator"]
                                booleana = True
                                if count == 99:
                                    count = 0
                                sillas.remove(str(x) + w)
                                break
                        else:
                              continue
                        break
                if booleana == True:
                    for benito in sillas:
                        if valorEsperado[benito] < valorActualF0:
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            sillas.append(sillaAsignada)
                            sillaAsignada = benito
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = count
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = baseDatos.iloc[i]["RecordLocator"] 
                            sillas.remove(sillaAsignada)
                    continue
                # Columnas A, C, D y F en primera fila
                if booleana == False and disponible11 == True: # Hay 4 sillas
                    for x in range(1,2):
                        for w in ["A","C","D","F"]:
                            booleana = False
                            asignados += 1
                            if asignados == 4:
                                disponible11 = False
                            if pd.isna(asientos.iloc[x-1][w]):
                                count += 1
                                asientos.iloc[x-1][w] = count
                                iDs.iloc[x-1][w] = baseDatos.iloc[i]["RecordLocator"]
                                booleana = True
                                if count == 99:
                                    count = 0
                                sillas.remove(str(x) + w)
                                break
                        else:
                              continue
                        break
                if booleana == True:
                    for benito in sillas:
                        if valorEsperado[benito] < valorActualF0:
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            sillas.append(sillaAsignada)
                            sillaAsignada = benito
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = count
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = baseDatos.iloc[i]["RecordLocator"] 
                            sillas.remove(sillaAsignada)
                    continue                  
                # Columnas ultimas tres filas
                if booleana == False and disponible12 == True:
                    for x in range(29,32):
                        for w in ["A","B","C","D","E","F"]:
                            booleana = False
                            asignados += 1
                            if asignados == 18:
                                disponible12 = False
                            if pd.isna(asientos.iloc[x-1][w]):
                                count += 1
                                asientos.iloc[x-1][w] = count
                                iDs.iloc[x-1][w] = baseDatos.iloc[i]["RecordLocator"]
                                booleana = True
                                if count == 99:
                                    count = 0
                                sillas.remove(str(x) + w)
                                break
                        else:
                              continue
                        break
                if booleana == True:
                    for benito in sillas:
                        if valorEsperado[benito] < valorActualF0:
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            sillas.append(sillaAsignada)
                            sillaAsignada = benito
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = count
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = baseDatos.iloc[i]["RecordLocator"] 
                            sillas.remove(sillaAsignada)
                    continue
                
                if booleana == False and disponible13 == True:   
                    for x in range(32,33):
                        for w in ["A","B"]:
                            booleana = False
                            asignados += 1
                            if asignados == 2:
                                disponible13 = False
                            if pd.isna(asientos.iloc[x-1][w]):
                                count += 1
                                asientos.iloc[x-1][w] = count
                                iDs.iloc[x-1][w] = baseDatos.iloc[i]["RecordLocator"]
                                booleana = True
                                if count == 99:
                                    count = 0
                                sillas.remove(str(x) + w)
                                break
                        else:
                              continue
                        break
                if booleana == True:
                    for benito in sillas:
                        if valorEsperado[benito] < valorActualF0:
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = np.nan
                            sillas.append(sillaAsignada)
                            sillaAsignada = benito
                            asientos.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = count
                            iDs.iloc[int(sillaAsignada[0:-1])-1][sillaAsignada[-1]] = baseDatos.iloc[i]["RecordLocator"] 
                            sillas.remove(sillaAsignada)
                    continue
        
    
    asignadosF=0
    F0_IMA=0
    for i in range(len(iDs)):
        for j in columnas:
            if pd.isna(iDs.iloc[i][j]) == False and iDs.iloc[i][j] != "X":
                asignadosF +=1
            if pd.isna(iDs.iloc[i][j]):
                F0_IMA+=valorEsperado[str(i+1)+j]
    FOs_IMA.append(F0_IMA)
    
    # F0_LS=0
    # for i in range(len(iDs)):
    #     for j in columnas:
    #         if pd.isna(iDs.iloc[i][j]) == False and iDs.iloc[i][j] != "X":
    #             asignadosF +=1
    #         if pd.isna(iDs.iloc[i][j]):
    #             F0_LS+=valorEsperado[str(i+1)+j]
    # FOs_LS.append(F0_LS)
                
              
end = time.time()

#Análisis de estadístico------------------------------------------------------
from statistics import median
from statistics import quantiles
#medianaLS = median(FOs_LS)
medianaILS = median(FOs_IMA)
#quantileLS=quantiles(FOs_LS)
quantileILS=quantiles(FOs_IMA)

print("CPU:")
print(end - start)
#plt.plot(FOs_LS,color='darkgreen',linestyle='-', linewidth=1, label="LS")

import matplotlib.pyplot as plt 
plt.xlabel('Instance')
plt.ylabel('Objective Function')
plt.plot(FOs_F,color='darkred',linestyle='--', linewidth=0.8, label="Base")
plt.plot(FOs_IMA,color='darkblue',linestyle='-', linewidth=0.8, label="LS & ILS")
plt.legend()
plt.show()

        
        
    
    
