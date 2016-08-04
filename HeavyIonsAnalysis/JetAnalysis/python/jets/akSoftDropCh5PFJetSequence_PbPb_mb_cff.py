

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDropCh5PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh5PFJets"),
    matched = cms.InputTag("ak5HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.5
    )

akSoftDropCh5PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh5HiGenJets"),
    matched = cms.InputTag("ak5HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.5
    )

akSoftDropCh5PFparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh5PFJets")
                                                        )

akSoftDropCh5PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akSoftDropCh5PFJets"),
    payload = "AK5PF_offline"
    )

akSoftDropCh5PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akSoftDropCh5CaloJets'))

#akSoftDropCh5PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak5HiCleanedGenJets'))

akSoftDropCh5PFbTagger = bTaggers("akSoftDropCh5PF",0.5)

#create objects locally since they dont load properly otherwise
#akSoftDropCh5PFmatch = akSoftDropCh5PFbTagger.match
akSoftDropCh5PFparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh5PFJets"), matched = cms.InputTag("selectedPartons"))
akSoftDropCh5PFPatJetFlavourAssociationLegacy = akSoftDropCh5PFbTagger.PatJetFlavourAssociationLegacy
akSoftDropCh5PFPatJetPartons = akSoftDropCh5PFbTagger.PatJetPartons
akSoftDropCh5PFJetTracksAssociatorAtVertex = akSoftDropCh5PFbTagger.JetTracksAssociatorAtVertex
akSoftDropCh5PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDropCh5PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh5PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh5PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh5PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh5PFCombinedSecondaryVertexBJetTags = akSoftDropCh5PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh5PFCombinedSecondaryVertexV2BJetTags = akSoftDropCh5PFbTagger.CombinedSecondaryVertexV2BJetTags
akSoftDropCh5PFJetBProbabilityBJetTags = akSoftDropCh5PFbTagger.JetBProbabilityBJetTags
akSoftDropCh5PFSoftPFMuonByPtBJetTags = akSoftDropCh5PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropCh5PFSoftPFMuonByIP3dBJetTags = akSoftDropCh5PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh5PFTrackCountingHighEffBJetTags = akSoftDropCh5PFbTagger.TrackCountingHighEffBJetTags
akSoftDropCh5PFTrackCountingHighPurBJetTags = akSoftDropCh5PFbTagger.TrackCountingHighPurBJetTags
akSoftDropCh5PFPatJetPartonAssociationLegacy = akSoftDropCh5PFbTagger.PatJetPartonAssociationLegacy

akSoftDropCh5PFImpactParameterTagInfos = akSoftDropCh5PFbTagger.ImpactParameterTagInfos
akSoftDropCh5PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh5PFJetProbabilityBJetTags = akSoftDropCh5PFbTagger.JetProbabilityBJetTags

akSoftDropCh5PFSecondaryVertexTagInfos = akSoftDropCh5PFbTagger.SecondaryVertexTagInfos
akSoftDropCh5PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh5PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh5PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh5PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh5PFCombinedSecondaryVertexBJetTags = akSoftDropCh5PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh5PFCombinedSecondaryVertexV2BJetTags = akSoftDropCh5PFbTagger.CombinedSecondaryVertexV2BJetTags

akSoftDropCh5PFSecondaryVertexNegativeTagInfos = akSoftDropCh5PFbTagger.SecondaryVertexNegativeTagInfos
akSoftDropCh5PFNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh5PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDropCh5PFNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh5PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDropCh5PFNegativeCombinedSecondaryVertexBJetTags = akSoftDropCh5PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDropCh5PFPositiveCombinedSecondaryVertexBJetTags = akSoftDropCh5PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDropCh5PFNegativeCombinedSecondaryVertexV2BJetTags = akSoftDropCh5PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDropCh5PFPositiveCombinedSecondaryVertexV2BJetTags = akSoftDropCh5PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDropCh5PFSoftPFMuonsTagInfos = akSoftDropCh5PFbTagger.SoftPFMuonsTagInfos
akSoftDropCh5PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh5PFSoftPFMuonBJetTags = akSoftDropCh5PFbTagger.SoftPFMuonBJetTags
akSoftDropCh5PFSoftPFMuonByIP3dBJetTags = akSoftDropCh5PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh5PFSoftPFMuonByPtBJetTags = akSoftDropCh5PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropCh5PFNegativeSoftPFMuonByPtBJetTags = akSoftDropCh5PFbTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDropCh5PFPositiveSoftPFMuonByPtBJetTags = akSoftDropCh5PFbTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDropCh5PFPatJetFlavourIdLegacy = cms.Sequence(akSoftDropCh5PFPatJetPartonAssociationLegacy*akSoftDropCh5PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akSoftDropCh5PFPatJetFlavourAssociation = akSoftDropCh5PFbTagger.PatJetFlavourAssociation
#akSoftDropCh5PFPatJetFlavourId = cms.Sequence(akSoftDropCh5PFPatJetPartons*akSoftDropCh5PFPatJetFlavourAssociation)

akSoftDropCh5PFJetBtaggingIP       = cms.Sequence(akSoftDropCh5PFImpactParameterTagInfos *
            (akSoftDropCh5PFTrackCountingHighEffBJetTags +
             akSoftDropCh5PFTrackCountingHighPurBJetTags +
             akSoftDropCh5PFJetProbabilityBJetTags +
             akSoftDropCh5PFJetBProbabilityBJetTags 
            )
            )

akSoftDropCh5PFJetBtaggingSV = cms.Sequence(akSoftDropCh5PFImpactParameterTagInfos
            *
            akSoftDropCh5PFSecondaryVertexTagInfos
            * (akSoftDropCh5PFSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh5PFSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh5PFCombinedSecondaryVertexBJetTags+
                akSoftDropCh5PFCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh5PFJetBtaggingNegSV = cms.Sequence(akSoftDropCh5PFImpactParameterTagInfos
            *
            akSoftDropCh5PFSecondaryVertexNegativeTagInfos
            * (akSoftDropCh5PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh5PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh5PFNegativeCombinedSecondaryVertexBJetTags+
                akSoftDropCh5PFPositiveCombinedSecondaryVertexBJetTags+
                akSoftDropCh5PFNegativeCombinedSecondaryVertexV2BJetTags+
                akSoftDropCh5PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh5PFJetBtaggingMu = cms.Sequence(akSoftDropCh5PFSoftPFMuonsTagInfos * (akSoftDropCh5PFSoftPFMuonBJetTags
                +
                akSoftDropCh5PFSoftPFMuonByIP3dBJetTags
                +
                akSoftDropCh5PFSoftPFMuonByPtBJetTags
                +
                akSoftDropCh5PFNegativeSoftPFMuonByPtBJetTags
                +
                akSoftDropCh5PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akSoftDropCh5PFJetBtagging = cms.Sequence(akSoftDropCh5PFJetBtaggingIP
            *akSoftDropCh5PFJetBtaggingSV
            *akSoftDropCh5PFJetBtaggingNegSV
#            *akSoftDropCh5PFJetBtaggingMu
            )

akSoftDropCh5PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akSoftDropCh5PFJets"),
        genJetMatch          = cms.InputTag("akSoftDropCh5PFmatch"),
        genPartonMatch       = cms.InputTag("akSoftDropCh5PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akSoftDropCh5PFcorr")),
        JetPartonMapSource   = cms.InputTag("akSoftDropCh5PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akSoftDropCh5PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akSoftDropCh5PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akSoftDropCh5PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akSoftDropCh5PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akSoftDropCh5PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akSoftDropCh5PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akSoftDropCh5PFJetBProbabilityBJetTags"),
            cms.InputTag("akSoftDropCh5PFJetProbabilityBJetTags"),
            #cms.InputTag("akSoftDropCh5PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akSoftDropCh5PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akSoftDropCh5PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akSoftDropCh5PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akSoftDropCh5PFJetID"),
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

akSoftDropCh5PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akSoftDropCh5PFJets"),
           	    R0  = cms.double( 0.5)
)
akSoftDropCh5PFpatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh5PFNjettiness:tau1','akSoftDropCh5PFNjettiness:tau2','akSoftDropCh5PFNjettiness:tau3']

akSoftDropCh5PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akSoftDropCh5PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak5HiCleanedGenJets',#'ak5HiGenJets',
                                                             rParam = 0.5,
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
                                                             bTagJetName = cms.untracked.string("akSoftDropCh5PF"),
                                                             jetName = cms.untracked.string("akSoftDropCh5PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropCh5GenJets"),
                                                             doGenTaus = False,
                                                             genTau1 = cms.InputTag("akSoftDropCh5GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropCh5GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropCh5GenNjettiness","tau3"),
                                                             doGenSym = True,
                                                             genSym = cms.InputTag("akSoftDropCh5GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropCh5GenJets","droppedBranches")
                                                             )

akSoftDropCh5PFJetSequence_mc = cms.Sequence(
                                                  #akSoftDropCh5PFclean
                                                  #*
                                                  akSoftDropCh5PFmatch
                                                  #*
                                                  #akSoftDropCh5PFmatchGroomed
                                                  *
                                                  akSoftDropCh5PFparton
                                                  *
                                                  akSoftDropCh5PFcorr
                                                  *
                                                  #akSoftDropCh5PFJetID
                                                  #*
                                                  akSoftDropCh5PFPatJetFlavourIdLegacy
                                                  #*
			                          #akSoftDropCh5PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akSoftDropCh5PFJetTracksAssociatorAtVertex
                                                  *
                                                  akSoftDropCh5PFJetBtagging
                                                  *
                                                  akSoftDropCh5PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akSoftDropCh5PFpatJetsWithBtagging
                                                  *
                                                  akSoftDropCh5PFJetAnalyzer
                                                  )

akSoftDropCh5PFJetSequence_data = cms.Sequence(akSoftDropCh5PFcorr
                                                    *
                                                    #akSoftDropCh5PFJetID
                                                    #*
                                                    akSoftDropCh5PFJetTracksAssociatorAtVertex
                                                    *
                                                    akSoftDropCh5PFJetBtagging
                                                    *
                                                    akSoftDropCh5PFNjettiness 
                                                    *
                                                    akSoftDropCh5PFpatJetsWithBtagging
                                                    *
                                                    akSoftDropCh5PFJetAnalyzer
                                                    )

akSoftDropCh5PFJetSequence_jec = cms.Sequence(akSoftDropCh5PFJetSequence_mc)
akSoftDropCh5PFJetSequence_mb = cms.Sequence(akSoftDropCh5PFJetSequence_mc)

akSoftDropCh5PFJetSequence = cms.Sequence(akSoftDropCh5PFJetSequence_mb)
akSoftDropCh5PFpatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh5PFJets:sym']
akSoftDropCh5PFpatJetsWithBtagging.userData.userInts.src += ['akSoftDropCh5PFJets:droppedBranches']
