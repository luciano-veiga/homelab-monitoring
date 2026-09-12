# Runbook: HighCPUUsageThinkCentre

## Alerta
- **Nome:** HighCPUUsageThinkCentre
- **Severidade:** Alta
- **Regra Prometheus:** uso de CPU do ThinkCentre acima do limiar definido em rules.yml, sustentado pelo tempo de `for`
- **Canais de notificação:** e-mail (Gmail SMTP) + webhook local

## O que significa
O ThinkCentre está com uso de CPU sustentado acima do normal. Pode indicar processo travado, carga de trabalho legítima alta, ou (em teste) geração artificial de carga.

## Verificação imediata
1. Checar status do alerta no Prometheus: Alerts > HighCPUUsageThinkCentre
2. Confirmar entrega da notificação no Alertmanager (e-mail e/ou webhook)
3. `top` ou `htop` no ThinkCentre para identificar processo consumindo CPU
4. `docker stats` para ver se algum container específico está consumindo mais que o esperado

## Diagnóstico
1. Identificar processo/container responsável via `top`/`docker stats`
2. Verificar se é pico pontual (job, backup, atualização) ou sustentado
3. Checar Grafana (dashboard CPU) para visualizar tendência e comparar com histórico

## Resolução
1. Processo legítimo (pico esperado): aguardar normalização e documentar
2. Processo travado/anômalo: reiniciar o serviço ou container responsável
3. Container consumindo demais: considerar limitar recursos no docker-compose.yml (cpus:)
4. Confirmar retorno ao normal: Grafana e Prometheus > Alerts > resolved

## Escalonamento
Ambiente de laboratório pessoal, sem plantão formal. Em produção real, esse seria o ponto de acionar o responsável de plantão se a CPU não normalizar em X minutos ou se impactar outros serviços.

## Referência real
Testado de ponta a ponta na etapa do Alertmanager: carga de CPU gerada via stress-ng no ThinkCentre, alerta passou por inactive → pending → firing no Prometheus, e foi entregue com sucesso nos dois canais (e-mail e webhook), confirmado em webhook-receiver/alerts.log. Ainda não há incidente real (não simulado) registrado para este alerta.

## Prevenção
- Monitorar tendência de CPU no Grafana para antecipar picos recorrentes
- Ajustar o limiar e o `for` da regra caso picos curtos e legítimos gerem falso positivo
- Definir limites de CPU por container no docker-compose.yml para conter processos anômalos
