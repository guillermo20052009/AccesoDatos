class ManejarArchivo:
    def leer_archivo(self, rutaArchivo, mode="r"):
        try:
            with open (rutaArchivo, mode) as f:
                return f.read()
        except Exception as e:
            print(f"Error leyendo el archivo: {e}")
    def escribirFichero(self, rutaArchivo, contenido,mode="w"):
        try:
            with open(rutaArchivo, mode) as f:
                f.write(contenido)
        except Exception as e:
            print(f"Error escribiendo en el archivo: {e}")

manejarArchivo = ManejarArchivo()
manejarArchivo.escribirFichero("77865330A","05/01/2005\n")
print(manejarArchivo.leer_archivo("77865330A"))
