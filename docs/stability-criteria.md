# Critérios de Estabilidade (SLI/SLO)

Este documento define os indicadores (SLI) e objetivos (SLO) de estabilidade para cada componente do laboratório. Cresce conforme novos equipamentos e monitoramentos são adicionados ao repositório.

| Componente | Indicador (SLI) | Objetivo (SLO) | Como validar |
|---|---|---|---|
| Prometheus | Disponibilidade do target `prometheus` | `up{job="prometheus"} == 1` por >= 99% do tempo em janela de 24h | Query no Prometheus + captura de tela |
| Node Exporter | Disponibilidade do target `node-exporter` | `up{job="node-exporter"} == 1` por >= 99% do tempo em janela de 24h | Query no Prometheus |
| Grafana | Carregamento do dashboard após restart | Dashboard exibe dados em até 60s após `docker compose up -d` | Teste manual documentado com print |
| Stack (geral) | Recuperação após reinício completo | Stack completo (`down && up -d`) volta a coletar sem intervenção manual | Teste documentado em `incidents/` ou `etapas/` |
| MikroTik (SNMP via Prometheus) | Disponibilidade do target mikrotik-snmp | up{job="mikrotik-snmp"} == 1 por >= 99% do tempo em janela de 24h | Query no Prometheus + grafico no Grafana |
| Zabbix | Disponibilidade do zabbix-server | Zabbix server is running = Yes por >= 99% do tempo | Dashboard Global view + item zabbix[process,...] |

## Histórico de validação

| Data | Componente | Resultado | Evidência |
|---|---|---|---|
| 2026-08-27 | Prometheus | up | curl /api/v1/targets |
| 2026-08-27 | Node Exporter | up | curl /api/v1/targets |

| 2026-08-28 | MikroTik hEX S | up (apos correcao de firewall e community) | snmpwalk via ThinkCentre |
| 2026-08-29 | MikroTik hEX S (via Prometheus) | up | curl /api/v1/targets + grafico no Grafana |
| 2026-08-30 | Zabbix (server+web+db) | up | Dashboard Global view, Zabbix server is running: Yes |
| 2026-08-30 | MikroTik hEX S (via Zabbix) | up | Latest data com 75 itens coletando (LLD SNMP) |
