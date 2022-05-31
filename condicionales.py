from calendar import c


calificacion = input("Introduce tu califiacion de la AZ-900")
calificacion = int(calificacion)
if calificacion < 700 :
    print("Reprobado")
elif calificacion > 1000:
    print("Error")
else :
    print("Aprobado")

edad = input("Introduce tu edad")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Bienvenido al mamitas")
elif edad > 100 :
    print("Si vienes acompañado de tus abuelitos si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajero del tiempo")
else :
    print("No puedes llevarte esos cigarros")

#En python no hay switch