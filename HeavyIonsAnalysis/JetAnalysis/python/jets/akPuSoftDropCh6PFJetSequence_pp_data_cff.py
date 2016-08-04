

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPuSoftDropCh6PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPuSoftDropCh6PFJets"),
    matched = cms.InputTag("ak6GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.6
    )

akPuSoftDropCh6PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh6GenJets"),
    matched = cms.InputTag("ak6GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.6
    )

akPuSoftDropCh6PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh6PFJets")
                                                        )

akPuSoftDropCh6PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akPuSoftDropCh6PFJets"),
    payload = "AKPu6PF_offline"
    )

akPuSoftDropCh6PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akPuSoftDropCh6CaloJets'))

#akPuSoftDropCh6PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak6GenJets'))

akPuSoftDropCh6PFbTagger = bTaggers("akPuSoftDropCh6PF",0.6)

#create objects locally since they dont load properly otherwise
#akPuSoftDropCh6PFmatch = akPuSoftDropCh6PFbTagger.match
akPuSoftDropCh6PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh6PFJets"), matched = cms.InputTag("genParticles"))
akPuSoftDropCh6PFPatJetFlavourAssociationLegacy = akPuSoftDropCh6PFbTagger.PatJetFlavourAssociationLegacy
akPuSoftDropCh6PFPatJetPartons = akPuSoftDropCh6PFbTagger.PatJetPartons
akPuSoftDropCh6PFJetTracksAssociatorAtVertex = akPuSoftDropCh6PFbTagger.JetTracksAssociatorAtVertex
akPuSoftDropCh6PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPuSoftDropCh6PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh6PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh6PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh6PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh6PFCombinedSecondaryVertexBJetTags = akPuSoftDropCh6PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh6PFCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh6PFbTagger.CombinedSecondaryVertexV2BJetTags
akPuSoftDropCh6PFJetBProbabilityBJetTags = akPuSoftDropCh6PFbTagger.JetBProbabilityBJetTags
akPuSoftDropCh6PFSoftPFMuonByPtBJetTags = akPuSoftDropCh6PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh6PFSoftPFMuonByIP3dBJetTags = akPuSoftDropCh6PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh6PFTrackCountingHighEffBJetTags = akPuSoftDropCh6PFbTagger.TrackCountingHighEffBJetTags
akPuSoftDropCh6PFTrackCountingHighPurBJetTags = akPuSoftDropCh6PFbTagger.TrackCountingHighPurBJetTags
akPuSoftDropCh6PFPatJetPartonAssociationLegacy = akPuSoftDropCh6PFbTagger.PatJetPartonAssociationLegacy

akPuSoftDropCh6PFImpactParameterTagInfos = akPuSoftDropCh6PFbTagger.ImpactParameterTagInfos
akPuSoftDropCh6PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh6PFJetProbabilityBJetTags = akPuSoftDropCh6PFbTagger.JetProbabilityBJetTags

akPuSoftDropCh6PFSecondaryVertexTagInfos = akPuSoftDropCh6PFbTagger.SecondaryVertexTagInfos
akPuSoftDropCh6PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh6PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh6PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh6PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh6PFCombinedSecondaryVertexBJetTags = akPuSoftDropCh6PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh6PFCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh6PFbTagger.CombinedSecondaryVertexV2BJetTags

akPuSoftDropCh6PFSecondaryVertexNegativeTagInfos = akPuSoftDropCh6PFbTagger.SecondaryVertexNegativeTagInfos
akPuSoftDropCh6PFNegativeSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh6PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh6PFNegativeSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh6PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh6PFNegativeCombinedSecondaryVertexBJetTags = akPuSoftDropCh6PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akPuSoftDropCh6PFPositiveCombinedSecondaryVertexBJetTags = akPuSoftDropCh6PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akPuSoftDropCh6PFNegativeCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh6PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPuSoftDropCh6PFPositiveCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh6PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPuSoftDropCh6PFSoftPFMuonsTagInfos = akPuSoftDropCh6PFbTagger.SoftPFMuonsTagInfos
akPuSoftDropCh6PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh6PFSoftPFMuonBJetTags = akPuSoftDropCh6PFbTagger.SoftPFMuonBJetTags
akPuSoftDropCh6PFSoftPFMuonByIP3dBJetTags = akPuSoftDropCh6PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh6PFSoftPFMuonByPtBJetTags = akPuSoftDropCh6PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh6PFNegativeSoftPFMuonByPtBJetTags = akPuSoftDropCh6PFbTagger.NegativeSoftPFMuonByPtBJetTags
akPuSoftDropCh6PFPositiveSoftPFMuonByPtBJetTags = akPuSoftDropCh6PFbTagger.PositiveSoftPFMuonByPtBJetTags
akPuSoftDropCh6PFPatJetFlavourIdLegacy = cms.Sequence(akPuSoftDropCh6PFPatJetPartonAssociationLegacy*akPuSoftDropCh6PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akPuSoftDropCh6PFPatJetFlavourAssociation = akPuSoftDropCh6PFbTagger.PatJetFlavourAssociation
#akPuSoftDropCh6PFPatJetFlavourId = cms.Sequence(akPuSoftDropCh6PFPatJetPartons*akPuSoftDropCh6PFPatJetFlavourAssociation)

akPuSoftDropCh6PFJetBtaggingIP       = cms.Sequence(akPuSoftDropCh6PFImpactParameterTagInfos *
            (akPuSoftDropCh6PFTrackCountingHighEffBJetTags +
             akPuSoftDropCh6PFTrackCountingHighPurBJetTags +
             akPuSoftDropCh6PFJetProbabilityBJetTags +
             akPuSoftDropCh6PFJetBProbabilityBJetTags 
            )
            )

akPuSoftDropCh6PFJetBtaggingSV = cms.Sequence(akPuSoftDropCh6PFImpactParameterTagInfos
            *
            akPuSoftDropCh6PFSecondaryVertexTagInfos
            * (akPuSoftDropCh6PFSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh6PFSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh6PFCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh6PFCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh6PFJetBtaggingNegSV = cms.Sequence(akPuSoftDropCh6PFImpactParameterTagInfos
            *
            akPuSoftDropCh6PFSecondaryVertexNegativeTagInfos
            * (akPuSoftDropCh6PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh6PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh6PFNegativeCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh6PFPositiveCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh6PFNegativeCombinedSecondaryVertexV2BJetTags+
                akPuSoftDropCh6PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh6PFJetBtaggingMu = cms.Sequence(akPuSoftDropCh6PFSoftPFMuonsTagInfos * (akPuSoftDropCh6PFSoftPFMuonBJetTags
                +
                akPuSoftDropCh6PFSoftPFMuonByIP3dBJetTags
                +
                akPuSoftDropCh6PFSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh6PFNegativeSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh6PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akPuSoftDropCh6PFJetBtagging = cms.Sequence(akPuSoftDropCh6PFJetBtaggingIP
            *akPuSoftDropCh6PFJetBtaggingSV
            *akPuSoftDropCh6PFJetBtaggingNegSV
#            *akPuSoftDropCh6PFJetBtaggingMu
            )

akPuSoftDropCh6PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akPuSoftDropCh6PFJets"),
        genJetMatch          = cms.InputTag("akPuSoftDropCh6PFmatch"),
        genPartonMatch       = cms.InputTag("akPuSoftDropCh6PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPuSoftDropCh6PFcorr")),
        JetPartonMapSource   = cms.InputTag("akPuSoftDropCh6PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akPuSoftDropCh6PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPuSoftDropCh6PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akPuSoftDropCh6PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh6PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPuSoftDropCh6PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPuSoftDropCh6PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akPuSoftDropCh6PFJetBProbabilityBJetTags"),
            cms.InputTag("akPuSoftDropCh6PFJetProbabilityBJetTags"),
            #cms.InputTag("akPuSoftDropCh6PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akPuSoftDropCh6PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akPuSoftDropCh6PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh6PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPuSoftDropCh6PFJetID"),
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

akPuSoftDropCh6PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akPuSoftDropCh6PFJets"),
           	    R0  = cms.double( 0.6)
)
akPuSoftDropCh6PFpatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh6PFNjettiness:tau1','akPuSoftDropCh6PFNjettiness:tau2','akPuSoftDropCh6PFNjettiness:tau3']

akPuSoftDropCh6PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPuSoftDropCh6PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak6GenJets',#'ak6GenJets',
                                                             rParam = 0.6,
                                                             matchJets = cms.untracked.bool(False),
                                                             matchTag = 'patJetsWithBtagging',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("generalTracks"),
                                                             fillGenJets = False,
                                                             isMC = False,
							     doSubEvent = False,
                                                             useHepMC = cms.untracked.bool(False),
							     genParticles = cms.untracked.InputTag("genParticles"),
							     eventInfoTag = cms.InputTag("generator"),
                                                             doLifeTimeTagging = cms.untracked.bool(True),
                                                             doLifeTimeTaggingExtras = cms.untracked.bool(False),
                                                             bTagJetName = cms.untracked.string("akPuSoftDropCh6PF"),
                                                             jetName = cms.untracked.string("akPuSoftDropCh6PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(False),
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

akPuSoftDropCh6PFJetSequence_mc = cms.Sequence(
                                                  #akPuSoftDropCh6PFclean
                                                  #*
                                                  akPuSoftDropCh6PFmatch
                                                  #*
                                                  #akPuSoftDropCh6PFmatchGroomed
                                                  *
                                                  akPuSoftDropCh6PFparton
                                                  *
                                                  akPuSoftDropCh6PFcorr
                                                  *
                                                  #akPuSoftDropCh6PFJetID
                                                  #*
                                                  akPuSoftDropCh6PFPatJetFlavourIdLegacy
                                                  #*
			                          #akPuSoftDropCh6PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akPuSoftDropCh6PFJetTracksAssociatorAtVertex
                                                  *
                                                  akPuSoftDropCh6PFJetBtagging
                                                  *
                                                  akPuSoftDropCh6PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akPuSoftDropCh6PFpatJetsWithBtagging
                                                  *
                                                  akPuSoftDropCh6PFJetAnalyzer
                                                  )

akPuSoftDropCh6PFJetSequence_data = cms.Sequence(akPuSoftDropCh6PFcorr
                                                    *
                                                    #akPuSoftDropCh6PFJetID
                                                    #*
                                                    akPuSoftDropCh6PFJetTracksAssociatorAtVertex
                                                    *
                                                    akPuSoftDropCh6PFJetBtagging
                                                    *
                                                    akPuSoftDropCh6PFNjettiness 
                                                    *
                                                    akPuSoftDropCh6PFpatJetsWithBtagging
                                                    *
                                                    akPuSoftDropCh6PFJetAnalyzer
                                                    )

akPuSoftDropCh6PFJetSequence_jec = cms.Sequence(akPuSoftDropCh6PFJetSequence_mc)
akPuSoftDropCh6PFJetSequence_mb = cms.Sequence(akPuSoftDropCh6PFJetSequence_mc)

akPuSoftDropCh6PFJetSequence = cms.Sequence(akPuSoftDropCh6PFJetSequence_data)
akPuSoftDropCh6PFpatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh6PFJets:sym']
akPuSoftDropCh6PFpatJetsWithBtagging.userData.userInts.src += ['akPuSoftDropCh6PFJets:droppedBranches']
