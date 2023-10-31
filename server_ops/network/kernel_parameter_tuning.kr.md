# 리눅스 커널 파라미터 튜닝

리눅스 커널 파라미터 튜닝은 서버 성능 최적화와 많은 관련이 있다.
특히 네트워크 관련 커널 파라미터들의 경우, DevOps적 관점에서 많은 튜닝이 필요한 분야이다.

## 네트워크 최적화를 위한 커널 파라미터 권고값

| 파라미터 | 설명 | 권고값 |
| --- | --- | --- |
| net.ipv4.tcp_keepalive_intvl | TCP TIME_WAIT 상태를 줄이기 위한 설정 | 15 |
| net.ipv4.tcp_keepalive_probes | 손실된 TCP 상태 감지 시간 설정 | 5 |
| net.ipv4.tcp_keepalive_time | keep alive 시간을 설정 | 30 |
| net.ipv4.ip_local_port_range | 사용할 수 있는 포트 범위를 설정 | 1024 - 65000 |
| net.core.netdev_max_backlog | 백로그에 들어오는 소켓 개수를 설정 | 2500 |
| net.ipv4.tcp_retries1 | TCP 연결에 문제가 있을 때 연결을 재시도하는 횟수 | 3 |
| net.ipv4.tcp_retries2 | TCP 연결을 끊기 전에 재시도하는 횟수 | 3 |
| net.core.rmem_max | TCP 수신 버퍼크기 최대값 설정 | 56777216 |
| net.core.rmem_default | TCP 수신 버퍼크기 기본값 설정 | 16777216 |
| net.core.wmem_max | TCP 전송 버퍼크기 최대값 설정 | 56777216 |
| net.core.wmem_default | TCP 전송 버퍼크기 기본값 설정 | 16777216 |
| net.ipv4.tcp_window_scaling | 65kb 이상의 큰 TCP 윈도우 스케일링 사용 | 1 |
| net.ipv4.tcp_orphan_retries | 서버 측에서 닫은 TCP 연결을 끊기 전에 확인하는 횟수 (기본값은 7로 50초에서 16분까지 소요) | 0 |
| net.ipv4.tcp_sack | SYNC 패킷을 전송한 후 일부 ACK를 받지 못했을 경우 선택적으로 받지 못한 ACK 패킷을 받도록 설정 (0은 받지 않는 설정, 1은 패킷 유실이 많은 사이트에 설정) | 0 |
| net.ipv4.tcp_fin_timeout | FIN 타임아웃을 시간을 줄여 FD를 빠르게 확보 | 15 |

## backlog

backlog는 물리적 네트워크 포트에서 패킷을 쌓아두는 커널의 큐 크기이다.
백로그가 크기만큼 요청 패킷을 쌓아놓을 수 있으며, 백로그 큐가 가득차게 되면 설정에 따라 패킷이 drop 되는 등의 이슈가 발생할 수 있다.

| 파라미터 | 설명 |
| --- | --- |
| net.core.netdev_max_backlog | 각 네트워크 장치 별로 커널이 처리하도록 쌓아두는 queue의 크기 |
| net.core.somaxconn | listen으로 바인딩 된 서버 내에서 accept를 기다리는 소켓의 최대 수 |
| net.ipv4.tcp_max_syn_backlog | SYN_RECEIVED 상태의 소켓(즉, connection incompleted)을 위한 queue |
| net.ipv4.tcp_syncookies | 1로 설정하면 TCP 연결에서 SYN Backlog가 가득찼을때 SYN패킷을 SYN Backlog에 저장하지 않고 ISN(Initial Sequence Number 을 만들어서 SYN + ACK를 클라이언트로 전송하여 SYN 패킷 Drop 방지 |

```bash
# net.core.netdev_max_backlog의 값을 확인
sysctl net.core.netdev_max_backlog

# net.core.netdev_max_backlog의 값을 30,000으로 설정
sudo sysctl -w net.core.netdev_max_backlog=30000

# net.core.somaxconn 값 확인
sysctl net.core.somaxconn

# net.core.somaxconn 값을 4096으로 증가
sudo sysctl -w net.core.somaxconn=4096

# net.ipv4.tcp_max_syn_backlog 값 확인
sysctl net.ipv4.tcp_max_syn_backlog

# net.ipv4.tcp_max_syn_backlog 값을 4096으로 설정 (net.core.somaxconn 값이 최대값임)
sudo sysctl -w net.ipv4.tcp_max_syn_backlog=4096

# net.ipv4.tcp_syncookies 값을 확인
sysctl net.ipv4.tcp_syncookies

# net.ipv4.tcp_syncookies 값을 1로 설정 (true)
#
# 1로 설정하면 TCP 연결에서 SYN Backlog가 가득찼을때 SYN패킷을 SYN Backlog에 저장하지 않고
# ISN(Initial Sequence Number 을 만들어서 SYN + ACK를 클라이언트로 전송하여 SYN 패킷 Drop 방지
#
sudo sysctl -w net.ipv4.tcp_syncookies=1
```
