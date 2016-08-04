

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDropCh3PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh3PFJets"),
    matched = cms.InputTag("ak3HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.3
    )

akSoftDropCh3PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh3HiGenJets"),
    matched = cms.InputTag("ak3HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.3
    )

akSoftDropCh3PFparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh3PFJets")
                                                        )

akSoftDropCh3PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akSoftDropCh3PFJets"),
    payload = "AK3PF_offline"
    )

akSoftDropCh3PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akSoftDropCh3CaloJets'))

#akSoftDropCh3PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak3HiSignalGenJets'))

akSoftDropCh3PFbTagger = bTaggers("akSoftDropCh3PF",0.3)

#create objects locally since they dont load properly otherwise
#akSoftDropCh3PFmatch = akSoftDropCh3PFbTagger.match
akSoftDropCh3PFparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh3PFJets"), matched = cms.InputTag("hiSignalGenParticles"))
akSoftDropCh3PFPatJetFlavourAssociationLegacy = akSoftDropCh3PFbTagger.PatJetFlavourAssociationLegacy
akSoftDropCh3PFPatJetPartons = akSoftDropCh3PFbTagger.PatJetPartons
akSoftDropCh3PFJetTracksAssociatorAtVertex = akSoftDropCh3PFbTagger.JetTracksAssociatorAtVertex
akSoftDropCh3PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDropCh3PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh3PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh3PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh3PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh3PFCombinedSecondaryVertexBJetTags = akSoftDropCh3PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh3PFCombinedSecondaryVertexV2BJetTags = akSoftDropCh3PFbTagger.CombinedSecondaryVertexV2BJetTags
akSoftDropCh3PFJetBProbabilityBJetTags = akSoftDropCh3PFbTagger.JetBProbabilityBJetTags
akSoftDropCh3PFSoftPFMuonByPtBJetTags = akSoftDropCh3PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropCh3PFSoftPFMuonByIP3dBJetTags = akSoftDropCh3PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh3PFTrackCountingHighEffBJetTags = akSoftDropCh3PFbTagger.TrackCountingHighEffBJetTags
akSoftDropCh3PFTrackCountingHighPurBJetTags = akSoftDropCh3PFbTagger.TrackCountingHighPurBJetTags
akSoftDropCh3PFPatJetPartonAssociationLegacy = akSoftDropCh3PFbTagger.PatJetPartonAssociationLegacy

akSoftDropCh3PFImpactParameterTagInfos = akSoftDropCh3PFbTagger.ImpactParameterTagInfos
akSoftDropCh3PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh3PFJetProbabilityBJetTags = akSoftDropCh3PFbTagger.JetProbabilityBJetTags

akSoftDropCh3PFSecondaryVertexTagInfos = akSoftDropCh3PFbTagger.SecondaryVertexTagInfos
akSoftDropCh3PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh3PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh3PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh3PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh3PFCombinedSecondaryVertexBJetTags = akSoftDropCh3PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh3PFCombinedSecondaryVertexV2BJetTags = akSoftDropCh3PFbTagger.CombinedSecondaryVertexV2BJetTags

akSoftDropCh3PFSecondaryVertexNegativeTagInfos = akSoftDropCh3PFbTagger.SecondaryVertexNegativeTagInfos
akSoftDropCh3PFNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh3PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDropCh3PFNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh3PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDropCh3PFNegativeCombinedSecondaryVertexBJetTags = akSoftDropCh3PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDropCh3PFPositiveCombinedSecondaryVertexBJetTags = akSoftDropCh3PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDropCh3PFNegativeCombinedSecondaryVertexV2BJetTags = akSoftDropCh3PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDropCh3PFPositiveCombinedSecondaryVertexV2BJetTags = akSoftDropCh3PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDropCh3PFSoftPFMuonsTagInfos = akSoftDropCh3PFbTagger.SoftPFMuonsTagInfos
akSoftDropCh3PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh3PFSoftPFMuonBJetTags = akSoftDropCh3PFbTagger.SoftPFMuonBJetTags
akSoftDropCh3PFSoftPFMuonByIP3dBJetTags = akSoftDropCh3PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh3PFSoftPFMuonByPtBJetTags = akSoftDropCh3PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropCh3PFNegativeSoftPFMuonByPtBJetTags = akSoftDropCh3PFbTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDropCh3PFPositiveSoftPFMuonByPtBJetTags = akSoftDropCh3PFbTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDropCh3PFPatJetFlavourIdLegacy = cms.Sequence(akSoftDropCh3PFPatJetPartonAssociationLegacy*akSoftDropCh3PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akSoftDropCh3PFPatJetFlavourAssociation = akSoftDropCh3PFbTagger.PatJetFlavourAssociation
#akSoftDropCh3PFPatJetFlavourId = cms.Sequence(akSoftDropCh3PFPatJetPartons*akSoftDropCh3PFPatJetFlavourAssociation)

akSoftDropCh3PFJetBtaggingIP       = cms.Sequence(akSoftDropCh3PFImpactParameterTagInfos *
            (akSoftDropCh3PFTrackCountingHighEffBJetTags +
             akSoftDropCh3PFTrackCountingHighPurBJetTags +
             akSoftDropCh3PFJetProbabilityBJetTags +
             akSoftDropCh3PFJetBProbabilityBJetTags 
            )
            )

akSoftDropCh3PFJetBtaggingSV = cms.Sequence(akSoftDropCh3PFImpactParameterTagInfos
            *
            akSoftDropCh3PFSecondaryVertexTagInfos
            * (akSoftDropCh3PFSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh3PFSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh3PFCombinedSecondaryVertexBJetTags+
                akSoftDropCh3PFCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh3PFJetBtaggingNegSV = cms.Sequence(akSoftDropCh3PFImpactParameterTagInfos
            *
            akSoftDropCh3PFSecondaryVertexNegativeTagInfos
            * (akSoftDropCh3PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh3PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh3PFNegativeCombinedSecondaryVertexBJetTags+
                akSoftDropCh3PFPositiveCombinedSecondaryVertexBJetTags+
                akSoftDropCh3PFNegativeCombinedSecondaryVertexV2BJetTags+
                akSoftDropCh3PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh3PFJetBtaggingMu = cms.Sequence(akSoftDropCh3PFSoftPFMuonsTagInfos * (akSoftDropCh3PFSoftPFMuonBJetTags
                +
                akSoftDropCh3PFSoftPFMuonByIP3dBJetTags
                +
                akSoftDropCh3PFSoftPFMuonByPtBJetTags
                +
                akSoftDropCh3PFNegativeSoftPFMuonByPtBJetTags
                +
                akSoftDropCh3PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akSoftDropCh3PFJetBtagging = cms.Sequence(akSoftDropCh3PFJetBtaggingIP
            *akSoftDropCh3PFJetBtaggingSV
            *akSoftDropCh3PFJetBtaggingNegSV
#            *akSoftDropCh3PFJetBtaggingMu
            )

akSoftDropCh3PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akSoftDropCh3PFJets"),
        genJetMatch          = cms.InputTag("akSoftDropCh3PFmatch"),
        genPartonMatch       = cms.InputTag("akSoftDropCh3PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akSoftDropCh3PFcorr")),
        JetPartonMapSource   = cms.InputTag("akSoftDropCh3PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akSoftDropCh3PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akSoftDropCh3PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akSoftDropCh3PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akSoftDropCh3PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akSoftDropCh3PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akSoftDropCh3PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akSoftDropCh3PFJetBProbabilityBJetTags"),
            cms.InputTag("akSoftDropCh3PFJetProbabilityBJetTags"),
            #cms.InputTag("akSoftDropCh3PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akSoftDropCh3PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akSoftDropCh3PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akSoftDropCh3PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akSoftDropCh3PFJetID"),
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

akSoftDropCh3PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akSoftDropCh3PFJets"),
           	    R0  = cms.double( 0.3)
)
akSoftDropCh3PFpatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh3PFNjettiness:tau1','akSoftDropCh3PFNjettiness:tau2','akSoftDropCh3PFNjettiness:tau3']

akSoftDropCh3PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akSoftDropCh3PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak3HiSignalGenJets',#'ak3HiGenJets',
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
                                                             bTagJetName = cms.untracked.string("akSoftDropCh3PF"),
                                                             jetName = cms.untracked.string("akSoftDropCh3PF"),
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

akSoftDropCh3PFJetSequence_mc = cms.Sequence(
                                                  #akSoftDropCh3PFclean
                                                  #*
                                                  akSoftDropCh3PFmatch
                                                  #*
                                                  #akSoftDropCh3PFmatchGroomed
                                                  *
                                                  akSoftDropCh3PFparton
                                                  *
                                                  akSoftDropCh3PFcorr
                                                  *
                                                  #akSoftDropCh3PFJetID
                                                  #*
                                                  akSoftDropCh3PFPatJetFlavourIdLegacy
                                                  #*
			                          #akSoftDropCh3PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akSoftDropCh3PFJetTracksAssociatorAtVertex
                                                  *
                                                  akSoftDropCh3PFJetBtagging
                                                  *
                                                  akSoftDropCh3PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akSoftDropCh3PFpatJetsWithBtagging
                                                  *
                                                  akSoftDropCh3PFJetAnalyzer
                                                  )

akSoftDropCh3PFJetSequence_data = cms.Sequence(akSoftDropCh3PFcorr
                                                    *
                                                    #akSoftDropCh3PFJetID
                                                    #*
                                                    akSoftDropCh3PFJetTracksAssociatorAtVertex
                                                    *
                                                    akSoftDropCh3PFJetBtagging
                                                    *
                                                    akSoftDropCh3PFNjettiness 
                                                    *
                                                    akSoftDropCh3PFpatJetsWithBtagging
                                                    *
                                                    akSoftDropCh3PFJetAnalyzer
                                                    )

akSoftDropCh3PFJetSequence_jec = cms.Sequence(akSoftDropCh3PFJetSequence_mc)
akSoftDropCh3PFJetSequence_mb = cms.Sequence(akSoftDropCh3PFJetSequence_mc)

akSoftDropCh3PFJetSequence = cms.Sequence(akSoftDropCh3PFJetSequence_mc)
akSoftDropCh3PFpatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh3PFJets:sym']
akSoftDropCh3PFpatJetsWithBtagging.userData.userInts.src += ['akSoftDropCh3PFJets:droppedBranches']
