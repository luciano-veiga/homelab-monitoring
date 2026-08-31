# Inventario de Monitoramento

Lista viva de tudo que esta sendo monitorado neste laboratorio. Atualizar sempre que um equipamento ou servico novo for adicionado.

| Item | Tipo | Metodo de coleta | Porta/Endpoint | Status | Adicionado em |
|---|---|---|---|---|---|
| ThinkCentre M720s (host) | Servidor | Node Exporter | 9100 | Ativo | 2026-08-27 |
| Prometheus | Servico de monitoramento | Self-scrape | 9090 | Ativo | 2026-08-27 |
| Grafana | Visualizacao | N/A | 3001 (mapeada para 3000) | Ativo | 2026-08-27 |
| MikroTik hEX S (HomeLab) | Roteador | SNMP v2c via snmp_exporter (Prometheus) | 161/UDP + 9116/TCP | Ativo | 2026-08-28 |
| Zabbix (server + web + db) | Serviço de monitoramento | Docker Compose | 8081 (web), 10051 (server) | Ativo | 2026-08-30 |
| MikroTik hEX S (via Zabbix) | Roteador | SNMP v2c direto no Zabbix (host MikroTik HomeLab) | 161/UDP | Ativo | 2026-08-30 |
