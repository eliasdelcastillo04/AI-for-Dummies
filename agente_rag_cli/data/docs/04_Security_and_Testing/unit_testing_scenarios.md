# Escenarios de Pruebas Unitarias e Integración (BDD)

Este documento centraliza los escenarios de prueba automatizados escritos en Gherkin (Given/When/Then), diseñados para testear la resiliencia financiera y la coreografía de eventos.

## Escenario 1: Tolerancia a Caídas de Stripe (Circuit Breaker)
Evalúa el comportamiento del sistema cuando la pasarela de pagos experimenta interrupciones (Timeouts).

**Given** que el `Billing Service` intenta procesar 50 renovaciones simultáneas
**And** la pasarela de Stripe está devolviendo errores `HTTP 503 Service Unavailable`
**When** los primeros 5 intentos de cobro fallan consecutivamente por latencia > 4000ms
**Then** el *Circuit Breaker* debe pasar a estado `OPEN`
**And** las 45 renovaciones restantes deben encolarse en la cola `Billing_Retry_Queue` (DLQ)
**And** el sistema NO debe marcar las suscripciones como `past_due` (Protección contra fallos ajenos)

## Escenario 2: Idempotencia en Cobros (Evitar Cobros Duplicados)
Garantiza que un usuario no pueda ser cobrado dos veces por un error de red o de capa UI.

**Given** un `Invoice` válido de $100.00 en estado `open`
**And** un cliente hace doble clic frenéticamente en el botón "Pagar Ahora"
**When** el frontend envía dos solicitudes `POST /charge` en milisegundos, ambas con el mismo `Idempotency-Key`
**Then** el servidor procesa la primera solicitud enviándola a MercadoPago
**And** la segunda solicitud es interceptada inmediatamente por el middleware de Idempotencia
**And** la respuesta de la segunda solicitud devuelve el `HTTP 200 OK` cacheados del resultado de la primera, sin generar un segundo cargo en la tarjeta.

## Escenario 3: Generación Segura de Webhooks (WhatsApp HSM)
**Given** un evento de `PaymentCompleted` consumido desde el Event Bus
**When** el `Notification Service` renderiza la plantilla HSM de recibo de cobro
**Then** el payload JSON resultante NO debe incluir campos ofuscados como la tarjeta de crédito
**And** el payload debe validar el esquema estricto del *Webhook Contract* de WhatsApp API antes del envío HTTP.
