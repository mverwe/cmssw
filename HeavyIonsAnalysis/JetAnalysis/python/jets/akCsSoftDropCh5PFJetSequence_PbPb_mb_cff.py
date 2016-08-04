

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akCsSoftDropCh5PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akCsSoftDropCh5PFJets"),
    matched = cms.InputTag("ak5HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.5
    )

akCsSoftDropCh5PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh5HiGenJets"),
    matched = cms.InputTag("ak5HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.5
    )

akCsSoftDropCh5PFparton = patJetPartonMatch.clone(src = cms.InputTag("akCsSoftDropCh5PFJets")
                                                        )

akCsSoftDropCh5PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akCsSoftDropCh5PFJets"),
    payload = "AK5PF_offline"
    )

akCsSoftDropCh5PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akCsSoftDropCh5CaloJets'))

#akCsSoftDropCh5PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak5HiCleanedGenJets'))

akCsSoftDropCh5PFbTagger = bTaggers("akCsSoftDropCh5PF",0.5)

#create objects locally since they dont load properly otherwise
#akCsSoftDropCh5PFmatch = akCsSoftDropCh5PFbTagger.match
akCsSoftDropCh5PFparton = patJetPartonMatch.clone(src = cms.InputTag("akCsSoftDropCh5PFJets"), matched = cms.InputTag("selectedPartons"))
akCsSoftDropCh5PFPatJetFlavourAssociationLegacy = akCsSoftDropCh5PFbTagger.PatJetFlavourAssociationLegacy
akCsSoftDropCh5PFPatJetPartons = akCsSoftDropCh5PFbTagger.PatJetPartons
akCsSoftDropCh5PFJetTracksAssociatorAtVertex = akCsSoftDropCh5PFbTagger.JetTracksAssociatorAtVertex
akCsSoftDropCh5PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akCsSoftDropCh5PFSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropCh5PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akCsSoftDropCh5PFSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropCh5PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akCsSoftDropCh5PFCombinedSecondaryVertexBJetTags = akCsSoftDropCh5PFbTagger.CombinedSecondaryVertexBJetTags
akCsSoftDropCh5PFCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh5PFbTagger.CombinedSecondaryVertexV2BJetTags
akCsSoftDropCh5PFJetBProbabilityBJetTags = akCsSoftDropCh5PFbTagger.JetBProbabilityBJetTags
akCsSoftDropCh5PFSoftPFMuonByPtBJetTags = akCsSoftDropCh5PFbTagger.SoftPFMuonByPtBJetTags
akCsSoftDropCh5PFSoftPFMuonByIP3dBJetTags = akCsSoftDropCh5PFbTagger.SoftPFMuonByIP3dBJetTags
akCsSoftDropCh5PFTrackCountingHighEffBJetTags = akCsSoftDropCh5PFbTagger.TrackCountingHighEffBJetTags
akCsSoftDropCh5PFTrackCountingHighPurBJetTags = akCsSoftDropCh5PFbTagger.TrackCountingHighPurBJetTags
akCsSoftDropCh5PFPatJetPartonAssociationLegacy = akCsSoftDropCh5PFbTagger.PatJetPartonAssociationLegacy

akCsSoftDropCh5PFImpactParameterTagInfos = akCsSoftDropCh5PFbTagger.ImpactParameterTagInfos
akCsSoftDropCh5PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akCsSoftDropCh5PFJetProbabilityBJetTags = akCsSoftDropCh5PFbTagger.JetProbabilityBJetTags

akCsSoftDropCh5PFSecondaryVertexTagInfos = akCsSoftDropCh5PFbTagger.SecondaryVertexTagInfos
akCsSoftDropCh5PFSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropCh5PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akCsSoftDropCh5PFSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropCh5PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akCsSoftDropCh5PFCombinedSecondaryVertexBJetTags = akCsSoftDropCh5PFbTagger.CombinedSecondaryVertexBJetTags
akCsSoftDropCh5PFCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh5PFbTagger.CombinedSecondaryVertexV2BJetTags

akCsSoftDropCh5PFSecondaryVertexNegativeTagInfos = akCsSoftDropCh5PFbTagger.SecondaryVertexNegativeTagInfos
akCsSoftDropCh5PFNegativeSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropCh5PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akCsSoftDropCh5PFNegativeSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropCh5PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akCsSoftDropCh5PFNegativeCombinedSecondaryVertexBJetTags = akCsSoftDropCh5PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akCsSoftDropCh5PFPositiveCombinedSecondaryVertexBJetTags = akCsSoftDropCh5PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akCsSoftDropCh5PFNegativeCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh5PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akCsSoftDropCh5PFPositiveCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh5PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akCsSoftDropCh5PFSoftPFMuonsTagInfos = akCsSoftDropCh5PFbTagger.SoftPFMuonsTagInfos
akCsSoftDropCh5PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akCsSoftDropCh5PFSoftPFMuonBJetTags = akCsSoftDropCh5PFbTagger.SoftPFMuonBJetTags
akCsSoftDropCh5PFSoftPFMuonByIP3dBJetTags = akCsSoftDropCh5PFbTagger.SoftPFMuonByIP3dBJetTags
akCsSoftDropCh5PFSoftPFMuonByPtBJetTags = akCsSoftDropCh5PFbTagger.SoftPFMuonByPtBJetTags
akCsSoftDropCh5PFNegativeSoftPFMuonByPtBJetTags = akCsSoftDropCh5PFbTagger.NegativeSoftPFMuonByPtBJetTags
akCsSoftDropCh5PFPositiveSoftPFMuonByPtBJetTags = akCsSoftDropCh5PFbTagger.PositiveSoftPFMuonByPtBJetTags
akCsSoftDropCh5PFPatJetFlavourIdLegacy = cms.Sequence(akCsSoftDropCh5PFPatJetPartonAssociationLegacy*akCsSoftDropCh5PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akCsSoftDropCh5PFPatJetFlavourAssociation = akCsSoftDropCh5PFbTagger.PatJetFlavourAssociation
#akCsSoftDropCh5PFPatJetFlavourId = cms.Sequence(akCsSoftDropCh5PFPatJetPartons*akCsSoftDropCh5PFPatJetFlavourAssociation)

akCsSoftDropCh5PFJetBtaggingIP       = cms.Sequence(akCsSoftDropCh5PFImpactParameterTagInfos *
            (akCsSoftDropCh5PFTrackCountingHighEffBJetTags +
             akCsSoftDropCh5PFTrackCountingHighPurBJetTags +
             akCsSoftDropCh5PFJetProbabilityBJetTags +
             akCsSoftDropCh5PFJetBProbabilityBJetTags 
            )
            )

akCsSoftDropCh5PFJetBtaggingSV = cms.Sequence(akCsSoftDropCh5PFImpactParameterTagInfos
            *
            akCsSoftDropCh5PFSecondaryVertexTagInfos
            * (akCsSoftDropCh5PFSimpleSecondaryVertexHighEffBJetTags+
                akCsSoftDropCh5PFSimpleSecondaryVertexHighPurBJetTags+
                akCsSoftDropCh5PFCombinedSecondaryVertexBJetTags+
                akCsSoftDropCh5PFCombinedSecondaryVertexV2BJetTags
              )
            )

akCsSoftDropCh5PFJetBtaggingNegSV = cms.Sequence(akCsSoftDropCh5PFImpactParameterTagInfos
            *
            akCsSoftDropCh5PFSecondaryVertexNegativeTagInfos
            * (akCsSoftDropCh5PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akCsSoftDropCh5PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akCsSoftDropCh5PFNegativeCombinedSecondaryVertexBJetTags+
                akCsSoftDropCh5PFPositiveCombinedSecondaryVertexBJetTags+
                akCsSoftDropCh5PFNegativeCombinedSecondaryVertexV2BJetTags+
                akCsSoftDropCh5PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akCsSoftDropCh5PFJetBtaggingMu = cms.Sequence(akCsSoftDropCh5PFSoftPFMuonsTagInfos * (akCsSoftDropCh5PFSoftPFMuonBJetTags
                +
                akCsSoftDropCh5PFSoftPFMuonByIP3dBJetTags
                +
                akCsSoftDropCh5PFSoftPFMuonByPtBJetTags
                +
                akCsSoftDropCh5PFNegativeSoftPFMuonByPtBJetTags
                +
                akCsSoftDropCh5PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akCsSoftDropCh5PFJetBtagging = cms.Sequence(akCsSoftDropCh5PFJetBtaggingIP
            *akCsSoftDropCh5PFJetBtaggingSV
            *akCsSoftDropCh5PFJetBtaggingNegSV
#            *akCsSoftDropCh5PFJetBtaggingMu
            )

akCsSoftDropCh5PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akCsSoftDropCh5PFJets"),
        genJetMatch          = cms.InputTag("akCsSoftDropCh5PFmatch"),
        genPartonMatch       = cms.InputTag("akCsSoftDropCh5PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akCsSoftDropCh5PFcorr")),
        JetPartonMapSource   = cms.InputTag("akCsSoftDropCh5PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akCsSoftDropCh5PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akCsSoftDropCh5PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akCsSoftDropCh5PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akCsSoftDropCh5PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akCsSoftDropCh5PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akCsSoftDropCh5PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akCsSoftDropCh5PFJetBProbabilityBJetTags"),
            cms.InputTag("akCsSoftDropCh5PFJetProbabilityBJetTags"),
            #cms.InputTag("akCsSoftDropCh5PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akCsSoftDropCh5PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akCsSoftDropCh5PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akCsSoftDropCh5PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akCsSoftDropCh5PFJetID"),
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

akCsSoftDropCh5PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akCsSoftDropCh5PFJets"),
           	    R0  = cms.double( 0.5)
)
akCsSoftDropCh5PFpatJetsWithBtagging.userData.userFloats.src += ['akCsSoftDropCh5PFNjettiness:tau1','akCsSoftDropCh5PFNjettiness:tau2','akCsSoftDropCh5PFNjettiness:tau3']

akCsSoftDropCh5PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akCsSoftDropCh5PFpatJetsWithBtagging"),
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
                                                             bTagJetName = cms.untracked.string("akCsSoftDropCh5PF"),
                                                             jetName = cms.untracked.string("akCsSoftDropCh5PF"),
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

akCsSoftDropCh5PFJetSequence_mc = cms.Sequence(
                                                  #akCsSoftDropCh5PFclean
                                                  #*
                                                  akCsSoftDropCh5PFmatch
                                                  #*
                                                  #akCsSoftDropCh5PFmatchGroomed
                                                  *
                                                  akCsSoftDropCh5PFparton
                                                  *
                                                  akCsSoftDropCh5PFcorr
                                                  *
                                                  #akCsSoftDropCh5PFJetID
                                                  #*
                                                  akCsSoftDropCh5PFPatJetFlavourIdLegacy
                                                  #*
			                          #akCsSoftDropCh5PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akCsSoftDropCh5PFJetTracksAssociatorAtVertex
                                                  *
                                                  akCsSoftDropCh5PFJetBtagging
                                                  *
                                                  akCsSoftDropCh5PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akCsSoftDropCh5PFpatJetsWithBtagging
                                                  *
                                                  akCsSoftDropCh5PFJetAnalyzer
                                                  )

akCsSoftDropCh5PFJetSequence_data = cms.Sequence(akCsSoftDropCh5PFcorr
                                                    *
                                                    #akCsSoftDropCh5PFJetID
                                                    #*
                                                    akCsSoftDropCh5PFJetTracksAssociatorAtVertex
                                                    *
                                                    akCsSoftDropCh5PFJetBtagging
                                                    *
                                                    akCsSoftDropCh5PFNjettiness 
                                                    *
                                                    akCsSoftDropCh5PFpatJetsWithBtagging
                                                    *
                                                    akCsSoftDropCh5PFJetAnalyzer
                                                    )

akCsSoftDropCh5PFJetSequence_jec = cms.Sequence(akCsSoftDropCh5PFJetSequence_mc)
akCsSoftDropCh5PFJetSequence_mb = cms.Sequence(akCsSoftDropCh5PFJetSequence_mc)

akCsSoftDropCh5PFJetSequence = cms.Sequence(akCsSoftDropCh5PFJetSequence_mb)
akCsSoftDropCh5PFpatJetsWithBtagging.userData.userFloats.src += ['akCsSoftDropCh5PFJets:sym']
akCsSoftDropCh5PFpatJetsWithBtagging.userData.userInts.src += ['akCsSoftDropCh5PFJets:droppedBranches']
