# Gestión de Tiers (Planes) y Cuotas Operativas

Esta política define la estructura comercial de nuestros tres planes principales (*Tiers*) y las reglas estrictas para el consumo de recursos (API y notificaciones).

## 1. Estructura de Tiers Comerciales

### Tier 1: Startup (Core SaaS)
Orientado a negocios emergentes que requieren automatización básica.
*   **Límite de Invoices:** Hasta 500 mensuales.
*   **Canales Soportados:** Email estándar.
*   **SLA (Service Level Agreement):** Soporte en 48 horas laborables.

### Tier 2: Growth (Business Automation)
Orientado a empresas en expansión con necesidades omnicanal.
*   **Límite de Invoices:** Hasta 5,000 mensuales.
*   **Canales Soportados:** Email prioritario + Integración nativa con WhatsApp Business API.
*   **SLA:** Soporte en 12 horas laborables.

### Tier 3: Enterprise (Scale & Custom)
Orientado a corporaciones B2B con alta volumetría.
*   **Límite de Invoices:** Ilimitado (Tarificación por volumen extra).
*   **Canales Soportados:** Omnicanal + Webhooks personalizados + Reportes dedicados.
*   **SLA:** Soporte 24/7 (Respuesta en < 1 hora).

## 2. Gestión de Cuotas y Límites de WhatsApp (Throttling)
Para evitar el abuso de la API de mensajería y salvaguardar la reputación de los números de envío (Quality Rating de Meta), se imponen las siguientes políticas de cuotas (Quotas):

*   **Soft Limit:** Cuando un Tenant consume el 80% de su cuota mensual de notificaciones HSM (High-Structured Messages), el sistema dispara una alerta preventiva invitando al *Upgrade*.
*   **Hard Limit:** Al llegar al 100% de la cuota, el bus de eventos encola las notificaciones no críticas con un retardo, bloqueando temporalmente envíos nuevos hasta el inicio del siguiente periodo, a menos que el cliente active el "Over-usage Billing" (Facturación por excedentes).

## 3. Protocolo de Degradación de Tier
Si un cliente decide reducir su plan (Downgrade), el sistema ejecutará un chequeo de integridad: si el uso actual del cliente (por ej. cantidad de usuarios activos) supera los límites del plan inferior solicitado, el sistema bloqueará el Downgrade obligando al usuario a purgar recursos antes de autorizar el cambio.
