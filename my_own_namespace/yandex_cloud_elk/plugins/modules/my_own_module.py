#!/usr/bin/python

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Create a text file with given content on the remote host

version_added: "1.0.0"

description:
    - This module creates (or overwrites) a text file at the given C(path) on
      the remote host, writing the given C(content) into it.
    - The module is idempotent — if the file already exists with the exact
      same content, no changes are made.

options:
    path:
        description: Path to the file that should be created on the remote host.
        required: true
        type: path
    content:
        description: Content that should be written into the file.
        required: true
        type: str

author:
    - ivan <ivankiselev6534@gmail.com> (@palm000palmovich)
'''

EXAMPLES = r'''
- name: Create a text file with some content
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/my_file.txt
    content: "Hello, world!"
'''

RETURN = r'''
path:
    description: Path to the file that was created or checked.
    type: str
    returned: always
    sample: '/tmp/my_file.txt'
content:
    description: Content that was written into the file.
    type: str
    returned: always
    sample: 'Hello, world!'
'''

import os
import tempfile

from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        path=dict(type='path', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        content=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    result['path'] = path
    result['content'] = content

    file_exists = os.path.isfile(path)
    current_content = None

    if file_exists:
        try:
            with open(path, 'r') as f:
                current_content = f.read()
        except OSError as e:
            module.fail_json(msg="Unable to read existing file %s: %s" % (path, str(e)), **result)

    if not file_exists or current_content != content:
        result['changed'] = True

    if module.check_mode:
        module.exit_json(**result)

    if result['changed']:
        try:
            tmp_fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(path) or '.')
            with os.fdopen(tmp_fd, 'w') as f:
                f.write(content)
            module.atomic_move(tmp_path, path)
        except OSError as e:
            module.fail_json(msg="Unable to write file %s: %s" % (path, str(e)), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
