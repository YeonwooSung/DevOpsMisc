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
