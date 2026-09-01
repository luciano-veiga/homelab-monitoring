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

## 2026-08-29

- Integrado MikroTik ao Prometheus via snmp_exporter (modulo if_mib)
- Troubleshooting documentado: incompatibilidade de versao entre snmp.yml (branch main) e imagem snmp-exporter (0.30.1), resolvido usando snmp.yml da tag v0.30.1
- Troubleshooting documentado: bind mount do prometheus.yml nao atualizava com restart, resolvido com docker compose down + up
- Job mikrotik-snmp confirmado com health up no Prometheus
- Integracao validada visualmente no Grafana (Explore) com metrica ifHCInOctets da interface ether2
- Atualizado docs/inventory.md, docs/stability-criteria.md e docs/runbooks/snmp-troubleshooting-mikrotik.md

## 2026-08-30

- Adicionado Zabbix (server, web, banco PostgreSQL) via Docker Compose como segundo pilar de monitoramento
- Troubleshooting documentado: conflito de porta 8080 com container evolution-evolution-api-1, resolvido mapeando zabbix-web para porta 8081
- Senha padrao do usuario Admin do Zabbix trocada por seguranca
- Host MikroTik HomeLab criado no Zabbix via SNMP, com template Network Generic Device by SNMP
- Troubleshooting documentado: campo SNMP community pre-preenchido incorretamente, corrigido para "public"
- Confirmados 75 itens coletando dados reais via LLD (ICMP + interfaces, incluindo pppoe-out1)
- Atualizado docs/inventory.md, docs/stability-criteria.md; criado docs/runbooks/zabbix-setup-troubleshooting.md

## 2026-08-31

- Atualizada documentação para refletir o estado real do repositório após as Etapas 2 e 3
- README.md: stack, roadmap e evidências atualizados (MikroTik/SNMP e Zabbix)
- Adicionado docs/architecture.md (visão geral dos componentes e decisões de design)
- Adicionado docs/topology.md (topologia de rede do MikroTik)
- Adicionado .gitignore
- Adicionada nota de segurança no docker-compose.yml sobre credenciais padrão
