

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDropCh2PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh2PFJets"),
    matched = cms.InputTag("ak2HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.2
    )

akSoftDropCh2PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh2HiGenJets"),
    matched = cms.InputTag("ak2HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.2
    )

akSoftDropCh2PFparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh2PFJets")
                                                        )

akSoftDropCh2PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akSoftDropCh2PFJets"),
    payload = "AK2PF_offline"
    )

akSoftDropCh2PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akSoftDropCh2CaloJets'))

#akSoftDropCh2PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak2HiSignalGenJets'))

akSoftDropCh2PFbTagger = bTaggers("akSoftDropCh2PF",0.2)

#create objects locally since they dont load properly otherwise
#akSoftDropCh2PFmatch = akSoftDropCh2PFbTagger.match
akSoftDropCh2PFparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh2PFJets"), matched = cms.InputTag("hiSignalGenParticles"))
akSoftDropCh2PFPatJetFlavourAssociationLegacy = akSoftDropCh2PFbTagger.PatJetFlavourAssociationLegacy
akSoftDropCh2PFPatJetPartons = akSoftDropCh2PFbTagger.PatJetPartons
akSoftDropCh2PFJetTracksAssociatorAtVertex = akSoftDropCh2PFbTagger.JetTracksAssociatorAtVertex
akSoftDropCh2PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDropCh2PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh2PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh2PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh2PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh2PFCombinedSecondaryVertexBJetTags = akSoftDropCh2PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh2PFCombinedSecondaryVertexV2BJetTags = akSoftDropCh2PFbTagger.CombinedSecondaryVertexV2BJetTags
akSoftDropCh2PFJetBProbabilityBJetTags = akSoftDropCh2PFbTagger.JetBProbabilityBJetTags
akSoftDropCh2PFSoftPFMuonByPtBJetTags = akSoftDropCh2PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropCh2PFSoftPFMuonByIP3dBJetTags = akSoftDropCh2PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh2PFTrackCountingHighEffBJetTags = akSoftDropCh2PFbTagger.TrackCountingHighEffBJetTags
akSoftDropCh2PFTrackCountingHighPurBJetTags = akSoftDropCh2PFbTagger.TrackCountingHighPurBJetTags
akSoftDropCh2PFPatJetPartonAssociationLegacy = akSoftDropCh2PFbTagger.PatJetPartonAssociationLegacy

akSoftDropCh2PFImpactParameterTagInfos = akSoftDropCh2PFbTagger.ImpactParameterTagInfos
akSoftDropCh2PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh2PFJetProbabilityBJetTags = akSoftDropCh2PFbTagger.JetProbabilityBJetTags

akSoftDropCh2PFSecondaryVertexTagInfos = akSoftDropCh2PFbTagger.SecondaryVertexTagInfos
akSoftDropCh2PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh2PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh2PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh2PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh2PFCombinedSecondaryVertexBJetTags = akSoftDropCh2PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh2PFCombinedSecondaryVertexV2BJetTags = akSoftDropCh2PFbTagger.CombinedSecondaryVertexV2BJetTags

akSoftDropCh2PFSecondaryVertexNegativeTagInfos = akSoftDropCh2PFbTagger.SecondaryVertexNegativeTagInfos
akSoftDropCh2PFNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh2PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDropCh2PFNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh2PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDropCh2PFNegativeCombinedSecondaryVertexBJetTags = akSoftDropCh2PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDropCh2PFPositiveCombinedSecondaryVertexBJetTags = akSoftDropCh2PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDropCh2PFNegativeCombinedSecondaryVertexV2BJetTags = akSoftDropCh2PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDropCh2PFPositiveCombinedSecondaryVertexV2BJetTags = akSoftDropCh2PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDropCh2PFSoftPFMuonsTagInfos = akSoftDropCh2PFbTagger.SoftPFMuonsTagInfos
akSoftDropCh2PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh2PFSoftPFMuonBJetTags = akSoftDropCh2PFbTagger.SoftPFMuonBJetTags
akSoftDropCh2PFSoftPFMuonByIP3dBJetTags = akSoftDropCh2PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh2PFSoftPFMuonByPtBJetTags = akSoftDropCh2PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropCh2PFNegativeSoftPFMuonByPtBJetTags = akSoftDropCh2PFbTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDropCh2PFPositiveSoftPFMuonByPtBJetTags = akSoftDropCh2PFbTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDropCh2PFPatJetFlavourIdLegacy = cms.Sequence(akSoftDropCh2PFPatJetPartonAssociationLegacy*akSoftDropCh2PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akSoftDropCh2PFPatJetFlavourAssociation = akSoftDropCh2PFbTagger.PatJetFlavourAssociation
#akSoftDropCh2PFPatJetFlavourId = cms.Sequence(akSoftDropCh2PFPatJetPartons*akSoftDropCh2PFPatJetFlavourAssociation)

akSoftDropCh2PFJetBtaggingIP       = cms.Sequence(akSoftDropCh2PFImpactParameterTagInfos *
            (akSoftDropCh2PFTrackCountingHighEffBJetTags +
             akSoftDropCh2PFTrackCountingHighPurBJetTags +
             akSoftDropCh2PFJetProbabilityBJetTags +
             akSoftDropCh2PFJetBProbabilityBJetTags 
            )
            )

akSoftDropCh2PFJetBtaggingSV = cms.Sequence(akSoftDropCh2PFImpactParameterTagInfos
            *
            akSoftDropCh2PFSecondaryVertexTagInfos
            * (akSoftDropCh2PFSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh2PFSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh2PFCombinedSecondaryVertexBJetTags+
                akSoftDropCh2PFCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh2PFJetBtaggingNegSV = cms.Sequence(akSoftDropCh2PFImpactParameterTagInfos
            *
            akSoftDropCh2PFSecondaryVertexNegativeTagInfos
            * (akSoftDropCh2PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh2PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh2PFNegativeCombinedSecondaryVertexBJetTags+
                akSoftDropCh2PFPositiveCombinedSecondaryVertexBJetTags+
                akSoftDropCh2PFNegativeCombinedSecondaryVertexV2BJetTags+
                akSoftDropCh2PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh2PFJetBtaggingMu = cms.Sequence(akSoftDropCh2PFSoftPFMuonsTagInfos * (akSoftDropCh2PFSoftPFMuonBJetTags
                +
                akSoftDropCh2PFSoftPFMuonByIP3dBJetTags
                +
                akSoftDropCh2PFSoftPFMuonByPtBJetTags
                +
                akSoftDropCh2PFNegativeSoftPFMuonByPtBJetTags
                +
                akSoftDropCh2PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akSoftDropCh2PFJetBtagging = cms.Sequence(akSoftDropCh2PFJetBtaggingIP
            *akSoftDropCh2PFJetBtaggingSV
            *akSoftDropCh2PFJetBtaggingNegSV
#            *akSoftDropCh2PFJetBtaggingMu
            )

akSoftDropCh2PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akSoftDropCh2PFJets"),
        genJetMatch          = cms.InputTag("akSoftDropCh2PFmatch"),
        genPartonMatch       = cms.InputTag("akSoftDropCh2PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akSoftDropCh2PFcorr")),
        JetPartonMapSource   = cms.InputTag("akSoftDropCh2PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akSoftDropCh2PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akSoftDropCh2PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akSoftDropCh2PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akSoftDropCh2PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akSoftDropCh2PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akSoftDropCh2PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akSoftDropCh2PFJetBProbabilityBJetTags"),
            cms.InputTag("akSoftDropCh2PFJetProbabilityBJetTags"),
            #cms.InputTag("akSoftDropCh2PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akSoftDropCh2PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akSoftDropCh2PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akSoftDropCh2PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akSoftDropCh2PFJetID"),
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

akSoftDropCh2PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akSoftDropCh2PFJets"),
           	    R0  = cms.double( 0.2)
)
akSoftDropCh2PFpatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh2PFNjettiness:tau1','akSoftDropCh2PFNjettiness:tau2','akSoftDropCh2PFNjettiness:tau3']

akSoftDropCh2PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akSoftDropCh2PFpatJetsWithBtagging"),
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
                                                             bTagJetName = cms.untracked.string("akSoftDropCh2PF"),
                                                             jetName = cms.untracked.string("akSoftDropCh2PF"),
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

akSoftDropCh2PFJetSequence_mc = cms.Sequence(
                                                  #akSoftDropCh2PFclean
                                                  #*
                                                  akSoftDropCh2PFmatch
                                                  #*
                                                  #akSoftDropCh2PFmatchGroomed
                                                  *
                                                  akSoftDropCh2PFparton
                                                  *
                                                  akSoftDropCh2PFcorr
                                                  *
                                                  #akSoftDropCh2PFJetID
                                                  #*
                                                  akSoftDropCh2PFPatJetFlavourIdLegacy
                                                  #*
			                          #akSoftDropCh2PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akSoftDropCh2PFJetTracksAssociatorAtVertex
                                                  *
                                                  akSoftDropCh2PFJetBtagging
                                                  *
                                                  akSoftDropCh2PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akSoftDropCh2PFpatJetsWithBtagging
                                                  *
                                                  akSoftDropCh2PFJetAnalyzer
                                                  )

akSoftDropCh2PFJetSequence_data = cms.Sequence(akSoftDropCh2PFcorr
                                                    *
                                                    #akSoftDropCh2PFJetID
                                                    #*
                                                    akSoftDropCh2PFJetTracksAssociatorAtVertex
                                                    *
                                                    akSoftDropCh2PFJetBtagging
                                                    *
                                                    akSoftDropCh2PFNjettiness 
                                                    *
                                                    akSoftDropCh2PFpatJetsWithBtagging
                                                    *
                                                    akSoftDropCh2PFJetAnalyzer
                                                    )

akSoftDropCh2PFJetSequence_jec = cms.Sequence(akSoftDropCh2PFJetSequence_mc)
akSoftDropCh2PFJetSequence_mb = cms.Sequence(akSoftDropCh2PFJetSequence_mc)

akSoftDropCh2PFJetSequence = cms.Sequence(akSoftDropCh2PFJetSequence_jec)
akSoftDropCh2PFJetAnalyzer.genPtMin = cms.untracked.double(1)
akSoftDropCh2PFJetAnalyzer.jetPtMin = cms.double(1)
akSoftDropCh2PFpatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh2PFJets:sym']
akSoftDropCh2PFpatJetsWithBtagging.userData.userInts.src += ['akSoftDropCh2PFJets:droppedBranches']
