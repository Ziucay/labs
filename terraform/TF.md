# Terraform

## Docker

Initial config state

```
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach            = false
    command           = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    cpu_shares        = 0
    entrypoint        = [
        "/docker-entrypoint.sh",
    ]
    env               = []
    gateway           = "172.17.0.1"
    hostname          = "7414e0666ec5"
    id                = "7414e0666ec5cd10d152e74a9d9ae6bcffb7561095057408be3d26f1dc2ae2a5"
    image             = "sha256:2d389e545974d4a93ebdef09b650753a55f72d1ab4518d17a30c0e1b3e297444"
    init              = false
    ip_address        = "172.17.0.2"
    ip_prefix_length  = 16
    ipc_mode          = "private"
    log_driver        = "json-file"
    logs              = false
    max_retry_count   = 0
    memory            = 0
    memory_swap       = 0
    must_run          = true
    name              = "tutorial"
    network_data      = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = ""
            network_name              = "bridge"
        },
    ]
    network_mode      = "default"
    privileged        = false
    publish_all_ports = false
    read_only         = false
    remove_volumes    = true
    restart           = "no"
    rm                = false
    security_opts     = []
    shm_size          = 64
    start             = true
    stdin_open        = false
    tty               = false

    ports {
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:2d389e545974d4a93ebdef09b650753a55f72d1ab4518d17a30c0e1b3e297444nginx:latest"
    keep_locally = false
    latest       = "sha256:2d389e545974d4a93ebdef09b650753a55f72d1ab4518d17a30c0e1b3e297444"
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:0b970013351304af46f322da1263516b188318682b2ab1091862497591189ff1"
}

```

State list:
```
docker_container.nginx
docker_image.nginx

```

Changes:

```
Terraform will perform the following actions:

  # docker_container.nginx must be replaced
-/+ resource "docker_container" "nginx" {
      + bridge            = (known after apply)
      ~ command           = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> (known after apply)
      + container_logs    = (known after apply)
      - cpu_shares        = 0 -> null
      - dns               = [] -> null
      - dns_opts          = [] -> null
      - dns_search        = [] -> null
      ~ entrypoint        = [
          - "/docker-entrypoint.sh",
        ] -> (known after apply)
      ~ env               = [] -> (known after apply)
      + exit_code         = (known after apply)
      ~ gateway           = "172.17.0.1" -> (known after apply)
      - group_add         = [] -> null
      ~ hostname          = "7414e0666ec5" -> (known after apply)
      ~ id                = "7414e0666ec5cd10d152e74a9d9ae6bcffb7561095057408be3d26f1dc2ae2a5" -> (known after apply)
      ~ init              = false -> (known after apply)
      ~ ip_address        = "172.17.0.2" -> (known after apply)
      ~ ip_prefix_length  = 16 -> (known after apply)
      ~ ipc_mode          = "private" -> (known after apply)
      - links             = [] -> null
      - log_opts          = {} -> null
      - max_retry_count   = 0 -> null
      - memory            = 0 -> null
      - memory_swap       = 0 -> null
      ~ name              = "tutorial" -> "nginx" # forces replacement
      ~ network_data      = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_address       = ""
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16
              - ipv6_gateway              = ""
              - network_name              = "bridge"
            },
        ] -> (known after apply)
      - network_mode      = "default" -> null
      - privileged        = false -> null
      - publish_all_ports = false -> null
      ~ security_opts     = [] -> (known after apply)
      ~ shm_size          = 64 -> (known after apply)
      - sysctls           = {} -> null
      - tmpfs             = {} -> null
        # (12 unchanged attributes hidden)

      + healthcheck {
          + interval     = (known after apply)
          + retries      = (known after apply)
          + start_period = (known after apply)
          + test         = (known after apply)
          + timeout      = (known after apply)
        }

      + labels {
          + label = (known after apply)
          + value = (known after apply)
        }

        # (1 unchanged block hidden)
    }
```

Output

```
container_id = "e85f00c3a60a964baaf074f73713cb97a9f1c4446b8943809bf470ac0a950d8e"
container_name = "nginx"
```

## Yandex cloud


```
terraform show
```

```
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2022-09-26T21:20:09Z"
    folder_id                 = "b1gikuat2qu2j0kjkpso"
    fqdn                      = "epdh6eo5pggua26rjeoh.auto.internal"
    id                        = "epdh6eo5pggua26rjeoh"
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-b"

    boot_disk {
        auto_delete = true
        device_name = "epdsv313f51cjg1kklvj"
        disk_id     = "epdsv313f51cjg1kklvj"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8lf95uopek213iph4j"
            size       = 30
            type       = "network-hdd"
        }
    }

    network_interface {
        index              = 0
        ip_address         = "192.168.10.34"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:11:33:b0:5c"
        nat                = true
        nat_ip_address     = "51.250.104.120"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e2lqh7t276t2m2jbpqqe"
    }

    placement_policy {
        host_affinity_rules = []
    }

    resources {
        core_fraction = 100
        cores         = 2
        gpus          = 0
        memory        = 2
    }

    scheduling_policy {
        preemptible = false
    }
}

# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at = "2022-09-26T21:11:07Z"
    folder_id  = "b1gikuat2qu2j0kjkpso"
    id         = "enp04f2of8lm4f3lngu3"
    labels     = {}
    name       = "network1"
    subnet_ids = [
        "e9bqsioo1uhpqe9pv4tc",
    ]
}

# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2022-09-26T21:20:08Z"
    folder_id      = "b1gikuat2qu2j0kjkpso"
    id             = "e2lqh7t276t2m2jbpqqe"
    labels         = {}
    name           = "subnet1"
    network_id     = "enp04f2of8lm4f3lngu3"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-b"
}


Outputs:

external_ip_address_vm_1 = "51.250.104.120"
internal_ip_address_vm_1 = "192.168.10.34"


```

```
terraform state list
```


```
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

Changes: 

```
~/terraform/terraform apply
yandex_vpc_network.network-1: Refreshing state... [id=enp04f2of8lm4f3lngu3]
yandex_vpc_subnet.subnet-1: Refreshing state... [id=e2lqh7t276t2m2jbpqqe]
yandex_compute_instance.vm-1: Refreshing state... [id=epdh6eo5pggua26rjeoh]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # yandex_compute_instance.vm-1 will be updated in-place
  ~ resource "yandex_compute_instance" "vm-1" {
        id                        = "epdh6eo5pggua26rjeoh"
      ~ name                      = "terraform1" -> "terraform-devops"
        # (9 unchanged attributes hidden)

        # (5 unchanged blocks hidden)
    }

Plan: 0 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_compute_instance.vm-1: Modifying... [id=epdh6eo5pggua26rjeoh]
yandex_compute_instance.vm-1: Modifications complete after 5s [id=epdh6eo5pggua26rjeoh]

Apply complete! Resources: 0 added, 1 changed, 0 destroyed.

Outputs:

external_ip_address_vm_1 = "51.250.104.120"
internal_ip_address_vm_1 = "192.168.10.34"
```

Outputs: 

```
external_ip_address_vm_1 = "51.250.104.120"
internal_ip_address_vm_1 = "192.168.10.34"
```

## Applied practices

- Using variables.tf to avoid constants in files
- Using outputs.tf for returning useful information
- Not putting PAT's and other sensitive info in config files, to avoid security leak
- Yandex mirror for terraform registry, to ease downloading providers
