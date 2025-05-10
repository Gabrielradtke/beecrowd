hora_ini, hora_final = map(int, input().split())

if hora_ini < hora_final:
    duracao = hora_final - hora_ini
elif hora_ini >= hora_final:
    duracao = (24 - hora_ini) + hora_final
elif hora_ini == hora_final:
    duracao = 24

print(f'O JOGO DUROU {duracao} HORA(S)')
