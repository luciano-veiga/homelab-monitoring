# Runbook: Mudança Planejada (Maintenance Window)

## Objetivo
Procedimento padrão para qualquer intervenção física ou lógica planejada no laboratório (realocação de equipamento, novo hardware, reconfiguração), evitando que alarmes esperados sejam tratados como incidentes reais.

## Diferença entre Incidente e Manutenção
- **Incidente:** falha não planejada, gera MTTD/MTTR como métrica de resposta a problema
- **Manutenção:** interrupção planejada e comunicada previamente (a si mesmo, no laboratório), com alarme esperado e silenciado

## Pré-requisitos antes de iniciar
1. Definir escopo exato: quais equipamentos/serviços serão afetados
2. Definir janela estimada de duração
3. Registrar horário de início pretendido

## Procedimento

### Antes
1. Criar Silence no Alertmanager para os alertas esperados (ex: InstanceDown do equipamento afetado), com duração um pouco maior que a janela estimada
2. Registrar timestamp de início do silence
3. Confirmar no Alertmanager que o silence está ativo (Silences > Active)

### Durante
1. Registrar timestamp de início da intervenção física/lógica
2. Executar a mudança (desligar, mover, remontar, religar)
3. Registrar timestamp de religamento/retorno

### Depois
1. Confirmar retorno dos targets no Prometheus (Targets > status UP)
2. Confirmar que os alertas voltaram a inactive/resolved
3. Remover o Silence manualmente se ainda estiver ativo (ou deixar expirar)
4. Registrar timestamp de fim da manutenção

## Checklist de evidência a coletar
- [ ] Timestamp: criação do silence
- [ ] Timestamp: início da intervenção física
- [ ] Timestamp: religamento
- [ ] Timestamp: targets voltaram a UP no Prometheus
- [ ] Timestamp: fim/expiração do silence
- [ ] Print ou log do Alertmanager mostrando o silence ativo
- [ ] Print do Prometheus Targets antes e depois

## Diferença de tratamento no changelog
Mudanças planejadas entram no CHANGELOG.md e em `docs/mudancas/` (não em `incidents/`), mantendo a distinção clara entre resposta a falha e evolução controlada da infraestrutura.

## Referência
Este runbook nasceu da necessidade real de mover o MikroTik e o ThinkCentre para um novo local organizado, com preparação para instalação futura de mini rack.
