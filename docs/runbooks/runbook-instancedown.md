# Runbook: InstanceDown

## Alerta
- **Nome:** InstanceDown
- **Severidade:** Crítica
- **Regra Prometheus:** target fora do ar (up == 0) por tempo definido em rules.yml
- **Canais de notificação:** e-mail (Gmail SMTP) + webhook local

## O que significa
Um target monitorado (ex: snmp-exporter, node-exporter) parou de responder ao scrape do Prometheus. Pode indicar container parado, falha de rede ou equipamento desligado.

## Verificação imediata
1. Checar status do alerta no Prometheus: Alerts > InstanceDown
2. Confirmar no Alertmanager se a notificação foi entregue (e-mail e/ou webhook)
3. `docker ps` no ThinkCentre para ver se o container relacionado está rodando
4. Se for equipamento externo (ex: MikroTik), testar ping direto: `ping 192.168.88.1`

## Diagnóstico
1. `docker logs <container>` para erro de crash
2. Se container ok mas sem resposta: checar rede (`docker network inspect`)
3. Se equipamento físico: checar energia, cabo, porta de switch

## Resolução
1. Container parado: `docker compose up -d <serviço>`
2. Equipamento físico desligado: religar e confirmar boot completo
3. Confirmar retorno do target: Prometheus > Targets > status UP

## Escalonamento
Ambiente de laboratório pessoal, sem plantão formal. Em produção real, esse seria o ponto de acionar o responsável de plantão se não resolvido em X minutos.

## Referência real (Incidentes 01 e 02)
| Incidente | Causa | MTTD | MTTR |
|---|---|---|---|
| 01 | Container snmp-exporter parado (simulado) | ~30s | 1h42min |
| 02 | Desligamento físico real do MikroTik | ~30s | ~5min |

MTTD consistente (~30s) nos dois casos, validando o tempo de detecção do Prometheus/Alertmanager. MTTR varia conforme disponibilidade do operador, não da ferramenta.

## Prevenção
- Manter scrape_interval e for adequados pra não gerar falso positivo em reinícios rápidos
- Documentar toda mudança física planejada como manutenção (ver runbook de mudança planejada), não como incidente
