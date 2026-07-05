# Webhooks y Contratos de WhatsApp API (Meta)

El sistema soporta mensajería bidireccional y notificaciones proactivas (*High-Structured Messages* o HSM) a través de Meta Cloud API. Toda comunicación PII está tokenizada.

## 1. Envío de Notificación Proactiva (Outbound Template)
Este payload se envía hacia Meta para despachar una notificación de recordatorio de cobro o recibo de pago, utilizando plantillas pre-aprobadas.

```json
{
  "messaging_product": "whatsapp",
  "to": "whatsapp_id_mock_12345",
  "type": "template",
  "template": {
    "name": "payment_receipt_v2",
    "language": {
      "code": "es_AR"
    },
    "components": [
      {
        "type": "body",
        "parameters": [
          {
            "type": "text",
            "text": "Factura de Julio 2026"
          },
          {
            "type": "text",
            "text": "$4,900.00"
          }
        ]
      }
    ]
  }
}
```

## 2. Recepción de Webhooks (Inbound Status)
Meta notifica de forma asíncrona a nuestra plataforma cuando un mensaje cambia de estado (`sent`, `delivered`, `read`, `failed`).

```json
{
  "object": "whatsapp_business_account",
  "entry": [
    {
      "id": "waba_id_mock_000",
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "statuses": [
              {
                "id": "wamid_mock_777888",
                "status": "read",
                "timestamp": "1698243600",
                "recipient_id": "whatsapp_id_mock_12345"
              }
            ]
          }
        }
      ]
    }
  ]
}
```
