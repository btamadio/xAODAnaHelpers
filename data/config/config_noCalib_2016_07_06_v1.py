from xAH_config import xAH_config
import os
c = xAH_config()

c.setalg("BasicEventSelection", {"m_debug": False,
                                 "m_truthLevelOnly": False,
                                 "m_applyGRLCut": False,
                                 "m_GRLxml": "$ROOTCOREBIN/data/xAODAnaHelpers/data15_13TeV.periodAllYear_DetStatus-v73-pro19-08_DQDefects-00-01-02_PHYS_StandardGRL_All_Good_25ns.xml",
                                 "m_doPUreweighting": False,
                                 "m_vertexContainerName": "PrimaryVertices",
                                 "m_PVNTrack": 2,
                                 "m_useMetaData": True,
                                 "m_derivationName": "EXOT3Kernel",
                                 "m_triggerSelection": "HLT_j.*|HLT_ht.*|L1_J.*|L1_HT.*|HLT_noalg_L1J.*",
                                 "m_storeTrigDecisions": True,
                                 "m_applyTriggerCut": False
                                })

c.setalg("TreeAlgo", {"m_debug": False,
                      "m_name": "outTree",
                      "m_jetContainerName": "AntiKt4EMTopoJets",
                      "m_jetDetailStr": "truth kinematic energy",
                      "m_fatJetContainerName":"AntiKt10LCTopoTrimmedPtFrac5SmallR20Jets",
                      "m_fatJetDetailStr":"kinematic substructure",
                      "m_trigDetailStr":"basic passTriggers",
                      "m_evtDetailStr":"pileup eventCleaning"
                    })
