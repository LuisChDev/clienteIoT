# Cliente IoT

se puede ejecutar la app con:

`docker-compose up`

hecho esto, quedará expuesta la dirección 0.0.0.0:80 para requests GET y POST.
un request GET retorna una página estática con información sobre patrones de diseño
empleados en la aplicación. un request POST, con mimeType application/json,
y los elementos 'temperature' (valor float)  y 'timestamp' (UNIX timestamp)
guarda estos datos en las bases de datos.

## Known issues

la base de datos MySQL puede no inicializarse correctamente la primera vez.
Si esto ocurre, se aconseja interrumpirla con `Ctrl-C` y volverla a iniciar
con el comando `docker-compose up` descrito anteriormente.
