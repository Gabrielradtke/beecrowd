# Lê o dia de início e extrai o número
dia_inicio = int(input().split()[1])

# Lê a hora de início e separa em horas, minutos e segundos
hora_inicio = list(map(int, input().split(" : ")))

# Lê o dia de fim e extrai o número
dia_fim = int(input().split()[1])

# Lê a hora de fim e separa em horas, minutos e segundos
hora_fim = list(map(int, input().split(" : ")))

# Converte tudo para segundos (dia * 86400 + hora * 3600 + minuto * 60 + segundos)
segundos_inicio = dia_inicio * 86400 + hora_inicio[0] * 3600 + hora_inicio[1] * 60 + hora_inicio[2]
segundos_fim = dia_fim * 86400 + hora_fim[0] * 3600 + hora_fim[1] * 60 + hora_fim[2]

# Diferença total em segundos
duracao = segundos_fim - segundos_inicio

# Converte de volta para dias, horas, minutos e segundos
dias = duracao // 86400
duracao %= 86400
horas = duracao // 3600
duracao %= 3600
minutos = duracao // 60
segundos = duracao % 60

# Imprime o resultado
print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
