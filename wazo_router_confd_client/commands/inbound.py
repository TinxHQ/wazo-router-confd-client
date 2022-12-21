# Copyright 2018-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_router_confd_client.command import ConfdCommand


class InboundCommand(ConfdCommand):

    resource = 'inbound'
    _ro_headers = {'Accept': 'application/json'}
    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def create(self, inbound):
        r = self.session.post(self.base_url, json=inbound, headers=self._rw_headers)
        self.raise_from_response(r)
        return r.json()

    def list(self):
        r = self.session.get(self.base_url, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()

    def get(self, inbound_uuid):
        url = f'{self.base_url}/{inbound_uuid}'
        r = self.session.get(url, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, inbound_uuid):
        url = f'{self.base_url}/{inbound_uuid}'
        r = self.session.delete(url, headers=self._ro_headers)
        self.raise_from_response(r)

    def update(self, inbound_uuid, inbound):
        url = f'{self.base_url}/{inbound_uuid}'
        r = self.session.put(url, json=inbound, headers=self._rw_headers)
        self.raise_from_response(r)
