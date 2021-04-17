# myblog
Blog personal desarrollado con el framework Django y apoyado con Foundation (framework CSS) para los templates. Por otro lado, implementé un atributo llamado "slug" en el modelo de Entrada para asignar, en este caso, cada título de un artículo para la URL. 

# Vista principal
La vista principal contiene de 5 secciones:
Primero, la sección de artículo principal. (Lado izquierdo de la parte de arriba)
Segundo, los 4 artículos secundarios que dueño del blog desea proyectar. (Lado derecho de la parte de arriba)
Tercero, una pequeña descripción del blogger que se presenta y a su vez un botón de suscripción. (Parte central)
Cuarto, los artículos recientemente subido al blog. (Parte de abajo) 

![image](https://user-images.githubusercontent.com/53346752/115108583-ea20ca80-9f36-11eb-953e-a4450eaf8881.png)

Y por último, un formulario de contactos donde el usuario puede mandar un mensaje, así como, un apartado pequeño que describe otras formas de contacto que son correo y número de telófono del blogger.

![image](https://user-images.githubusercontent.com/53346752/115108803-0c671800-9f38-11eb-8242-b947611a5c6b.png)

# Sección de artículos
Esta sección inicia con la vista de un buscador de artículos de acuerdo al título del artículo que desee buscar el usuario.
También se visuliza todos los artículos del blog con una paginación para mostrar los artículos faltantes y un apartado llamado "Categorías" que según la categoría seleccionada se muestran los artículos relacionos a dicha categoría.

![image](https://user-images.githubusercontent.com/53346752/115108843-33bde500-9f38-11eb-875d-e2cabad30fc9.png)

# Login de usuario
El acceso de usuario tiene las funciones de acceder y registrar.

![image](https://user-images.githubusercontent.com/53346752/115109075-60bec780-9f39-11eb-9efe-8cca76f2d77b.png)

# Registro de usuario
Para registrarse un usuario en el blog, se debe llenar los datos solicitados en el formulario para posteriormente tener una cuenta de usuario.

![image](https://user-images.githubusercontent.com/53346752/115109118-8cda4880-9f39-11eb-9cef-0c1efaea8e08.png)

# Agregar a favoritos
Cada uno de los artículos contiene un botón llamado "Agregar a favoritos" lo cuál solo es funcional cuando hay un usuario logueado al blog.
Vista de un par de artículos:
![image](https://user-images.githubusercontent.com/53346752/115109206-01ad8280-9f3a-11eb-9287-1c99cd2c0b97.png)

![image](https://user-images.githubusercontent.com/53346752/115109216-0d00ae00-9f3a-11eb-9530-b12d4bffd35e.png)

![image](https://user-images.githubusercontent.com/53346752/115109249-3f121000-9f3a-11eb-9f31-b7697f35ef34.png)

# Perfil del usuario
En esta vista se visualiza los artículos favoritos que agregó el usuario guardados en su perfil.

![image](https://user-images.githubusercontent.com/53346752/115109363-0161b700-9f3b-11eb-8466-6313809ff62a.png)

Como se pudieron percatar, en la vista de los artículos expuestos y la vista del perfil del usuario ya no tenemos el botón de Acceder (que permitia mostrar el acceso de usuarios), ya que esto se muestra cuando no hay un usuario logueado en el blog. Caso contrario, con un usuario logueado se muestra el botón de Perfil.

![image](https://user-images.githubusercontent.com/53346752/115109312-b778d100-9f3a-11eb-9c4b-c903bc0db196.png)

# SEO con Sitemap
Así como, la implementación de sitemap, lo cuál es un archivo que sirve como herramienta la mejora de búsqueda y posicionamiento en el buscador de Google. Adicionalmente, genera un archivo "sitemap.xml" (el nombre es relativo pero debe tener la terminación de ".xml" para guardarse como archivo de lectura).

Archivo generado a través de las URL's definidas en este proyecto:

![image](https://user-images.githubusercontent.com/53346752/115087843-9e3d3980-9ed4-11eb-89a2-535eecccc541.png)
