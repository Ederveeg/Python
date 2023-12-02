#Este programa es para calcular gastos mensuales

#Preguntas sobre cuanto se gasto en los primeros tres meses del año
gasto_enero = int(input("Cuanto dinero gastaste el mes de enero? "))
gasto_feb = int(input("Cuanto dinero gastaste el mes de febrero? "))
gasto_marzo = int(input("Cuanto dinero gastaste el mes de marzo? "))

#Suma de las variables para el gasto total
gasto_total = gasto_enero + gasto_feb + gasto_marzo

#Aqui se calcula el gasto promedio
gasto_promedio = int(gasto_total/3)

#Prints sobre cada uno de los meses
print("Tus gastos de enero fueron", gasto_enero, "pesos")
print("Tus gastos de febrero fueron", gasto_feb, "pesos")
print("Tus gastos de marzo fueron", gasto_marzo, "pesos")

#Print de gasto total y promedio
print("En el primer trimestre del año gastaste", gasto_total, "pesos")
print("Tu gasto promedio es de", gasto_promedio,"pesos")