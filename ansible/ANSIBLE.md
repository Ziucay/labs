# Ansible run results

```
(venv) sarvar@sarvar-H410M-H-V3:~/labs/ansible$ ansible-playbook ./playbooks/dev/main.yml --diff

PLAY [Deploy docker] ******************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************
ok: [vm01]

TASK [docker : include_tasks] *********************************************************************************************************************
included: /home/sarvar/labs/ansible/roles/docker/tasks/setup-Debian.yml for vm01

TASK [docker : Ensure old versions of Docker are not installed.] **********************************************************************************
ok: [vm01]

TASK [docker : Ensure dependencies are installed.] ************************************************************************************************
ok: [vm01]

TASK [docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] *******************************************
ok: [vm01]

TASK [docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ****************************************************************
skipping: [vm01]

TASK [docker : Add Docker apt key.] ***************************************************************************************************************
changed: [vm01]

TASK [docker : Ensure curl is present (on older systems without SNI).] ****************************************************************************
skipping: [vm01]

TASK [docker : Add Docker apt key (alternative for older systems without SNI).] *******************************************************************
skipping: [vm01]

TASK [docker : Add Docker repository.] ************************************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable

changed: [vm01]

TASK [docker : Install Docker packages.] **********************************************************************************************************
skipping: [vm01]

TASK [docker : Install Docker packages (with downgrade option).] **********************************************************************************
ok: [vm01]

TASK [docker : Install docker-compose plugin.] ****************************************************************************************************
skipping: [vm01]

TASK [docker : Install docker-compose-plugin (with downgrade option).] ****************************************************************************
skipping: [vm01]

TASK [docker : Ensure /etc/docker/ directory exists.] *********************************************************************************************
skipping: [vm01]

TASK [docker : Configure Docker daemon options.] **************************************************************************************************
skipping: [vm01]

TASK [docker : Ensure Docker is started and enabled at boot.] *************************************************************************************
ok: [vm01]

TASK [docker : Ensure handlers are notified now to avoid firewall conflicts.] *********************************************************************

TASK [docker : include_tasks] *********************************************************************************************************************
included: /home/sarvar/labs/ansible/roles/docker/tasks/install_compose.yml for vm01

TASK [docker : Check current docker-compose version.] *********************************************************************************************
ok: [vm01]

TASK [docker : set_fact] **************************************************************************************************************************
ok: [vm01]

TASK [docker : Delete existing docker-compose version if it's different.] *************************************************************************
ok: [vm01]

TASK [docker : Install Docker Compose (if configured).] *******************************************************************************************
changed: [vm01]

TASK [docker : Get docker group info using getent.] ***********************************************************************************************
skipping: [vm01]

TASK [docker : Check if there are any users to add to the docker group.] **************************************************************************

TASK [docker : include_tasks] *********************************************************************************************************************
skipping: [vm01]

PLAY RECAP ****************************************************************************************************************************************
vm01                       : ok=14   changed=3    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0  
```

# ansible-inventory results

```
(venv) sarvar@sarvar-H410M-H-V3:~/labs/ansible$ ansible-inventory ./inventory/yandex_cloud.yml --list
{
    "_meta": {
        "hostvars": {
            "vm01": {
                "ansible_become": true,
                "ansible_host": "158.160.14.35",
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "vm01"
        ]
    }
}
```

# Bonus task

1. Install `yandexcloud`

```commandline
pip install yandexcloud
```

2. Create `yc_oauth` file in ansible root folder, put yc OAuth token in it 

Running playbook

```
(venv) sarvar@sarvar-H410M-H-V3:~/labs/ansible$ ansible-playbook ./playbooks/dev/main.yml --diff

PLAY [Deploy docker] *****************************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************
ok: [terraform-devops]

TASK [docker : include_tasks] ********************************************************************************************************************
included: /home/sarvar/labs/ansible/roles/docker/tasks/setup-Debian.yml for terraform-devops

TASK [docker : Ensure old versions of Docker are not installed.] *********************************************************************************
ok: [terraform-devops]

TASK [docker : Ensure dependencies are installed.] ***********************************************************************************************
ok: [terraform-devops]

TASK [docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ******************************************
ok: [terraform-devops]

TASK [docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ***************************************************************
skipping: [terraform-devops]

TASK [docker : Add Docker apt key.] **************************************************************************************************************
changed: [terraform-devops]

TASK [docker : Ensure curl is present (on older systems without SNI).] ***************************************************************************
skipping: [terraform-devops]

TASK [docker : Add Docker apt key (alternative for older systems without SNI).] ******************************************************************
skipping: [terraform-devops]

TASK [docker : Add Docker repository.] ***********************************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable

changed: [terraform-devops]

TASK [docker : Install Docker packages.] *********************************************************************************************************
skipping: [terraform-devops]

TASK [docker : Install Docker packages (with downgrade option).] *********************************************************************************
ok: [terraform-devops]

TASK [docker : Install docker-compose plugin.] ***************************************************************************************************
skipping: [terraform-devops]

TASK [docker : Install docker-compose-plugin (with downgrade option).] ***************************************************************************
skipping: [terraform-devops]

TASK [docker : Ensure /etc/docker/ directory exists.] ********************************************************************************************
skipping: [terraform-devops]

TASK [docker : Configure Docker daemon options.] *************************************************************************************************
skipping: [terraform-devops]

TASK [docker : Ensure Docker is started and enabled at boot.] ************************************************************************************
ok: [terraform-devops]

TASK [docker : Ensure handlers are notified now to avoid firewall conflicts.] ********************************************************************

TASK [docker : include_tasks] ********************************************************************************************************************
included: /home/sarvar/labs/ansible/roles/docker/tasks/install_compose.yml for terraform-devops

TASK [docker : Check current docker-compose version.] ********************************************************************************************
ok: [terraform-devops]

TASK [docker : set_fact] *************************************************************************************************************************
ok: [terraform-devops]

TASK [docker : Delete existing docker-compose version if it's different.] ************************************************************************
ok: [terraform-devops]

TASK [docker : Install Docker Compose (if configured).] ******************************************************************************************
changed: [terraform-devops]

TASK [docker : Get docker group info using getent.] **********************************************************************************************
skipping: [terraform-devops]

TASK [docker : Check if there are any users to add to the docker group.] *************************************************************************

TASK [docker : include_tasks] ********************************************************************************************************************
skipping: [terraform-devops]

PLAY RECAP ***************************************************************************************************************************************
terraform-devops           : ok=14   changed=3    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0 
```

Inventory


```
(venv) sarvar@sarvar-H410M-H-V3:~/labs/ansible$ ansible-inventory ./inventory/yacloud_compute.yml --list
{
    "_meta": {
        "hostvars": {
            "terraform-devops": {
                "ansible_host": "130.193.43.158"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yacloud"
        ]
    },
    "yacloud": {
        "hosts": [
            "terraform-devops"
        ]
    }
}
```

# Lab 6

```
(venv) sarvar@sarvar-H410M-H-V3:~/labs/ansible$ ansible-playbook ./playbooks/dev/app_python.yml --diff

PLAY [Deploy Python app] ******************************************************************************

TASK [Gathering Facts] ********************************************************************************
ok: [terraform-devops]

TASK [docker : include_tasks] *************************************************************************
included: /home/sarvar/labs/ansible/roles/docker/tasks/setup-Debian.yml for terraform-devops

TASK [docker : Ensure old versions of Docker are not installed.] **************************************
ok: [terraform-devops]

TASK [docker : Ensure dependencies are installed.] ****************************************************
ok: [terraform-devops]

TASK [docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ***
ok: [terraform-devops]

TASK [docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ********************
skipping: [terraform-devops]

TASK [docker : Add Docker apt key.] *******************************************************************
ok: [terraform-devops]

TASK [docker : Ensure curl is present (on older systems without SNI).] ********************************
skipping: [terraform-devops]

TASK [docker : Add Docker apt key (alternative for older systems without SNI).] ***********************
skipping: [terraform-devops]

TASK [docker : Add Docker repository.] ****************************************************************
ok: [terraform-devops]

TASK [docker : Upgrade pip] ***************************************************************************
changed: [terraform-devops]

TASK [docker : install python modules for docker] *****************************************************
ok: [terraform-devops] => (item={'name': 'docker'})
ok: [terraform-devops] => (item={'name': 'docker-compose'})

TASK [docker : Install Docker packages.] **************************************************************
skipping: [terraform-devops]

TASK [docker : Install Docker packages (with downgrade option).] **************************************
ok: [terraform-devops]

TASK [docker : Install docker-compose plugin.] ********************************************************
skipping: [terraform-devops]

TASK [docker : Install docker-compose-plugin (with downgrade option).] ********************************
skipping: [terraform-devops]

TASK [docker : Ensure /etc/docker/ directory exists.] *************************************************
skipping: [terraform-devops]

TASK [docker : Configure Docker daemon options.] ******************************************************
skipping: [terraform-devops]

TASK [docker : Ensure Docker is started and enabled at boot.] *****************************************
ok: [terraform-devops]

TASK [docker : Ensure handlers are notified now to avoid firewall conflicts.] *************************

TASK [docker : include_tasks] *************************************************************************
included: /home/sarvar/labs/ansible/roles/docker/tasks/install_compose.yml for terraform-devops

TASK [docker : Check current docker-compose version.] *************************************************
ok: [terraform-devops]

TASK [docker : set_fact] ******************************************************************************
ok: [terraform-devops]

TASK [docker : Delete existing docker-compose version if it's different.] *****************************
skipping: [terraform-devops]

TASK [docker : Install Docker Compose (if configured).] ***********************************************
skipping: [terraform-devops]

TASK [docker : Get docker group info using getent.] ***************************************************
skipping: [terraform-devops]

TASK [docker : Check if there are any users to add to the docker group.] ******************************

TASK [docker : include_tasks] *************************************************************************
skipping: [terraform-devops]

TASK [webapp : Wipe if flag set] **********************************************************************
included: /home/sarvar/labs/ansible/roles/webapp/tasks/wipe.yml for terraform-devops

TASK [webapp : Wipe the docker] ***********************************************************************
fatal: [terraform-devops]: FAILED! => {"changed": false, "msg": "Configuration error - yaml.parser.ParserError: while parsing a block mapping\n  in \"/app/docker-compose.yml\", line 3, column 5\nexpected <block end>, but found '<scalar>'\n  in \"/app/docker-compose.yml\", line 3, column 35"}
...ignoring

TASK [webapp : Delete folder] *************************************************************************
--- before
+++ after
@@ -1,10 +1,4 @@
 {
     "path": "/app",
-    "path_content": {
-        "directories": [],
-        "files": [
-            "/app/docker-compose.yml"
-        ]
-    },
-    "state": "directory"
+    "state": "absent"
 }

changed: [terraform-devops]

TASK [webapp : Create folder] *************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/app",
-    "state": "absent"
+    "state": "directory"
 }

changed: [terraform-devops]

TASK [webapp : Install Docker-compose] ****************************************************************
--- before
+++ after: /home/sarvar/.ansible/tmp/ansible-local-25758c0_9klr3/tmpry3hqwh9/docker-compose.yml
@@ -0,0 +1,7 @@
+services:
+  moscow_time:
+    image: ziucay/pythonapp:latest
+    container_name: moscow_time
+    ports:
+      - "8000:8000"
+    restart: always
\ No newline at end of file

changed: [terraform-devops]

TASK [webapp : Start docker-compose service] **********************************************************
changed: [terraform-devops]

PLAY RECAP ********************************************************************************************
terraform-devops           : ok=20   changed=5    unreachable=0    failed=0    skipped=13   rescued=0    ignored=1   


```
