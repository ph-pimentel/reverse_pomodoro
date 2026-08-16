import json
from datetime import datetime

def main():
    months = {
                '01': 'Janeiro',
                '02': 'Fevereiro',
                '03': 'Março',
                '04': 'Abril', 
                '05': 'Maio',
                '06': 'Junho',
                '07': 'Julho',
                '08': 'Agosto',
                '09': 'Setembro',
                '10': 'Outubro',
                '11': 'Novembro',
                '12': 'Dezembro'
    }
    path = "projects/reverse_pomodoro/reverse_pomo.json"

    print(f"""Bem-vindo! Selecione a opção desejada:""")
    user_choise = int(input(f"""
Registrar Tempo = 1
Visualizar Tempo Total Mês Atual = 2
Best Time of Mês = 3
Your Choice ->  """))
    if user_choise == 1:
        register_time(path, months)
    elif user_choise == 2:
        total_work_month(path, months)
    elif user_choise == 3:
        best_time_month(path, months)
    else:
        print("Selecione uma opção válida!")

def register_time(path, months):
    while True:
        with open(path, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        # Date
        date_format = date_brazilian(get_date())
        #Work time
        minutos_work = int(input('Quantos minutos de trabalho?'))
        segundos_work = int(input('Quantos segundos de trabalho?'))
        total_work = (minutos_work * 60) + segundos_work

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
    
        with open(path, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

        print("Registro feito!!")
        break

def total_work_month(path, months):
    while True:
        with open(path, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        
        month_select = input("Selecione um mês \n->")

        for number_month, name_month in months.items():
            if month_select == name_month:
                total_second_month = 0
                print(month_select)
                for i in range(len(dados['logs'][month_select])):

                    all_dates_times = dados['logs'][month_select][i].values()
                    date, time = all_dates_times
                    total_second_month += time

                horas, rest_segundos = divmod(total_second_month, 3600)
                minutos, segundos = divmod(rest_segundos, 60)

                total_work = f"Total time {month_select}: {horas}h {minutos}m {segundos}s"
                break
        else:
            print("Selecione um mês válido")
            break
        print(total_work)
        break

def best_time_month(path, months):
    while True:
        with open(path, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        
        month_select = input("Selecione um mês \n->")

        for number_month, name_month in months.items():
            if month_select == name_month:
                last_time = 0
                for i in range(len(dados['logs'][month_select])):
                        data_per = dados['logs'][month_select][i].values()
                        data, time = data_per
                        if last_time < time:
                            last_time = time

                horas, rest_segundos = divmod(last_time, 3600)
                minutos, segundos = divmod(rest_segundos, 60)

                best_time = f"Best time of {month_select}: {horas}h {minutos}m {segundos}s"
                break
        else:
            print("Selecione um mês válido")
            break
        print(best_time)
        break
            

# Utils
def get_date():
    return datetime.now()

def date_brazilian(date):
    date_brazilian = date.strftime("%d/%m/%Y")
    return date_brazilian

def clean_month(register):
    date, temp = register.items()
    date_clean = date[1]
    month = date_clean[3:-5]
    return month


if __name__ == '__main__':
    main()