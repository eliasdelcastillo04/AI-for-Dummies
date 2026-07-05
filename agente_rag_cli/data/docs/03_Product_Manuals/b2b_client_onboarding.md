# Guía Ejecutiva de Onboarding para Clientes B2B

El objetivo de este manual es estandarizar la activación de un nuevo cliente institucional (Tenant) en la plataforma, minimizando el "Time-to-Value" (TTV) y garantizando la correcta vinculación de las pasarelas financieras y canales de comunicación.

## Fase 1: Creación del Perfil y Configuración Multi-Tenant
1. **Creación del Espacio de Trabajo (Workspace):** El Account Executive provisiona el Tenant en el panel de administración, asignando un UUID único.
2. **Asignación de Tier Comercial:** Se define si el cliente operará en *Startup*, *Growth* o *Enterprise*. Esto condicionará sus *Rate Limits* automáticos.

## Fase 2: Configuración del Billing Portal (Stripe / MercadoPago)
1. **Vinculación de Cuenta Conectada (Connect/OAuth):** El cliente debe autorizar a nuestra plataforma a gestionar pagos en su nombre mediante el flujo OAuth oficial de la pasarela.
2. **Mapeo de Productos:** Importación y sincronización del catálogo de productos y precios del cliente hacia nuestro motor de facturación.

## Fase 3: Activación Omnicanal (WhatsApp Business API)
1. **Verificación de Facebook Business Manager:** Obligatorio para enviar más de 250 mensajes/día.
2. **Aprobación de Plantillas (HSM):** El cliente redacta sus plantillas de recordatorio de cobro (Ej: *"Hola {{1}}, tu factura de {{2}} está lista"*). Soporte técnico las envía a Meta para su validación (TLA: 2-24 hrs).
3. **Prueba de Humo (Smoke Test):** Ejecución de un cobro de prueba de $1.00 USD para validar que el *webhook* de pago exitoso dispara correctamente el *webhook* de notificación hacia el teléfono de prueba.

## Fase 4: Go-Live
Firma del *Sign-off* técnico y entrega de credenciales RBAC (Role-Based Access Control) al Administrador Principal del cliente.
