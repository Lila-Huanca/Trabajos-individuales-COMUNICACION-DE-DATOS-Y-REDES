## Laboratorio del módulo 11: Uso de balanceadores de carga
Información general sobre el laboratorio
Sigue estos pasos para crear y configurar un balanceador de carga, registrar una página web como destino del balanceador de carga y probar el balanceador de carga.

## Tarea 1. Lanzar una instancia de EC2
1.2. En esta tarea, lanzarás una instancia de Amazon Elastic Compute Cloud (Amazon EC2) como lo has hecho en laboratorios anteriores.

1.3. Primero, ponemos Star Lab para cargar el AWS y este se ponga en verde, como la siguiente imagen:

![Captura de pantalla 2024-05-30 113719](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/caca8ea1-2f82-428c-b45d-beea623281d1)

- Entrar a AWS Seleccionas EC2:
![Captura de pantalla 2024-05-29 142536](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/0252c52c-1b61-4bcb-ba8e-085557db683f)

1.4. Selecciona el botón Lanzar instancia en medio de la página y luego selecciona Lanzar instancia en el menú desplegable.



1.5. En el panel Nombre y etiquetas:
En Nombre, introduce "Web Server 1".

![Captura de pantalla 2024-05-29 15134578](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/6e4bf162-2a70-481d-abd9-f8b5dc6b3956)

Antes de continuar, espera a que la instancia muestre lo siguiente:

1.5.1. Estado de la instancia:  En ejecución
Comprobación de estado:  2/2 comprobaciones superadas
Sugerencia: Para actualizar la información de la instancia, selecciona el icono de actualización .

![Captura de pantalla 2024-05-30 122859](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/a88a83c7-ff4f-4087-888d-c8539fe4ee5b)

## Tarea 2. Acceder al sitio web de la instancia de EC2

1.5.2. En la pestaña Detalles, copia la Dirección IPv4 pública de tu instancia, a continuación abre una nueva pestaña en tu navegador web y pega y carga la dirección.

![Captura de pantalla 2024-05-30 123314](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/0f6c9fc2-e0e0-467a-8aac-4bb4963e0e31)

Debería mostrar la página del servidor web con el mensaje Hello World! This is server 1.

Nota: Si no aparece la página web, asegúrate de estar accediendo a la página con http:// (y no con https://).

![Captura de pantalla 2024-05-30 123438](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/9bb1ddee-2d14-4902-8a15-a355f6c801b0)

## Tarea 3. Crear una segunda instancia de EC2 para el balanceo de carga

3.1. Selecciona la instancia Web Server 1.

En el menú Acciones, selecciona Imágenes y plantillas y después selecciona Lanzar más como esta
![Captura de pantalla 2024-05-30 124836](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/11d03d04-b8e3-4c8c-a432-1fca2fbb981c)

3.2. Panel Nombre y etiquetas, cambia el nombre a Web Server 2.

![Captura de pantalla 2024-05-30 125118](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/97efb0ff-ff5e-4252-b95d-d4ae7f19b5be)

3.3. En la sección Par de claves (inicio de sesión), en la lista desplegable Nombre del par de claves - obligatorio, selecciona vockey.

![Captura de pantalla 2024-05-30 125716](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/95c047c8-a911-43a9-9689-6359677f4067)

3.4. En la lista desplegable Subred, selecciona la subred existente en la Zona de disponibilidad us-east-1b.

![Captura de pantalla 2024-05-30 130258](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/0e1c5a0b-7717-4f2a-b39f-d1b8e23565b4)

3.5. Selecciona Lanzar instancia.
![Captura de pantalla 2024-05-30 130551](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/563f9f8c-b5c3-4e07-b66a-c37933ccefe2)

## Tarea 4. Acceder al sitio web en la segunda instancia de EC2
Selecciona la instancia Web Server 2.
En la pestaña Detalles, copia la Dirección IPv4 pública de tu instancia, a continuación abre una nueva pestaña en tu navegador web y pega y carga la dirección.

![Captura de pantalla 2024-05-30 131003](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/59ef2320-fe7d-4cc1-b1bf-3bddfa7cad5f)

![Captura de pantalla 2024-05-30 130944](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/9359cd15-9e00-440d-9611-d50eaecc3492)

## Tarea 5. Crear un balanceador de carga

![Captura de pantalla 2024-05-30 131351](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/2754d2be-1a9c-4015-85a1-8ef272b95925)
