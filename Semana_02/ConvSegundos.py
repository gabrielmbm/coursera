segundosStr = input("Digite o número de segundos para conversão: ")
totalSeg = int(segundosStr)

dias = totalSeg // 86400
segRestDia = totalSeg % 86400
horas = segRestDia // 3600
segRestHoras = segRestDia % 3600
minutos = segRestHoras // 60
segRestFinal = segRestHoras % 60

print(dias,"dia",horas,"hora,",minutos,"minuto e",segRestFinal,"segundo.")

# if horas > 1:
#     print(horas,"horas,",minutos,"minutos e",segRestFinal,"segundos.")
# else :
#     print(horas,"hora,",minutos,"minutos e",segRestFinal,"segundos.")
 



# segundosStr = input("Digite o número de segundos para conversão: ")
# totalSeg = int(segundosStr)

# horas = totalSeg // 3600
# segRest = totalSeg % 3600
# minutos = segRest // 60
# segRestFinal = segRest % 60
# if horas > 1:
#     print(horas,"horas,",minutos,"minutos e",segRestFinal,"segundos.")
# else :
#     print(horas,"hora,",minutos,"minutos e",segRestFinal,"segundos.")
 