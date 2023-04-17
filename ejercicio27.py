def calcularDias(dias):
    anios = dias // 365
    dias_restantes = dias % 365
    meses = dias_restantes // 30
    dias_restantes = dias_restantes % 30

    # print(dias_restantes)
    return f"Equivale a {anios} años, {meses} meses y {dias_restantes} días."

print(calcularDias(9920))


# function calcularDias(dias){
#     let anios = Math.floor(dias/365);//Math.floor para redondear
#     let dias_restantes = (dias%365);
#     let meses = Math.floor(dias_restantes/30);//Math.floor para redondear
#     dias_restantes = dias_restantes%30;
    
#     //console.log(dias_restantes)
#     return `Equivale a ${anios} años, ${meses} meses  y ${dias_restantes} dias.`
# }

# console.log(calcularDias(9920));