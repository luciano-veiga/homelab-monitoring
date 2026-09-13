# Mudanca Planejada 01: Realocacao fisica do MikroTik e ThinkCentre

## Status
Concluida em 2026-09-13

## Escopo
Mover o MikroTik e o ThinkCentre para um ambiente dedicado preparado especificamente para eles, com previsao de instalacao futura de um mini rack para novos equipamentos.

## Impacto esperado
- MikroTik: perda de conectividade durante o transporte/reconexao (alerta InstanceDown esperado)
- ThinkCentre: possivel interrupcao de containers durante o desligamento/remontagem (alerta InstanceDown esperado)

## Timestamps
- Criacao do silence: 2026-09-13T11:57:44Z (08:57 BRT)
- Inicio da intervencao fisica (desligamento): ~09:00 BRT (12:00Z)
- Religamento MikroTik e ThinkCentre: ~10:47 BRT (13:47Z)
- Targets voltaram a UP no Prometheus: confirmado as ~10:47 BRT, scrapes normalizados em segundos
- Fim/expiracao do silence: 2026-09-13T13:50:00Z (10:50 BRT), expirado automaticamente sem necessidade de acao manual
- Duracao total da manutencao: ~1h47min

## Evidencias
- Print do silence ativo (Alertmanager > Silences > Active)
- Print do docker ps / docker compose up -d confirmando 10/10 containers rodando pos-boot
- Print do Prometheus Targets confirmando mikrotik-snmp, node-exporter e prometheus como UP
- Print do Zabbix confirmando que nenhum problema novo foi gerado pela manutencao (os 2 problemas existentes - interface ether3 e Zabbix agent - sao anteriores e nao relacionados)
- Print do silence expirado (Alertmanager > Silences > Expired)

## Observacoes
- Horarios de desligamento/religamento estimados a partir do timestamp do silence e do uptime dos containers, nao cronometrados manualmente em tempo real. Melhoria para a proxima mudanca planejada: cronometrar timestamps exatos no momento da acao.
- Zabbix nao gerou nenhum problema novo relacionado a manutencao, apenas o alerta esperado de restart do host (severidade Warning, autoresolvido).
- Nenhum alerta de e-mail ou webhook disparado durante a janela do silence, confirmando a eficacia da pratica de Maintenance Window.

## Runbook de referencia
docs/runbooks/runbook-mudanca-planejada.md
