# Laboratorio 2 del Módulo 4: Creación de un Bucket de S3

## Información General sobre el Laboratorio

A lo largo de este ejercicio de laboratorio, se le guiará a través de una serie de instrucciones destinadas a configurar con éxito unbucket de Amazon Simple Storage Service (Amazon S3), que servirá como plataforma de alojamiento para un sitio web estático.

## Tarea 1. Crear un Bucket de S3
1.1. Primero, ponemos Star Lab para cargar el AWS y este se ponga en verde, como la siguiente imagen:
![Captura de pantalla 2024-05-29 160905](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/0af1989e-bf21-474d-8abc-12eb9b97b548)

1.2. Despues, al entrar a AWS Seleccionas S3:
![Captura de pantalla 2024-05-29 161233](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/2f45b051-06f3-48a3-b9a4-d7f6e0c5fdbb)

Selecciona Crear bucket en la parte derecha de la página, como se muestra en la siguiente imagen:
![Captura de pantalla 2024-05-29 161439](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/54037d9c-f96b-409f-a1d6-8944dfaa5274)

1.3. Nombre del bucket, introduce un nombre exclusivo compatible con el sistema de nombres de dominio (DNS) para el nuevo bucket.
  
![Captura de pantalla 2024-05-29 162050](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/a7dd1f6d-d705-4a1c-b8d9-bcf8d1b8f6cf)

1.4. Configuración de Seguridad
A). Quita la marca de la casilla Bloquear todo el acceso público.
B). Marca la casilla "Reconozco que la configuración actual puede provocar que este bucket y los objetos que contiene se vuelvan públicos".
![Captura de pantalla 2024-05-29 162545](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/bc404fc1-a503-4e3f-b926-81af4b43c220)

1.5. Desplázate hasta la parte inferior de la página y selecciona Crear bucket.
![Captura de pantalla 2024-05-29 162236](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/ea00dfce-28c6-498e-94b4-dd98f09b7340)

1.6. El nuevo bucket aparece en la lista Buckets.
![Captura de pantalla 2024-05-29 162852](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/ee7a90af-4ba2-454d-89f7-1a41143aad6b)

## Tarea 2. Añadir una Política de Bucket para que el Contenido esté Disponible Públicamente

2.1. Eliga el enlace para el nombre del bucket y, a continuación, selecciona la pestaña Permisos.
![Captura de pantalla 2024-05-29 163351](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/6c551ee4-c7ba-4980-9501-612ce5cfe2d2)

2.2. En la sección Política de bucket, selecciona Editar.
![Captura de pantalla 2024-05-29 163517](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/0175bc0a-40a0-4b01-a101-2a80aadd5d38)

Copie la siguiente política de bucket y pégala en el editor de políticas.
```json

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::example-bucket/*"
            ]
        }
    ]
}
```

![Captura de pantalla 2024-05-29 170413](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/cc3487e3-010d-4a89-89d0-b5f5409c8f8c)
Asi mismo una vez de poner el codigo, cambiar la parte baja, "example-bucket" Por el bucket creado, en este caso es: "paginaweb15" y después pones en; "Guardamos los cambios".

## Tarea 3. Subir un documento HTML
3.1. Primero guardamos un archivo index en nuestras carpetas.

3.2. Seleccionamos la pestaña Objetos.

3.3. Cargamos el archivo index y brindamos el acceso a las propiedades.

![Captura de pantalla 2024-05-29 171436](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/d317ec47-0a4e-493c-8982-9c68c2c59016)

3.4. Carga el archivo index.html en tu bucket.
Selecciona Cargar.
Arrastra y suelta el archivo index.html en la página de carga.
Como alternativa, selecciona Añadir archivos, navega al archivo y selecciona Abrir.

![Captura de pantalla 2024-05-29 173727](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/0ed0d390-3e8e-4bc4-92e0-d9a6d6688544)

3.5. Amplía la sección Propiedades.
3.6. Asegúrate de que está seleccionada la clase de almacenamiento "Estándar".

![Captura de pantalla 2024-05-29 173911](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/d5d4599d-a757-4e92-a4e5-c9ff90f9ea27)

3.7. En la parte inferior de la página, selecciona "Cargar".

![Captura de pantalla 2024-05-29 174122](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/5b5eb55b-65b5-494d-b87c-b02f51afca31)

3.8. Selecciona Cerrar.

![Captura de pantalla 2024-05-29 174211](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/558d3c54-dc00-4864-a07d-b7556f1434dc)

3.9. El archivo index.html aparece en la lista Objetos.
![Captura de pantalla 2024-05-29 183922](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/640bf8b7-53c9-4350-9e99-16f1bdc7a6a9)

## Tarea 4. Probar el sitio web

4.1. Selecciona la pestaña Propiedades y desplázate a la sección Alojamiento de sitios web estáticos.

4.2. Selecciona Editar.
![Captura de pantalla 2024-05-29 1706098](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/a4b0be64-0067-4d87-b6d8-da4b89b183e4)

4.3. En el cuadro de texto Documento de índice, introduce index.html.
![Captura de pantalla 2024-05-29 1834569](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/9cc5cfef-1232-4804-b4b0-881c23c7aa0b)
4.4 Copiamos el URL

4.5 Abrimos URL

![Captura de pantalla 2024-05-29 1576889](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/9dfe68d1-4d8d-4160-8821-da0d9955a40d)

Laboratorio completado ¡Enhorabuena! Has completado el laboratorio. Seleccione "Finalizar laboratorio" en la parte superior de la página y seleccione "Sí" Para confirmar que quieres dar por concluido el laboratorio.

![Captura de pantalla 2024-05-29 182847](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/cfe721d7-7150-421c-a967-e7f037a3ef7b)

"" HAS TERMINADO SATISFACTORIAMENTE EL LABORATORIO ""
