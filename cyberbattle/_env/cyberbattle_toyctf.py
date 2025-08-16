# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from ..samples.toyctf import toy_ctf
from . import cyberbattle_env

class CyberBattleToyCtf(cyberbattle_env.CyberBattleEnv):
    def __init__(self, defender_agent=None, **kwargs):
        # Pass defender_agent into CyberBattleEnv constructor
        super().__init__(
            initial_environment=toy_ctf.new_environment(),
            defender_agent=defender_agent,
            **kwargs
        )