# Copyright (c) 2011-2012 OpenStack, LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from nova import config
from nova import flags
from nova.scheduler import filters

CONF = config.CONF


class IsolatedHostsFilter(filters.BaseHostFilter):
    """Returns host."""

    def host_passes(self, host_state, filter_properties):
        spec = filter_properties.get('request_spec', {})
        props = spec.get('instance_properties', {})
        image_ref = props.get('image_ref')
        image_isolated = image_ref in CONF.isolated_images
        host_isolated = host_state.host in CONF.isolated_hosts
        return image_isolated == host_isolated
