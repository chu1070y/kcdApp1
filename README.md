# 실행방법

> module/aws에 ip주소 변경 필요

##### 도커 빌드

```docker build -t kcdapp1 .```

##### 컨테이너 띄우기 (fastapi & sqs)

```docker-compose -f ./docker-compose.yml up -d```

# sqs 큐 생성

```
docker exec -it localstack sh
aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name test1
```

