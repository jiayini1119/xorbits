# Copyright 2022-2023 XProbe Inc.
# derived from copyright 1999-2021 Alibaba Group Holding Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ...config import Config, is_bool, is_integer, is_list

task_options = Config()

# supervisor
task_options.register_option("optimize_tileable_graph", True, validator=is_bool)
task_options.register_option("optimize_chunk_graph", True, validator=is_bool)
task_options.register_option("fuse_enabled", True, validator=is_bool)
task_options.register_option("reserved_finish_tasks", 25, validator=is_integer)

# worker
task_options.register_option("runtime_engines", ["numexpr", "cupy"], validator=is_list)
