### Temas: IAM, S3

## Usuarios IAM
## Pregunta: Explica el proceso de creación y gestión de un usuario IAM, incluyendo la asignación de permisos y políticas.
### Crear un usuario de IAM

Acceso al Panel de IAM: Inicia sesión en la Consola de AWS y navega hasta el servicio de IAM.

![Captura de pantalla 2024-06-05 165817](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/ea45be8d-e898-4309-b972-805a6a69ae77)

Crear un Usuario IAM: Haz clic en "Usuarios" en el panel de navegación izquierdo y luego en "Agregar usuario". Ingresa el nombre del usuario y selecciona el tipo de acceso (consola, programático o ambos).

![Captura de pantalla 2024-06-05 165952](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/e7ba6052-30ce-417c-bce3-f803e2db0233)
 Despues poner crear usuario,Añadir directamente las políticas existentes, crear, añadir politicas  Busca AdministratorAccess y selecciona la política, luego selecciona Siguiente: Etiquetas. Añadir usuario.  ID de clave de acceso y Clave de acceso secreta.
 
![Captura de pantalla 2024-06-05 172526](https://github.com/Lila-Huanca/Trabajos-individuales-COMUNICACION-DE-DATOS-Y-REDES/assets/166184502/a7a538ce-f2a4-4938-afd9-64d5e78dc2da)


## Grupos IAM
## Pregunta: Describe cómo crear y gestionar grupos IAM, y cómo se pueden utilizar para simplificar la administración de permisos

Beneficios de los Grupos IAM: Los grupos IAM simplifican la administración de permisos al permitirte asignar permisos a múltiples usuarios de manera centralizada. Esto facilita la aplicación de principios de menor privilegio y reduce el riesgo de errores de permisos individuales. Además, cuando un usuario es agregado o removido de un grupo, sus permisos se actualizan automáticamente, lo que simplifica la gestión de cambios en la organización.

En resumen, la creación y gestión de grupos IAM te permite organizar a tus usuarios y asignar permisos de manera eficiente, lo que facilita la administración de accesos y la aplicación de políticas de seguridad en AWS.

## Grupos:

|**Concepto**|**Definición**|
| :- | :- |
|**AWS Identity and Access Management [IAM]**|Aplica controles para usuarios que necesitan acceder a recursos informáticos.|
|**Rol**|Identidad de IAM con permisos específicos.|
|**Usuario**|Entidad creada en AWS para representar a personas o aplicaciones que interactúan con AWS. Compuesto por nombre y credenciales.|
|**Grupo de seguridad**|Actúa como firewall virtual para controlar tráfico entrante y saliente en instancias.|
|**Política**|Objeto de AWS que define permisos cuando se asocia a una identidad o recurso. Evaluada por AWS en solicitudes de entidades principales.|
|**Amazon Inspector**|Es la ayuda a identificar vulnerabilidades de seguridad y desviaciones de prácticas recomendadas en aplicaciones antes y durante la ejecución.|
|**Grupo de IAM**|Conjunto de usuarios de IAM con permisos específicos. Facilita la administración de permisos.|
|**Usuario raíz**|Identidad inicial con acceso total a todos los servicios y recursos de AWS al crear una cuenta.|
|**Credencial**|Verifica la identidad del usuario y su permiso para acceder a recursos solicitados.|
|**Habilitación de Multi-Factor Authentication (MFA)**|Requiere autenticación con dos o más métodos independientes.|
|**Notación de objetos JavaScript [JSON]**|Es el sintaxis para almacenar e intercambiar datos.|
|**Multi-Factor Authentication [MFA]**|Es un sistema de seguridad que verifica la identidad mediante múltiples métodos independientes.|

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



