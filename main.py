import json
from datetime import datetime

# Utils
def get_date():
    return datetime.now()

def date_brazilian(date):
    date_brazilian = date.strftime("%d/%m/%Y")
    return date_brazilian

def clean_month(register):
    date_clean = register["date"]
    return date_clean[3:-5]

# Complex Functions
def register_time(path, months, min_time, sec_time):
    with open(path, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        # Date
    date_format = date_brazilian(get_date())
        #Work time
    total_work = (min_time * 60) + sec_time

        #Make register
    register = {
        "date": date_format,
        "time_sec": total_work
    }

        #Clean month to Verify
    month_format = clean_month(register)

        #Insert in JSON
    for number_month, name_month in months.items():
        if month_format == number_month:
            dados["logs"][name_month].append(register)
            break
    
    with open(path, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    return "Registro feito!!"

def total_work_month(path, months, month_select):

    with open(path, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    # Versão mais viavel para verificar registro
    logs = dados['logs'].get(month_select, [])
    if not logs:
        return f"Nenhum registro encontrado para {month_select}."

    #função já encaixada
    total_second_month = sum(item["time_sec"] for item in logs)

    horas, rest_segundos = divmod(total_second_month, 3600)
    minutos, segundos = divmod(rest_segundos, 60)

    return f"Total time {month_select}: {horas}h {minutos}m {segundos}s"

def best_time_month(path, months, month_select):
    if month_select not in months.values():
        return "Selecione um mês válido"

    with open(path, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    logs = dados['logs'].get(month_select, [])
    if not logs:
        return f"Nenhum registro encontrado para {month_select}."

    #Função Max + key
    max_log = max(logs, key= lambda value: value["time_sec"])
    best_seconds = max_log["time_sec"]

    horas, rest_segundos = divmod(best_seconds, 3600)
    minutos, segundos = divmod(rest_segundos, 60)

    return f"Best time of {month_select}: {horas}h {minutos}m {segundos}s ({max_log['date']})"


