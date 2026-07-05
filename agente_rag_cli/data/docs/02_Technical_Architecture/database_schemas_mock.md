# Esquemas de Base de Datos y Trazabilidad (Mocks)

La persistencia de datos sigue reglas de diseño *Multi-Tenant* e inmutabilidad estricta. Todo evento financiero se respalda en tablas de solo inserción (Append-Only) para generar un *Audit Trail* robusto.

## 1. Diagrama Entidad-Relación (Mermaid ERD)
*Todos los nombres, IDs y atributos mostrados representan la arquitectura, no datos reales de clientes.*

```mermaid
erDiagram
    TENANTS ||--o{ SUBSCRIPTIONS : "has"
    TENANTS ||--o{ USERS : "employs"
    SUBSCRIPTIONS ||--o{ INVOICES : "generates"
    INVOICES ||--o{ AUDIT_LOGS : "triggers"

    TENANTS {
        uuid id PK
        string business_name
        string tier_level
        timestamp created_at
    }

    SUBSCRIPTIONS {
        uuid id PK
        uuid tenant_id FK
        string status "active | past_due | canceled"
        string gateway_sub_id "Token Stripe"
        timestamp next_billing_date
    }

    INVOICES {
        uuid id PK
        uuid subscription_id FK
        decimal amount_due
        string currency
        string payment_status "paid | open | void"
    }

    AUDIT_LOGS {
        uuid id PK
        uuid entity_id "Polymorphic"
        string event_type "invoice.paid | msg.sent"
        json payload_snapshot "Immutable state"
        timestamp recorded_at
    }
```

## 2. Inmutabilidad y Audit Logs
La tabla `AUDIT_LOGS` está estructurada para cumplir con normativas de auditoría financiera (ej. SOX compliance adaptado). No se permiten operaciones `UPDATE` o `DELETE` sobre estos registros. Cualquier modificación en un `INVOICE` requiere la creación de un nuevo registro correctivo (Nota de Crédito) y un nuevo *Audit Log*.
