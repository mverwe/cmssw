

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPuSoftDropCh2PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPuSoftDropCh2PFJets"),
    matched = cms.InputTag("ak2HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.2
    )

akPuSoftDropCh2PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh2HiGenJets"),
    matched = cms.InputTag("ak2HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.2
    )

akPuSoftDropCh2PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh2PFJets")
                                                        )

akPuSoftDropCh2PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akPuSoftDropCh2PFJets"),
    payload = "AKPu2PF_offline"
    )

akPuSoftDropCh2PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akPuSoftDropCh2CaloJets'))

#akPuSoftDropCh2PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak2HiSignalGenJets'))

akPuSoftDropCh2PFbTagger = bTaggers("akPuSoftDropCh2PF",0.2)

#create objects locally since they dont load properly otherwise
#akPuSoftDropCh2PFmatch = akPuSoftDropCh2PFbTagger.match
akPuSoftDropCh2PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh2PFJets"), matched = cms.InputTag("hiSignalGenParticles"))
akPuSoftDropCh2PFPatJetFlavourAssociationLegacy = akPuSoftDropCh2PFbTagger.PatJetFlavourAssociationLegacy
akPuSoftDropCh2PFPatJetPartons = akPuSoftDropCh2PFbTagger.PatJetPartons
akPuSoftDropCh2PFJetTracksAssociatorAtVertex = akPuSoftDropCh2PFbTagger.JetTracksAssociatorAtVertex
akPuSoftDropCh2PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPuSoftDropCh2PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh2PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh2PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh2PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh2PFCombinedSecondaryVertexBJetTags = akPuSoftDropCh2PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh2PFCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh2PFbTagger.CombinedSecondaryVertexV2BJetTags
akPuSoftDropCh2PFJetBProbabilityBJetTags = akPuSoftDropCh2PFbTagger.JetBProbabilityBJetTags
akPuSoftDropCh2PFSoftPFMuonByPtBJetTags = akPuSoftDropCh2PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh2PFSoftPFMuonByIP3dBJetTags = akPuSoftDropCh2PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh2PFTrackCountingHighEffBJetTags = akPuSoftDropCh2PFbTagger.TrackCountingHighEffBJetTags
akPuSoftDropCh2PFTrackCountingHighPurBJetTags = akPuSoftDropCh2PFbTagger.TrackCountingHighPurBJetTags
akPuSoftDropCh2PFPatJetPartonAssociationLegacy = akPuSoftDropCh2PFbTagger.PatJetPartonAssociationLegacy

akPuSoftDropCh2PFImpactParameterTagInfos = akPuSoftDropCh2PFbTagger.ImpactParameterTagInfos
akPuSoftDropCh2PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh2PFJetProbabilityBJetTags = akPuSoftDropCh2PFbTagger.JetProbabilityBJetTags

akPuSoftDropCh2PFSecondaryVertexTagInfos = akPuSoftDropCh2PFbTagger.SecondaryVertexTagInfos
akPuSoftDropCh2PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh2PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh2PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh2PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh2PFCombinedSecondaryVertexBJetTags = akPuSoftDropCh2PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh2PFCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh2PFbTagger.CombinedSecondaryVertexV2BJetTags

akPuSoftDropCh2PFSecondaryVertexNegativeTagInfos = akPuSoftDropCh2PFbTagger.SecondaryVertexNegativeTagInfos
akPuSoftDropCh2PFNegativeSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh2PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh2PFNegativeSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh2PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh2PFNegativeCombinedSecondaryVertexBJetTags = akPuSoftDropCh2PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akPuSoftDropCh2PFPositiveCombinedSecondaryVertexBJetTags = akPuSoftDropCh2PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akPuSoftDropCh2PFNegativeCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh2PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPuSoftDropCh2PFPositiveCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh2PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPuSoftDropCh2PFSoftPFMuonsTagInfos = akPuSoftDropCh2PFbTagger.SoftPFMuonsTagInfos
akPuSoftDropCh2PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh2PFSoftPFMuonBJetTags = akPuSoftDropCh2PFbTagger.SoftPFMuonBJetTags
akPuSoftDropCh2PFSoftPFMuonByIP3dBJetTags = akPuSoftDropCh2PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh2PFSoftPFMuonByPtBJetTags = akPuSoftDropCh2PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh2PFNegativeSoftPFMuonByPtBJetTags = akPuSoftDropCh2PFbTagger.NegativeSoftPFMuonByPtBJetTags
akPuSoftDropCh2PFPositiveSoftPFMuonByPtBJetTags = akPuSoftDropCh2PFbTagger.PositiveSoftPFMuonByPtBJetTags
akPuSoftDropCh2PFPatJetFlavourIdLegacy = cms.Sequence(akPuSoftDropCh2PFPatJetPartonAssociationLegacy*akPuSoftDropCh2PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akPuSoftDropCh2PFPatJetFlavourAssociation = akPuSoftDropCh2PFbTagger.PatJetFlavourAssociation
#akPuSoftDropCh2PFPatJetFlavourId = cms.Sequence(akPuSoftDropCh2PFPatJetPartons*akPuSoftDropCh2PFPatJetFlavourAssociation)

akPuSoftDropCh2PFJetBtaggingIP       = cms.Sequence(akPuSoftDropCh2PFImpactParameterTagInfos *
            (akPuSoftDropCh2PFTrackCountingHighEffBJetTags +
             akPuSoftDropCh2PFTrackCountingHighPurBJetTags +
             akPuSoftDropCh2PFJetProbabilityBJetTags +
             akPuSoftDropCh2PFJetBProbabilityBJetTags 
            )
            )

akPuSoftDropCh2PFJetBtaggingSV = cms.Sequence(akPuSoftDropCh2PFImpactParameterTagInfos
            *
            akPuSoftDropCh2PFSecondaryVertexTagInfos
            * (akPuSoftDropCh2PFSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh2PFSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh2PFCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh2PFCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh2PFJetBtaggingNegSV = cms.Sequence(akPuSoftDropCh2PFImpactParameterTagInfos
            *
            akPuSoftDropCh2PFSecondaryVertexNegativeTagInfos
            * (akPuSoftDropCh2PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh2PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh2PFNegativeCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh2PFPositiveCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh2PFNegativeCombinedSecondaryVertexV2BJetTags+
                akPuSoftDropCh2PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh2PFJetBtaggingMu = cms.Sequence(akPuSoftDropCh2PFSoftPFMuonsTagInfos * (akPuSoftDropCh2PFSoftPFMuonBJetTags
                +
                akPuSoftDropCh2PFSoftPFMuonByIP3dBJetTags
                +
                akPuSoftDropCh2PFSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh2PFNegativeSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh2PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akPuSoftDropCh2PFJetBtagging = cms.Sequence(akPuSoftDropCh2PFJetBtaggingIP
            *akPuSoftDropCh2PFJetBtaggingSV
            *akPuSoftDropCh2PFJetBtaggingNegSV
#            *akPuSoftDropCh2PFJetBtaggingMu
            )

akPuSoftDropCh2PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akPuSoftDropCh2PFJets"),
        genJetMatch          = cms.InputTag("akPuSoftDropCh2PFmatch"),
        genPartonMatch       = cms.InputTag("akPuSoftDropCh2PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPuSoftDropCh2PFcorr")),
        JetPartonMapSource   = cms.InputTag("akPuSoftDropCh2PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akPuSoftDropCh2PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPuSoftDropCh2PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akPuSoftDropCh2PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh2PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPuSoftDropCh2PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPuSoftDropCh2PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akPuSoftDropCh2PFJetBProbabilityBJetTags"),
            cms.InputTag("akPuSoftDropCh2PFJetProbabilityBJetTags"),
            #cms.InputTag("akPuSoftDropCh2PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akPuSoftDropCh2PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akPuSoftDropCh2PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh2PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPuSoftDropCh2PFJetID"),
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

akPuSoftDropCh2PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akPuSoftDropCh2PFJets"),
           	    R0  = cms.double( 0.2)
)
akPuSoftDropCh2PFpatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh2PFNjettiness:tau1','akPuSoftDropCh2PFNjettiness:tau2','akPuSoftDropCh2PFNjettiness:tau3']

akPuSoftDropCh2PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPuSoftDropCh2PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak2HiSignalGenJets',#'ak2HiGenJets',
                                                             rParam = 0.2,
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
                                                             bTagJetName = cms.untracked.string("akPuSoftDropCh2PF"),
                                                             jetName = cms.untracked.string("akPuSoftDropCh2PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropCh2GenJets"),
                                                             doGenTaus = False,
                                                             genTau1 = cms.InputTag("akSoftDropCh2GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropCh2GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropCh2GenNjettiness","tau3"),
                                                             doGenSym = True,
                                                             genSym = cms.InputTag("akSoftDropCh2GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropCh2GenJets","droppedBranches")
                                                             )

akPuSoftDropCh2PFJetSequence_mc = cms.Sequence(
                                                  #akPuSoftDropCh2PFclean
                                                  #*
                                                  akPuSoftDropCh2PFmatch
                                                  #*
                                                  #akPuSoftDropCh2PFmatchGroomed
                                                  *
                                                  akPuSoftDropCh2PFparton
                                                  *
                                                  akPuSoftDropCh2PFcorr
                                                  *
                                                  #akPuSoftDropCh2PFJetID
                                                  #*
                                                  akPuSoftDropCh2PFPatJetFlavourIdLegacy
                                                  #*
			                          #akPuSoftDropCh2PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akPuSoftDropCh2PFJetTracksAssociatorAtVertex
                                                  *
                                                  akPuSoftDropCh2PFJetBtagging
                                                  *
                                                  akPuSoftDropCh2PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akPuSoftDropCh2PFpatJetsWithBtagging
                                                  *
                                                  akPuSoftDropCh2PFJetAnalyzer
                                                  )

akPuSoftDropCh2PFJetSequence_data = cms.Sequence(akPuSoftDropCh2PFcorr
                                                    *
                                                    #akPuSoftDropCh2PFJetID
                                                    #*
                                                    akPuSoftDropCh2PFJetTracksAssociatorAtVertex
                                                    *
                                                    akPuSoftDropCh2PFJetBtagging
                                                    *
                                                    akPuSoftDropCh2PFNjettiness 
                                                    *
                                                    akPuSoftDropCh2PFpatJetsWithBtagging
                                                    *
                                                    akPuSoftDropCh2PFJetAnalyzer
                                                    )

akPuSoftDropCh2PFJetSequence_jec = cms.Sequence(akPuSoftDropCh2PFJetSequence_mc)
akPuSoftDropCh2PFJetSequence_mb = cms.Sequence(akPuSoftDropCh2PFJetSequence_mc)

akPuSoftDropCh2PFJetSequence = cms.Sequence(akPuSoftDropCh2PFJetSequence_jec)
akPuSoftDropCh2PFJetAnalyzer.genPtMin = cms.untracked.double(1)
akPuSoftDropCh2PFJetAnalyzer.jetPtMin = cms.double(1)
akPuSoftDropCh2PFpatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh2PFJets:sym']
akPuSoftDropCh2PFpatJetsWithBtagging.userData.userInts.src += ['akPuSoftDropCh2PFJets:droppedBranches']
