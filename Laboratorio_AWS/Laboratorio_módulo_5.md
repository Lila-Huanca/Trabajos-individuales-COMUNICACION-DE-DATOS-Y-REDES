# Laboratorio del Módulo 5: Uso de CloudFront como CDN para un Sitio Web

## Información General sobre el Laboratorio

En este laboratorio, utilizarás Amazon CloudFront como red de entrega de contenido (CDN) para un sitio web almacenado en Amazon Simple Storage Service (Amazon S3).

## Tarea 1. Crear un Bucket de S3 mediante AWS CLI

Primero, ponemos Star Lab para cargar el AWS y este se ponga en verde, como la siguiente imagen:

![Captura08829](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/384d46b6-04f4-44e8-be5f-f6a41ca54a34)

Despues, al entrar a AWS Seleccionas CloudShell:

![Captura123](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/8d73af90-8b89-4044-bcf3-c9e5a1808683)

AWS CloudShell es un shell basado en navegador que da acceso a la línea de comandos para los recursos de AWS en la región de AWS seleccionada.
3. Copia y pega el siguiente código en un editor de texto:

```
cd ~
aws s3api create-bucket --bucket (bucket-name) --region us-east-1
```
![Captura0928034](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/f6ec53e2-2f89-4f03-bfaf-e544d0d5d7ad)

4. Ejecuta el código actualizado en el terminal de CloudShell.
El resultado debe tener un aspecto similar al siguiente:
```
{
   "Location": "/mylabbucket12345"
}
```
![Captura96466](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/2677a82c-7346-4658-bc86-6872b3bf9d86)

## Tarea 2: Añadir una política de bucket

En esta tarea, añadirás una política de bucket a través de AWS CLI para que el contenido esté disponible públicamente.

2.1. En la consola, selecciona el menú **Servicios**, localiza la sección **Almacenamiento** y elige **S3**.

![Captura 465787](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/42f252a6-63cb-41a0-a161-69031f8a1f9a)




