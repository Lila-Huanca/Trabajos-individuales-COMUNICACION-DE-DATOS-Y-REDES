# Laboratorio 1 del módulo 4: Lanzamiento de una instancia de EC2
## Tarea 1. Comenzar a crear la instancia y asignarle un nombre
Primero, ponemos Star Lab para cargar el AWS y este se ponga en verde, como la siguiente imagen:
![Captura de pantalla 2024-05-29 142218](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/126b848e-c776-4047-993e-6b6d825952d2)

Despues, al entrar a AWS Seleccionas EC2:
![Captura de pantalla 2024-05-29 142536](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/0252c52c-1b61-4bcb-ba8e-085557db683f)

Así mismo después del anterior paso seleccione, Lanzar la instancia:
![Captura de pantalla 2024-05-29 142826](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/b2b5514d-def3-4596-9f72-5f0ff1d86ede)

Una vez lanzada la instancia, se le debe poner un nombre: Llamala Web Server 1
![Captura de pantalla 2024-05-29 15134578](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/6e4bf162-2a70-481d-abd9-f8b5dc6b3956)

## Tarea 2. Imágenes de aplicación y SO
Selecciona una AMI a partir de la cual crear la instancia:
En la lista de AMI disponibles de Quick Start, mantén la AMI predeterminada de Amazon Linux seleccionada.
Además, mantén seleccionada la Amazon Linux 2023 AMI x86_64 (HVM) predeterminada.
El tipo de imagen de máquina de Amazon (AMI) que selecciones determina el sistema operativo (SO) que se ejecutará en la instancia de EC2 que inicies. En este caso, has seleccionado Amazon Linux 2023 como SO invitado.
![Captura de pantalla 2024-05-29 144439](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/eea48b9e-cc23-426b-872d-372d6ad12d31)

## Tarea 3. Elegir el tipo de instancia
Especifica un tipo de instancia:
En el panel Tipo de instancia, mantén el tipo predeterminado t2.micro seleccionado.
El Tipo de instancia define los recursos de hardware asignados a la instancia. Este tipo de instancia tiene 1 unidad de procesamiento central virtual (CPU) y 1 GiB de memoria.
![Captura de pantalla 2024-05-29 14412](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/1fe6e1b9-532c-4121-bca0-28a2fabc9eab)

## Tarea 4. Seleccionar un par de claves
Selecciona el par de claves que quieras asociar con la instancia:
En el menú Nombre del par de claves, selecciona vockey.
El par de claves vockey que has seleccionado te permitirá conectarte a esta instancia mediante SSH después de que se haya iniciado. Aunque no tendrás que hacer eso en este laboratorio, sigue siendo necesario para identificar un par de claves existente, crear uno nuevo o al lanzar una instancia.
![Captura de pantalla 2024-05-29 145342](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/546efd9e-940a-4325-aaf8-270af8234f7e)

## Tarea 5. Configuración de red
Junto a la configuración de red, selecciona Editar. Después en Firewall (grupos de seguridad), selecciona el valor predeterminado La opción Crear grupo de seguridad está seleccionada.
Configura un nuevo grupo de seguridad:

### Mantén la selección predeterminada Crear un nuevo grupo de seguridad.
  
- Nombre del grupo de seguridad: borra el texto e introduce "Web Server"

- Descripción: borra el texto e introduce"Security group for my web server"

- Selecciona [Eliminar] Para eliminar la regla de entrada SSH predeterminada.

![Captura de pantalla 2024-05-29 151051](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/1d408c7c-10b5-421a-a5f7-467649740ac9)

## Tarea 6. Configurar el almacenamiento
En la sección Configurar almacenamiento, mantén la configuración predeterminada.

Iniciarás la instancia de Amazon EC2 usando un volumen predeterminado de disco de Elastic Block Store (EBS). Este será tu volumen raíz (denominado también volumen de arranque) que alojará el sistema operativo invitado de Amazon Linux 2023 que especificaste antes. Se ejecutará en un disco duro SSD de uso general (gp2) de 8 GiB de tamaño. Como alternativa, podrías añadir más volúmenes de almacenamiento, aunque eso no resulta necesario en este laboratorio.
![Captura de pantalla 2024-05-29 151034](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/cf04553a-b511-4328-ba6d-fc01e87d9fd1)

## Tarea 7: Detalles avanzados
Configura un script para que se ejecute en la instancia cuando se inicie:

Expande el panel Detalles avanzados.

Desplázate hacia la parte inferior de la página y copia y pega el código.

![Captura de pantalla 2024-05-29 1512345](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/9cfd54f7-7e97-4fe4-aabc-b78158610d4c)

## Tarea 8: Revisar la instancia y lanzarla
Primeroselecciona "Lanzar la instancia", despues seleccione "Ver todas las instancias", asímismo seleccione la instancia "Web Server 1" revisa la información de la pestaña Detalles que se muestra en el panel inferior.

Observa que la instancia tiene una dirección DNS de IPv4 pública. Puedes utilizar esta dirección IP para comunicarte con la instancia desde Internet. Antes de continuar, espera a que la instancia muestre lo siguiente:

Estado de la instancia: En ejecución

Comprobación de estado: 2/2 comprobaciones superadas

![Captura de pantalla 2024-05-29 152658](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/38e5f862-f7e8-486a-8b1a-c93e38194928)

## Tarea 9: Acceder a la instancia de EC2
Cuando lanzaste la instancia de EC2, proporcionaste un script que instaló un servidor web y creó una página web sencilla. En esta tarea, intentarás acceder al contenido desde el servidor web.

En la pestaña Detalles, copia el valor de la Dirección IPv4 pública de la instancia en el portapapeles.
![Captura de pantalla 2024-05-29 153214](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/3d927784-049b-40cf-b1d7-a0b6c913d943)

## Tarea 10: Actualizar el grupo de seguridad
No puedes acceder al servidor web porque el grupo de seguridad no permite el tráfico entrante en el puerto 80, que se utiliza para las solicitudes web HTTP. En esta tarea, actualizarás el grupo de seguridad.
![Captura de pantalla 2024-05-29 153433](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/4a9dcc93-194b-44ad-85c6-7f247a96cee4)

Vuelve a la pestaña del navegador de la Consola de administración de EC2. En el panel de navegación izquierdo, en Red y seguridad, selecciona Grupos de seguridad. Selecciona el grupo de seguridad Web Server que creaste al lanzar la instancia de EC2. En el panel inferior, selecciona la pestaña Reglas de entrada.
![Captura de pantalla 2024-05-29 153833](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/a0a1722e-0b99-4f41-a9d2-9d22302f7d4c)

## Tarea 11: Crear una regla de entrada
Selecciona Editar reglas de entrada y, a continuación, selecciona Añadir regla.
Configura lo siguiente:
Tipo: HTTP
Fuente: Cualquier lugar-IPv4
"Selecciona Guardar reglas".
La nueva regla HTTP de entrada crea una entrada para las direcciones IP IPv4 IP (0.0.0.0/0) y IPv6 (::/0).
![Captura de pantalla 2024-05-29 154130](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/f692a540-1264-46eb-9676-47bc72ca8d72)

## Tarea 12: Probar la regla
Vuelve a la pestaña que utilizaste para intentar conectarte al servidor web. Actualiza la página. Debería mostrar la página del servidor web con el mensaje Hello World!
![Captura de pantalla 2024-05-29 154434](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/36068bd4-7783-450a-b2c3-142b2b14a62c)

Laboratorio completado
¡Enhorabuena! Has completado el laboratorio.
Seleccione "Finalizar laboratorio" en la parte superior de la página y seleccione "Sí" 
Para confirmar que quieres dar por concluido el laboratorio.
![Captura de pantalla 2024-05-29 154838](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/77e86e0c-e8a0-4488-9172-29b5cb5dced4)

"" HAS TERMINADO SATISFACTORIAMENTE EL LABORATORIO ""
