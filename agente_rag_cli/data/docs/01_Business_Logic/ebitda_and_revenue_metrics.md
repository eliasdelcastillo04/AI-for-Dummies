# Métricas Financieras y de Rendimiento B2B (KPIs)

Este documento centraliza las definiciones corporativas, fórmulas de cálculo y estandarizaciones de las métricas clave de negocio. Su propósito es alinear la inteligencia de negocio y ofrecer un marco unificado de referencia.

## 1. Monthly Recurring Revenue (MRR)
Ingreso mensual normalizado y predecible generado por todas las suscripciones activas (Tenants).

**Fórmula de Cálculo:**
`MRR = Σ (Valor Anual del Contrato / 12) + (Suscripciones Mensuales)`

**Consideraciones:**
*   Excluye ingresos únicos (ej. setup fees o consultoría).
*   Se ajusta dinámicamente ante *upgrades* (Expansion MRR) y *downgrades* (Contraction MRR).

## 2. Annual Recurring Revenue (ARR)
La anualización del MRR, utilizada para valoraciones macro y predicción financiera de alto nivel.

**Fórmula de Cálculo:**
`ARR = MRR Actual * 12`

## 3. Customer Acquisition Cost (CAC)
El costo promedio invertido para adquirir un nuevo Tenant B2B.

**Fórmula de Cálculo:**
`CAC = (Gastos Totales de Ventas + Gastos de Marketing) / Nuevos Clientes Adquiridos`

## 4. Life-Time Value (LTV)
Proyección de la ganancia bruta que un cliente B2B generará durante todo su ciclo de vida en la plataforma.

**Fórmula de Cálculo:**
`LTV = (ARPU * Margen Bruto) / Customer Churn Rate`
*(ARPU: Average Revenue Per User)*

## 5. Churn Rate (Tasa de Abandono)
Mide la fuga de clientes o pérdida de ingresos recurrentes.

*   **Logo Churn:** Porcentaje de clientes B2B que cancelan su suscripción.
*   **Revenue Churn:** Porcentaje de pérdida de MRR debido a cancelaciones y *downgrades*.

## 6. EBITDA
Beneficio antes de intereses, impuestos, depreciaciones y amortizaciones. Representa la rentabilidad operativa neta de la plataforma B2B.

**Enfoque de Optimización (SaaS):**
Nuestra plataforma automatiza los ciclos de cobro y comunicaciones para reducir agresivamente el CAC, mitigar el Churn involuntario (mediante *dunning*) e impulsar la expansión (Upgrades sin fricción). Esta eficiencia operativa impacta de manera directa y positiva en los márgenes de EBITDA de nuestros clientes.
