from xAH_config import xAH_config
import os
c = xAH_config()

c.setalg("BasicEventSelection", {"m_debug": False,
                                 "m_truthLevelOnly": True,
                                 "m_applyGRLCut": False,
                                 "m_doPUreweighting": False,
                                 "m_useMetaData": False,
                                 "m_applyTriggerCut": False,
                                 "m_applyPrimaryVertexCut": False
                                })

c.setalg("TreeAlgo", {"m_debug": False,
                      "m_name": "outTree",
                      "m_jetContainerName": "AntiKt4TruthJets",
                      "m_jetDetailStr": "kinematic truth_details",
                      "m_fatJetContainerName":"TrimmedAntiKt10TruthJets",
                      "m_fatJetDetailStr":"kinematic substructure"
                    })
