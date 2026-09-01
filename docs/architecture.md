# Arquitetura

Visão geral dos componentes deste laboratório de observabilidade e como eles se conectam.

    ThinkCentre M720s (host)
    │
    ├── Node Exporter (:9100) ──────► Prometheus (:9090) ──► Grafana (:3001)
    │                                       ▲
    ├── snmp_exporter (:9116) ─────────────┘
    │         ▲
    │         │ SNMP v2c (161/UDP)
    │         │
    └── MikroTik hEX S (192.168.88.1) ──── SNMP v2c (161/UDP) ────► Zabbix
                                                                      (server + web :8081 + db)

## Componentes

| Componente | Função | Porta |
|---|---|---|
| Prometheus | Coleta e armazena métricas de host e rede | 9090 |
| Grafana | Visualização em dashboards | 3001 (mapeada para 3000) |
| Node Exporter | Expõe métricas do host (CPU, memória, disco) | 9100 |
| snmp_exporter | Traduz métricas SNMP para formato Prometheus | 9116 |
| MikroTik hEX S | Roteador físico monitorado via SNMP | 161/UDP (equipamento) |
| Zabbix (server) | Segundo pilar de monitoramento, coleta ativa/passiva | 10051 |
| Zabbix (web) | Interface de administração e dashboards | 8081 |
| Zabbix (db) | PostgreSQL, armazenamento do Zabbix | interno |

## Dois caminhos de monitoramento do MikroTik

O MikroTik é monitorado por dois pilares independentes e redundantes:

1. **Prometheus** consulta o `snmp_exporter`, que faz a query SNMP no MikroTik (módulo `if_mib`) e traduz para métricas Prometheus, visualizadas no Grafana.
2. **Zabbix** consulta o MikroTik diretamente via SNMP, com descoberta automática (LLD) de interfaces e disponibilidade (ICMP).

Essa redundância foi intencional: permite comparar dois modelos de observabilidade (pull via Prometheus/exporter vs. coleta nativa do Zabbix) dentro do mesmo laboratório.

## Decisões de design

- **Módulo `if_mib` (MIB-II genérica)** foi escolhido em vez de uma MIB proprietária MikroTik, priorizando um módulo reaproveitável para outros fabricantes de equipamentos de rede que venham a ser adicionados ao laboratório.
- **snmp.yml otimizado** de 2MB (arquivo oficial completo, com centenas de módulos) para 34KB (apenas o módulo `if_mib`), reduzindo o que é versionado no repositório sem perder funcionalidade.
- **Zabbix como segundo pilar**, não substituto do Prometheus/Grafana — o objetivo é simular um ambiente NOC/ISP real, onde múltiplas ferramentas de monitoramento frequentemente coexistem.
