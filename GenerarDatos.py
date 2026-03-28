import random
import csv
from datetime import datetime, timedelta, time
NUM_MUSICOS=1000000 
NUM_GRUPOS=200000         
NUM_DISCOS=1000000        
NUM_CONCIERTOS=100000     
NUM_ENTRADAS=24000000     

GENEROS= [ "clasica", "blues", "jazz", "rock&roll", "gospel", "soul",
    "rock", "metal", "funk", "disco", "techno", "pop", "reggae", "hiphop", "salsa"]
Paises=["España", "Francia", "Italia", "Reino Unido", "Alemania", "Luxemburgo", "Belgica", "Austria", "Grecia", "Noruega",
        "Dinamarca", "Lituania", "Estonia", "Polonia", "Ucrania", "Chipre", "Turquia", "Rumania", "Hungria", "Portugal", "Irlanda"]


def random_dni():
    num = random.randint(10000000, 99999999)
    letra = random.choice("QWERTYUIOPASDFGHJKLZXCVBNM")
    return f"{num}{letra}"

def random_telefono():
    return random.randint(100000000, 999999999)

def random_cp():
    return random.randint(10000, 99999)

def random_ciudad():
    return random.choice(["Madrid", "Barcelona", "Valencia", "Guadalajara", "Toledo", "Albacete"])

def random_provincia(a):
    if a=="Madrid" or a=="Barcelona" or a=="Valencia":
        b=a
    else: 
        b="Castilla La Mancha"
    return b

def random_instrumentos():
    instrumentos = ["Guitarra", "Triangulo", "Bajo", "Organo", "Ocarina", "Saxo", "Violin", "Trompeta"]
    return ", ".join(random.sample(instrumentos, random.randint(1, 3)))

def random_grupo():
    return random.randint(1, NUM_GRUPOS)

def random_pais():
    return random.choice(Paises)

def random_fecha():
    inicio = datetime(1950, 1, 1)
    fin = datetime(2025, 12, 31)
    dias = (fin - inicio).days
    fecha_random = inicio + timedelta(days=random.randint(0, dias))
    return fecha_random #fecha_random.strftime("%Y-%m-%d")

def random_duracion():
    minutos = random.randint(2, 7)
    segundos = random.randint(0, 59)
    if (minutos==7):
        segundos=0
    return time(minutos, segundos)

def random_compositor():
    return "nombre"+str(random.randint(1, NUM_MUSICOS+1))

def random_disco():
    return random.randint(1, NUM_DISCOS)

def random_recinto(a):
    if a=="Madrid":
        b=random.randint(1, 5)
    elif a=="Barcelona": 
        b=random.randint(6, 8)
    elif a=="Valencia": 
        b=random.randint(9, 10)
    elif a=="Guadalajara": 
        b=random.randint(11, 13)
    elif a=="Toledo": 
        b=14
    else:
        b=15
    return "Recinto "+str(b)

def random_web(grupo):
    return "www."+grupo+".es"

def random_genero():
    return random.choice(GENEROS)

def random_precio():
    return round(random.uniform(20, 100), 2)

def random_localidad():
    return random.choice(Paises)

def random_concierto():
    return random.randint(1, NUM_CONCIERTOS+1)

def random_formato():
    return random.choice(["CD", "Vinilo", "Casette", "Digital"])

print("generando musicos")
with open("musicos.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Codigo_musico", "DNI", "Nombre", "Direccion", "Cod_postal", "Ciudad", "Provincia", "Telefono", "Intrumento", "Cod_grupo"])
    k=1
    contador=0
    q=random.randint(1,10)
    for i in range(1, NUM_MUSICOS + 1):
        dir=random_ciudad()              
        writer.writerow([i, random_dni(),"nombre "+str(i), random_pais(), random_cp(), dir, random_provincia(dir), random_telefono(), random_instrumentos(), k])
        contador=contador+1
        if(contador>=q):
            contador=0
            k+=1   
            if(NUM_MUSICOS-i>0):
                q=random.randint(1,min(10, NUM_MUSICOS-i))
            else:
                q=1     
         

print("generando canciones")
with open("canciones.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Cod_cancion", "Nombre", "Compositor", "Fecha_grabacion", "Duracion", "Cod_discos"])
    for i in range(1, NUM_DISCOS + 1):
        NUM_CANCIONES=random.randint(8, 16)
        for j in range(NUM_CANCIONES):
            disco= random.randint(1, 1+NUM_DISCOS)
            writer.writerow([i, "nombre "+str(i), random_compositor(), random_fecha(), random_duracion(), disco])

print("generando concierto")
conciertos = []
with open("concierto.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Cod_concierto", "fecha", "Pais", "Ciudad", "Recinto"])
    for i in range(1, NUM_CONCIERTOS + 1):
        ciudad=random_ciudad()
        writer.writerow([i, random_fecha(), random_pais(), ciudad, random_recinto(ciudad)])
        conciertos.append(i)  # guardar IDs para luego asociar

grupos = []
print("generando grupos")
with open("Grupos.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Cod_grupo", "Nombre de grupo", "Genero", "Pais", "Webb"])
    for i in range(1, NUM_GRUPOS + 1):
        nombre="nombre "+str(i)
        writer.writerow([i, nombre, random_genero(), random_pais(), random_web(nombre)])
        grupos.append(i)

rel = []        
for g in grupos:
    asig = random.sample(conciertos, min(10, NUM_CONCIERTOS))
    for c in asig:
        rel.append([g, c])

for c in conciertos:
    # Verificar si el concierto ya tiene grupo asignado
    if not any(r[1] == c for r in rel):
        g = random.choice(grupos)
        rel.append([g, c])

print("generar relacion")
with open("relacion_grupo_concierto.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Cod_grupo", "Cod_concierto"])
    for i in rel:
        writer.writerow(i)

print("generar entrada")
with open("entrada.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Cod_entrada", "Localidad", "Precio", "Usuario", "Concierto"])
    for i in range(1, NUM_ENTRADAS + 1):
        writer.writerow([i, random_localidad(), random_precio(),"usuario "+str(i), random_concierto()])

print("Generando discos")
with open("discos.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Cod_disco", "Titulo", "Fecha", "Genero", "Formato", "Cod_grupo"])
    for i in range(1, NUM_DISCOS + 1):
        writer.writerow([i, "Titulo "+str(i), random_fecha(), random_genero(), random_formato(), random_grupo()])
