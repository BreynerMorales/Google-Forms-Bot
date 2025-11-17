import requests
import random
import time
import json
# URL de envío del formulario (nota: termina en "formResponse")
# 'https://docs.google.com/forms/d/e/XXXXXXXXXXXXX/formResponse'
url = "https://docs.google.com/forms/d/e/1FAIpQLSdwsdEf3MequBh-THTY3e2hg5KxmZRiDwCXoYR0On5kHQtWGQ/formResponse"
data_promedio = []
data_horas = []

def get_random_edad():
    """Edades entre 17-24"""
    return random.choice([17,18,19,20,21,22,23,24])
def get_random_promedio():
    """Promedio del ciclo pasado"""
    # ¿Cuál es tu promedio ponderado del ciclo pasado? (Use punto decimal en caso sea necesario) 
    # En caso no tenga un promedio, coloque el valor de "0"
    prom = round(random.uniform(11, 16), 2)
    while True:
        if prom not in data_promedio:
            data_promedio.append(prom)
            break
        else:
            prom = round(random.uniform(11, 16), 2)

    return prom
def get_cursos_retirados():
    #¿Cuántos cursos has llegado a desaprobar o retirarte desde que empezaste la universidad?
    return random.choice(["0","1","2","3","4 o más"])
def get_random_horas():
    # ¿Cuántas horas usas el celular al día? 
    # (Si quiere decir 1 hora y 30 minutos es 1.3)
    # Ejemplos: 4,  4.3,  3.45,  5.40, etc

    hour = round(random.uniform(1, 5), 2)
    while True:
        if hour not in data_horas:
            data_horas.append(hour)
            break
        else:
            hour = round(random.uniform(1, 5), 2)
    return hour
def get_random_type_content():
    # ¿Cuál es el tipo de contenido que más consumes en el celular?
    return random.choice(["Redes Sociales","Educativo","Entretenimiento","Compras en línea","Trabajo"])
def get_random_social_media():
    # ¿Cuál es la red social que más utilizas actualmente?
    return random.choice(["Instagram","Tik Tok","WhatsApp","Facebook","X( ex Twitter)","Youtube"])
def get_random_use_social_media():
    def numero_valido():
        while True:
            num = random.randint(10, 350)
            if num % 10 not in [1,2,3,4,6,7,8,9]:
                return num
    minutes_social_media_use = numero_valido()
    return minutes_social_media_use
def get_random_uso_redes():
    # ¿Consideras que el uso de redes sociales reduce el tiempo efectivo que dedicas al estudio?
    return random.choice(["Si","No"])
def get_hour_quantity():
    # ¿Cuántas horas dedicas al estudio en una semana (de lunes a domingo)?
    # (Respuesta numérica. Ejemplo: 5, 10, 15, etc.)
    def numero_valido():
        while True:
            num = random.randint(5, 35)
            if num % 10 not in [1,9]:
                return num
    hour_studio = numero_valido()
    return hour_studio
def get_random_procast_option():
    #  ¿El uso de redes sociales te lleva a procrastinar tus estudios?)
    return random.choice(["Nunca","Rara vez","A veces","Frecuentemente","Siempre"])
def get_random_frencuency_movil():
    # ¿Con qué frecuencia usas tu dispositivo móvil durante clases?
    return random.choice(["Nunca","Rara vez","A veces","Frecuentemente","Siempre"])
def get_random_frecuency_no_education():
    # ¿Qué tan frecuente usas el celular durante las clases con fines no educativos?
    return random.choice(["Nunca","Rara vez","A veces","Casi siempre","Siempre"])
def get_quantity_notification():
    # ¿Cuántas veces, aproximadamente, te interrumpe el celular por notificaciones durante una hora de estudio?
    # (Escribe un número entero. Ejemplo: 0, 2, 5, etc.)
    return random.randint(0, 10)
def get_random_state_movil():
    # ¿En qué estado sueles mantener tu celular mientras estudias?
    return random.choice(["Modo Sonido","Modo Vibración","Modo Silencio","Apagado"])
def get_random_time_sleep():
    # ¿Cuántas horas diarias llegas a dormir normalmente?
    return random.choice(["4","5","6","7","8","9","más de 9"])
def get_random_before_sleep():
    # ¿Usas el celular antes de dormir?
    return random.choice(["Sí","No","A veces"])
def get_random_hour_sleep():
    # ¿Cuál es el grado de influencia del uso del teléfono celular en tus horas de sueño?
    return random.choice(["Nada","Poco","Algo","Regular","Bastante"])
def get_random_exercise():
    # ¿Cuántas horas dedicas al ejercicio físico a la semana? (Ej. deportes, correr, gimnasio, caminar, etc.)
    return random.choice([random.randint(1, 25),round(random.uniform(1, 25), 1)])
def get_random_activity_extra():
    # ¿En cuántas actividades extracurriculares participas actualmente por semana? (Ej. deportes, talleres, voluntariado, comités estudiantiles, etc.)
    actividad_extra = random.randint(0, 5)
    return actividad_extra
def get_random_hour_activity_extra():
    # ¿Cuantas horas semanales dedica a actividades extracurriculares? (Sino participa en actividades extracurriculares poner 0)
    return random.randint(1, 8)
def get_random_hour_Free():
    # ¿Cuantas horas totales libres tiene a la semana? (Descontando clases, sueño y responsabilidades fijas)
    return random.randint(3, 20)
def get_random_academic_App():
    # ¿Usas aplicaciones de organización académica (como Google Calendar, Notion, Trello, etc.) en tu celular para gestionar tus tareas y horarios de estudio?
    return random.choice(["Sí","No"])
def get_random_aprendizaje():
    # ¿Qué estrategia de aprendizaje virtual usas frecuentemente?
    return random.choice(["Auditiva","Audiovisual","Lectura digital","Inteligencia Artificial"])
def get_random_consideras():
    # ¿Consideras que el uso de aplicaciones académicas mejora tu rendimiento académico?
    return random.choice(["No","Un poco","Mas o menos","Bastante"])
def get_random_type_connection():
    # ¿Qué tipo de conexión a internet usas con mayor frecuencia?
    return random.choice(["Wifi","Datos moviles","Ethernet"])
def get_random_quantity_gb():
    # ¿Cuántos datos móviles consumes al mes? (en GB y dos decimales Ej 19.85, 5.67) 
    return random.randint(1, 150)
def get_random_use_eat():
    # ¿Con qué frecuencia usas tu dispositivo móvil mientras comes?
    return random.choice(["Nunca","Rara vez","A veces","Frecuentemente","Siempre"])
data = []
# Enviar n respuestas
for number in range(2):
    actividad_extra = get_random_activity_extra()
    if actividad_extra == 0:
        horas_extra =  0
    else:
        horas_extra = get_random_hour_activity_extra()
    form_data = {
        "entry.2096314078"  : "Grupo 6", #Grupo
        "entry.316285319"   : get_random_edad(), #Edad
        "entry.1190851348"  : get_random_promedio(),
        "entry.1633308658"  : get_cursos_retirados(),
        "entry.1049724336"  : get_random_horas(),
        "entry.420604432"   : get_random_type_content(),
        "entry.1093720040"  : get_random_social_media(),
        "entry.2017033610"  : get_random_use_social_media(),
        "entry.1088651984"  : get_random_uso_redes(),
        "entry.756147250"   : get_hour_quantity(),
        "entry.1061230157"  : get_random_procast_option(),
        "entry.2106205244"  : get_random_frencuency_movil(),
        "entry.1979712278"  : get_random_frecuency_no_education(),
        "entry.2017851752"  : get_quantity_notification(),
        "entry.1332619897"  : get_random_state_movil(),
        "entry.2027581868"  : get_random_time_sleep(),
        "entry.2028635836"  : get_random_before_sleep(),
        "entry.1752862824"  : get_random_hour_sleep(),
        "entry.443857224"   : get_random_exercise(),
        "entry.1806257970"  : actividad_extra,
        "entry.1522315096"  : horas_extra,
        "entry.1892815086"  : get_random_hour_Free(),
        "entry.925737578"   : get_random_academic_App(),
        "entry.467285403"   : get_random_aprendizaje(),
        "entry.1898105354"  : get_random_consideras(),
        "entry.1146181940"  : get_random_type_connection(),
        "entry.1333387492"  : get_random_quantity_gb(),
        "entry.1093392535"  : get_random_use_eat()
    }
    response = requests.post(url, data=form_data)
    data.append(form_data)
    print(f"> > > Response form google number {number+1} STATUS:{response.status_code} -  add JSON file")
    
    time.sleep(0.5)  # esperar 0.5 segundos entre respuestas

# Guardar el archivo JSON sin escape Unicode
with open('Response_forms.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)