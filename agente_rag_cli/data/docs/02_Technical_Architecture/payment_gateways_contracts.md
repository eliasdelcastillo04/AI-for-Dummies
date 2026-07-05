# Contratos de Pasarelas de Pago (Mocks)

Las integraciones de cobro interactúan mediante webhooks entrantes. A continuación se presentan las estructuras JSON sanitizadas que nuestro sistema espera recibir y parsear desde las pasarelas principales.

## 1. Evento de Cobro Exitoso (Stripe Mock)
Este payload es emitido cuando un ciclo de suscripción se cobra de forma exitosa. Se utiliza para habilitar servicios y desencadenar facturación electrónica.

```json
{
  "id": "evt_mock_00000000000000",
  "object": "event",
  "api_version": "2023-10-16",
  "created": 1698243120,
  "type": "invoice.payment_succeeded",
  "data": {
    "object": {
      "id": "in_mock_00000000000000",
      "object": "invoice",
      "amount_due": 4900,
      "amount_paid": 4900,
      "currency": "usd",
      "customer": "cus_mock_87654321",
      "status": "paid",
      "subscription": "sub_mock_12345678"
    }
  }
}
```

## 2. Evento de Pago Fallido (Dunning Trigger)
Este evento dispara la máquina de estados de *Dunning* descrita en las políticas de facturación.

```json
{
  "id": "evt_mock_failed_0000000",
  "type": "invoice.payment_failed",
  "data": {
    "object": {
      "id": "in_mock_failed_000000",
      "amount_due": 9900,
      "attempt_count": 1,
      "next_payment_attempt": 1698415920,
      "status": "open",
      "billing_reason": "subscription_cycle"
    }
  }
}
```
