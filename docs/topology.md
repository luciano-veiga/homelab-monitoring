# Topologia de Rede

Registro vivo da topologia de rede do laboratório. Atualizar sempre que um equipamento ou enlace novo for adicionado.

## Diagrama atual

    Internet
       │
       │ ether1 (DHCP, distância 1 — WAN principal)
       │ pppoe-out1 (PPPoE, distância 2 — rota de teste, CGNAT)
       │
    MikroTik hEX S (HomeLab) — 192.168.88.1
       │
       │ ether2
       │
    ThinkCentre M720s (host)
       └── Prometheus / Grafana / Node Exporter / Zabbix

Portas restantes do MikroTik (ether3-5, sfp1, bridge) disponíveis para expansão do laboratório.

## Equipamentos

| Equipamento | Modelo | IP de gerência | Observação |
|---|---|---|---|
| Roteador | MikroTik hEX S | 192.168.88.1 | RouterOS 6.49.20 (long-term), MIPS 1004Kc V2.15, 4 cores, 880 MHz, 256 MiB RAM |
| Host | ThinkCentre M720s | — | Roda toda a stack de monitoramento via Docker Compose |

## Enlaces WAN

| Interface | Tipo | Distância da rota | Status |
|---|---|---|---|
| ether1 | DHCP | 1 (principal) | Ativo |
| pppoe-out1 | PPPoE | 2 (paralelo/teste) | Ativo, IP via CGNAT (100.64.x.x) |

## Notas

- IPv6 habilitado no MikroTik (pacote `ipv6` ativado + reboot); DHCPv6 Client configurado na `pppoe-out1`, mas a sessão permanece em "searching" — solicitação DHCPv6 enviada corretamente (confirmado via Torch), sem resposta do lado do provedor para essa sessão específica. Troubleshooting pausado, pendente de checagem do lado do provedor (BRAS/RADIUS).
- `ether5` foi removida do bridge antes de configurar como cliente PPPoE, para evitar conflito de papéis na interface.
