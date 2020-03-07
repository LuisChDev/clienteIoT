# Cliente IoT

se puede ejecutar la app con:

`docker-compose up`

hecho esto, quedará expuesta la dirección 0.0.0.0:80 para requests GET y POST.
un request GET retorna una página estática con información sobre patrones de diseño
empleados en la aplicación. un request POST, con mimeType application/json,
y los elementos 'temperature' (valor float)  y 'timestamp' (UNIX timestamp)
guarda estos datos en las bases de datos.
