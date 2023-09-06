# Airflow for K8S

`KubernetesPodOperator`는 Kuberntes cluster에서 Airflow가 실행중일 때 사용자가 원하는 docker image에서 task를 실행하는 task를 만드는 Operator이다.
Airflow는 여러 가지 서비스들을 Orchestration할 수 있다는 강점을 가지고 있다.
직접 데이터를 처리하는 서비스들을 여러 개 만들수도 있는데 이 때 각각의 서비스의 의존성이 다를 수 있는데 이 때 KubernetesPodOperator 를 사용하면 독립적인 컨테이너 환경에서 서비스를 실행할 수 있다.

## Installation

KubernetesPodOperator가 포함된 kubernetes provider package를 설치하기 위해서는 아래 커멘드를 사용하면 된다:

```bash
$ pip install apache-airflow[cncf.kubernetes]
```

## References

- [Airflow KubernetesPodOperator](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/operators.html)
