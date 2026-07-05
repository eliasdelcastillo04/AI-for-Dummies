# Protocolos de Enmascaramiento y Tokenización (PII & PCI-DSS)

Para mantener los estándares de higiene de datos y cumplir con normativas (GDPR, PCI-DSS), este documento establece las reglas obligatorias de sanitización en bases de datos y *Audit Logs*.

## 1. Reglas de Enmascaramiento Financiero (PCI-DSS)
El sistema backend tiene terminantemente prohibido almacenar el PAN (Primary Account Number) o el CVV de las tarjetas de crédito.
*   **Tokenización:** Solo se almacena el ID del token provisto por la pasarela de pago (`pm_mock_12345`).
*   **Enmascaramiento en Logs:** Si un payload de error de Stripe retorna detalles, el número de tarjeta debe sanitizarse antes de guardarse en el `AUDIT_LOG`.
    *   *Formato Aceptado:* `**** **** **** 4242`
    *   *Formato Prohibido:* `4111 1111 1111 4242`

## 2. Sanitización de Información de Identificación Personal (PII)
*   **Correos Electrónicos en Logs:** Las direcciones de email utilizadas en parámetros de búsqueda o logs de depuración deben sufrir una ofuscación parcial (Ej. `joh***@empresa.com`) o un *hashing* unidireccional (SHA-256) si se requiere indexación.
*   **Números de WhatsApp:** En los reportes analíticos para el cliente, los últimos 4 dígitos del MSISDN deben ofuscarse (`+54 9 11 4321-****`), a menos que el rol del usuario tenga permisos explícitos de `view_raw_pii`.

## 3. Prevención de Fugas de Credenciales (Secrets Leakage)
Cualquier clave que comience con `sk_live_`, `Bearer`, o `whsec_` está vetada de ser impresa en la salida estándar (STDOUT), registros de aplicación, o retornada en respuestas de la API REST hacia el front-end. El middleware global de sanitización reemplazará estos valores por `[REDACTED_SECRET]`.
