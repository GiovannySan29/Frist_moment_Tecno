"""
Una institución educativa se encuentra en proceso de finalizar semestre y en proceso de admisión para el próximo semestre. La institución requiere un software que le permita solucionar estas dos problemáticas con las siguientes restricciones. 
Para finalización de semestre: 
Se desean subir las notas de los alumnos al sistema de los programas de Desarrollo de software y Telecomunicaciones, para ello, se le pide al docente el número de alumnos, nombre de cada alumno, programa académico, si es hombre, mujer, no binario, además, las 5 notas obtenidas durante el curso. El software calcula el promedio de las 5 notas. Al finalizar la ejecución debe mostrar cuántos hombres, mujeres y no bonarios hay en cada programa académico, el promedio de notas por cada programa y el listado de alumnos con el respectivo promedio de cada uno.
Para el proceso de admisión 
La institución requiere que se le muestre cuántos estudiantes en total se matricularon y el promedio de edad de los matriculados, además, requiere saber cuántos hombres y mujeres se matricularon.
El proceso de admisión termina hasta que el usuario decida que ya no se van a matricular más personas.
"""

def averageStudent():
    average = 0
    for j in range(1,5):
        average += int(input(f"Ingrese nota {j}: "))
    average = average / 5
    return average

numAlumnos = 0
students = []
countWomenSoftware = 0
countMenSoftware = 0
countNotBinarySoftware = 0
countWomenTelecomunications = 0
countMenTelecomunications = 0
countNotBinaryTelecomunications = 0
averageTelecomunications = 0
averageSoftware = 0
countStudents = 0
averageAge = 0
countWomen = 0
countMen = 0
average = 0
stopAdmission = 0
program = []
menu = input("¿Qué desea hacer? - admision(admi) - matrícula(matri): ")
if menu == "admi":
    numAlumnos = int(input("Ingrese número de alumnos: "))
    for i in range(numAlumnos):
        name = input("Ingrese nombre: ")
        # program = input("Ingrese los programas que quiere para estudiar: ")
        academicProgram = input("Ingrese programa académico -> s - software - t - telecomunicaciones ")
        if academicProgram == "s" or academicProgram == "S":
            genero = ["m", "h", "nb","M", "H", "NB"]
            sex = input("Ingrese sexo - m(mujer), h(hombre), nb(no binario): ")
            while sex not in genero:
                if sex == genero:
                    if sex == "m" or sex == "M":
                        countWomenSoftware+=1
                    elif sex == "h" or sex == "H":
                        countMenSoftware+=1
                    elif sex == "nb" or sex=="NB":
                        countNotBinarySoftware+=1
                else:
                    print("no valido: ")                             
                    sex = input("Ingrese sexo - m(mujer), h(hombre), nb(no binario): ")  
            average = averageStudent()
            students.append({"name": name, "average": average})
            averageSoftware+=average
        else:
            genero = ["m", "h", "nb","M", "H", "NB"]
            sex = input("Ingrese sexo - m(mujer), h(hombre), nb(no binario): ")
            while sex not in genero:
                if sex == genero:
                    if sex == "m" or sex == "M":
                        countWomenTelecomunications+=1
                    elif sex == "h" or sex == "H":
                        countMenTelecomunications+=1
                    elif sex == "nb" or sex=="NB":
                        countNotBinaryTelecomunications +=1
                else:
                    print("no valido: ")            
                    sex = input("Ingrese sexo - m(mujer), h(hombre), nb(no binario): ")  
            average = averageStudent()
            students.append({"name": name, "average": average})
            averageTelecomunications += average


            averageSoftware = averageSoftware/(countMenSoftware+countNotBinarySoftware+countWomenSoftware)
            averageTelecomunications = averageTelecomunications/(countMenTelecomunications+countNotBinaryTelecomunications+countWomenTelecomunications)
            print(f"Promedio Software: {averageSoftware}")
            print(f"Número de mujeres en Software: {countWomenSoftware}")
            print(f"Número de Hombre en Software: {countMenSoftware}")
            print(f"Número de no binarios en Software: {countNotBinarySoftware}")
            print(f"Promedio Telecomunicaciones: {averageTelecomunications}")
            print(f"Número de mujeres en Telecomunicaciones: {countWomenTelecomunications}")
            print(f"Número de Hombre en Telecomunicaciones: {countMenTelecomunications}")
            print(f"Número de no binarios en Telecomunicaciones: {countNotBinaryTelecomunications}")
                for i in range(students): # for i in range(len(students))
                   print(f"Nombre: {i['name']} - Nota final: {i['average']}")

else:
    while True:
        averageAge+=int(input("Ingrese edad: "))
        sex = input("Ingrese sexo: ")
        if sex == "m" or sex == "M":
            countWomen+=1
        elif sex == "h" or sex == "H":
            countMen+=1
        stopAdmission = input("si desea parar de matricular ingrese s, de lo contrario cualquier tecla para continuar: ")
        countStudents+=1
        if stopAdmission == "s" or stopAdmission == "S":
            break

    averageAge = averageAge/countStudents
    print(f"Número de estudiantes matriculados: {countStudents}")
    print(f"Promedio de edad de matriculados: {averageAge}")
    print(f"Número de mujeres matriculadas: {countWomen}")
    print(f"Número de hombre matriculados: {countMen}")
    
    
    