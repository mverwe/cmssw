

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akCsSoftDropCh3PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akCsSoftDropCh3PFJets"),
    matched = cms.InputTag("ak3HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.3
    )

akCsSoftDropCh3PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh3HiGenJets"),
    matched = cms.InputTag("ak3HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.3
    )

akCsSoftDropCh3PFparton = patJetPartonMatch.clone(src = cms.InputTag("akCsSoftDropCh3PFJets")
                                                        )

akCsSoftDropCh3PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akCsSoftDropCh3PFJets"),
    payload = "AK3PF_offline"
    )

akCsSoftDropCh3PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akCsSoftDropCh3CaloJets'))

#akCsSoftDropCh3PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak3HiCleanedGenJets'))

akCsSoftDropCh3PFbTagger = bTaggers("akCsSoftDropCh3PF",0.3)

#create objects locally since they dont load properly otherwise
#akCsSoftDropCh3PFmatch = akCsSoftDropCh3PFbTagger.match
akCsSoftDropCh3PFparton = patJetPartonMatch.clone(src = cms.InputTag("akCsSoftDropCh3PFJets"), matched = cms.InputTag("selectedPartons"))
akCsSoftDropCh3PFPatJetFlavourAssociationLegacy = akCsSoftDropCh3PFbTagger.PatJetFlavourAssociationLegacy
akCsSoftDropCh3PFPatJetPartons = akCsSoftDropCh3PFbTagger.PatJetPartons
akCsSoftDropCh3PFJetTracksAssociatorAtVertex = akCsSoftDropCh3PFbTagger.JetTracksAssociatorAtVertex
akCsSoftDropCh3PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akCsSoftDropCh3PFSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropCh3PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akCsSoftDropCh3PFSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropCh3PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akCsSoftDropCh3PFCombinedSecondaryVertexBJetTags = akCsSoftDropCh3PFbTagger.CombinedSecondaryVertexBJetTags
akCsSoftDropCh3PFCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh3PFbTagger.CombinedSecondaryVertexV2BJetTags
akCsSoftDropCh3PFJetBProbabilityBJetTags = akCsSoftDropCh3PFbTagger.JetBProbabilityBJetTags
akCsSoftDropCh3PFSoftPFMuonByPtBJetTags = akCsSoftDropCh3PFbTagger.SoftPFMuonByPtBJetTags
akCsSoftDropCh3PFSoftPFMuonByIP3dBJetTags = akCsSoftDropCh3PFbTagger.SoftPFMuonByIP3dBJetTags
akCsSoftDropCh3PFTrackCountingHighEffBJetTags = akCsSoftDropCh3PFbTagger.TrackCountingHighEffBJetTags
akCsSoftDropCh3PFTrackCountingHighPurBJetTags = akCsSoftDropCh3PFbTagger.TrackCountingHighPurBJetTags
akCsSoftDropCh3PFPatJetPartonAssociationLegacy = akCsSoftDropCh3PFbTagger.PatJetPartonAssociationLegacy

akCsSoftDropCh3PFImpactParameterTagInfos = akCsSoftDropCh3PFbTagger.ImpactParameterTagInfos
akCsSoftDropCh3PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akCsSoftDropCh3PFJetProbabilityBJetTags = akCsSoftDropCh3PFbTagger.JetProbabilityBJetTags

akCsSoftDropCh3PFSecondaryVertexTagInfos = akCsSoftDropCh3PFbTagger.SecondaryVertexTagInfos
akCsSoftDropCh3PFSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropCh3PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akCsSoftDropCh3PFSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropCh3PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akCsSoftDropCh3PFCombinedSecondaryVertexBJetTags = akCsSoftDropCh3PFbTagger.CombinedSecondaryVertexBJetTags
akCsSoftDropCh3PFCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh3PFbTagger.CombinedSecondaryVertexV2BJetTags

akCsSoftDropCh3PFSecondaryVertexNegativeTagInfos = akCsSoftDropCh3PFbTagger.SecondaryVertexNegativeTagInfos
akCsSoftDropCh3PFNegativeSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropCh3PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akCsSoftDropCh3PFNegativeSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropCh3PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akCsSoftDropCh3PFNegativeCombinedSecondaryVertexBJetTags = akCsSoftDropCh3PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akCsSoftDropCh3PFPositiveCombinedSecondaryVertexBJetTags = akCsSoftDropCh3PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akCsSoftDropCh3PFNegativeCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh3PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akCsSoftDropCh3PFPositiveCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh3PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akCsSoftDropCh3PFSoftPFMuonsTagInfos = akCsSoftDropCh3PFbTagger.SoftPFMuonsTagInfos
akCsSoftDropCh3PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akCsSoftDropCh3PFSoftPFMuonBJetTags = akCsSoftDropCh3PFbTagger.SoftPFMuonBJetTags
akCsSoftDropCh3PFSoftPFMuonByIP3dBJetTags = akCsSoftDropCh3PFbTagger.SoftPFMuonByIP3dBJetTags
akCsSoftDropCh3PFSoftPFMuonByPtBJetTags = akCsSoftDropCh3PFbTagger.SoftPFMuonByPtBJetTags
akCsSoftDropCh3PFNegativeSoftPFMuonByPtBJetTags = akCsSoftDropCh3PFbTagger.NegativeSoftPFMuonByPtBJetTags
akCsSoftDropCh3PFPositiveSoftPFMuonByPtBJetTags = akCsSoftDropCh3PFbTagger.PositiveSoftPFMuonByPtBJetTags
akCsSoftDropCh3PFPatJetFlavourIdLegacy = cms.Sequence(akCsSoftDropCh3PFPatJetPartonAssociationLegacy*akCsSoftDropCh3PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akCsSoftDropCh3PFPatJetFlavourAssociation = akCsSoftDropCh3PFbTagger.PatJetFlavourAssociation
#akCsSoftDropCh3PFPatJetFlavourId = cms.Sequence(akCsSoftDropCh3PFPatJetPartons*akCsSoftDropCh3PFPatJetFlavourAssociation)

akCsSoftDropCh3PFJetBtaggingIP       = cms.Sequence(akCsSoftDropCh3PFImpactParameterTagInfos *
            (akCsSoftDropCh3PFTrackCountingHighEffBJetTags +
             akCsSoftDropCh3PFTrackCountingHighPurBJetTags +
             akCsSoftDropCh3PFJetProbabilityBJetTags +
             akCsSoftDropCh3PFJetBProbabilityBJetTags 
            )
            )

akCsSoftDropCh3PFJetBtaggingSV = cms.Sequence(akCsSoftDropCh3PFImpactParameterTagInfos
            *
            akCsSoftDropCh3PFSecondaryVertexTagInfos
            * (akCsSoftDropCh3PFSimpleSecondaryVertexHighEffBJetTags+
                akCsSoftDropCh3PFSimpleSecondaryVertexHighPurBJetTags+
                akCsSoftDropCh3PFCombinedSecondaryVertexBJetTags+
                akCsSoftDropCh3PFCombinedSecondaryVertexV2BJetTags
              )
            )

akCsSoftDropCh3PFJetBtaggingNegSV = cms.Sequence(akCsSoftDropCh3PFImpactParameterTagInfos
            *
            akCsSoftDropCh3PFSecondaryVertexNegativeTagInfos
            * (akCsSoftDropCh3PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akCsSoftDropCh3PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akCsSoftDropCh3PFNegativeCombinedSecondaryVertexBJetTags+
                akCsSoftDropCh3PFPositiveCombinedSecondaryVertexBJetTags+
                akCsSoftDropCh3PFNegativeCombinedSecondaryVertexV2BJetTags+
                akCsSoftDropCh3PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akCsSoftDropCh3PFJetBtaggingMu = cms.Sequence(akCsSoftDropCh3PFSoftPFMuonsTagInfos * (akCsSoftDropCh3PFSoftPFMuonBJetTags
                +
                akCsSoftDropCh3PFSoftPFMuonByIP3dBJetTags
                +
                akCsSoftDropCh3PFSoftPFMuonByPtBJetTags
                +
                akCsSoftDropCh3PFNegativeSoftPFMuonByPtBJetTags
                +
                akCsSoftDropCh3PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akCsSoftDropCh3PFJetBtagging = cms.Sequence(akCsSoftDropCh3PFJetBtaggingIP
            *akCsSoftDropCh3PFJetBtaggingSV
            *akCsSoftDropCh3PFJetBtaggingNegSV
#            *akCsSoftDropCh3PFJetBtaggingMu
            )

akCsSoftDropCh3PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akCsSoftDropCh3PFJets"),
        genJetMatch          = cms.InputTag("akCsSoftDropCh3PFmatch"),
        genPartonMatch       = cms.InputTag("akCsSoftDropCh3PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akCsSoftDropCh3PFcorr")),
        JetPartonMapSource   = cms.InputTag("akCsSoftDropCh3PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akCsSoftDropCh3PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akCsSoftDropCh3PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akCsSoftDropCh3PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akCsSoftDropCh3PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akCsSoftDropCh3PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akCsSoftDropCh3PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akCsSoftDropCh3PFJetBProbabilityBJetTags"),
            cms.InputTag("akCsSoftDropCh3PFJetProbabilityBJetTags"),
            #cms.InputTag("akCsSoftDropCh3PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akCsSoftDropCh3PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akCsSoftDropCh3PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akCsSoftDropCh3PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akCsSoftDropCh3PFJetID"),
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

akCsSoftDropCh3PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akCsSoftDropCh3PFJets"),
           	    R0  = cms.double( 0.3)
)
akCsSoftDropCh3PFpatJetsWithBtagging.userData.userFloats.src += ['akCsSoftDropCh3PFNjettiness:tau1','akCsSoftDropCh3PFNjettiness:tau2','akCsSoftDropCh3PFNjettiness:tau3']

akCsSoftDropCh3PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akCsSoftDropCh3PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak3HiCleanedGenJets',#'ak3HiGenJets',
                                                             rParam = 0.3,
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
                                                             bTagJetName = cms.untracked.string("akCsSoftDropCh3PF"),
                                                             jetName = cms.untracked.string("akCsSoftDropCh3PF"),
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

akCsSoftDropCh3PFJetSequence_mc = cms.Sequence(
                                                  #akCsSoftDropCh3PFclean
                                                  #*
                                                  akCsSoftDropCh3PFmatch
                                                  #*
                                                  #akCsSoftDropCh3PFmatchGroomed
                                                  *
                                                  akCsSoftDropCh3PFparton
                                                  *
                                                  akCsSoftDropCh3PFcorr
                                                  *
                                                  #akCsSoftDropCh3PFJetID
                                                  #*
                                                  akCsSoftDropCh3PFPatJetFlavourIdLegacy
                                                  #*
			                          #akCsSoftDropCh3PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akCsSoftDropCh3PFJetTracksAssociatorAtVertex
                                                  *
                                                  akCsSoftDropCh3PFJetBtagging
                                                  *
                                                  akCsSoftDropCh3PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akCsSoftDropCh3PFpatJetsWithBtagging
                                                  *
                                                  akCsSoftDropCh3PFJetAnalyzer
                                                  )

akCsSoftDropCh3PFJetSequence_data = cms.Sequence(akCsSoftDropCh3PFcorr
                                                    *
                                                    #akCsSoftDropCh3PFJetID
                                                    #*
                                                    akCsSoftDropCh3PFJetTracksAssociatorAtVertex
                                                    *
                                                    akCsSoftDropCh3PFJetBtagging
                                                    *
                                                    akCsSoftDropCh3PFNjettiness 
                                                    *
                                                    akCsSoftDropCh3PFpatJetsWithBtagging
                                                    *
                                                    akCsSoftDropCh3PFJetAnalyzer
                                                    )

akCsSoftDropCh3PFJetSequence_jec = cms.Sequence(akCsSoftDropCh3PFJetSequence_mc)
akCsSoftDropCh3PFJetSequence_mb = cms.Sequence(akCsSoftDropCh3PFJetSequence_mc)

akCsSoftDropCh3PFJetSequence = cms.Sequence(akCsSoftDropCh3PFJetSequence_mb)
akCsSoftDropCh3PFpatJetsWithBtagging.userData.userFloats.src += ['akCsSoftDropCh3PFJets:sym']
akCsSoftDropCh3PFpatJetsWithBtagging.userData.userInts.src += ['akCsSoftDropCh3PFJets:droppedBranches']
