import datetime

def generate_dates(year):
	# Inicializa uma data com o ano escolhido
	date = datetime.date(year, 1, 1)

	# Enquanto a data for menor que o ano atual, gera uma nova data
	# e adiciona um dia a ela
	while date.year < datetime.datetime.now().year:
		yield date.strftime("%d%m%Y")
		date += datetime.timedelta(days=1)


# Gera as datas a partir do ano 2000
for date in gerenerate_dates(2000):
	print(date)
