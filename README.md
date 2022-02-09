## PROYECTO FINAL DE PYTHON DJANGO CODERHOUSE

En este proyecto se va aplicar todo lo aprendido en la utilización del framework de django, la idea es implementar un sitio web totalmente funcional con el modelo MVT, en medida de que valla agregando funcionalidades se ira actualizando este documento.

### PARTICIPANTES EN EL PROYECTO

* JUAN HUERTAS
* KAREN GERICKE
* LEANDRO GARCIA

## IMPLEMENTACIÓN DE FUNCIONALIDADES.

1. El directorio principal en donde esta instalado el proyecto es: localhost:8000/gestionventas o 127.0.0.1:8000/gestionventas; para un acceso mas sencillo y directo y al ser una unica aplicación se habilito la redireccion automatica pudiendo ingresar directamente al proyecto sin necesidad de digitar la url completa, solo con localhost:8000 0 127.0.0.1:8000

2. las herencias de las platillas html se realizaron a traves de un template padre que fue copiado totalmente y transferido a inicio.html, con lo cual todas las plantillas heredadas provienen de platilla padre "inicio.html" a la cual se puede acceder y observar asi su configuración.

3. las clases del modelo se encuentran dentro de la APP gestionventas del proyecto luxurycars archivo models.py y estan compuestas de la siguiente forma:

>> * class marcasvehiculo: esta clase del modelo fue creada para almacenar en la base de datos 4 atributos ("Marca, Serie, Año_fabricacion, Pais_fabricación") permite la asignación y registro de nuevas marcas de vehiculos adquiridas por luxurycars latam.

>> * class vendedore: esta clase del modelo fue creada para almacenar en la base de datos 4 atributos ("nombre_vendedor, apellido_vendedor, email_vendedor, sucursal") permite la asignación y registro de nuevos vendedores asignados dentro de luxurycars latam.

>> * class venta: esta clase del modelo fue creada para almacenar en la base de datos 4 atributos ("vehiculo_vendido, precio, garantia_tiempo, garantia_kilometros") permite la asignación y registro de las ventas realizadas de vehoculos en luxurycars latam.

4. para poder almacenar la información directamente en la base de datos del proyecto Luxurycars latam se han habilitado 3 formularios uno por cada clase expuestas en el inciso anterior para acceder a los formularios y su funcionalidad las urls son las siguientes:

>> * "formulario de la clase marcasvehiculo el cual permite ingresar nuevos registros de vehiculos asignados para la venta" = http://localhost:8000/gestionventas/formulario_marcas/

>> * "formulario de la clase vendedore el cual permite ingresar nuevos registros de vendedores y empleados asignados para las diferentes sucursales de luxurycars latam" = http://localhost:8000/gestionventas/formulario_vendedores/

>> * "formulario de la clase venta el cual permite ingresar nuevos registros de vehiculos vendidos y negocios concretados en luxurycars latam" = http://localhost:8000/gestionventas/formulario_ventas/

5. Se realizo un formulario de busqueda para consultar en la base de datos, si un registro de marca se encuentra o no en el modelo "marcavehiculo"; para acceder al formulario por favor ingresar a : http://localhost:8000/gestionventas/buscarmarca/ en esta ubicacion encontrara un campo de donde ingresar una marca de un vehiculo para realizar la comprobación si esta se encuentra o no dentro del modelo.

## MODIFICACIONES Y CONSIGNAS PROYECTO FINAL

1. Tal cual como se solicita se crea una seccion llamada nosotros que esta ubicada en http://localhost:8000/gestionventas/nosotros/ en esta seccion se encuentra información sobre el proyecto y sus creadores.