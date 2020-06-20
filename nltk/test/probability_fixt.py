# -*- coding: utf-8 -*-


# probability.doctest uses HMM which requires numpy;
# skip probability.doctest if numpy is not available


def setup_module(module):
    from nose import SkipTest

    try:
        import numpy
    except ImportError as e:
        raise SkipTest("probability.doctest requires numpy") from e
