segundosStr = input("Digite o número de segundos para conversão: ")
totalSeg = int(segundosStr)

dias = totalSeg // 86400
segRestDia = totalSeg % 86400
horas = segRestDia // 3600
segRestHoras = segRestDia % 3600
minutos = segRestHoras // 60
segRestFinal = segRestHoras % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segRestFinal,"segundos.")