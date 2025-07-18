Este script fue desarrollado como respuesta a un challenge técnico. Se encarga de procesar y validar información contenida en un archivo `estudios.csv` con datos sobre estudios médicos.

1. Lee el archivo `estudios.csv` usando `pandas`.
2. Limpia espacios en blanco en los campos de texto.
3. Convierte la columna `Fecha` al tipo de dato `datetime`.
4. Realiza validaciones:
   - Detecta edades inválidas (menores a 0 o mayores a 120).
   - Detecta registros con el campo `Estudio` vacío.
   - Verifica que el campo `ID_Estudio` no tenga duplicados.
   - Cuenta la cantidad de estudios con estado `"Fallido"`.
5. Genera un resumen con:
   - Cantidad de estudios por tipo (excluyendo vacíos).
   - Rango de fechas (fecha más antigua y más reciente).
6. Imprime un resumen de errores si los hay.  
   Si todo es válido, imprime: `"Todos los datos son válidos"`.
