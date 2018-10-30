# CalculadoraDocker
Webservices calculadora con imagen de docker
Lenguaje Python
Requisitos:
Docker
Para la ejecución se debe descargar la carpeta ContainerCalculadora, desde una consola de PowerShell:
1. Ubicarse dentro de la ruta en donde se dejo la carpeta ContainerCalculadora
2. Compilar y generar la imagen con el siguiente comando: docker build -t calculadora .
3. Verificar que se haya cargado la imagen con el comando docker image ls
4. Correr la aplicación con el siguiente comando: docker run -p 5000:80 calculadora

Para consumir el servicio debe ingresar de la siguiente forma:

1. http://localhost:5000/sumnumbers/10:5:5 En el caso de la suma, puede ingresar más parámetros separados por :
2. http://localhost:5000/restwonumbers/10:5 En el caso de la resta, solo se restan dos números
3. http://localhost:5000/mulnumbers/10:5:2 En la multiplicación, puede ingresar más parámetros separados por :
4. http://localhost:5000/divtwonumbers/10:5 En la división, solo se restan dos números
