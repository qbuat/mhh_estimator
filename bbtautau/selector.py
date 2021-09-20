import awkward as ak
from . import log
log = log.getChild(__name__)

def _select(ak_array, is_signal=True, truth_based=True, cutflow_dict={}, verbose=False):
    """
    """
    if 'initial' in cutflow_dict.keys():
        cutflow_dict['initial'] += len(ak_array)
    else:
        cutflow_dict['initial'] = len(ak_array)

    if verbose:
        log.info('--- cutflow ---')
        log.info('initial: {}'.format(cutflow_dict['initial']))

    # build the higgs object (subset of truth particles)
    if truth_based and is_signal:
        ak_array['higgs'] = ak_array.TruthParticles___NominalAuxDyn[ak_array.TruthParticles___NominalAuxDyn.pdgId == 25]
        ak_array = ak_array[ak.num(ak_array.higgs) == 2]
        if 'two higges' in cutflow_dict.keys():
            cutflow_dict['two higges'] += len(ak_array)
        else:
            cutflow_dict['two higges'] = len(ak_array)

        if verbose:
            log.info('two higges: {}'.format(cutflow_dict['two higges']))

    # build the selected taus container (simple truth matching selection)
    if truth_based:
        ak_array['taus'] = ak_array.TauJets___NominalAuxDyn[ak_array.TauJets___NominalAuxDyn.TATTruthMatch == 15]
        if 'two taus' in cutflow_dict.keys():
            cutflow_dict['two taus'] += len(ak_array)
        else:
            cutflow_dict['two taus'] = len(ak_array)

        if verbose:
            log.info('two taus: {}'.format(cutflow_dict['two taus']))

    # apply tau ID
    ak_array['taus'] = ak_array.taus[ak_array.taus.isRNNMedium == 1]
    ak_array = ak_array[ak.num(ak_array.taus) == 2]
    if 'two medium taus' in cutflow_dict.keys():
        cutflow_dict['two medium taus'] += len(ak_array)
    else:
        cutflow_dict['two medium taus'] = len(ak_array)
        
    if verbose:
        log.info('two medium taus: {}'.format(cutflow_dict['two medium taus']))


    # build the selected b-jets container (simple truth matching selection)
    if truth_based:
        ak_array['bjets'] = ak_array.AntiKt4EMPFlowJets_BTagging201903___NominalAuxDyn[ak_array.AntiKt4EMPFlowJets_BTagging201903___NominalAuxDyn.isBJet == 1]
        ak_array = ak_array[ak.num(ak_array.bjets) == 2]
        if 'two b-jets' in cutflow_dict.keys():
            cutflow_dict['two b-jets'] += len(ak_array)
        else:
            cutflow_dict['two b-jets'] = len(ak_array)
        
        if verbose:
            log.info('two b-jets: {}'.format(cutflow_dict['two b-jets']))


    return ak_array
