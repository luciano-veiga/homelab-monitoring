# Incidente 01 — Queda simulada do snmp-exporter (InstanceDown)

## Resumo

Incidente controlado, simulado propositalmente para validar a capacidade de deteccao e resposta do laboratorio, medindo MTTD (Mean Time To Detect) e MTTR (Mean Time To Resolve) com dados reais.

## Cenario

Container `snmp-exporter` parado propositalmente (`docker compose stop snmp-exporter`), interrompendo a coleta SNMP do MikroTik via Prometheus e derrubando o job `mikrotik-snmp` para `up == 0`.

## Timeline

| Evento | Horario (UTC) | Horario (Bahia, UTC-3) |
|---|---|---|
| T0 - Prometheus detecta `up == 0` (regra InstanceDown, `for: 1m`) | 21:20:33 | 18:20:33 |
| T1 - Alertmanager envia notificacao de firing (e-mail + webhook) | 21:21:03 | 18:21:03 |
| T2 - Operador executa a correcao (`docker compose start snmp-exporter`) | 23:03:42 | 20:03:42 |
| T3 - Prometheus confirma `up == 1`, alerta resolvido | 23:03:48 | 20:03:48 |

## Indicadores

- **MTTD (T1 - T0):** ~30 segundos (dominado pelo `group_wait: 30s` do Alertmanager; a deteccao tecnica do Prometheus foi praticamente imediata apos o `for: 1m` da regra)
- **MTTR (T3 - T1):** 1h 42min 45s

## Analise

O MTTD foi rapido e dentro do esperado pela configuracao (regra com `for: 1m` + `group_wait: 30s` do Alertmanager). O MTTR foi alto porque o operador estava em outras atividades no momento do disparo do alerta, sem monitoramento ativo ou plantao formal — cenario realista para laboratorios pessoais e times pequenos sem NOC 24/7.

Esse dado reforca a importancia de notificacoes redundantes (e-mail +
webhook, ja implementadas) e evidencia a diferenca entre "o sistema de alertas funciona" (MTTD baixo, ja provado na Etapa Alertmanager) e "o processo de resposta e rapido" (depende de disponibilidade humana, plantao, escalonamento - fora do escopo tecnico do Alertmanager).

## Acao de correcao


```bash
docker compose ps
docker compose logs snmp-exporter --tail 20
docker compose start snmp-exporter
```

Diagnostico confirmou o container parado (nao um crash), sem necessidade de investigacao adicional.

## Evidencias

- E-mail de firing e resolved recebido (mesma estrutura de evidencias da Etapa Alertmanager)
- Timestamps extraidos de webhook-receiver/alerts.log

## Proximos passos

- Formalizar runbook de resposta a incidente (Etapa 7 - SRE)
- Considerar definir um SLO de MTTR para cenarios sem plantao ativo, documentando a expectativa realista em vez de uma meta irreal de resposta imediata
