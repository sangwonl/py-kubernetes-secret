## Usage
```
$ export REGISTRY_LOGIN_EMAIL=not@val.id
$ export REGISTRY_HOSTS=https://gcr.io
$ ./gensecret.sh ./secret.yml
$ cat ./secret.yml
apiVersion: v1
kind: Secret
metadata:
  name: myregistrykey
  type: kubernetes.io/dockercfg
  data:
    .dockercfg: wczov..sample..LmFAZ21pbYTJWrVmZMWFph
```
