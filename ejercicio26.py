def fibonacci(numero):
    serie = [0, 1]

    for i in range(2, numero+1):
        serie.append(serie[i-1] + serie[i-2])

    return [serie, serie[numero]]

print("Serie completa: ", fibonacci(10)[0])
print("Serie fib: ", fibonacci(10)[1])


# function fibonacci(numero){
#     let serie =[0, 1];

#     for(let i =2; i<= numero; i++){
#         //console.log(i);
#         serie.push(serie[i -1] +serie[i - 2]);
#     }

#     //console.log(serie);
#     return [serie, serie[numero]];
# }

# console.log("Serie completa: ",fibonacci(10)[0]);
# console.log("Serie fib: ",fibonacci(10)[1]);