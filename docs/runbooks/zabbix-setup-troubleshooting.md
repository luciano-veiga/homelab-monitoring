# Runbook: Configuracao do Zabbix (Docker Compose)

## Contexto

Adicao do Zabbix (server, web, banco PostgreSQL) ao laboratorio via Docker Compose, como segundo pilar de monitoramento ao lado do Prometheus/Grafana.

## Problema 1: conflito de porta 8080

Ao subir o zabbix-web pela primeira vez, o Docker retornou erro de porta ja alocada:

Bind for :::8080 failed: port is already allocated

Diagnostico:

sudo ss -tlnp | grep 8080
docker ps --format "table {{.Names}}\t{{.Ports}}" | grep 8080

Resultado: a porta 8080 ja estava em uso pelo container evolution-evolution-api-1 (stack de automacao/IA local rodando no mesmo host).

Solucao: mapear o zabbix-web para a porta 8081 externa, mantendo a porta interna 8080 do container:

ports:
  - "8081:8080"

## Problema 2: campo SNMP community pre-preenchido incorretamente

Ao criar o host do
MikroTik no Zabbix com interface SNMP, o campo "SNMP community" veio pre-preenchido com uma macro padrao ({$SNMP_COMMUNITY}) em vez do valor real usado no equipamento (public, ja validado nos testes anteriores com snmpwalk).

Solucao: substituir manualmente o valor do campo por "public" antes de salvar o host.

## Resultado

Apos as duas correcoes, o host MikroTik HomeLab foi criado com sucesso no Zabbix, com o template "Network Generic Device by SNMP" vinculado. A descoberta automatica (LLD) identificou 75 itens, incluindo ICMP ping/loss/response time e metricas de todas as interfaces (bridge, ether1-5, pppoe-out1), confirmando coleta de dados real minutos apos a configuracao.
