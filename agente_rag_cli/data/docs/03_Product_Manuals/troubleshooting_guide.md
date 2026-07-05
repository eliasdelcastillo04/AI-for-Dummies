# Matriz de Resolución de Problemas (Troubleshooting)

Esta guía estandariza la respuesta técnica de soporte (Nivel 1 y 2) ante fallos comunes en los flujos de facturación y mensajería.

## Códigos de Error Financieros (Billing)

### `ERR_PAYMENT_DECLINED_402`
*   **Descripción:** La pasarela rechazó el cargo.
*   **Resolución L1:** Verificar en el *Audit Log* el sub-código de rechazo (ej. `insufficient_funds`, `expired_card`). Explicar al cliente y solicitar actualización de método de pago. El *Dunning* automático ya debería estar activo.
*   **Escalamiento L2:** Solo si el sub-código es `do_not_honor` repetitivo en múltiples clientes, investigar caída global de red procesadora.

### `ERR_IDEMPOTENCY_CLASH`
*   **Descripción:** El sistema intentó procesar la misma factura dos veces.
*   **Resolución:** El *Circuit Breaker* interceptó la petición gracias a la clave de idempotencia (`Idempotency-Key`). Informar al cliente que la transacción original fue exitosa y no hubo cargo doble.

## Códigos de Error de Mensajería (WhatsApp API)

### `ERR_WA_RATE_LIMIT_429`
*   **Descripción:** El Tenant excedió su límite de notificaciones salientes o el *Tier* de Meta (ej. > 1,000 mensajes en 24h para cuentas nuevas).
*   **Resolución L1:** Verificar el "Quality Rating" del número en el Dashboard de Meta. Si está en verde, iniciar proceso de verificación comercial para subir de Tier. Los mensajes fallidos están en la DLQ (*Dead Letter Queue*) y se purgarán en 24h.

### `ERR_WA_TEMPLATE_REJECTED`
*   **Descripción:** La plantilla HSM (notificación de cobro) intentó enviar variables bloqueadas (ej. solicitar contraseñas) o publicidad no solicitada.
*   **Resolución:** Rehacer la plantilla eliminando palabras clave marcadas por el filtro de spam de Meta (ej. "Oferta", "Promoción") y limitándola estrictamente a notificaciones transaccionales (recibos, alertas de vencimiento).
