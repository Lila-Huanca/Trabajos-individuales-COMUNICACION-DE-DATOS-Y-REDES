### Temas: IAM, S3

## Usuarios IAM
## Pregunta: Explica el proceso de creación y gestión de un usuario IAM, incluyendo la asignación de permisos y políticas.
### Crear un usuario de IAM

Acceso al Panel de IAM: Inicia sesión en la Consola de AWS y navega hasta el servicio de IAM.

![Captura de pantalla 2024-06-05 165817](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/ea45be8d-e898-4309-b972-805a6a69ae77)

Crear un Usuario IAM: Haz clic en "Usuarios" en el panel de navegación izquierdo y luego en "Agregar usuario". Ingresa el nombre del usuario y selecciona el tipo de acceso (consola, programático o ambos).

![Captura de pantalla 2024-06-05 182737](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/33971303-5f60-4189-8fa9-04d70192f760)


![Captura desde 2024-06-06 11-19-15](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/dc8eccf8-2693-4daa-b9ca-eaa2ce4da070)

### **Modo empresarial**

|**Usuario**|**En el grupo**|**Permisos**|
| :- | :- | :- |
|**user-1**|**S3-Support**|**Acceso de solo lectura a Amazon S3**|
|**user-2**|**EC2-Support**|**Acceso de solo lectura a Amazon EC2**|
|**user-3**|**EC2-Admin**|**Ver, iniciar y detener instancias de Amazon EC2**|


 Despues poner crear usuario,Añadir directamente las políticas existentes, crear, añadir politicas  Busca AdministratorAccess y selecciona la política, luego selecciona Siguiente: Etiquetas. Añadir usuario.  ID de clave de acceso y Clave de acceso secreta.

 ### **Probar permisos de user-1**

- En el panel de navegación de la izquierda, selecciona **Panel**.
- Inicia sesión con las siguientes credenciales:
  - **Nombre de usuario de IAM:** user-1
  - **Contraseña:** Lab-Password1

## Grupos IAM
## Pregunta: Describe cómo crear y gestionar grupos IAM, y cómo se pueden utilizar para simplificar la administración de permisos

Beneficios de los Grupos IAM: Los grupos IAM simplifican la administración de permisos al permitirte asignar permisos a múltiples usuarios de manera centralizada. Esto facilita la aplicación de principios de menor privilegio y reduce el riesgo de errores de permisos individuales. Además, cuando un usuario es agregado o removido de un grupo, sus permisos se actualizan automáticamente, lo que simplifica la gestión de cambios en la organización.

En resumen, la creación y gestión de grupos IAM te permite organizar a tus usuarios y asignar permisos de manera eficiente, lo que facilita la administración de accesos y la aplicación de políticas de seguridad en AWS.


## Code: 

- Gestión de objetos en un Bucket.
- Permisos de acceso
- Simula el manejo de permisos mediante un diccionario de permisos

cmd: 

```
class S3BucketWithPermissions(S3Bucket):
 def __init__(self):
 super().__init__()
 self.permissions = {}
 def set_permission(self, bucket, key, permission):
 if bucket not in self.permissions:
 self.permissions[bucket] = {}
 self.permissions[bucket][key] = permission

 def check_permission(self, bucket, key, action):
 return self.permissions.get(bucket, {}).get(key) == action

```



