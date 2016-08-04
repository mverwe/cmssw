

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPuSoftDropCh5PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPuSoftDropCh5PFJets"),
    matched = cms.InputTag("ak5GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.5
    )

akPuSoftDropCh5PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh5GenJets"),
    matched = cms.InputTag("ak5GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.5
    )

akPuSoftDropCh5PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh5PFJets")
                                                        )

akPuSoftDropCh5PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akPuSoftDropCh5PFJets"),
    payload = "AKPu5PF_offline"
    )

akPuSoftDropCh5PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akPuSoftDropCh5CaloJets'))

#akPuSoftDropCh5PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak5GenJets'))

akPuSoftDropCh5PFbTagger = bTaggers("akPuSoftDropCh5PF",0.5)

#create objects locally since they dont load properly otherwise
#akPuSoftDropCh5PFmatch = akPuSoftDropCh5PFbTagger.match
akPuSoftDropCh5PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh5PFJets"), matched = cms.InputTag("genParticles"))
akPuSoftDropCh5PFPatJetFlavourAssociationLegacy = akPuSoftDropCh5PFbTagger.PatJetFlavourAssociationLegacy
akPuSoftDropCh5PFPatJetPartons = akPuSoftDropCh5PFbTagger.PatJetPartons
akPuSoftDropCh5PFJetTracksAssociatorAtVertex = akPuSoftDropCh5PFbTagger.JetTracksAssociatorAtVertex
akPuSoftDropCh5PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPuSoftDropCh5PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh5PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh5PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh5PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh5PFCombinedSecondaryVertexBJetTags = akPuSoftDropCh5PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh5PFCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh5PFbTagger.CombinedSecondaryVertexV2BJetTags
akPuSoftDropCh5PFJetBProbabilityBJetTags = akPuSoftDropCh5PFbTagger.JetBProbabilityBJetTags
akPuSoftDropCh5PFSoftPFMuonByPtBJetTags = akPuSoftDropCh5PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh5PFSoftPFMuonByIP3dBJetTags = akPuSoftDropCh5PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh5PFTrackCountingHighEffBJetTags = akPuSoftDropCh5PFbTagger.TrackCountingHighEffBJetTags
akPuSoftDropCh5PFTrackCountingHighPurBJetTags = akPuSoftDropCh5PFbTagger.TrackCountingHighPurBJetTags
akPuSoftDropCh5PFPatJetPartonAssociationLegacy = akPuSoftDropCh5PFbTagger.PatJetPartonAssociationLegacy

akPuSoftDropCh5PFImpactParameterTagInfos = akPuSoftDropCh5PFbTagger.ImpactParameterTagInfos
akPuSoftDropCh5PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh5PFJetProbabilityBJetTags = akPuSoftDropCh5PFbTagger.JetProbabilityBJetTags

akPuSoftDropCh5PFSecondaryVertexTagInfos = akPuSoftDropCh5PFbTagger.SecondaryVertexTagInfos
akPuSoftDropCh5PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh5PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh5PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh5PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh5PFCombinedSecondaryVertexBJetTags = akPuSoftDropCh5PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh5PFCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh5PFbTagger.CombinedSecondaryVertexV2BJetTags

akPuSoftDropCh5PFSecondaryVertexNegativeTagInfos = akPuSoftDropCh5PFbTagger.SecondaryVertexNegativeTagInfos
akPuSoftDropCh5PFNegativeSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh5PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh5PFNegativeSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh5PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh5PFNegativeCombinedSecondaryVertexBJetTags = akPuSoftDropCh5PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akPuSoftDropCh5PFPositiveCombinedSecondaryVertexBJetTags = akPuSoftDropCh5PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akPuSoftDropCh5PFNegativeCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh5PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPuSoftDropCh5PFPositiveCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh5PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPuSoftDropCh5PFSoftPFMuonsTagInfos = akPuSoftDropCh5PFbTagger.SoftPFMuonsTagInfos
akPuSoftDropCh5PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh5PFSoftPFMuonBJetTags = akPuSoftDropCh5PFbTagger.SoftPFMuonBJetTags
akPuSoftDropCh5PFSoftPFMuonByIP3dBJetTags = akPuSoftDropCh5PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh5PFSoftPFMuonByPtBJetTags = akPuSoftDropCh5PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh5PFNegativeSoftPFMuonByPtBJetTags = akPuSoftDropCh5PFbTagger.NegativeSoftPFMuonByPtBJetTags
akPuSoftDropCh5PFPositiveSoftPFMuonByPtBJetTags = akPuSoftDropCh5PFbTagger.PositiveSoftPFMuonByPtBJetTags
akPuSoftDropCh5PFPatJetFlavourIdLegacy = cms.Sequence(akPuSoftDropCh5PFPatJetPartonAssociationLegacy*akPuSoftDropCh5PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akPuSoftDropCh5PFPatJetFlavourAssociation = akPuSoftDropCh5PFbTagger.PatJetFlavourAssociation
#akPuSoftDropCh5PFPatJetFlavourId = cms.Sequence(akPuSoftDropCh5PFPatJetPartons*akPuSoftDropCh5PFPatJetFlavourAssociation)

akPuSoftDropCh5PFJetBtaggingIP       = cms.Sequence(akPuSoftDropCh5PFImpactParameterTagInfos *
            (akPuSoftDropCh5PFTrackCountingHighEffBJetTags +
             akPuSoftDropCh5PFTrackCountingHighPurBJetTags +
             akPuSoftDropCh5PFJetProbabilityBJetTags +
             akPuSoftDropCh5PFJetBProbabilityBJetTags 
            )
            )

akPuSoftDropCh5PFJetBtaggingSV = cms.Sequence(akPuSoftDropCh5PFImpactParameterTagInfos
            *
            akPuSoftDropCh5PFSecondaryVertexTagInfos
            * (akPuSoftDropCh5PFSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh5PFSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh5PFCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh5PFCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh5PFJetBtaggingNegSV = cms.Sequence(akPuSoftDropCh5PFImpactParameterTagInfos
            *
            akPuSoftDropCh5PFSecondaryVertexNegativeTagInfos
            * (akPuSoftDropCh5PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh5PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh5PFNegativeCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh5PFPositiveCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh5PFNegativeCombinedSecondaryVertexV2BJetTags+
                akPuSoftDropCh5PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh5PFJetBtaggingMu = cms.Sequence(akPuSoftDropCh5PFSoftPFMuonsTagInfos * (akPuSoftDropCh5PFSoftPFMuonBJetTags
                +
                akPuSoftDropCh5PFSoftPFMuonByIP3dBJetTags
                +
                akPuSoftDropCh5PFSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh5PFNegativeSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh5PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akPuSoftDropCh5PFJetBtagging = cms.Sequence(akPuSoftDropCh5PFJetBtaggingIP
            *akPuSoftDropCh5PFJetBtaggingSV
            *akPuSoftDropCh5PFJetBtaggingNegSV
#            *akPuSoftDropCh5PFJetBtaggingMu
            )

akPuSoftDropCh5PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akPuSoftDropCh5PFJets"),
        genJetMatch          = cms.InputTag("akPuSoftDropCh5PFmatch"),
        genPartonMatch       = cms.InputTag("akPuSoftDropCh5PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPuSoftDropCh5PFcorr")),
        JetPartonMapSource   = cms.InputTag("akPuSoftDropCh5PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akPuSoftDropCh5PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPuSoftDropCh5PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akPuSoftDropCh5PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh5PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPuSoftDropCh5PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPuSoftDropCh5PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akPuSoftDropCh5PFJetBProbabilityBJetTags"),
            cms.InputTag("akPuSoftDropCh5PFJetProbabilityBJetTags"),
            #cms.InputTag("akPuSoftDropCh5PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akPuSoftDropCh5PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akPuSoftDropCh5PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh5PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPuSoftDropCh5PFJetID"),
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

akPuSoftDropCh5PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akPuSoftDropCh5PFJets"),
           	    R0  = cms.double( 0.5)
)
akPuSoftDropCh5PFpatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh5PFNjettiness:tau1','akPuSoftDropCh5PFNjettiness:tau2','akPuSoftDropCh5PFNjettiness:tau3']

akPuSoftDropCh5PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPuSoftDropCh5PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak5GenJets',#'ak5GenJets',
                                                             rParam = 0.5,
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
                                                             bTagJetName = cms.untracked.string("akPuSoftDropCh5PF"),
                                                             jetName = cms.untracked.string("akPuSoftDropCh5PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(False),
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

akPuSoftDropCh5PFJetSequence_mc = cms.Sequence(
                                                  #akPuSoftDropCh5PFclean
                                                  #*
                                                  akPuSoftDropCh5PFmatch
                                                  #*
                                                  #akPuSoftDropCh5PFmatchGroomed
                                                  *
                                                  akPuSoftDropCh5PFparton
                                                  *
                                                  akPuSoftDropCh5PFcorr
                                                  *
                                                  #akPuSoftDropCh5PFJetID
                                                  #*
                                                  akPuSoftDropCh5PFPatJetFlavourIdLegacy
                                                  #*
			                          #akPuSoftDropCh5PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akPuSoftDropCh5PFJetTracksAssociatorAtVertex
                                                  *
                                                  akPuSoftDropCh5PFJetBtagging
                                                  *
                                                  akPuSoftDropCh5PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akPuSoftDropCh5PFpatJetsWithBtagging
                                                  *
                                                  akPuSoftDropCh5PFJetAnalyzer
                                                  )

akPuSoftDropCh5PFJetSequence_data = cms.Sequence(akPuSoftDropCh5PFcorr
                                                    *
                                                    #akPuSoftDropCh5PFJetID
                                                    #*
                                                    akPuSoftDropCh5PFJetTracksAssociatorAtVertex
                                                    *
                                                    akPuSoftDropCh5PFJetBtagging
                                                    *
                                                    akPuSoftDropCh5PFNjettiness 
                                                    *
                                                    akPuSoftDropCh5PFpatJetsWithBtagging
                                                    *
                                                    akPuSoftDropCh5PFJetAnalyzer
                                                    )

akPuSoftDropCh5PFJetSequence_jec = cms.Sequence(akPuSoftDropCh5PFJetSequence_mc)
akPuSoftDropCh5PFJetSequence_mb = cms.Sequence(akPuSoftDropCh5PFJetSequence_mc)

akPuSoftDropCh5PFJetSequence = cms.Sequence(akPuSoftDropCh5PFJetSequence_jec)
akPuSoftDropCh5PFJetAnalyzer.genPtMin = cms.untracked.double(1)
akPuSoftDropCh5PFJetAnalyzer.jetPtMin = cms.double(1)
akPuSoftDropCh5PFpatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh5PFJets:sym']
akPuSoftDropCh5PFpatJetsWithBtagging.userData.userInts.src += ['akPuSoftDropCh5PFJets:droppedBranches']
