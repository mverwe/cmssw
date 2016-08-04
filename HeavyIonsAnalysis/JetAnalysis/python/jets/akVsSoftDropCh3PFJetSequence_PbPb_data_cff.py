

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropCh3PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropCh3PFJets"),
    matched = cms.InputTag("ak3HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.3
    )

akVsSoftDropCh3PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh3HiGenJets"),
    matched = cms.InputTag("ak3HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.3
    )

akVsSoftDropCh3PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh3PFJets")
                                                        )

akVsSoftDropCh3PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropCh3PFJets"),
    payload = "AK3PF_offline"
    )

akVsSoftDropCh3PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropCh3CaloJets'))

#akVsSoftDropCh3PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak3HiSignalGenJets'))

akVsSoftDropCh3PFbTagger = bTaggers("akVsSoftDropCh3PF",0.3)

#create objects locally since they dont load properly otherwise
#akVsSoftDropCh3PFmatch = akVsSoftDropCh3PFbTagger.match
akVsSoftDropCh3PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh3PFJets"), matched = cms.InputTag("hiSignalGenParticles"))
akVsSoftDropCh3PFPatJetFlavourAssociationLegacy = akVsSoftDropCh3PFbTagger.PatJetFlavourAssociationLegacy
akVsSoftDropCh3PFPatJetPartons = akVsSoftDropCh3PFbTagger.PatJetPartons
akVsSoftDropCh3PFJetTracksAssociatorAtVertex = akVsSoftDropCh3PFbTagger.JetTracksAssociatorAtVertex
akVsSoftDropCh3PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropCh3PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh3PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh3PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh3PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh3PFCombinedSecondaryVertexBJetTags = akVsSoftDropCh3PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh3PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh3PFbTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropCh3PFJetBProbabilityBJetTags = akVsSoftDropCh3PFbTagger.JetBProbabilityBJetTags
akVsSoftDropCh3PFSoftPFMuonByPtBJetTags = akVsSoftDropCh3PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh3PFSoftPFMuonByIP3dBJetTags = akVsSoftDropCh3PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh3PFTrackCountingHighEffBJetTags = akVsSoftDropCh3PFbTagger.TrackCountingHighEffBJetTags
akVsSoftDropCh3PFTrackCountingHighPurBJetTags = akVsSoftDropCh3PFbTagger.TrackCountingHighPurBJetTags
akVsSoftDropCh3PFPatJetPartonAssociationLegacy = akVsSoftDropCh3PFbTagger.PatJetPartonAssociationLegacy

akVsSoftDropCh3PFImpactParameterTagInfos = akVsSoftDropCh3PFbTagger.ImpactParameterTagInfos
akVsSoftDropCh3PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh3PFJetProbabilityBJetTags = akVsSoftDropCh3PFbTagger.JetProbabilityBJetTags

akVsSoftDropCh3PFSecondaryVertexTagInfos = akVsSoftDropCh3PFbTagger.SecondaryVertexTagInfos
akVsSoftDropCh3PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh3PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh3PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh3PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh3PFCombinedSecondaryVertexBJetTags = akVsSoftDropCh3PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh3PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh3PFbTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropCh3PFSecondaryVertexNegativeTagInfos = akVsSoftDropCh3PFbTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropCh3PFNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh3PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh3PFNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh3PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh3PFNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropCh3PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropCh3PFPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropCh3PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropCh3PFNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh3PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropCh3PFPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh3PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropCh3PFSoftPFMuonsTagInfos = akVsSoftDropCh3PFbTagger.SoftPFMuonsTagInfos
akVsSoftDropCh3PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh3PFSoftPFMuonBJetTags = akVsSoftDropCh3PFbTagger.SoftPFMuonBJetTags
akVsSoftDropCh3PFSoftPFMuonByIP3dBJetTags = akVsSoftDropCh3PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh3PFSoftPFMuonByPtBJetTags = akVsSoftDropCh3PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh3PFNegativeSoftPFMuonByPtBJetTags = akVsSoftDropCh3PFbTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropCh3PFPositiveSoftPFMuonByPtBJetTags = akVsSoftDropCh3PFbTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropCh3PFPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropCh3PFPatJetPartonAssociationLegacy*akVsSoftDropCh3PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropCh3PFPatJetFlavourAssociation = akVsSoftDropCh3PFbTagger.PatJetFlavourAssociation
#akVsSoftDropCh3PFPatJetFlavourId = cms.Sequence(akVsSoftDropCh3PFPatJetPartons*akVsSoftDropCh3PFPatJetFlavourAssociation)

akVsSoftDropCh3PFJetBtaggingIP       = cms.Sequence(akVsSoftDropCh3PFImpactParameterTagInfos *
            (akVsSoftDropCh3PFTrackCountingHighEffBJetTags +
             akVsSoftDropCh3PFTrackCountingHighPurBJetTags +
             akVsSoftDropCh3PFJetProbabilityBJetTags +
             akVsSoftDropCh3PFJetBProbabilityBJetTags 
            )
            )

akVsSoftDropCh3PFJetBtaggingSV = cms.Sequence(akVsSoftDropCh3PFImpactParameterTagInfos
            *
            akVsSoftDropCh3PFSecondaryVertexTagInfos
            * (akVsSoftDropCh3PFSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh3PFSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh3PFCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh3PFCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh3PFJetBtaggingNegSV = cms.Sequence(akVsSoftDropCh3PFImpactParameterTagInfos
            *
            akVsSoftDropCh3PFSecondaryVertexNegativeTagInfos
            * (akVsSoftDropCh3PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh3PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh3PFNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh3PFPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh3PFNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropCh3PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh3PFJetBtaggingMu = cms.Sequence(akVsSoftDropCh3PFSoftPFMuonsTagInfos * (akVsSoftDropCh3PFSoftPFMuonBJetTags
                +
                akVsSoftDropCh3PFSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropCh3PFSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh3PFNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh3PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropCh3PFJetBtagging = cms.Sequence(akVsSoftDropCh3PFJetBtaggingIP
            *akVsSoftDropCh3PFJetBtaggingSV
            *akVsSoftDropCh3PFJetBtaggingNegSV
#            *akVsSoftDropCh3PFJetBtaggingMu
            )

akVsSoftDropCh3PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropCh3PFJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropCh3PFmatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropCh3PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropCh3PFcorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropCh3PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropCh3PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropCh3PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropCh3PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh3PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropCh3PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropCh3PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropCh3PFJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropCh3PFJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropCh3PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropCh3PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropCh3PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh3PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropCh3PFJetID"),
        addBTagInfo = True,
        addTagInfos = True,
        addDiscriminators = True,
        addAssociatedTracks = True,
        addJetCharge = False,
        addJetID = False,
        getJetMCFlavour = False,
        addGenPartonMatch = False,
        addGenJetMatch = False,
        embedGenJetMatch = False,
        embedGenPartonMatch = False,
        # embedCaloTowers = False,
        # embedPFCandidates = True
        )

akVsSoftDropCh3PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropCh3PFJets"),
           	    R0  = cms.double( 0.3)
)
akVsSoftDropCh3PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh3PFNjettiness:tau1','akVsSoftDropCh3PFNjettiness:tau2','akVsSoftDropCh3PFNjettiness:tau3']

akVsSoftDropCh3PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropCh3PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak3HiSignalGenJets',#'ak3HiGenJets',
                                                             rParam = 0.3,
                                                             matchJets = cms.untracked.bool(False),
                                                             matchTag = 'patJetsWithBtagging',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("hiGeneralTracks"),
                                                             fillGenJets = False,
                                                             isMC = False,
							     doSubEvent = False,
                                                             useHepMC = cms.untracked.bool(False),
							     genParticles = cms.untracked.InputTag("genParticles"),
							     eventInfoTag = cms.InputTag("generator"),
                                                             doLifeTimeTagging = cms.untracked.bool(True),
                                                             doLifeTimeTaggingExtras = cms.untracked.bool(False),
                                                             bTagJetName = cms.untracked.string("akVsSoftDropCh3PF"),
                                                             jetName = cms.untracked.string("akVsSoftDropCh3PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropCh3GenJets"),
                                                             doGenTaus = False,
                                                             genTau1 = cms.InputTag("akSoftDropCh3GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropCh3GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropCh3GenNjettiness","tau3"),
                                                             doGenSym = True,
                                                             genSym = cms.InputTag("akSoftDropCh3GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropCh3GenJets","droppedBranches")
                                                             )

akVsSoftDropCh3PFJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropCh3PFclean
                                                  #*
                                                  akVsSoftDropCh3PFmatch
                                                  #*
                                                  #akVsSoftDropCh3PFmatchGroomed
                                                  *
                                                  akVsSoftDropCh3PFparton
                                                  *
                                                  akVsSoftDropCh3PFcorr
                                                  *
                                                  #akVsSoftDropCh3PFJetID
                                                  #*
                                                  akVsSoftDropCh3PFPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropCh3PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropCh3PFJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropCh3PFJetBtagging
                                                  *
                                                  akVsSoftDropCh3PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropCh3PFpatJetsWithBtagging
                                                  *
                                                  akVsSoftDropCh3PFJetAnalyzer
                                                  )

akVsSoftDropCh3PFJetSequence_data = cms.Sequence(akVsSoftDropCh3PFcorr
                                                    *
                                                    #akVsSoftDropCh3PFJetID
                                                    #*
                                                    akVsSoftDropCh3PFJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropCh3PFJetBtagging
                                                    *
                                                    akVsSoftDropCh3PFNjettiness 
                                                    *
                                                    akVsSoftDropCh3PFpatJetsWithBtagging
                                                    *
                                                    akVsSoftDropCh3PFJetAnalyzer
                                                    )

akVsSoftDropCh3PFJetSequence_jec = cms.Sequence(akVsSoftDropCh3PFJetSequence_mc)
akVsSoftDropCh3PFJetSequence_mb = cms.Sequence(akVsSoftDropCh3PFJetSequence_mc)

akVsSoftDropCh3PFJetSequence = cms.Sequence(akVsSoftDropCh3PFJetSequence_data)
akVsSoftDropCh3PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh3PFJets:sym']
akVsSoftDropCh3PFpatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropCh3PFJets:droppedBranches']
