# UnegWeb
Web para mantener informados en todo momento a los estudiantes de la UNEG.

*¿Como probarlo?*.
    
    */Debes tener un poco de conocimiento en Python 2.7 y Django(indispensable)
    
    --| Si estas trabajando con Windows , debes instalar Python 2.7 y configurar las variables de entorno
        para trabajar con algunos comandos de Python y Django.
        
     -| Si estas trabajando con Linux/Mac ya deberia venir una verison de Python 2.7 por defecto.
   
     */ Una ves instalado Python (y haber configurado las variables de entorno en windows).
        Abrimos la Terminal o CMD ( "Windows+R" en windows) e instalamos pip.
          
          +En Linux: #apt-get install python-pip.
          
          +En Mac: $sudo easy_install pip.
          
          +En Windows: Descargas "get-pip.py" mediante este link https://bootstrap.pypa.io/get-pip.py
            Luego mediante la terminal posicionas en la carpeta en la cual se descargo el archivo y
            ejecutas el archivo con el comando ">python get-pip.py" y se instalara.
            
      /* Ya teniendo pip (administrador de paquetes de python) procederemos a instalar "virtualenv"
         con el comando "$pip install virtualenv".
      
      
      
      /* Ya teniendo 'pip' y 'virtualenv' ahora crearemos un entorno virtual.
         + Solo ejecutamos el comando "$virtualenv Nombre_de_mi_entorno_virtual"
         
      /* Una ves aqui entramos a la carpeta que contiene el entorno virutal ya creado y ejecutamos el comando
          En Mac/Linux :"source bin/activate". En Windows "bin\activate"
         Al ejecutar el comando deberemos ver en la terminal algo asi 
      
      (Nombre_de_mi_entorno_virtual)tu_direccion$
      
      Luego usamos "pip freeze" para ver que paquetes estan instalados en nuestro entorno virtual.
      
      No deberian haber paquetes instalados y por lo tanto instalaremos los paquetes de el archivo
      "requerimientos.txt" que esta en el repositorio ubicandonos en la carpeta donde se encuentra el archivo
       escribimos el comando "$pip install -r requerimientos.txt"
       
      Solo quedaria hacer una prueba del servidor yendonos a la capeta "Unegweb" y escribimos "$python manage.py runserver"
      abrimos la direccion "127.0.0.1:8000" y listo ;D
    
-*NOTAS*-

	1)Commit 26/06/17
	  -Actualmente estamos trabajando con Django 1.10 usando Python 2.7 del lado del servidor.
      
      -Se esta implementando Materializecss para el diseño.
      
      -Aun no hay modelos en la base de datos, y los modelos que seran añadidos aun no seran definitivos.
      
      -Los templates actuales no poseen formularios y aun son de prueba
      
      -Los archivos estaticos son de pruebas, apesar de que se esta trabajando con materializecss se tiene
       la carpeta de Bootstrap3 debido a que en dado caso se reciba apoyo de otros desarrolladores. Se tomara
       en cuenta el apoyo dado

         
        
