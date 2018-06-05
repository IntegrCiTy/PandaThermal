#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd


class _FullNetwork:

    def __init__(self):
        self.edges = pd.DataFrame(columns=["name", "pipe_name", "type", "length_m", "diameter_m"])
        self.nodes = pd.DataFrame(columns=["name", "node_name", "type"])
