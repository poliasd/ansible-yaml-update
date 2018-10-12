YAML Config Update
=========

This role will update the configuration of yaml files


Role Variables
--------------

in var/main.yaml:

services:
  - "/path/to/the/file/that/will/be/changed1":
    params:
      - yaml configuration that will be updated
  - "/path/to/the/file/that/will/be/changed2":
    params:
      - yaml configuration that will be updated    

 ### Run the role:
```
ansible-playbook -i hosts roles.yaml --ask-pass --sudo
```