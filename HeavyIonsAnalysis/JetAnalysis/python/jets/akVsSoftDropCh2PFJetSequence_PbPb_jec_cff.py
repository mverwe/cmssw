

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropCh2PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropCh2PFJets"),
    matched = cms.InputTag("ak2HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.2
    )

akVsSoftDropCh2PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh2HiGenJets"),
    matched = cms.InputTag("ak2HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.2
    )

akVsSoftDropCh2PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh2PFJets")
                                                        )

akVsSoftDropCh2PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropCh2PFJets"),
    payload = "AK2PF_offline"
    )

akVsSoftDropCh2PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropCh2CaloJets'))

#akVsSoftDropCh2PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak2HiSignalGenJets'))

akVsSoftDropCh2PFbTagger = bTaggers("akVsSoftDropCh2PF",0.2)

#create objects locally since they dont load properly otherwise
#akVsSoftDropCh2PFmatch = akVsSoftDropCh2PFbTagger.match
akVsSoftDropCh2PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh2PFJets"), matched = cms.InputTag("hiSignalGenParticles"))
akVsSoftDropCh2PFPatJetFlavourAssociationLegacy = akVsSoftDropCh2PFbTagger.PatJetFlavourAssociationLegacy
akVsSoftDropCh2PFPatJetPartons = akVsSoftDropCh2PFbTagger.PatJetPartons
akVsSoftDropCh2PFJetTracksAssociatorAtVertex = akVsSoftDropCh2PFbTagger.JetTracksAssociatorAtVertex
akVsSoftDropCh2PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropCh2PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh2PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh2PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh2PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh2PFCombinedSecondaryVertexBJetTags = akVsSoftDropCh2PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh2PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh2PFbTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropCh2PFJetBProbabilityBJetTags = akVsSoftDropCh2PFbTagger.JetBProbabilityBJetTags
akVsSoftDropCh2PFSoftPFMuonByPtBJetTags = akVsSoftDropCh2PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh2PFSoftPFMuonByIP3dBJetTags = akVsSoftDropCh2PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh2PFTrackCountingHighEffBJetTags = akVsSoftDropCh2PFbTagger.TrackCountingHighEffBJetTags
akVsSoftDropCh2PFTrackCountingHighPurBJetTags = akVsSoftDropCh2PFbTagger.TrackCountingHighPurBJetTags
akVsSoftDropCh2PFPatJetPartonAssociationLegacy = akVsSoftDropCh2PFbTagger.PatJetPartonAssociationLegacy

akVsSoftDropCh2PFImpactParameterTagInfos = akVsSoftDropCh2PFbTagger.ImpactParameterTagInfos
akVsSoftDropCh2PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh2PFJetProbabilityBJetTags = akVsSoftDropCh2PFbTagger.JetProbabilityBJetTags

akVsSoftDropCh2PFSecondaryVertexTagInfos = akVsSoftDropCh2PFbTagger.SecondaryVertexTagInfos
akVsSoftDropCh2PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh2PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh2PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh2PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh2PFCombinedSecondaryVertexBJetTags = akVsSoftDropCh2PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh2PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh2PFbTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropCh2PFSecondaryVertexNegativeTagInfos = akVsSoftDropCh2PFbTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropCh2PFNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh2PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh2PFNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh2PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh2PFNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropCh2PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropCh2PFPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropCh2PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropCh2PFNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh2PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropCh2PFPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh2PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropCh2PFSoftPFMuonsTagInfos = akVsSoftDropCh2PFbTagger.SoftPFMuonsTagInfos
akVsSoftDropCh2PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh2PFSoftPFMuonBJetTags = akVsSoftDropCh2PFbTagger.SoftPFMuonBJetTags
akVsSoftDropCh2PFSoftPFMuonByIP3dBJetTags = akVsSoftDropCh2PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh2PFSoftPFMuonByPtBJetTags = akVsSoftDropCh2PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh2PFNegativeSoftPFMuonByPtBJetTags = akVsSoftDropCh2PFbTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropCh2PFPositiveSoftPFMuonByPtBJetTags = akVsSoftDropCh2PFbTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropCh2PFPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropCh2PFPatJetPartonAssociationLegacy*akVsSoftDropCh2PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropCh2PFPatJetFlavourAssociation = akVsSoftDropCh2PFbTagger.PatJetFlavourAssociation
#akVsSoftDropCh2PFPatJetFlavourId = cms.Sequence(akVsSoftDropCh2PFPatJetPartons*akVsSoftDropCh2PFPatJetFlavourAssociation)

akVsSoftDropCh2PFJetBtaggingIP       = cms.Sequence(akVsSoftDropCh2PFImpactParameterTagInfos *
            (akVsSoftDropCh2PFTrackCountingHighEffBJetTags +
             akVsSoftDropCh2PFTrackCountingHighPurBJetTags +
             akVsSoftDropCh2PFJetProbabilityBJetTags +
             akVsSoftDropCh2PFJetBProbabilityBJetTags 
            )
            )

akVsSoftDropCh2PFJetBtaggingSV = cms.Sequence(akVsSoftDropCh2PFImpactParameterTagInfos
            *
            akVsSoftDropCh2PFSecondaryVertexTagInfos
            * (akVsSoftDropCh2PFSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh2PFSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh2PFCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh2PFCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh2PFJetBtaggingNegSV = cms.Sequence(akVsSoftDropCh2PFImpactParameterTagInfos
            *
            akVsSoftDropCh2PFSecondaryVertexNegativeTagInfos
            * (akVsSoftDropCh2PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh2PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh2PFNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh2PFPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh2PFNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropCh2PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh2PFJetBtaggingMu = cms.Sequence(akVsSoftDropCh2PFSoftPFMuonsTagInfos * (akVsSoftDropCh2PFSoftPFMuonBJetTags
                +
                akVsSoftDropCh2PFSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropCh2PFSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh2PFNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh2PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropCh2PFJetBtagging = cms.Sequence(akVsSoftDropCh2PFJetBtaggingIP
            *akVsSoftDropCh2PFJetBtaggingSV
            *akVsSoftDropCh2PFJetBtaggingNegSV
#            *akVsSoftDropCh2PFJetBtaggingMu
            )

akVsSoftDropCh2PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropCh2PFJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropCh2PFmatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropCh2PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropCh2PFcorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropCh2PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropCh2PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropCh2PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropCh2PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh2PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropCh2PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropCh2PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropCh2PFJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropCh2PFJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropCh2PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropCh2PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropCh2PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh2PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropCh2PFJetID"),
        addBTagInfo = True,
        addTagInfos = True,
        addDiscriminators = True,
        addAssociatedTracks = True,
        addJetCharge = False,
        addJetID = False,
        getJetMCFlavour = True,
        addGenPartonMatch = True,
        addGenJetMatch = True,
        embedGenJetMatch = True,
        embedGenPartonMatch = True,
        # embedCaloTowers = False,
        # embedPFCandidates = True
        )

akVsSoftDropCh2PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropCh2PFJets"),
           	    R0  = cms.double( 0.2)
)
akVsSoftDropCh2PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh2PFNjettiness:tau1','akVsSoftDropCh2PFNjettiness:tau2','akVsSoftDropCh2PFNjettiness:tau3']

akVsSoftDropCh2PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropCh2PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak2HiSignalGenJets',#'ak2HiGenJets',
                                                             rParam = 0.2,
                                                             matchJets = cms.untracked.bool(False),
                                                             matchTag = 'patJetsWithBtagging',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("hiGeneralTracks"),
                                                             fillGenJets = True,
                                                             isMC = True,
							     doSubEvent = True,
                                                             useHepMC = cms.untracked.bool(False),
							     genParticles = cms.untracked.InputTag("genParticles"),
							     eventInfoTag = cms.InputTag("generator"),
                                                             doLifeTimeTagging = cms.untracked.bool(True),
                                                             doLifeTimeTaggingExtras = cms.untracked.bool(False),
                                                             bTagJetName = cms.untracked.string("akVsSoftDropCh2PF"),
                                                             jetName = cms.untracked.string("akVsSoftDropCh2PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropCh2GenJets"),
                                                             doGenTaus = False,
                                                             genTau1 = cms.InputTag("akSoftDropCh2GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropCh2GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropCh2GenNjettiness","tau3"),
                                                             doGenSym = True,
                                                             genSym = cms.InputTag("akSoftDropCh2GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropCh2GenJets","droppedBranches")
                                                             )

akVsSoftDropCh2PFJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropCh2PFclean
                                                  #*
                                                  akVsSoftDropCh2PFmatch
                                                  #*
                                                  #akVsSoftDropCh2PFmatchGroomed
                                                  *
                                                  akVsSoftDropCh2PFparton
                                                  *
                                                  akVsSoftDropCh2PFcorr
                                                  *
                                                  #akVsSoftDropCh2PFJetID
                                                  #*
                                                  akVsSoftDropCh2PFPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropCh2PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropCh2PFJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropCh2PFJetBtagging
                                                  *
                                                  akVsSoftDropCh2PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropCh2PFpatJetsWithBtagging
                                                  *
                                                  akVsSoftDropCh2PFJetAnalyzer
                                                  )

akVsSoftDropCh2PFJetSequence_data = cms.Sequence(akVsSoftDropCh2PFcorr
                                                    *
                                                    #akVsSoftDropCh2PFJetID
                                                    #*
                                                    akVsSoftDropCh2PFJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropCh2PFJetBtagging
                                                    *
                                                    akVsSoftDropCh2PFNjettiness 
                                                    *
                                                    akVsSoftDropCh2PFpatJetsWithBtagging
                                                    *
                                                    akVsSoftDropCh2PFJetAnalyzer
                                                    )

akVsSoftDropCh2PFJetSequence_jec = cms.Sequence(akVsSoftDropCh2PFJetSequence_mc)
akVsSoftDropCh2PFJetSequence_mb = cms.Sequence(akVsSoftDropCh2PFJetSequence_mc)

akVsSoftDropCh2PFJetSequence = cms.Sequence(akVsSoftDropCh2PFJetSequence_jec)
akVsSoftDropCh2PFJetAnalyzer.genPtMin = cms.untracked.double(1)
akVsSoftDropCh2PFJetAnalyzer.jetPtMin = cms.double(1)
akVsSoftDropCh2PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh2PFJets:sym']
akVsSoftDropCh2PFpatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropCh2PFJets:droppedBranches']
