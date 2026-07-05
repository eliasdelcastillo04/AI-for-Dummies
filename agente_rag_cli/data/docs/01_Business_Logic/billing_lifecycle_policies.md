# Políticas del Ciclo de Vida de Facturación

Este documento establece los protocolos comerciales inmutables para la gestión de cobros recurrentes, el manejo de fallos transaccionales y las normativas de prorrateo para suscripciones B2B.

## 1. Protocolo de Dunning (Recuperación de Cobros)
En caso de que un intento de cobro a la tarjeta de crédito de un cliente falle (ej. fondos insuficientes, tarjeta expirada), el sistema inicia una secuencia automatizada de *Dunning* para prevenir el *Churn involuntario*.

**Secuencia Oficial:**
*   **Día 0:** Falla el cobro inicial. El sistema cambia el estado del invoice a `past_due` y emite una notificación de advertencia (WhatsApp/Email). El servicio no se interrumpe.
*   **Día 3:** Primer reintento automático (*Soft Retry*). Si falla, se envía un enlace directo de actualización de tarjeta vía WhatsApp (Token seguro).
*   **Día 5:** Segundo reintento automático. Se envía notificación crítica: el servicio será degradado o suspendido en 48h.
*   **Día 7:** Tercer y último reintento automático (*Hard Retry*). Si falla, la suscripción pasa a estado `unpaid` o `canceled`. La cuenta del Tenant se bloquea o degrada al *Free Tier*.

## 2. Reglas de Prorrateo (Proration)
Los ajustes en las cuotas por cambios de plan a mitad del ciclo de facturación se rigen por la política de **Prorrateo Exacto al Segundo**.

*   **Upgrades (Subida de Plan):** El cliente recibe un crédito por el tiempo no utilizado del plan anterior y se le cobra inmediatamente la diferencia proporcional del nuevo plan por el resto del ciclo.
*   **Downgrades (Bajada de Plan):** El cliente retiene el acceso al plan superior hasta que termine el ciclo de facturación actual. El nuevo precio reducido aplica recién en el inicio del próximo ciclo (No se emiten devoluciones automáticas en efectivo por tiempo no usado).

## 3. Periodos de Gracia y Renovaciones
*   Las suscripciones anuales incluyen un **periodo de gracia de 5 días** posteriores a la fecha de vencimiento antes de la interrupción del servicio.
*   Las renovaciones se ejecutan de forma automática a las 00:00 UTC de la fecha de aniversario, requiriendo que el método de pago predeterminado se encuentre verificado y con autorización activa (`setup_intent.succeeded`).
