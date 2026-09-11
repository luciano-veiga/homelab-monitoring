# Incidente 02 — Desligamento fisico real do MikroTik

## Resumo

Incidente real (nao simulado como teste tecnico) causado pelo desligamento do cabo de energia do MikroTik para realizar mudancas no ambiente fisico. Diferente do Incidente 01 (parada de container), este evento validou a deteccao de falha na camada fisica do equipamento de rede.

## Cenario

Cabo de energia do MikroTik hEX S desconectado intencionalmente para realizar mudancas no ambiente fisico (reorganizacao, cabeamento, etc.). O equipamento ficou completamente sem energia durante a intervencao.

## Timeline

| Evento | Horario (UTC) | Horario (Bahia, UTC-3) |
|---|---|---|
| T0 - Prometheus detecta `up == 0` (regra InstanceDown, `for: 1m`) | 14:43:48 | 11:43:48 |
| T1 - Alertmanager envia notificacao de firing (e-mail + webhook) | 14:44:18 | 11:44:18 |
| T3 - Prometheus confirma `up == 1`, alerta resolvido | ~14:49:18 | ~11:49:18 |

## Indicadores

- **MTTD (T1 - T0):** ~30 segundos (consistente com o Incidente 01 - `for: 1m` da regra + `group_wait: 30s` do Alertmanager)
- **MTTR (aproximado):** ~5 minutos (energia religada e equipamento de volta rapidamente apos concluir a mudanca fisica)

## Analise

Este incidente reforca a validade do Incidente 01 em um cenario diferente: a falha nao veio de um container parado propositalmente para teste, mas de uma acao fisica real (desligamento do cabo de energia). O MTTD se manteve consistente (~30s), confirmando que a deteccao via SNMP/Prometheus responde igualmente bem a falhas de coleta (software) e falhas de energia (hardware) no equipamento monitorado.

O MTTR foi significativamente menor que o Incidente 01 (~5min contra ~1h42min), porque desta vez o operador estava presente e ativamente envolvido na mudanca fisica, restaurando a energia assim que a intervencao foi concluida.

## Acao de correcao

Cabo de energia reconectado ao MikroTik apos concluir a mudanca no ambiente fisico. Nenhum diagnostico adicional foi necessario, ja que a causa era conhecida desde o inicio (acao intencional, nao uma falha inesperada).

## Evidencias

![E-mails de firing e resolved na caixa de entrada](evidencias-incidente-02/01-incidente02-firing-resolved-inbox.png)
*Sequencia de notificacoes [FIRING:1] e [RESOLVED] recebidas por e-mail para o alerta InstanceDown, causado pelo desligamento fisico real do MikroTik.*

- Timestamps extraidos de `webhook-receiver/alerts.log`

## Proximos passos

- Considerar um terceiro incidente controlado simulando falha de disco ou memoria real (nao via fallocate simulado)
- Avancar para a formalizacao de runbooks SRE, consolidando os padroes observados nos Incidentes 01 e 02
