# Etapa 01 - Definicao do Projeto e Criterios de Sucesso

## Objetivo

Estabelecer, antes de qualquer expansao do laboratorio, o que significa estabilidade para cada componente da arquitetura de observabilidade, e definir a estrutura do repositorio como um projeto vivo (nao um entregavel fechado).

## Escopo desta etapa

- Levantamento do estado atual do stack (Prometheus, Grafana, Node Exporter)
- Definicao dos criterios de estabilidade (SLI/SLO) por componente
- Criacao da estrutura de pastas que suporta crescimento continuo (docs, etapas, incidents, diagrams, scenarios)
- Inicio do inventario vivo de equipamentos e servicos monitorados

## O que foi feito

- Repositorio clonado localmente no ThinkCentre M720s (sysadmin-ThinkCentre-M720s)
- Branch etapa-01-definicao-e-criterios criada
- Estrutura de pastas criada: docs/runbooks, etapas, incidents, diagrams, scenarios
- Criado docs/stability-criteria.md com tabela SLI/SLO para Prometheus, Node Exporter, Grafana e stack geral
- Criado docs/inventory.md com os 3 itens atualmente monitorados
- Criado CHANGELOG.md para registro cronologico da evolucao do projeto

## Evidencia

Consulta aos targets do Prometheus confirmou os dois servicos em estado up:

- job=prometheus, instance=localhost:9090, health=up
- job=node-exporter, instance=node-exporter:9100, health=up

## Criterio de conclusao desta etapa

Etapa considerada concluida quando:

- [x] Criterios de estabilidade documentados e mensuraveis (SLI/SLO)
- [x] Estrutura de pastas do repositorio criada
- [x] Inventario inicial documentado
- [x] Estado atual do stack validado com evidencia real (nao suposicao)

## Proxima etapa

Etapa 02 - Inventario e mapeamento detalhado da infraestrutura simulada (definicao do que sera adicionado: MikroTik, Zabbix, etc.)
