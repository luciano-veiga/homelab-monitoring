# Critérios de Estabilidade (SLI/SLO)

Este documento define os indicadores (SLI) e objetivos (SLO) de estabilidade para cada componente do laboratório. Cresce conforme novos equipamentos e monitoramentos são adicionados ao repositório.

| Componente | Indicador (SLI) | Objetivo (SLO) | Como validar |
|---|---|---|---|
| Prometheus | Disponibilidade do target `prometheus` | `up{job="prometheus"} == 1` por >= 99% do tempo em janela de 24h | Query no Prometheus + captura de tela |
| Node Exporter | Disponibilidade do target `node-exporter` | `up{job="node-exporter"} == 1` por >= 99% do tempo em janela de 24h | Query no Prometheus |
| Grafana | Carregamento do dashboard após restart | Dashboard exibe dados em até 60s após `docker compose up -d` | Teste manual documentado com print |
| Stack (geral) | Recuperação após reinício completo | Stack completo (`down && up -d`) volta a coletar sem intervenção manual | Teste documentado em `incidents/` ou `etapas/` |

## Histórico de validação

| Data | Componente | Resultado | Evidência |
|---|---|---|---|
| 2026-08-27 | Prometheus | up | curl /api/v1/targets |
| 2026-08-27 | Node Exporter | up | curl /api/v1/targets |
