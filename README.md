# 🚀 TALENT MATCH - PB-02 (Sesión 2)

Este proyecto contiene la estructura base y la arquitectura inicial para **TALENT MATCH**, cumpliendo con los objetivos técnicos requeridos en la **Sesión 2: Arquitectura, apps y configuración Django**.

## 📋 Objetivos Completados

1. **Configuración Avanzada por Entornos**: Separación de las configuraciones globales del proyecto en un módulo limpio y estructurado (`base.py`, `development.py`, `testing.py`, `production.py`) dentro de la carpeta `settings/`.
2. **Seguridad y Variables Ocultas**: Implementación de `python-dotenv` para la gestión segura de credenciales, aislando las claves del sistema en un archivo confidencial `.env` y aportando una plantilla pública `.env.example`.
3. **Monitoreo (Logging)**: Configuración de un sistema de logging básico dentro de `base.py` configurado para registrar y mostrar eventos técnicos del backend directamente por la consola.
4. **Modelo de Usuario Escalable**: Creación e integración de la aplicación `accounts` junto con una entidad de usuario personalizada `accounts.User` (derivada de `AbstractUser`). Esto permitirá la futura incorporación de campos específicos del negocio sin comprometer la integridad de la base de datos.

---

## 🛠️ Instrucciones de Ejecución Local

Para levantar este proyecto en tu entorno local, sigue estos pasos desde la terminal de PowerShell:

```powershell
# 1. Instalar dependencias necesarias
pip install python-dotenv

# 2. Generar las migraciones para el nuevo modelo de usuario
python manage.py makemigrations accounts --settings=TALENT_MATCH.settings.development

# 3. Aplicar las migraciones a la base de datos local
python manage.py migrate --settings=TALENT_MATCH.settings.development

# 4. Iniciar el servidor de desarrollo
python manage.py runserver --settings=TALENT_MATCH.settings.development
```

Una vez iniciado, el proyecto estará disponible en la dirección local: `http://127.0.0`
