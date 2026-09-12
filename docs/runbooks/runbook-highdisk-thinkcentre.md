# Runbook: HighDiskUsageThinkCentre

## Alerta
- **Nome:** HighDiskUsageThinkCentre
- **Severidade:** Alta
- **Regra Prometheus:** espaço livre em disco do ThinkCentre abaixo do limiar definido em rules.yml
- **Canais de notificação:** e-mail (Gmail SMTP) + webhook local

## O que significa
O disco do ThinkCentre está com espaço livre abaixo do esperado. Pode indicar acúmulo de logs, imagens Docker não utilizadas, dados de métricas (Prometheus TSDB) crescendo, ou uso legítimo crescente.

## Verificação imediata
1. Checar status do alerta no Prometheus: Alerts > HighDiskUsageThinkCentre
2. Confirmar entrega da notificação no Alertmanager (e-mail e/ou webhook)
3. `df -h` no ThinkCentre para confirmar percentual real de uso
4. `du -sh /var/lib/docker/*` para identificar consumo por volumes/imagens Docker

## Diagnóstico
1. Identificar maior consumidor: logs de container, volumes órfãos, imagens antigas, dados do Prometheus
2. `docker system df` para visão geral de espaço usado por Docker
3. Checar Grafana (dashboard de disco) para ver velocidade de crescimento

## Resolução
1. Limpeza segura: `docker system prune` (imagens/containers/volumes não utilizados)
2. Logs grandes: rotacionar ou truncar logs antigos
3. Retenção do Prometheus: revisar `--storage.tsdb.retention.time` se TSDB for o principal consumidor
4. Confirmar retorno ao normal: `df -h` e Prometheus > Alerts > resolved

## Escalonamento
Ambiente de laboratório pessoal, sem plantão formal. Em produção real, esse seria o ponto de acionar o responsável de plantão se o disco continuar subindo após a limpeza inicial.

## Referência real
Testado de ponta a ponta na etapa do Alertmanager: espaço ocupado artificialmente via `fallocate` (23% para 14% livre), alerta disparou firing corretamente. Observação registrada: o webhook não recebeu a notificação de resolved (só o e-mail chegou) — ponto de atenção para investigar na configuração do webhook-receiver ou do Alertmanager.

## Prevenção
- Configurar rotação de log automática nos containers (`logging: driver: json-file, options: max-size`)
- Revisar periodicamente a retenção do Prometheus TSDB
- Investigar a falha de entrega do resolved no webhook antes de depender dele em cenário real
