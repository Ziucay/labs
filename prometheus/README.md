```bash
docker build -t my-prometheus .

docker run -d -p 9090:9090 --rm --name my-prometheus --network-alias my-prometheus  my-prometheus
```
