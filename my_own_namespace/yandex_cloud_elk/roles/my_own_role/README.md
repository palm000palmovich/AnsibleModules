# my_own_role

Роль-обёртка над модулем `my_own_namespace.yandex_cloud_elk.my_own_module`:
создаёт текстовый файл с заданным содержимым на удалённом хосте.

## Переменные роли

| Переменная           | По умолчанию                       | Описание                                   |
|-----------------------|-------------------------------------|---------------------------------------------|
| `my_own_role_path`    | `/tmp/my_own_module_test.txt`       | Путь к файлу, который будет создан          |
| `my_own_role_content` | `"Hello from my_own_module!"`       | Содержимое, которое будет записано в файл   |

Значения по умолчанию заданы в [`defaults/main.yml`](defaults/main.yml) и могут
быть переопределены при вызове роли.

## Пример использования

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
