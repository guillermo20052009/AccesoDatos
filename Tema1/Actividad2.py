class ManejarArchivo:
    def leer_archivo(self, rutaArchivo, mode="r"):
        try:
            
            #La estructura open as hace que nos despreocupemos de cerrar el archivo
            with open (rutaArchivo, mode) as f:
                
            # f.read lee el archivo
                return f.read() 
        except Exception as e:
            print(f"Error leyendo el archivo: {e}")

    # El parametro mode nos indica como vamos a abrir el archivo la w significa escritura
    def escribirFichero(self, rutaArchivo, contenido,mode="w"): 
        try:

            #Aqui usamos el mode para abrir el archivo
            with open(rutaArchivo, mode) as f:

                #f.write escribe en el archivo
                f.write(contenido)
        except Exception as e:
            print(f"Error escribiendo en el archivo: {e}")

#Instanciamos un objeto de la clase, escribimos en el fichero y luego lo leemos
manejarArchivo = ManejarArchivo()
manejarArchivo.escribirFichero("77865330A","05/01/2005\n")
print(manejarArchivo.leer_archivo("77865330A"))
