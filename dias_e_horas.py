# Alexsey

#recebe dia
dias = int(input("Dias:"))
#recebe hora
horas = int(input("Horas:"))
#recebe minutos
minutos = int(input("Minutos:"))
#recebe segundos
segundos = int(input("Segundos:"))
# Um dia tem 24 horas, logo 24 * 3600 segundos
# Uma hora tem 3600 (60 * 60) segundos50
# Um minuto tem 60 segundos


total_em_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print("Convertido em segundos é igual a %10d segundos." % total_em_segundos)

#############################

# Vanessa
dias = int(input("dias:"))
horas = int(input("horas:"))
minutos = int(input("minutos:"))
segundos = int(input("segundos:"))
sd=dias*86400
sh=horas*3600
sm=minutos*60
st=segundos+sd+sh+sm
print(st)