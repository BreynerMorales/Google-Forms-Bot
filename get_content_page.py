# pip install beautifulsoup4
from bs4 import BeautifulSoup

import requests
import ast
#OBTENER EL FORMULARIO
#'https://docs.google.com/forms/d/e/XXXXXXXXXXXXX/viewform'
#ENVIAR RESPUESTAS
#'https://docs.google.com/forms/d/e/XXXXXXXXXXXXX/formResponse'

#ENCUESTADO: CUALQUIER PERSONA - EDITOR RESTRINGIDO:
url = "https://docs.google.com/forms/d/e/1FAIpQLScIIl36aUGp47RXc7f1GGecqiftLZkGS2m7Xd57D1UFH4ZC3g/viewform?usp=header"

url_viewform = ""
url_response = ""

if "https://docs.google.com/forms/d/e/" in url:
    if "?usp=header" in url:
        url = url.replace("?usp=header","")
    unique_code = url.split("/")[6]
    print("Unique code of form:",unique_code)
    url_viewform = f'https://docs.google.com/forms/d/e/{unique_code}/viewform'
    url_response = f'https://docs.google.com/forms/d/e/{unique_code}/formResponse'

    response = requests.get(url_viewform)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        print(html)
        # Obtener una etiqueta form
        formulario = soup.find('form')
        id_form = formulario.get('id')
        
        def parse_google_forms_question(data):
            try:
                replacements = {
                    "null": "None",
                    "true": "True",
                    "false": "False"
                }
                for old, new in replacements.items():
                    data = data.replace(old, new)
                print(ast.literal_eval(data)[0])
                question_id = data[0]
                question_text = data[1]
                # question_type = data[3]

                # # Extraer opciones
                # options_raw = data[4][0][1]
                # options = [opt[0] for opt in options_raw]

                # # Imprimir en formato tabulado
                # print('-' * 40)
                # print(f'ID de pregunta:       {question_id}')
                # print(f'Texto de la pregunta: {question_text}')
                # print(f'Tipo de pregunta:     {question_type} ({"Opción múltiple" if question_type == 2 else "Otro"})')
                # print('-' * 40)
                # print('Opciones disponibles:')
                # for idx, opt in enumerate(options, 1):
                #     print(f'  {idx}. {opt}')
                # print('-' * 40)
                # print(f'ID para envío automático: entry.{question_id}')
            except Exception as e:
                print(f'Error al procesar la estructura: {e}')
        #OBTIENE TODOS LOS DIVS DEL FORMULARIO
        print("Id form:",id_form)
        questions = formulario.find_all('div',recursive=False)
        for i in questions:
            if i.get('class') != None: 
                print(i.get('class')) #['RH5hzf', 'RLS9Fe']
                content_questions = i.find_all('div',recursive=False)
                class_content = content_questions[0].get('class') #lrKTG
                divs_main_form = content_questions[0].find_all('div',recursive=False)
                print(len(divs_main_form)) 
                structure = {
                    "header": divs_main_form[0],
                    "body": divs_main_form[1],
                    "footer": divs_main_form[2]
                }
                #DIVS CON LAS PREGUNTAS DEL FORMULARIO
                questions_items = structure["body"].find_all('div',recursive=False)
                print("Number of questions:",len(questions_items))
                # ITERA SOBRE LOS DIVS DE LAS PREGUNTAS Y ACCEDE A LOS PARAMETROS
                for questions in questions_items:
                    item_q = questions.find_all('div',recursive=False)
                    data = item_q[0].get('data-params')
                    data =  data.replace("%.@.","")
                    data = f'[{data}'
                    print("----------------------------------------------------------------")
                    parse_google_forms_question(data)
                    print("----------------------------------------------------------------")
                # data_info_question = questions_items[0].find_all('div',recursive=False)
                # print(data_info_question[0].get('data-params'))
                # for i in questions_items:
                
    else:
        print(f"Error al acceder: {response.status_code}")
else:
    print("This url in not a google Form")