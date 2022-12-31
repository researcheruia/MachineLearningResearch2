"""Este paquete, cuando se ejecuta, descarga datos de fármacos de https://go.drugbank.com y
de https://reference.medscape.com. La manera correcta de usar este paquete NO es importandolo
dentro de otro programa, sino que debe ejecutarse en el 'command prompt'. El paquete ya está
listo para descargar los datos requeridos, de modo que no se le deben introducir parámetros."""
# TODO Mejorar el nivel de abstracción del paquete, de momento sólo trabaja con los https://go.drugbank.com y
#  https://reference.medscape.com. Además, se requiere optimizar el código para que se ejecute de manera más eficiente

from Soups import executing


if __name__ == "__main__":
    executing()
