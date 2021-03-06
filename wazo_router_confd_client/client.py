# Copyright 2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+


from wazo_lib_rest_client.client import BaseClient


class ConfdClient(BaseClient):

    namespace = 'wazo_router_confd_client.commands'

    def __init__(self,
                 host,
                 port=9486,
                 version='1.0',
                 **kwargs):
        super(ConfdClient, self).__init__(
              host=host,
              port=port,
              version=version,
              **kwargs)
