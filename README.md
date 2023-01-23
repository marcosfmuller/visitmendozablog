# visitmendozablog
Visit Mendoza Blog

![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)

## Logo de nuestra cuenta

<img src="https://github.com/marcosfmuller/visitmendozablog/blob/main/media/avatars/avatarAdmin.jpg" width=150><br>

## Proyecto

:construction: Proyecto en construcción :construction:

La finalidad de nuestro blog es acercar Mendoza al turista, y al propio mendocino, mostrando lugares tipicos de la provincia para pasar un buen momento.<br>

## Navegación por la web

Se ingresa al Blog a través de la url: 127.0.0.1:8000/ <br>
El blog está compuesto por 3 Apps: 
* `AppAccounts:` donde se desarrolló todo el código referido a la administración de cuentas y usuarios.
* `AppBlog:` donde se desarrolló todo el código referido a los posts.
* `AppMessages:`donde se desarrlló todo el código para el envio y recepción de mensajes entre usuarios.

En la parte superior de la pagina principal encontramos la barra de navegación: Acerca de | Hoteles | Gastronomía | Actividades | Chat | <br>
En la barra de navegacion tambien encontramos las opciones para Registrarme | Iniciar Sesion y en el caso de ya estar loggeado, la opcion Cerrar Sesión.
Haciendo click en el nombre de usuario hay dos opciones dependiendo de si el usuario es:
* `Superuser o Staff:` te direcciona a un Panel de Control:
  * Modificar Perfil:
    * Editar: email, nombre, apellido y cargar o modificar avatar.
  * Ver Usuarios:
    * Editar un Usuario.
    * Eliminar un Usuario.
  * Opciones de Post:
    * Crear un Post.
    * Editar un Post.
    * Eliminar un Post.
    * Administrar Sitio (localhost:8000/admin)
* `Usuario común:`
  * Modificar Perfil:
    * Edigar: email, nombre, apellido y cargar o modificar avatar.

Hay una barra de búsqueda, en la cual, ubicados en la pagina principal, se puede buscar por cualquier palabra que este contenida en el título, descripción o cuerpo del post. Si entramos a una categoría en la barra de navegacion y hacemos uso de la barra de búsqueda, buscará sólo en la categoría actual.
Siguiendo con la navegación en la página principal, haciendo scroll hacia abajo se encuentran listados los posts de todas las categorías ordenados de mas reciente a más antigüo. 
Cada Post se visualiza en forma acotada, mostrando el Título y una descripción. Para ver el post completo, se necesita tener usauario y estar loggeado.
Haciendo click en los botones de "Anterior" y "Siguiente" se puede navegar entre las distintas paginas de posts.<br>

Al pie de la web se encuentran los inconos de nuestras redes sociales, los cuales los llevarán a la url de cada red social en particular.

## Tecnologías utilizadas
* Python
* Django Framework
* Html
* CSS

## Autor
| [<img src="https://user-images.githubusercontent.com/117835925/206094445-92c7ff56-5acb-4de1-b814-970321896dca.jpg" width=115><br><sub>Marcos Müller</sub>](https://github.com/marcosfmuller)|
| :---: | 
