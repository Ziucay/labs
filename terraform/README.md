# Installation and configuration

- Follow this instruction to setup terraform with yandex cloud:
https://cloud.yandex.ru/docs/tutorials/infrastructure-management/terraform-quickstart


## Troubleshooting

After all configuration is done, you will have to renew token

```bash
export YC_TOKEN=$(yc iam create-token)
```