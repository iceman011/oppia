# coding: utf-8
#
# Copyright 2014 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, softwar
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Rules for Real With Units."""

__author__ = 'Zoe Madden-Wood'

from extensions.rules import base


class Equals(base.RealWithUnitRule):
    description = 'is equal to {{x|RealWithUnit}}'
    is_generic = False

    def _evaluate(self, subject):
        return subject["parsed"] == self.x["parsed"]

