/*

Dado un string y un numero,repetir el string 
tantas veces como el numero indique.

Ejemplo:

repiteme("ramon", 2)   //Devuelve ramonramon

Como hacerlo:
-Crear una funcion que reciba los dos parametros
-Bucle hasta el numero
-Concatenar string

*/

// Funcion clasica
function repiteme(texto, numero_repeticiones){
    let resultado = "";

    for(let i = 0; i < numero_repeticiones; i++){
        resultado += texto;
    }

    return resultado;

}

console.log(repiteme("Ramon", 8));

//Funcion propotipo
String.prototype.repiteme = function repiteme(numero_repeticiones){
    let resultado = "";

    for(let i = 0; i < numero_repeticiones; i++){
        resultado += this;
    }

    return resultado;

}

console.log("Ramon Pascual web".repiteme(5))