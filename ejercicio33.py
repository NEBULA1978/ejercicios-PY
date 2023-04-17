import datetime
import time

class Relog:
    def __init__(self):
        now = datetime.datetime.now()
        self.horas = now.hour
        self.minutos = now.minute
        self.segundos = now.second
    
    def actualizar(self, segundos):
        self.segundos += segundos
        
        # actualiza segundos
        if self.segundos >= 60:
            self.minutos += 1
            self.segundos = 0
        
        # actualiza minutos
        if self.minutos >= 60:
            self.horas += 1
            self.minutos = 0
        
        # actualiza horas
        if self.horas >= 24:
            self.horas = 0
    
    def mostrar(self):
        self.actualizar(1)
        print(f"{self.horas}:{self.minutos}:{self.segundos}")
    
    def encender(self):
        while True:
            self.mostrar()
            time.sleep(1)

mi_relog = Relog()
mi_relog.encender()


# /*

# COmo hacerlo:

# -Crear una clase
# -Inicializar propiedades con hora actual
# -Metodo con setInterval
# Metodo para mostrar la hora
# -Metodo para sumar segundos a la hora
# -Metodo para sumar segundos a la hora y actualizar hora minutos y segundos.


# */
# class Relog {

#     constructor(){
#         this.fecha = new Date();
#         this.horas = this.fecha.getHours();
#         this.minutos = this.fecha.getMinutes();
#         this.segundos = this.fecha.getSeconds();
#     }

#     actualizar(segundos){
#         this.segundos += segundos;

#         //actualiar segundos
#         if(this.segundos >= 60){
#             this.minutos++;
#             this.segundos = 0;
#         }
        
#         //actualiar minutos
#          if(this.segundos >= 60){
#             this.horas++;
#             this.minutos = 0;
#         }
        
#         //actualiar horas
#          if(this.horas >= 24){
#             this.horas = 0;
#         }
#     }

#     mostrar(){
#         this.actualizar(1);
#         console.log(`${this.horas}:${this.minutos}:${this.segundos}`);
#     }

#     encender(){
#         setInterval(() => {
#             this.mostrar();
#         }, 1000);
#     }

# }

# let mi_relog = new Relog();
# mi_relog.encender();


# function relogRapido(){
#     setInterval(()=> {
#         const fecha = new Date();
#         const horas = fecha.getHours();
#         const minutos = fecha.getMinutes();
#         const segundos = fecha.getSeconds();


#         console.log(`${horas}:${minutos}:${segundos}`);
#     }, 1000);
# }

# //relogRapido();