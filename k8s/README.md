# Output of `kubectl get pods,svc`

```
NAME                             READY   STATUS    RESTARTS   AGE
pod/pythonapp-7b77d96fd5-cj97m   1/1     Running   0          10m

NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          171m
service/pythonapp    LoadBalancer   10.103.187.0   <pending>     8000:30303/TCP   4m45s

```

## Output of `kubectl get pods,svc` from yaml files

```
NAME                                        READY   STATUS    RESTARTS   AGE
pod/pythonapp-deployment-777778d7f4-4tgds   1/1     Running   0          27m
pod/pythonapp-deployment-777778d7f4-k4sxp   1/1     Running   0          27m
pod/pythonapp-deployment-777778d7f4-wqjph   1/1     Running   0          27m

NAME                        TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes          ClusterIP      10.96.0.1      <none>        443/TCP          3h28m
service/pythonapp-service   LoadBalancer   10.96.15.170   <pending>     8000:32756/TCP   60s

```

## Output of `minikube service --all`

```
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|-------------------|-------------|---------------------------|
| NAMESPACE |       NAME        | TARGET PORT |            URL            |
|-----------|-------------------|-------------|---------------------------|
| default   | pythonapp-service |        8000 | http://192.168.49.2:30896 |
|-----------|-------------------|-------------|---------------------------|
🎉  Opening service default/pythonapp-service in default browser...


```

## Outputs for extra app

```
NAME                                       READY   STATUS    RESTARTS   AGE
pod/kotlinapp-deployment-c59fd6479-4f22s   1/1     Running   0          65s
pod/kotlinapp-deployment-c59fd6479-t697w   1/1     Running   0          65s
pod/kotlinapp-deployment-c59fd6479-x6q9p   1/1     Running   0          65s

NAME                        TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kotlinapp-service   LoadBalancer   10.109.212.63   <pending>     8080:32684/TCP   39s
service/kubernetes          ClusterIP      10.96.0.1       <none>        443/TCP          5h12m



|-----------|-------------------|-------------|---------------------------|
| NAMESPACE |       NAME        | TARGET PORT |            URL            |
|-----------|-------------------|-------------|---------------------------|
| default   | kotlinapp-service |        8080 | http://192.168.49.2:32684 |
|-----------|-------------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🎉  Opening service default/kotlinapp-service in default browser...

```
