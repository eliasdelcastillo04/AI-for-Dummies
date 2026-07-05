# Control de Acceso Basado en Roles (RBAC)

La arquitectura *Multi-Tenant* requiere un control de acceso granular para prevenir la fuga de datos laterales y garantizar el principio de menor privilegio (Least Privilege Principle).

## 1. Matriz de Permisos IAM (Identity and Access Management)

### Nivel 1: Tenant Owner (Dueño de la Cuenta B2B)
*   **Lectura:** Acceso global a todos los datos, facturas, métricas y usuarios del Tenant.
*   **Escritura:** Capacidad para configurar integraciones (Stripe/WhatsApp), invitar usuarios y modificar los detalles bancarios.
*   **Peligro (Destructivo):** Capacidad de cancelar la suscripción principal (Downgrade) o eliminar el Tenant.

### Nivel 2: Billing Manager (Gerente de Finanzas)
*   **Lectura:** Acceso total a reportes de EBITDA, Invoices, Suscripciones y *Audit Logs* financieros.
*   **Escritura:** Autorizado para emitir **Refunds** (Reembolsos), aplicar cupones de descuento y forzar intentos de cobro (Trigger Dunning).
*   **Restricción:** No puede eliminar usuarios ni alterar las claves de API (Webhooks).

### Nivel 3: Support Agent (Atención al Cliente)
*   **Lectura:** Acceso limitado a perfiles de usuarios, estados de facturas y registros de mensajes enviados vía WhatsApp.
*   **Escritura:** Solo puede reenviar notificaciones (Resend Receipt) y modificar datos demográficos básicos (ej. Nombre, Teléfono).
*   **Restricción Estricta:** No puede visualizar información de tarjetas, emitir reembolsos ni acceder a métricas macro (MRR/EBITDA).

## 2. Aislamiento Multi-Tenant (Row-Level Security)
A nivel de base de datos PostgreSQL, se aplican políticas RLS (Row-Level Security). Toda consulta `SELECT`, `UPDATE` o `DELETE` inyecta automáticamente el `tenant_id` en la cláusula `WHERE`, evaluado a través del token JWT en la cabecera de la petición REST. Es matemáticamente imposible que un usuario de un Tenant extraiga facturas de otro Tenant.
