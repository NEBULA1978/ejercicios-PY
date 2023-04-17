def tabla_multiplicar(numero):
    resultado = f"# Tabla del {numero} #\n"

    for i in range(11):
        multiplicacion = i * numero
        resultado += f"{i} x {numero} = {multiplicacion}\n"

    return resultado

print(tabla_multiplicar(5))

# /*
# BIEN
# Advertyencias:

# PRACTICAR Y RAZONAR

# Hacer tabla multiplicar

# */ 

# function tablaMultiplicar(numero){
#     //let resultado = "# Tabla del "+numero+" #";
#     let resultado = `# Tbla del ${numero} # \n`;// con \n salto linea

#     for(let i = 0; i <= 10; i++){
#         let multiplicacion = (i*numero);

#         //console.log(multiplicacion)
#         //concadeno resultado para que se avea bien
#         resultado += `${i} x ${numero} = ${multiplicacion} \n`
#     }
#     return resultado;

# }

# console.log(tablaMultiplicar(5))