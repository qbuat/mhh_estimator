import os
from .sample import sample

DEFAULT_PATH = '/Users/jvbackus/data'
PATH = os.getenv("CXAOD_PATH", DEFAULT_PATH)

dihiggs_01 = sample(
    'HH_01',
    r'$HH \to bb\tau_{h}\tau_{h} (\kappa_{\lambda} = 1)$',
    # r'$HH (\lambda = 1.)$',
    'red',
    600023, PATH)
dihiggs_10 = sample(
    'HH_10', r'$HH \to bb \tau_{h}\tau_{h} (\kappa_{\lambda} = 10)$', 'blue',
    600024, PATH)

ztautau = sample(
    'ztautau',
    r'$Z\to\tau\tau$ + jets',
    'green',
    [
        364128,
        364129,
        364130,
        364131,
        364132,
        364133,
        364134,
        364135,
        364136,
        364137,
        364138,
        364139,
        364140,
        364141,
        ], PATH)

ttbar = sample(
    'ttbar',
    'Top Quark',
    'orange',
    [
        410470,
        410471,
        410644,
        410645,
        410646,
        410647,
        410658,
        410659,
        ], PATH)

MMC_HH_01 = sample(
    'mmc_HH_01',
    r'$HH \to bb\tau_{h}\tau_{h} (\kappa_{\lambda} = 1)$',
    'purple',
    None,
    PATH)
