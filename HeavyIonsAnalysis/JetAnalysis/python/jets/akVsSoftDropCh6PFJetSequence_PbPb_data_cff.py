

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropCh6PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropCh6PFJets"),
    matched = cms.InputTag("ak6HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.6
    )

akVsSoftDropCh6PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh6HiGenJets"),
    matched = cms.InputTag("ak6HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.6
    )

akVsSoftDropCh6PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh6PFJets")
                                                        )

akVsSoftDropCh6PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropCh6PFJets"),
    payload = "AK6PF_offline"
    )

akVsSoftDropCh6PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropCh6CaloJets'))

#akVsSoftDropCh6PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak6HiSignalGenJets'))

akVsSoftDropCh6PFbTagger = bTaggers("akVsSoftDropCh6PF",0.6)

#create objects locally since they dont load properly otherwise
#akVsSoftDropCh6PFmatch = akVsSoftDropCh6PFbTagger.match
akVsSoftDropCh6PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh6PFJets"), matched = cms.InputTag("hiSignalGenParticles"))
akVsSoftDropCh6PFPatJetFlavourAssociationLegacy = akVsSoftDropCh6PFbTagger.PatJetFlavourAssociationLegacy
akVsSoftDropCh6PFPatJetPartons = akVsSoftDropCh6PFbTagger.PatJetPartons
akVsSoftDropCh6PFJetTracksAssociatorAtVertex = akVsSoftDropCh6PFbTagger.JetTracksAssociatorAtVertex
akVsSoftDropCh6PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropCh6PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh6PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh6PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh6PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh6PFCombinedSecondaryVertexBJetTags = akVsSoftDropCh6PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh6PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh6PFbTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropCh6PFJetBProbabilityBJetTags = akVsSoftDropCh6PFbTagger.JetBProbabilityBJetTags
akVsSoftDropCh6PFSoftPFMuonByPtBJetTags = akVsSoftDropCh6PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh6PFSoftPFMuonByIP3dBJetTags = akVsSoftDropCh6PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh6PFTrackCountingHighEffBJetTags = akVsSoftDropCh6PFbTagger.TrackCountingHighEffBJetTags
akVsSoftDropCh6PFTrackCountingHighPurBJetTags = akVsSoftDropCh6PFbTagger.TrackCountingHighPurBJetTags
akVsSoftDropCh6PFPatJetPartonAssociationLegacy = akVsSoftDropCh6PFbTagger.PatJetPartonAssociationLegacy

akVsSoftDropCh6PFImpactParameterTagInfos = akVsSoftDropCh6PFbTagger.ImpactParameterTagInfos
akVsSoftDropCh6PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh6PFJetProbabilityBJetTags = akVsSoftDropCh6PFbTagger.JetProbabilityBJetTags

akVsSoftDropCh6PFSecondaryVertexTagInfos = akVsSoftDropCh6PFbTagger.SecondaryVertexTagInfos
akVsSoftDropCh6PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh6PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh6PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh6PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh6PFCombinedSecondaryVertexBJetTags = akVsSoftDropCh6PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh6PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh6PFbTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropCh6PFSecondaryVertexNegativeTagInfos = akVsSoftDropCh6PFbTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropCh6PFNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh6PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh6PFNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh6PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh6PFNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropCh6PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropCh6PFPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropCh6PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropCh6PFNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh6PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropCh6PFPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh6PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropCh6PFSoftPFMuonsTagInfos = akVsSoftDropCh6PFbTagger.SoftPFMuonsTagInfos
akVsSoftDropCh6PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh6PFSoftPFMuonBJetTags = akVsSoftDropCh6PFbTagger.SoftPFMuonBJetTags
akVsSoftDropCh6PFSoftPFMuonByIP3dBJetTags = akVsSoftDropCh6PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh6PFSoftPFMuonByPtBJetTags = akVsSoftDropCh6PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh6PFNegativeSoftPFMuonByPtBJetTags = akVsSoftDropCh6PFbTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropCh6PFPositiveSoftPFMuonByPtBJetTags = akVsSoftDropCh6PFbTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropCh6PFPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropCh6PFPatJetPartonAssociationLegacy*akVsSoftDropCh6PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropCh6PFPatJetFlavourAssociation = akVsSoftDropCh6PFbTagger.PatJetFlavourAssociation
#akVsSoftDropCh6PFPatJetFlavourId = cms.Sequence(akVsSoftDropCh6PFPatJetPartons*akVsSoftDropCh6PFPatJetFlavourAssociation)

akVsSoftDropCh6PFJetBtaggingIP       = cms.Sequence(akVsSoftDropCh6PFImpactParameterTagInfos *
            (akVsSoftDropCh6PFTrackCountingHighEffBJetTags +
             akVsSoftDropCh6PFTrackCountingHighPurBJetTags +
             akVsSoftDropCh6PFJetProbabilityBJetTags +
             akVsSoftDropCh6PFJetBProbabilityBJetTags 
            )
            )

akVsSoftDropCh6PFJetBtaggingSV = cms.Sequence(akVsSoftDropCh6PFImpactParameterTagInfos
            *
            akVsSoftDropCh6PFSecondaryVertexTagInfos
            * (akVsSoftDropCh6PFSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh6PFSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh6PFCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh6PFCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh6PFJetBtaggingNegSV = cms.Sequence(akVsSoftDropCh6PFImpactParameterTagInfos
            *
            akVsSoftDropCh6PFSecondaryVertexNegativeTagInfos
            * (akVsSoftDropCh6PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh6PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh6PFNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh6PFPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh6PFNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropCh6PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh6PFJetBtaggingMu = cms.Sequence(akVsSoftDropCh6PFSoftPFMuonsTagInfos * (akVsSoftDropCh6PFSoftPFMuonBJetTags
                +
                akVsSoftDropCh6PFSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropCh6PFSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh6PFNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh6PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropCh6PFJetBtagging = cms.Sequence(akVsSoftDropCh6PFJetBtaggingIP
            *akVsSoftDropCh6PFJetBtaggingSV
            *akVsSoftDropCh6PFJetBtaggingNegSV
#            *akVsSoftDropCh6PFJetBtaggingMu
            )

akVsSoftDropCh6PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropCh6PFJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropCh6PFmatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropCh6PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropCh6PFcorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropCh6PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropCh6PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropCh6PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropCh6PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh6PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropCh6PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropCh6PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropCh6PFJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropCh6PFJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropCh6PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropCh6PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropCh6PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh6PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropCh6PFJetID"),
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

akVsSoftDropCh6PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropCh6PFJets"),
           	    R0  = cms.double( 0.6)
)
akVsSoftDropCh6PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh6PFNjettiness:tau1','akVsSoftDropCh6PFNjettiness:tau2','akVsSoftDropCh6PFNjettiness:tau3']

akVsSoftDropCh6PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropCh6PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak6HiSignalGenJets',#'ak6HiGenJets',
                                                             rParam = 0.6,
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
                                                             bTagJetName = cms.untracked.string("akVsSoftDropCh6PF"),
                                                             jetName = cms.untracked.string("akVsSoftDropCh6PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropCh6GenJets"),
                                                             doGenTaus = False,
                                                             genTau1 = cms.InputTag("akSoftDropCh6GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropCh6GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropCh6GenNjettiness","tau3"),
                                                             doGenSym = True,
                                                             genSym = cms.InputTag("akSoftDropCh6GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropCh6GenJets","droppedBranches")
                                                             )

akVsSoftDropCh6PFJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropCh6PFclean
                                                  #*
                                                  akVsSoftDropCh6PFmatch
                                                  #*
                                                  #akVsSoftDropCh6PFmatchGroomed
                                                  *
                                                  akVsSoftDropCh6PFparton
                                                  *
                                                  akVsSoftDropCh6PFcorr
                                                  *
                                                  #akVsSoftDropCh6PFJetID
                                                  #*
                                                  akVsSoftDropCh6PFPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropCh6PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropCh6PFJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropCh6PFJetBtagging
                                                  *
                                                  akVsSoftDropCh6PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropCh6PFpatJetsWithBtagging
                                                  *
                                                  akVsSoftDropCh6PFJetAnalyzer
                                                  )

akVsSoftDropCh6PFJetSequence_data = cms.Sequence(akVsSoftDropCh6PFcorr
                                                    *
                                                    #akVsSoftDropCh6PFJetID
                                                    #*
                                                    akVsSoftDropCh6PFJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropCh6PFJetBtagging
                                                    *
                                                    akVsSoftDropCh6PFNjettiness 
                                                    *
                                                    akVsSoftDropCh6PFpatJetsWithBtagging
                                                    *
                                                    akVsSoftDropCh6PFJetAnalyzer
                                                    )

akVsSoftDropCh6PFJetSequence_jec = cms.Sequence(akVsSoftDropCh6PFJetSequence_mc)
akVsSoftDropCh6PFJetSequence_mb = cms.Sequence(akVsSoftDropCh6PFJetSequence_mc)

akVsSoftDropCh6PFJetSequence = cms.Sequence(akVsSoftDropCh6PFJetSequence_data)
akVsSoftDropCh6PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh6PFJets:sym']
akVsSoftDropCh6PFpatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropCh6PFJets:droppedBranches']
