# Protocolos de Optimización UX/UI y Accesibilidad

Nuestra interfaz está diseñada para minimizar la carga cognitiva del usuario corporativo, maximizando la eficiencia operativa. Todo diseño debe apegarse a los siguientes estándares de Grado Industrial.

## 1. Accesibilidad (WCAG 2.1 Nivel AA)
*   **Contraste de Color:** Todos los textos, botones primarios (ej. "Pagar Ahora", "Emitir Factura") y alertas deben tener un ratio de contraste mínimo de 4.5:1 contra su fondo.
*   **Navegación por Teclado:** Toda acción transaccional debe ser accesible vía `Tab` y accionable vía `Enter` o `Espacio`. El estado `:focus` debe ser claramente visible (ej. anillo de contorno de 2px azul).

## 2. Micro-Interacciones y Prevención de Errores
*   **Prevención de Doble Carga Financiera:** Inmediatamente después de que un usuario hace clic en "Procesar Cobro", el botón debe pasar a estado `disabled` e inyectar un *spinner* de carga para prevenir clics dobles que generen cargos duplicados en la tarjeta.
*   **Esqueletos de Carga (Skeleton Loaders):** Para evitar el "salto" de contenido (Cumulative Layout Shift - CLS), las tablas de facturas y tableros de métricas (EBITDA/MRR) deben mostrar *skeletons* grises mientras se resuelven las llamadas a la API.

## 3. Estados Transaccionales Claros
Las alertas y etiquetas (*badges*) del ciclo de facturación se codifican semánticamente por color:
*   🟢 **Éxito (Verde):** `Paid`, `Active`, `Message Delivered`.
*   🟡 **Advertencia (Amarillo/Naranja):** `Past Due`, `Retry Scheduled`, `Quota Near Limit`.
*   🔴 **Crítico (Rojo):** `Canceled`, `Payment Failed`, `Message Rejected`.
