# Copyright 2016 Autodesk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import absolute_import

import json
from . import args_from


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'to_json'):
            obj = obj.to_json()
        return obj


@args_from(json.dump)
def json_dump(*args, **kwargs):
    return json.dump(*args, cls=JsonEncoder, **kwargs)


@args_from(json.dumps)
def json_dumps(*args, **kwargs):
    return json.dumps(*args, cls=JsonEncoder, **kwargs)
