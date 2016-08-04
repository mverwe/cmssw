

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPuSoftDropCh3PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPuSoftDropCh3PFJets"),
    matched = cms.InputTag("ak3GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.3
    )

akPuSoftDropCh3PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh3GenJets"),
    matched = cms.InputTag("ak3GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.3
    )

akPuSoftDropCh3PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh3PFJets")
                                                        )

akPuSoftDropCh3PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akPuSoftDropCh3PFJets"),
    payload = "AKPu3PF_offline"
    )

akPuSoftDropCh3PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akPuSoftDropCh3CaloJets'))

#akPuSoftDropCh3PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak3GenJets'))

akPuSoftDropCh3PFbTagger = bTaggers("akPuSoftDropCh3PF",0.3)

#create objects locally since they dont load properly otherwise
#akPuSoftDropCh3PFmatch = akPuSoftDropCh3PFbTagger.match
akPuSoftDropCh3PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh3PFJets"), matched = cms.InputTag("genParticles"))
akPuSoftDropCh3PFPatJetFlavourAssociationLegacy = akPuSoftDropCh3PFbTagger.PatJetFlavourAssociationLegacy
akPuSoftDropCh3PFPatJetPartons = akPuSoftDropCh3PFbTagger.PatJetPartons
akPuSoftDropCh3PFJetTracksAssociatorAtVertex = akPuSoftDropCh3PFbTagger.JetTracksAssociatorAtVertex
akPuSoftDropCh3PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPuSoftDropCh3PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh3PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh3PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh3PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh3PFCombinedSecondaryVertexBJetTags = akPuSoftDropCh3PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh3PFCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh3PFbTagger.CombinedSecondaryVertexV2BJetTags
akPuSoftDropCh3PFJetBProbabilityBJetTags = akPuSoftDropCh3PFbTagger.JetBProbabilityBJetTags
akPuSoftDropCh3PFSoftPFMuonByPtBJetTags = akPuSoftDropCh3PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh3PFSoftPFMuonByIP3dBJetTags = akPuSoftDropCh3PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh3PFTrackCountingHighEffBJetTags = akPuSoftDropCh3PFbTagger.TrackCountingHighEffBJetTags
akPuSoftDropCh3PFTrackCountingHighPurBJetTags = akPuSoftDropCh3PFbTagger.TrackCountingHighPurBJetTags
akPuSoftDropCh3PFPatJetPartonAssociationLegacy = akPuSoftDropCh3PFbTagger.PatJetPartonAssociationLegacy

akPuSoftDropCh3PFImpactParameterTagInfos = akPuSoftDropCh3PFbTagger.ImpactParameterTagInfos
akPuSoftDropCh3PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh3PFJetProbabilityBJetTags = akPuSoftDropCh3PFbTagger.JetProbabilityBJetTags

akPuSoftDropCh3PFSecondaryVertexTagInfos = akPuSoftDropCh3PFbTagger.SecondaryVertexTagInfos
akPuSoftDropCh3PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh3PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh3PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh3PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh3PFCombinedSecondaryVertexBJetTags = akPuSoftDropCh3PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh3PFCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh3PFbTagger.CombinedSecondaryVertexV2BJetTags

akPuSoftDropCh3PFSecondaryVertexNegativeTagInfos = akPuSoftDropCh3PFbTagger.SecondaryVertexNegativeTagInfos
akPuSoftDropCh3PFNegativeSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh3PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh3PFNegativeSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh3PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh3PFNegativeCombinedSecondaryVertexBJetTags = akPuSoftDropCh3PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akPuSoftDropCh3PFPositiveCombinedSecondaryVertexBJetTags = akPuSoftDropCh3PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akPuSoftDropCh3PFNegativeCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh3PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPuSoftDropCh3PFPositiveCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh3PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPuSoftDropCh3PFSoftPFMuonsTagInfos = akPuSoftDropCh3PFbTagger.SoftPFMuonsTagInfos
akPuSoftDropCh3PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh3PFSoftPFMuonBJetTags = akPuSoftDropCh3PFbTagger.SoftPFMuonBJetTags
akPuSoftDropCh3PFSoftPFMuonByIP3dBJetTags = akPuSoftDropCh3PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh3PFSoftPFMuonByPtBJetTags = akPuSoftDropCh3PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh3PFNegativeSoftPFMuonByPtBJetTags = akPuSoftDropCh3PFbTagger.NegativeSoftPFMuonByPtBJetTags
akPuSoftDropCh3PFPositiveSoftPFMuonByPtBJetTags = akPuSoftDropCh3PFbTagger.PositiveSoftPFMuonByPtBJetTags
akPuSoftDropCh3PFPatJetFlavourIdLegacy = cms.Sequence(akPuSoftDropCh3PFPatJetPartonAssociationLegacy*akPuSoftDropCh3PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akPuSoftDropCh3PFPatJetFlavourAssociation = akPuSoftDropCh3PFbTagger.PatJetFlavourAssociation
#akPuSoftDropCh3PFPatJetFlavourId = cms.Sequence(akPuSoftDropCh3PFPatJetPartons*akPuSoftDropCh3PFPatJetFlavourAssociation)

akPuSoftDropCh3PFJetBtaggingIP       = cms.Sequence(akPuSoftDropCh3PFImpactParameterTagInfos *
            (akPuSoftDropCh3PFTrackCountingHighEffBJetTags +
             akPuSoftDropCh3PFTrackCountingHighPurBJetTags +
             akPuSoftDropCh3PFJetProbabilityBJetTags +
             akPuSoftDropCh3PFJetBProbabilityBJetTags 
            )
            )

akPuSoftDropCh3PFJetBtaggingSV = cms.Sequence(akPuSoftDropCh3PFImpactParameterTagInfos
            *
            akPuSoftDropCh3PFSecondaryVertexTagInfos
            * (akPuSoftDropCh3PFSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh3PFSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh3PFCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh3PFCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh3PFJetBtaggingNegSV = cms.Sequence(akPuSoftDropCh3PFImpactParameterTagInfos
            *
            akPuSoftDropCh3PFSecondaryVertexNegativeTagInfos
            * (akPuSoftDropCh3PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh3PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh3PFNegativeCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh3PFPositiveCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh3PFNegativeCombinedSecondaryVertexV2BJetTags+
                akPuSoftDropCh3PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh3PFJetBtaggingMu = cms.Sequence(akPuSoftDropCh3PFSoftPFMuonsTagInfos * (akPuSoftDropCh3PFSoftPFMuonBJetTags
                +
                akPuSoftDropCh3PFSoftPFMuonByIP3dBJetTags
                +
                akPuSoftDropCh3PFSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh3PFNegativeSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh3PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akPuSoftDropCh3PFJetBtagging = cms.Sequence(akPuSoftDropCh3PFJetBtaggingIP
            *akPuSoftDropCh3PFJetBtaggingSV
            *akPuSoftDropCh3PFJetBtaggingNegSV
#            *akPuSoftDropCh3PFJetBtaggingMu
            )

akPuSoftDropCh3PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akPuSoftDropCh3PFJets"),
        genJetMatch          = cms.InputTag("akPuSoftDropCh3PFmatch"),
        genPartonMatch       = cms.InputTag("akPuSoftDropCh3PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPuSoftDropCh3PFcorr")),
        JetPartonMapSource   = cms.InputTag("akPuSoftDropCh3PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akPuSoftDropCh3PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPuSoftDropCh3PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akPuSoftDropCh3PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh3PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPuSoftDropCh3PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPuSoftDropCh3PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akPuSoftDropCh3PFJetBProbabilityBJetTags"),
            cms.InputTag("akPuSoftDropCh3PFJetProbabilityBJetTags"),
            #cms.InputTag("akPuSoftDropCh3PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akPuSoftDropCh3PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akPuSoftDropCh3PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh3PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPuSoftDropCh3PFJetID"),
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

akPuSoftDropCh3PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akPuSoftDropCh3PFJets"),
           	    R0  = cms.double( 0.3)
)
akPuSoftDropCh3PFpatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh3PFNjettiness:tau1','akPuSoftDropCh3PFNjettiness:tau2','akPuSoftDropCh3PFNjettiness:tau3']

akPuSoftDropCh3PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPuSoftDropCh3PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak3GenJets',#'ak3GenJets',
                                                             rParam = 0.3,
                                                             matchJets = cms.untracked.bool(False),
                                                             matchTag = 'patJetsWithBtagging',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("generalTracks"),
                                                             fillGenJets = True,
                                                             isMC = True,
							     doSubEvent = True,
                                                             useHepMC = cms.untracked.bool(False),
							     genParticles = cms.untracked.InputTag("genParticles"),
							     eventInfoTag = cms.InputTag("generator"),
                                                             doLifeTimeTagging = cms.untracked.bool(True),
                                                             doLifeTimeTaggingExtras = cms.untracked.bool(False),
                                                             bTagJetName = cms.untracked.string("akPuSoftDropCh3PF"),
                                                             jetName = cms.untracked.string("akPuSoftDropCh3PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(False),
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

akPuSoftDropCh3PFJetSequence_mc = cms.Sequence(
                                                  #akPuSoftDropCh3PFclean
                                                  #*
                                                  akPuSoftDropCh3PFmatch
                                                  #*
                                                  #akPuSoftDropCh3PFmatchGroomed
                                                  *
                                                  akPuSoftDropCh3PFparton
                                                  *
                                                  akPuSoftDropCh3PFcorr
                                                  *
                                                  #akPuSoftDropCh3PFJetID
                                                  #*
                                                  akPuSoftDropCh3PFPatJetFlavourIdLegacy
                                                  #*
			                          #akPuSoftDropCh3PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akPuSoftDropCh3PFJetTracksAssociatorAtVertex
                                                  *
                                                  akPuSoftDropCh3PFJetBtagging
                                                  *
                                                  akPuSoftDropCh3PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akPuSoftDropCh3PFpatJetsWithBtagging
                                                  *
                                                  akPuSoftDropCh3PFJetAnalyzer
                                                  )

akPuSoftDropCh3PFJetSequence_data = cms.Sequence(akPuSoftDropCh3PFcorr
                                                    *
                                                    #akPuSoftDropCh3PFJetID
                                                    #*
                                                    akPuSoftDropCh3PFJetTracksAssociatorAtVertex
                                                    *
                                                    akPuSoftDropCh3PFJetBtagging
                                                    *
                                                    akPuSoftDropCh3PFNjettiness 
                                                    *
                                                    akPuSoftDropCh3PFpatJetsWithBtagging
                                                    *
                                                    akPuSoftDropCh3PFJetAnalyzer
                                                    )

akPuSoftDropCh3PFJetSequence_jec = cms.Sequence(akPuSoftDropCh3PFJetSequence_mc)
akPuSoftDropCh3PFJetSequence_mb = cms.Sequence(akPuSoftDropCh3PFJetSequence_mc)

akPuSoftDropCh3PFJetSequence = cms.Sequence(akPuSoftDropCh3PFJetSequence_mc)
akPuSoftDropCh3PFpatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh3PFJets:sym']
akPuSoftDropCh3PFpatJetsWithBtagging.userData.userInts.src += ['akPuSoftDropCh3PFJets:droppedBranches']
