# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_router_confd_client.command import ConfdCommand


class CarriersCommand(ConfdCommand):

    resource = 'carriers'
    _ro_headers = {'Accept': 'application/json'}
    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def create(self, carrier):
        r = self.session.post(self.base_url, json=carrier, headers=self._rw_headers)
        self.raise_from_response(r)
        return r.json()

    def list(self):
        r = self.session.get(self.base_url, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()

    def get(self, carrier_uuid):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=carrier_uuid)
        r = self.session.get(url, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, carrier_uuid):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=carrier_uuid)
        r = self.session.delete(url, headers=self._ro_headers)
        self.raise_from_response(r)

    def update(self, carrier_uuid, carrier):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=carrier_uuid)
        r = self.session.put(url, json=carrier, headers=self._rw_headers)
        self.raise_from_response(r)
