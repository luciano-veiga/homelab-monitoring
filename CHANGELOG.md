# Changelog

Registro cronológico da evolução deste laboratório de observabilidade.

## 2026-08-27

- Iniciada a Etapa 1 (definição e critérios) do plano de evolução para laboratório de observabilidade estilo NOC/ISP
- Criada estrutura de pastas: docs/runbooks, etapas, incidents, diagrams, scenarios
- Criado docs/stability-criteria.md com critérios de estabilidade (SLI/SLO) para Prometheus, Node Exporter, Grafana e stack geral
- Validado: target prometheus em up, target node-exporter em up (via /api/v1/targets)

## 2026-08-28

- Iniciada a Etapa 2 (mapeamento e integracao de equipamentos)
- Primeiro equipamento de rede fisico integrado: MikroTik hEX S (RouterOS 6.49.20), monitorado via SNMP
- Troubleshooting real documentado em docs/runbooks/snmp-troubleshooting-mikrotik.md: firewall bloqueando porta 161/UDP e community SNMP desabilitada
- Adicionado MikroTik ao docs/inventory.md e docs/stability-criteria.md
- Validado com sucesso via snmpwalk a partir do ThinkCentre
