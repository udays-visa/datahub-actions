# Copyright 2021 Acryl Data, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from abc import abstractmethod

from datahub_actions.events.event import EnvelopedEvent
from datahub_actions.pipeline.context import ActionContext


class Action:
    """The base class for all DataHub Actions"""

    @classmethod
    @abstractmethod
    def create(cls, config_dict: dict, ctx: ActionContext) -> "Action":
        """Factory method to create an instance of an Action"""
        pass

    @abstractmethod
    def act(self, event: EnvelopedEvent):
        """Take Action on DataHub events"""
        pass
