# pip install beautifulsoup4
from bs4 import BeautifulSoup

import requests
import ast

import random
import time
import json

print("**********************************************************")
print("              W E L C O ME - RANDOM GENERATOR RESPONSE")
print("**********************************************************")
quantity_data = int(input("Cuantas respuestas deseas generar ?: "))
#OBTENER EL FORMULARIO
#'https://docs.google.com/forms/d/e/XXXXXXXXXXXXX/viewform'
#ENVIAR RESPUESTAS
#'https://docs.google.com/forms/d/e/XXXXXXXXXXXXX/formResponse'

#ENCUESTADO: CUALQUIER PERSONA - EDITOR RESTRINGIDO:
url = "Your url form"

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
        #print(html)
        # Obtener una etiqueta form
        formulario = soup.find('form')
        id_form = formulario.get('id')
        
        
    
        def safe_get(lst, index, default=None):
            """Retorna lst[index] si existe, sino default."""
            return lst[index] if len(lst) > index else default


        def parse_google_forms_question(data):
            replacements = {
                    "null": "None",
                    "true": "True",
                    "false": "False"
                }
            for old, new in replacements.items():
                data = data.replace(old, new)
            new_eval = ast.literal_eval(data)[0]

            # ==========================================
            #  CAMPOS PRINCIPALES
            # ==========================================
            question_id = safe_get(new_eval, 0)
            question_text = safe_get(new_eval, 1)
            question_metadatos = safe_get(new_eval, 2)
            question_type = safe_get(new_eval, 3)
            options_block = safe_get(new_eval, 4, [])

            # Campos adicionales (pueden no existir)
            extra_1 = safe_get(new_eval, 5)
            extra_2 = safe_get(new_eval, 6)
            extra_3 = safe_get(new_eval, 7)
            extra_4 = safe_get(new_eval, 8)
            extra_5 = safe_get(new_eval, 9)
            extra_6 = safe_get(new_eval, 10)
            extra_7 = safe_get(new_eval, 11)

            internal_labels = safe_get(new_eval, 12)      # [None, "Edad"] o None


            # ==========================================
            #  BLOQUE DE OPCIONES
            # ==========================================
            block = safe_get(options_block, 0, [])

            internal_group_id     = safe_get(block, 0)
            option_list           = safe_get(block, 1, [])
            allow_custom_answer   = safe_get(block, 2)

            flag_1 = safe_get(block, 3)
            flag_2 = safe_get(block, 4)
            flag_3 = safe_get(block, 5)
            flag_4 = safe_get(block, 6)
            flag_5 = safe_get(block, 7)
            flag_6 = safe_get(block, 8)
            flag_7 = safe_get(block, 9)
            flag_8 = safe_get(block, 10)

            validations = safe_get(block, 11, [])


            # ==========================================
            #  OPCIONES
            # ==========================================
            options_response = ""
            for opt in option_list:
                text = safe_get(opt, 0, "<empty>")
                selected = safe_get(opt, -1, False)
                state = "Not personalized" if not selected else "Yes personalized"
                options_response += f"\n\t{state} > {text}"


            # ==========================================
            #  IMPRIMIR TODO
            # ==========================================
            # print('*' * 80)
            data_print=(f"""
        --- INFORMACIÓN PRINCIPAL ---
        ID automatic send     : {question_id}
        Question              : {question_text}
        Metadatos             : {question_metadatos}
        Type                  : {question_type}

        --- BLOQUE DE OPCIONES ---
        Internal Group ID     : {internal_group_id}
        Allow Custom ("Otros"): {allow_custom_answer}

        --- FLAGS DEL BLOQUE ---
        Flag 1                : {flag_1}
        Flag 2                : {flag_2}
        Flag 3                : {flag_3}
        Flag 4                : {flag_4}
        Flag 5                : {flag_5}
        Flag 6                : {flag_6}
        Flag 7                : {flag_7}
        Flag 8                : {flag_8}
        Validations           : {validations}

        --- OPCIONES ---
        {options_response}
        
        ****************** RANDOM RESPONSE ******************
        {random.choice(option_list)[0]}
        --- CAMPOS EXTERNOS ---
        Extra 1               : {extra_1}
        Extra 2               : {extra_2}
        Extra 3               : {extra_3}
        Extra 4               : {extra_4}
        Extra 5               : {extra_5}
        Extra 6               : {extra_6}
        Extra 7               : {extra_7}

        Internal labels       : {internal_labels}

        """)
            # print('*' * 80)
            # print(option_list)
            if '' == option_list[-1][0]:
                option_list.pop()
            # print(f'"entry.{question_id}" : "{random.choice(option_list)[0]}"')
            return question_id,random.choice(option_list)[0]
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
            # except Exception as e:
            #     print(f'Error al procesar la estructura: {e}')
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
                # print(questions_items[0])
                print("Number of questions:",len(questions_items))
                # ITERA SOBRE LOS DIVS DE LAS PREGUNTAS Y ACCEDE A LOS PARAMETROS
                data_send = []
                for message_send in range(quantity_data):
                    response_random = ''
                    comma = ''
                    for questions in questions_items:
                        # questions ya es un Tag de BeautifulSoup, no necesitas volver a parsear
                        hidden_inputs = questions.find_all("input", {"name": True, "type": "hidden"})
                        
                        for input_tag in hidden_inputs:
                            name = input_tag.get("name")
                            if name.startswith("entry.") and "_sentinel" in name:
                                entry_id = name.split("_")[0]  # Ej: 'entry.1628231781'
                                #print(entry_id)
                                #entry_ids.append(entry_id)

                        item_q = questions.find_all('div',recursive=False)
                        data = item_q[0].get('data-params')
                        data =  data.replace("%.@.","")
                        data = f'[{data}'
                        response = parse_google_forms_question(data)
                        response_random += f'{comma}"{entry_id}" : "{response[1]}"' 
                        # print(response_random)
                        comma = ',\n'

                    json_data_send = '{ replace }'
                    form_data = json.loads(json_data_send.replace("replace",response_random))
                    # print(form_data)
                    response = requests.post(url_response, data=form_data)
                    data_send.append(form_data)

                    print(f"> > > Response form google number {message_send+1} STATUS:{response.status_code} -  add JSON file")
                    time.sleep(0.5)  # esperar 0.5 segundos entre respuestas

                # data_info_question = questions_items[0].find_all('div',recursive=False)
                # print(data_info_question[0].get('data-params'))
                # for i in questions_items:
                # Guardar el archivo JSON sin escape Unicode
                with open('Response_forms_migajero.json', 'w', encoding='utf-8') as file:
                    json.dump(form_data, file, indent=4, ensure_ascii=False)
                
    else:
        print(f"Error al acceder: {response.status_code}")
else:
    print("This url in not a google Form")