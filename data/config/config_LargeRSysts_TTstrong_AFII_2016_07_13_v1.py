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

c.setalg("JetCalibrator", {"m_name": "JetCalibration",
                           "m_setAFII": True,
                           "m_debug": False,
                           "m_inContainerName": "AntiKt4EMTopoJets",
                           "m_outContainerName": "AntiKt4EMTopoJetsCalib",
                           "m_jetAlgo": "AntiKt4EMTopo",
                           "m_doCleaning":True,
                           "m_saveAllCleanDecisions":True,
                           "m_calibSequence":"JetArea_Residual_Origin_EtaJES_GSC",
                           "m_calibConfigFullSim":"JES_MC15cRecommendation_May2016.config",
                           "m_calibConfigAFII":"JES_MC15Prerecommendation_AFII_June2015.config",
                           "m_calibConfigData":"JES_MC15cRecommendation_May2016.config",
                           })

c.setalg("JetCalibrator", {"m_name": "FatJetCalibration",
                           "m_setAFII": True,
                           "m_debug": False,
                           "m_inContainerName":"AntiKt10LCTopoTrimmedPtFrac5SmallR20Jets",
                           "m_outContainerName": "AntiKt10LCTopoTrimmedPtFrac5SmallR20JetsCalib",
                           "m_jetAlgo":"AntiKt10LCTopoTrimmedPtFrac5SmallR20",
                           "m_doCleaning":False,
                           "m_calibSequence":"EtaJES_JMS",
                           "m_calibConfigFullSim":"JES_MC15recommendation_FatJet_June2015.config",
                           "m_calibConfigAFII":"JES_MC15recommendation_FatJet_June2015.config",
                           "m_calibConfigData":"JES_MC15recommendation_FatJet_June2015.config",
                           "m_systName":"All",
                           "m_systVal":1,
			   "m_JESUncertConfig":"UJ_2015/ICHEP2016/TopTagging_strong.config",
                           "m_outputAlgo":"FatJetSysts",
			   "m_JESUncertMCType":"MC15c",
                           "m_applyFatJetPreSel":True
                           })

c.setalg("BJetEfficiencyCorrector", {"m_name": "BTagFix60",
                                     "m_debug": False,
                                     "m_inContainerName": "AntiKt4EMTopoJetsCalib",
                                     "m_corrFileName":"$ROOTCOREBIN/data/xAODAnaHelpers/2016-20_7-13TeV-MC15-CDI-July12_v1.root",
                                     "m_operatingPt": "FixedCutBEff_60",
                                     "m_taggerName":"MV2c10",
                                     "m_decor": "BTag",
                                     "m_decorSF": "",
                                     "m_systVal":1,
                                     "m_systName":"All"
                                    })

c.setalg("BJetEfficiencyCorrector", {"m_name": "BTagFix70",
                                     "m_debug": False,
                                     "m_inContainerName": "AntiKt4EMTopoJetsCalib",
                                     "m_corrFileName":"$ROOTCOREBIN/data/xAODAnaHelpers/2016-20_7-13TeV-MC15-CDI-July12_v1.root",
                                     "m_operatingPt": "FixedCutBEff_70",
                                     "m_taggerName":"MV2c10",
                                     "m_decor": "BTag",
                                     "m_decorSF": "",
                                     "m_systVal":1,
                                     "m_systName":"All"
                                    })
c.setalg("BJetEfficiencyCorrector", {"m_name": "BTagFix77",
                                     "m_debug": False,
                                     "m_inContainerName": "AntiKt4EMTopoJetsCalib",
                                     "m_corrFileName":"$ROOTCOREBIN/data/xAODAnaHelpers/2016-20_7-13TeV-MC15-CDI-July12_v1.root",
                                     "m_operatingPt": "FixedCutBEff_77",
                                     "m_taggerName":"MV2c10",
                                     "m_decor": "BTag",
                                     "m_decorSF": "",
                                     "m_systVal":1,
                                     "m_systName":"All"
                                    })

c.setalg("BJetEfficiencyCorrector", {"m_name": "BTagFix85",
                                     "m_debug": False,
                                     "m_inContainerName": "AntiKt4EMTopoJetsCalib",
                                     "m_corrFileName":"$ROOTCOREBIN/data/xAODAnaHelpers/2016-20_7-13TeV-MC15-CDI-July12_v1.root",
                                     "m_operatingPt": "FixedCutBEff_85",
                                     "m_taggerName":"MV2c10",
                                     "m_decor": "BTag",
                                     "m_decorSF": "",
                                     "m_systVal":1,
                                     "m_systName":"All"
                                    })

c.setalg("BJetEfficiencyCorrector", {"m_name": "BTagFlat60",
                                     "m_debug": False,
                                     "m_inContainerName": "AntiKt4EMTopoJetsCalib",
                                     "m_corrFileName":"$ROOTCOREBIN/data/xAODAnaHelpers/2016-20_7-13TeV-MC15-CDI-July12_v1.root",
                                     "m_operatingPt": "FlatBEff_60",
                                     "m_taggerName":"MV2c10",
                                     "m_decor": "BTag",
                                     "m_decorSF": "",
                                     "m_systVal":1,
                                     "m_systName":"All"
                                    })

c.setalg("BJetEfficiencyCorrector", {"m_name": "BTagFlat70",
                                     "m_debug": False,
                                     "m_inContainerName": "AntiKt4EMTopoJetsCalib",
                                     "m_corrFileName":"$ROOTCOREBIN/data/xAODAnaHelpers/2016-20_7-13TeV-MC15-CDI-July12_v1.root",
                                     "m_operatingPt": "FlatBEff_70",
                                     "m_taggerName":"MV2c10",
                                     "m_decor": "BTag",
                                     "m_decorSF": "",
                                     "m_systVal":1,
                                     "m_systName":"All"
                                    })
c.setalg("BJetEfficiencyCorrector", {"m_name": "BTagFlat77",
                                     "m_debug": False,
                                     "m_inContainerName": "AntiKt4EMTopoJetsCalib",
                                     "m_corrFileName":"$ROOTCOREBIN/data/xAODAnaHelpers/2016-20_7-13TeV-MC15-CDI-July12_v1.root",
                                     "m_operatingPt": "FlatBEff_77",
                                     "m_taggerName":"MV2c10",
                                     "m_decor": "BTag",
                                     "m_decorSF": "",
                                     "m_systVal":1,
                                     "m_systName":"All"
                                    })

c.setalg("BJetEfficiencyCorrector", {"m_name": "BTagFlat85",
                                     "m_debug": False,
                                     "m_inContainerName": "AntiKt4EMTopoJetsCalib",
                                     "m_corrFileName":"$ROOTCOREBIN/data/xAODAnaHelpers/2016-20_7-13TeV-MC15-CDI-July12_v1.root",
                                     "m_operatingPt": "FlatBEff_85",
                                     "m_taggerName":"MV2c10",
                                     "m_decor": "BTag",
                                     "m_decorSF": "",
                                     "m_systVal":1,
                                     "m_systName":"All"
                                    })

c.setalg("TreeAlgo", {"m_debug": False,
                      "m_name": "outTree",
                      "m_jetContainerName": "AntiKt4EMTopoJetsCalib",
                      "m_jetDetailStr": "truth kinematic energy clean scales flavorTag sfFTagFix60707785 sfFTagFlt60707785",
                      "m_fatJetContainerName":"AntiKt10LCTopoTrimmedPtFrac5SmallR20JetsCalib",
                      "m_fatJetDetailStr":"kinematic substructure",
                      "m_trigDetailStr":"basic passTriggers",
                      "m_evtDetailStr":"pileup eventCleaning",
                      "m_jetSystsVec":"JetSysts",
                      "m_fatJetSystsVec":"FatJetSysts"
                    })
