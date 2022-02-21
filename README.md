## PROYECTO FINAL DE PYTHON DJANGO CODERHOUSE

En este proyecto se va aplicar todo lo aprendido en la utilización del framework de django, la idea es implementar un sitio web totalmente funcional con el modelo MVT, en medida de que valla agregando funcionalidades se ira actualizando este documento.

### PARTICIPANTES EN EL PROYECTO

* **JUAN HUERTAS**

### URL DE VIDEO EXPLICATORIO DEL PROYECTO

        https://youtu.be/sxxAipU20VY

## IMPLEMENTACIÓN DE FUNCIONALIDADES.

1. El directorio principal en donde esta instalado el proyecto es: localhost:8000/gestionventas o 127.0.0.1:8000/gestionventas; para un acceso mas sencillo y directo y al ser una unica aplicación se habilito la redireccion automatica pudiendo ingresar directamente al proyecto sin necesidad de digitar la url completa, solo con http://localhost:8000/ o http://127.0.0.1:8000

2. las herencias de las platillas html se realizaron a traves de un template padre que fue copiado totalmente y transferido a inicio.html, con lo cual todas las plantillas heredadas provienen de platilla padre "inicio.html" a la cual se puede acceder y observar asi su configuración.

3. las clases del modelo se encuentran dentro de la APP gestionventas del proyecto luxurycars archivo models.py y estan compuestas de la siguiente forma:

>> * class marcasvehiculo: esta clase del modelo fue creada para almacenar en la base de datos 4 atributos ("Marca, Serie, Año_fabricacion, Pais_fabricación") permite la asignación y registro de nuevas marcas de vehiculos adquiridas por luxurycars latam.

>> * class vendedore: esta clase del modelo fue creada para almacenar en la base de datos 4 atributos ("nombre_vendedor, apellido_vendedor, email_vendedor, sucursal") permite la asignación y registro de nuevos vendedores asignados dentro de luxurycars latam.

>> * class venta: esta clase del modelo fue creada para almacenar en la base de datos 4 atributos ("vehiculo_vendido, precio, garantia_tiempo, garantia_kilometros") permite la asignación y registro de las ventas realizadas de vehoculos en luxurycars latam.

>> * class avatar: esta clase del modelo fue creada para almacenar en la base de datos 2 atributos("user", "imagen") permite la asignación y registro de un avatar de activación a los usuarios registrados en Luxurycars Latam.

4. la pagina web cuenta con acceso libre sin login a 3 secciones (pagina de inicio, nosotros, marcas) 

## MODIFICACIONES Y CONSIGNAS PROYECTO FINAL

5. Tal cual como se solicita se crea una seccion llamada nosotros que esta ubicada en http://localhost:8000/gestionventas/nosotros/ en esta seccion se encuentra información sobre el proyecto y sus creadores, de igual forma una seccion llamada marcas que tiene acceso a algunos de los productos de luxurycars ubicada en http://localhost:8000/gestionventas/marcas/ 

6. Se solicita realizar un CRUD completo en un modelo que tenga la capacidad de (Crear, Leer, Modificar, Borrar nuevos registros), en este caso decidi crear el crud bajo el modelo de clase Vendedore la cual como lo explique en los parrafos anteriores, nos permite agregar, listar y ver todos los registros de empleados de luxurycars, para ingresar debemos acceder a http://localhost:8000/gestionventas/listaVendedores como medida de seguridad se puede acceder unicamente estando logeado.

7. Se agrego un sistema de autentificación o login robusto para acceder de forma segura a secciones privadas en la pagina web de luxurycars, el sistema esta compuesto de un login de acceso para usuarios registrados ubicado en http://localhost:8000/gestionventas/login/ y un sistema de registro ubicado en http://localhost:8000/gestionventas/registrar/ ambos realizan comprobación en base de datos y en caso de login informa error cuando se ingresa un usuario erroneo y un mensaje de exito cuando es el usuario registrado se logea de forma exitosa, y por ultimo un logout que permite cerrar sesion actual del usuario que este logeado ubicado en http://localhost:8000/gestionventas/logout/  

8. Se agrega un sistema de modificación de perfil de usuarios registrados, para poder modificar el usuario se requiere login, para acceder ingresamos a http://localhost:8000/gestionventas/perfil/ y asi podremos modificar campos como (nombre, apellido, email, contraseña, imagen de avatar) del usuario registrado.

9. Se agrega modelo con función de avatar el cual permite asignar una imagen a los usuarios, almacenando las imagenes en la carpeta media y utilizandolo al momento de iniciar sesion, se puede observar en models y en la base de datos la información ingresada. 