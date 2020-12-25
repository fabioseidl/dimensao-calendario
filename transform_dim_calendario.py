import pandas as pd
    
def get_calendar(dt_start, dt_end):
    months = ["Unknown", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    week_day = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-Feira', 'Sexta-feira', 'Sábado', 'Domingo']
    dim_calendar = pd.DataFrame()
    dim_calendar["data"] = pd.date_range(start=dt_start, end=dt_end)
    dim_calendar["cod_data"] = dim_calendar.data.apply(lambda x: x.strftime("%Y") + x.strftime("%m") + x.strftime("%d"))
    dim_calendar["ano"] = dim_calendar.data.apply(lambda x: x.strftime("%Y"))
    dim_calendar["mes"] = dim_calendar.data.apply(lambda x: x.strftime("%m"))
    dim_calendar["dia"] = dim_calendar.data.apply(lambda x: x.strftime("%d"))
    dim_calendar["nome_mes"] = dim_calendar.mes.apply(lambda x: months[int(x)])
    dim_calendar["mes_ano"] = dim_calendar.data.apply(lambda x: x.strftime("%m-%Y"))
    dim_calendar["num_semana"] = dim_calendar.data.apply(lambda x: x.strftime("%U"))
    dim_calendar["dia_semana"] = dim_calendar.data.apply(lambda x: week_day[x.weekday()])
    dim_calendar["estacao"] = dim_calendar.data.apply(lambda x: get_season(x))
    return dim_calendar

def get_season(date):
    month_day = int(date.strftime("%m%d"))
    if (month_day >= 320 and month_day <= 620): return "Outono"
    if (month_day >= 621 and month_day <= 921): return "Inverno"
    if (month_day >= 922 and month_day <= 1220): return "Primavera"
    if (month_day >= 1221 or month_day <= 319): return "Verão"

def main():
    try:
        dim_calendario = get_calendar('01/01/2010', '31/12/2030')
        dim_calendario.to_csv("dim_calendario.csv", sep=';', encoding='utf-8', index=False)
        print("Transformação da dimensão calendário concluída com sucesso!!!")
    except Exception as e:
        print("Ocorreu uma falha na transformação da dimensão calendario. \n" + str(e))

if __name__ == '__main__':
    main()