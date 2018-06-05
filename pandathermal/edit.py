#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import logging

logging.basicConfig(level=logging.WARNING)


class _SupNetwork:

    def __init__(self):
        self.srces = pd.DataFrame(columns=["name", "m_dot_m3/s", "p_kW", "t_deg.C"])
        self.sinks = pd.DataFrame(columns=["name", "op_%", "p_kW", "bypass"])
        self.pipes = pd.DataFrame(columns=["name", "length_m", "diameter_m"])


def create_empty_network():
    """
    Create an empty network

    :return: a Network object that will later contain all the network components.
    """
    return _SupNetwork()


def create_srce(net, name, m_dot, p_inj, t_inj):
    pass


def create_sink(net, name, op, p_dem, bypass=False):
    pass
