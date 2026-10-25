# Ansible Collection - my_own_namespace.yandex_cloud_elk

Коллекция содержит собственный модуль и роль для создания текстового файла
с заданным содержимым на удалённом хосте.

## Содержимое коллекции

### Модули

- [my_own_module](plugins/modules/my_own_module.py) — создаёт (или перезаписывает)
  текстовый файл по пути `path` с содержимым `content`. Модуль идемпотентен:
  если файл уже существует с таким же содержимым, изменений не происходит.

### Роли

- [my_own_role](roles/my_own_role) — обёртка над `my_own_module` со значениями
  параметров по умолчанию (см. `roles/my_own_role/README.md`).

## Требования

- ansible-core >= 2.15

## Пример использования

Через модуль напрямую:

```yaml
- hosts: localhost
  tasks:
    - name: Create a text file with given content
      my_own_namespace.yandex_cloud_elk.my_own_module:
        path: /tmp/my_file.txt
        content: "Hello, world!"
```

Через роль (со значениями по умолчанию или переопределёнными переменными):

```yaml
- hosts: localhost
  roles:
    - role: my_own_namespace.yandex_cloud_elk.my_own_role
      vars:
        my_own_role_path: /tmp/my_file.txt
        my_own_role_content: "Hello, world!"
```

## Лицензия

GPL-2.0-or-later

## Автор

ivan (@palm000palmovich)
