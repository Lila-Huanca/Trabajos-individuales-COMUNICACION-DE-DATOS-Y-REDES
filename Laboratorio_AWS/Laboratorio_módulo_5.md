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
![Captura 65879](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/cd5e1e2b-1997-4203-9b27-b42b75657229)

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

Elige el nombre del bucket que acabas de crear.

![Captura 1234556](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/0e251e6e-eb8a-481d-afa0-a520f3e94f1b)

2.2. Selecciona la pestaña Permisos. En Bloquear acceso público (configuración del bucket), selecciona Editar.

2.3. Desactiva la casilla de Bloquear todo el acceso público. Elige Guardar cambios. Confirma los cambios.

![Captura 4657687980](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/b63520b2-3f54-4d15-a3e7-24e267123dbb)

2.4. Desplázate hasta Propiedad del objeto y selecciona Editar. Selecciona ACL habilitadas. Comprueba el reconocimiento y selecciona Guardar cambios.

![Captura 456768](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/79a179f4-8027-4081-8981-9b49ff8e7dca)

2.5. En la sección Política del bucket, selecciona Editar.

2.6. Para conceder acceso de lectura pública a tu sitio web, copia y pega la siguiente política del bucket en el editor de políticas:

```json
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Sid":"PublicReadForGetBucketObjects",
         "Effect":"Allow",
         "Principal":"*",
         "Action":[
            "s3:GetObject"
         ],
         "Resource":[
            "arn:aws:s3:::example-bucket/*"
         ]
      }
   ]
}
```

![captura 214363](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/bf656815-1e7b-48b5-a894-e2f1133634a6)

En la política, reemplaza example-bucket por el nombre del bucket. En la parte inferior de la página, selecciona Guardar cambios.

## Tarea 3. Subir un documento HTML
En esta tarea, subirás el archivo index.html de tu página web en el bucket de S3.

Abre el menú contextual (haz clic con el botón derecho) del siguiente enlace y, a continuación, elige Save link as (Guardar enlace como): index.html

Guarda el archivo index.html en el equipo local.

En la consola, selecciona la pestaña Objetos.

Carga el archivo index.html en tu bucket.

Selecciona Cargar.
Arrastra y suelta el archivo index.html en la página de carga. También puedes seleccionar Añadir archivos, buscar el archivo y usar la opción Abrir.

![captura 253476](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/46ce4411-1fd5-4084-b81d-8629f2aa9472)

3.1. Expande la sección Permisos.
En ACL predefinidas, selecciona Conceder acceso de lectura público.

![Captura 78956789](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/78c976e2-aed2-4d4f-a75a-ed1448c2a988)

3.2. Debajo de la configuración seleccionada aparece un mensaje parecido a este: No se recomienda otorgar acceso de lectura público.

3.3. Marca la casilla que aparece junto a Entiendo que debajo del mensaje de advertencia.

3.4. En la parte inferior de la página, selecciona Cargar.

3.5. Selecciona "Cerrar".

3.6. El archivo index.html aparece en la lista Objetos.

![Captura 12425](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/3881865c-1cea-44ef-9bda-941c53f2de62)

## Tarea 4. Probar el sitio web
4.1. Selecciona la pestaña Propiedades y desplázate a la sección Alojamiento de sitios web estáticos.

4.2. Selecciona Editar.

4.3. Selecciona Habilitar.




