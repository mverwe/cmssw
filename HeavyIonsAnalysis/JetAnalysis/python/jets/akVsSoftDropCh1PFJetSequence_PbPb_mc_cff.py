

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropCh1PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropCh1PFJets"),
    matched = cms.InputTag("ak1HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akVsSoftDropCh1PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh1HiGenJets"),
    matched = cms.InputTag("ak1HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akVsSoftDropCh1PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh1PFJets")
                                                        )

akVsSoftDropCh1PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropCh1PFJets"),
    payload = "AK1PF_offline"
    )

akVsSoftDropCh1PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropCh1CaloJets'))

#akVsSoftDropCh1PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak1HiSignalGenJets'))

akVsSoftDropCh1PFbTagger = bTaggers("akVsSoftDropCh1PF",0.1)

#create objects locally since they dont load properly otherwise
#akVsSoftDropCh1PFmatch = akVsSoftDropCh1PFbTagger.match
akVsSoftDropCh1PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh1PFJets"), matched = cms.InputTag("hiSignalGenParticles"))
akVsSoftDropCh1PFPatJetFlavourAssociationLegacy = akVsSoftDropCh1PFbTagger.PatJetFlavourAssociationLegacy
akVsSoftDropCh1PFPatJetPartons = akVsSoftDropCh1PFbTagger.PatJetPartons
akVsSoftDropCh1PFJetTracksAssociatorAtVertex = akVsSoftDropCh1PFbTagger.JetTracksAssociatorAtVertex
akVsSoftDropCh1PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropCh1PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh1PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh1PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh1PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh1PFCombinedSecondaryVertexBJetTags = akVsSoftDropCh1PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh1PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh1PFbTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropCh1PFJetBProbabilityBJetTags = akVsSoftDropCh1PFbTagger.JetBProbabilityBJetTags
akVsSoftDropCh1PFSoftPFMuonByPtBJetTags = akVsSoftDropCh1PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh1PFSoftPFMuonByIP3dBJetTags = akVsSoftDropCh1PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh1PFTrackCountingHighEffBJetTags = akVsSoftDropCh1PFbTagger.TrackCountingHighEffBJetTags
akVsSoftDropCh1PFTrackCountingHighPurBJetTags = akVsSoftDropCh1PFbTagger.TrackCountingHighPurBJetTags
akVsSoftDropCh1PFPatJetPartonAssociationLegacy = akVsSoftDropCh1PFbTagger.PatJetPartonAssociationLegacy

akVsSoftDropCh1PFImpactParameterTagInfos = akVsSoftDropCh1PFbTagger.ImpactParameterTagInfos
akVsSoftDropCh1PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh1PFJetProbabilityBJetTags = akVsSoftDropCh1PFbTagger.JetProbabilityBJetTags

akVsSoftDropCh1PFSecondaryVertexTagInfos = akVsSoftDropCh1PFbTagger.SecondaryVertexTagInfos
akVsSoftDropCh1PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh1PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh1PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh1PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh1PFCombinedSecondaryVertexBJetTags = akVsSoftDropCh1PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh1PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh1PFbTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropCh1PFSecondaryVertexNegativeTagInfos = akVsSoftDropCh1PFbTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropCh1PFNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh1PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh1PFNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh1PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh1PFNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropCh1PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropCh1PFPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropCh1PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropCh1PFNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh1PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropCh1PFPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh1PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropCh1PFSoftPFMuonsTagInfos = akVsSoftDropCh1PFbTagger.SoftPFMuonsTagInfos
akVsSoftDropCh1PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh1PFSoftPFMuonBJetTags = akVsSoftDropCh1PFbTagger.SoftPFMuonBJetTags
akVsSoftDropCh1PFSoftPFMuonByIP3dBJetTags = akVsSoftDropCh1PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh1PFSoftPFMuonByPtBJetTags = akVsSoftDropCh1PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh1PFNegativeSoftPFMuonByPtBJetTags = akVsSoftDropCh1PFbTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropCh1PFPositiveSoftPFMuonByPtBJetTags = akVsSoftDropCh1PFbTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropCh1PFPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropCh1PFPatJetPartonAssociationLegacy*akVsSoftDropCh1PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropCh1PFPatJetFlavourAssociation = akVsSoftDropCh1PFbTagger.PatJetFlavourAssociation
#akVsSoftDropCh1PFPatJetFlavourId = cms.Sequence(akVsSoftDropCh1PFPatJetPartons*akVsSoftDropCh1PFPatJetFlavourAssociation)

akVsSoftDropCh1PFJetBtaggingIP       = cms.Sequence(akVsSoftDropCh1PFImpactParameterTagInfos *
            (akVsSoftDropCh1PFTrackCountingHighEffBJetTags +
             akVsSoftDropCh1PFTrackCountingHighPurBJetTags +
             akVsSoftDropCh1PFJetProbabilityBJetTags +
             akVsSoftDropCh1PFJetBProbabilityBJetTags 
            )
            )

akVsSoftDropCh1PFJetBtaggingSV = cms.Sequence(akVsSoftDropCh1PFImpactParameterTagInfos
            *
            akVsSoftDropCh1PFSecondaryVertexTagInfos
            * (akVsSoftDropCh1PFSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh1PFSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh1PFCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh1PFCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh1PFJetBtaggingNegSV = cms.Sequence(akVsSoftDropCh1PFImpactParameterTagInfos
            *
            akVsSoftDropCh1PFSecondaryVertexNegativeTagInfos
            * (akVsSoftDropCh1PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh1PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh1PFNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh1PFPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh1PFNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropCh1PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh1PFJetBtaggingMu = cms.Sequence(akVsSoftDropCh1PFSoftPFMuonsTagInfos * (akVsSoftDropCh1PFSoftPFMuonBJetTags
                +
                akVsSoftDropCh1PFSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropCh1PFSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh1PFNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh1PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropCh1PFJetBtagging = cms.Sequence(akVsSoftDropCh1PFJetBtaggingIP
            *akVsSoftDropCh1PFJetBtaggingSV
            *akVsSoftDropCh1PFJetBtaggingNegSV
#            *akVsSoftDropCh1PFJetBtaggingMu
            )

akVsSoftDropCh1PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropCh1PFJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropCh1PFmatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropCh1PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropCh1PFcorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropCh1PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropCh1PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropCh1PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropCh1PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh1PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropCh1PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropCh1PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropCh1PFJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropCh1PFJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropCh1PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropCh1PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropCh1PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh1PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropCh1PFJetID"),
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

akVsSoftDropCh1PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropCh1PFJets"),
           	    R0  = cms.double( 0.1)
)
akVsSoftDropCh1PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh1PFNjettiness:tau1','akVsSoftDropCh1PFNjettiness:tau2','akVsSoftDropCh1PFNjettiness:tau3']

akVsSoftDropCh1PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropCh1PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak1HiSignalGenJets',#'ak1HiGenJets',
                                                             rParam = 0.1,
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
                                                             bTagJetName = cms.untracked.string("akVsSoftDropCh1PF"),
                                                             jetName = cms.untracked.string("akVsSoftDropCh1PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropCh1GenJets"),
                                                             doGenTaus = False,
                                                             genTau1 = cms.InputTag("akSoftDropCh1GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropCh1GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropCh1GenNjettiness","tau3"),
                                                             doGenSym = True,
                                                             genSym = cms.InputTag("akSoftDropCh1GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropCh1GenJets","droppedBranches")
                                                             )

akVsSoftDropCh1PFJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropCh1PFclean
                                                  #*
                                                  akVsSoftDropCh1PFmatch
                                                  #*
                                                  #akVsSoftDropCh1PFmatchGroomed
                                                  *
                                                  akVsSoftDropCh1PFparton
                                                  *
                                                  akVsSoftDropCh1PFcorr
                                                  *
                                                  #akVsSoftDropCh1PFJetID
                                                  #*
                                                  akVsSoftDropCh1PFPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropCh1PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropCh1PFJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropCh1PFJetBtagging
                                                  *
                                                  akVsSoftDropCh1PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropCh1PFpatJetsWithBtagging
                                                  *
                                                  akVsSoftDropCh1PFJetAnalyzer
                                                  )

akVsSoftDropCh1PFJetSequence_data = cms.Sequence(akVsSoftDropCh1PFcorr
                                                    *
                                                    #akVsSoftDropCh1PFJetID
                                                    #*
                                                    akVsSoftDropCh1PFJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropCh1PFJetBtagging
                                                    *
                                                    akVsSoftDropCh1PFNjettiness 
                                                    *
                                                    akVsSoftDropCh1PFpatJetsWithBtagging
                                                    *
                                                    akVsSoftDropCh1PFJetAnalyzer
                                                    )

akVsSoftDropCh1PFJetSequence_jec = cms.Sequence(akVsSoftDropCh1PFJetSequence_mc)
akVsSoftDropCh1PFJetSequence_mb = cms.Sequence(akVsSoftDropCh1PFJetSequence_mc)

akVsSoftDropCh1PFJetSequence = cms.Sequence(akVsSoftDropCh1PFJetSequence_mc)
akVsSoftDropCh1PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh1PFJets:sym']
akVsSoftDropCh1PFpatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropCh1PFJets:droppedBranches']
