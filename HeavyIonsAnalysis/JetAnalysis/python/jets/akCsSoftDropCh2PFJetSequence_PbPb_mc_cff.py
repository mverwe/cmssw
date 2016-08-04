

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akCsSoftDropCh2PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akCsSoftDropCh2PFJets"),
    matched = cms.InputTag("ak2HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.2
    )

akCsSoftDropCh2PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh2HiGenJets"),
    matched = cms.InputTag("ak2HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.2
    )

akCsSoftDropCh2PFparton = patJetPartonMatch.clone(src = cms.InputTag("akCsSoftDropCh2PFJets")
                                                        )

akCsSoftDropCh2PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akCsSoftDropCh2PFJets"),
    payload = "AK2PF_offline"
    )

akCsSoftDropCh2PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akCsSoftDropCh2CaloJets'))

#akCsSoftDropCh2PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak2HiSignalGenJets'))

akCsSoftDropCh2PFbTagger = bTaggers("akCsSoftDropCh2PF",0.2)

#create objects locally since they dont load properly otherwise
#akCsSoftDropCh2PFmatch = akCsSoftDropCh2PFbTagger.match
akCsSoftDropCh2PFparton = patJetPartonMatch.clone(src = cms.InputTag("akCsSoftDropCh2PFJets"), matched = cms.InputTag("hiSignalGenParticles"))
akCsSoftDropCh2PFPatJetFlavourAssociationLegacy = akCsSoftDropCh2PFbTagger.PatJetFlavourAssociationLegacy
akCsSoftDropCh2PFPatJetPartons = akCsSoftDropCh2PFbTagger.PatJetPartons
akCsSoftDropCh2PFJetTracksAssociatorAtVertex = akCsSoftDropCh2PFbTagger.JetTracksAssociatorAtVertex
akCsSoftDropCh2PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akCsSoftDropCh2PFSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropCh2PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akCsSoftDropCh2PFSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropCh2PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akCsSoftDropCh2PFCombinedSecondaryVertexBJetTags = akCsSoftDropCh2PFbTagger.CombinedSecondaryVertexBJetTags
akCsSoftDropCh2PFCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh2PFbTagger.CombinedSecondaryVertexV2BJetTags
akCsSoftDropCh2PFJetBProbabilityBJetTags = akCsSoftDropCh2PFbTagger.JetBProbabilityBJetTags
akCsSoftDropCh2PFSoftPFMuonByPtBJetTags = akCsSoftDropCh2PFbTagger.SoftPFMuonByPtBJetTags
akCsSoftDropCh2PFSoftPFMuonByIP3dBJetTags = akCsSoftDropCh2PFbTagger.SoftPFMuonByIP3dBJetTags
akCsSoftDropCh2PFTrackCountingHighEffBJetTags = akCsSoftDropCh2PFbTagger.TrackCountingHighEffBJetTags
akCsSoftDropCh2PFTrackCountingHighPurBJetTags = akCsSoftDropCh2PFbTagger.TrackCountingHighPurBJetTags
akCsSoftDropCh2PFPatJetPartonAssociationLegacy = akCsSoftDropCh2PFbTagger.PatJetPartonAssociationLegacy

akCsSoftDropCh2PFImpactParameterTagInfos = akCsSoftDropCh2PFbTagger.ImpactParameterTagInfos
akCsSoftDropCh2PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akCsSoftDropCh2PFJetProbabilityBJetTags = akCsSoftDropCh2PFbTagger.JetProbabilityBJetTags

akCsSoftDropCh2PFSecondaryVertexTagInfos = akCsSoftDropCh2PFbTagger.SecondaryVertexTagInfos
akCsSoftDropCh2PFSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropCh2PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akCsSoftDropCh2PFSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropCh2PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akCsSoftDropCh2PFCombinedSecondaryVertexBJetTags = akCsSoftDropCh2PFbTagger.CombinedSecondaryVertexBJetTags
akCsSoftDropCh2PFCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh2PFbTagger.CombinedSecondaryVertexV2BJetTags

akCsSoftDropCh2PFSecondaryVertexNegativeTagInfos = akCsSoftDropCh2PFbTagger.SecondaryVertexNegativeTagInfos
akCsSoftDropCh2PFNegativeSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropCh2PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akCsSoftDropCh2PFNegativeSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropCh2PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akCsSoftDropCh2PFNegativeCombinedSecondaryVertexBJetTags = akCsSoftDropCh2PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akCsSoftDropCh2PFPositiveCombinedSecondaryVertexBJetTags = akCsSoftDropCh2PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akCsSoftDropCh2PFNegativeCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh2PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akCsSoftDropCh2PFPositiveCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh2PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akCsSoftDropCh2PFSoftPFMuonsTagInfos = akCsSoftDropCh2PFbTagger.SoftPFMuonsTagInfos
akCsSoftDropCh2PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akCsSoftDropCh2PFSoftPFMuonBJetTags = akCsSoftDropCh2PFbTagger.SoftPFMuonBJetTags
akCsSoftDropCh2PFSoftPFMuonByIP3dBJetTags = akCsSoftDropCh2PFbTagger.SoftPFMuonByIP3dBJetTags
akCsSoftDropCh2PFSoftPFMuonByPtBJetTags = akCsSoftDropCh2PFbTagger.SoftPFMuonByPtBJetTags
akCsSoftDropCh2PFNegativeSoftPFMuonByPtBJetTags = akCsSoftDropCh2PFbTagger.NegativeSoftPFMuonByPtBJetTags
akCsSoftDropCh2PFPositiveSoftPFMuonByPtBJetTags = akCsSoftDropCh2PFbTagger.PositiveSoftPFMuonByPtBJetTags
akCsSoftDropCh2PFPatJetFlavourIdLegacy = cms.Sequence(akCsSoftDropCh2PFPatJetPartonAssociationLegacy*akCsSoftDropCh2PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akCsSoftDropCh2PFPatJetFlavourAssociation = akCsSoftDropCh2PFbTagger.PatJetFlavourAssociation
#akCsSoftDropCh2PFPatJetFlavourId = cms.Sequence(akCsSoftDropCh2PFPatJetPartons*akCsSoftDropCh2PFPatJetFlavourAssociation)

akCsSoftDropCh2PFJetBtaggingIP       = cms.Sequence(akCsSoftDropCh2PFImpactParameterTagInfos *
            (akCsSoftDropCh2PFTrackCountingHighEffBJetTags +
             akCsSoftDropCh2PFTrackCountingHighPurBJetTags +
             akCsSoftDropCh2PFJetProbabilityBJetTags +
             akCsSoftDropCh2PFJetBProbabilityBJetTags 
            )
            )

akCsSoftDropCh2PFJetBtaggingSV = cms.Sequence(akCsSoftDropCh2PFImpactParameterTagInfos
            *
            akCsSoftDropCh2PFSecondaryVertexTagInfos
            * (akCsSoftDropCh2PFSimpleSecondaryVertexHighEffBJetTags+
                akCsSoftDropCh2PFSimpleSecondaryVertexHighPurBJetTags+
                akCsSoftDropCh2PFCombinedSecondaryVertexBJetTags+
                akCsSoftDropCh2PFCombinedSecondaryVertexV2BJetTags
              )
            )

akCsSoftDropCh2PFJetBtaggingNegSV = cms.Sequence(akCsSoftDropCh2PFImpactParameterTagInfos
            *
            akCsSoftDropCh2PFSecondaryVertexNegativeTagInfos
            * (akCsSoftDropCh2PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akCsSoftDropCh2PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akCsSoftDropCh2PFNegativeCombinedSecondaryVertexBJetTags+
                akCsSoftDropCh2PFPositiveCombinedSecondaryVertexBJetTags+
                akCsSoftDropCh2PFNegativeCombinedSecondaryVertexV2BJetTags+
                akCsSoftDropCh2PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akCsSoftDropCh2PFJetBtaggingMu = cms.Sequence(akCsSoftDropCh2PFSoftPFMuonsTagInfos * (akCsSoftDropCh2PFSoftPFMuonBJetTags
                +
                akCsSoftDropCh2PFSoftPFMuonByIP3dBJetTags
                +
                akCsSoftDropCh2PFSoftPFMuonByPtBJetTags
                +
                akCsSoftDropCh2PFNegativeSoftPFMuonByPtBJetTags
                +
                akCsSoftDropCh2PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akCsSoftDropCh2PFJetBtagging = cms.Sequence(akCsSoftDropCh2PFJetBtaggingIP
            *akCsSoftDropCh2PFJetBtaggingSV
            *akCsSoftDropCh2PFJetBtaggingNegSV
#            *akCsSoftDropCh2PFJetBtaggingMu
            )

akCsSoftDropCh2PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akCsSoftDropCh2PFJets"),
        genJetMatch          = cms.InputTag("akCsSoftDropCh2PFmatch"),
        genPartonMatch       = cms.InputTag("akCsSoftDropCh2PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akCsSoftDropCh2PFcorr")),
        JetPartonMapSource   = cms.InputTag("akCsSoftDropCh2PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akCsSoftDropCh2PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akCsSoftDropCh2PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akCsSoftDropCh2PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akCsSoftDropCh2PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akCsSoftDropCh2PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akCsSoftDropCh2PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akCsSoftDropCh2PFJetBProbabilityBJetTags"),
            cms.InputTag("akCsSoftDropCh2PFJetProbabilityBJetTags"),
            #cms.InputTag("akCsSoftDropCh2PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akCsSoftDropCh2PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akCsSoftDropCh2PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akCsSoftDropCh2PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akCsSoftDropCh2PFJetID"),
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

akCsSoftDropCh2PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akCsSoftDropCh2PFJets"),
           	    R0  = cms.double( 0.2)
)
akCsSoftDropCh2PFpatJetsWithBtagging.userData.userFloats.src += ['akCsSoftDropCh2PFNjettiness:tau1','akCsSoftDropCh2PFNjettiness:tau2','akCsSoftDropCh2PFNjettiness:tau3']

akCsSoftDropCh2PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akCsSoftDropCh2PFpatJetsWithBtagging"),
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
                                                             bTagJetName = cms.untracked.string("akCsSoftDropCh2PF"),
                                                             jetName = cms.untracked.string("akCsSoftDropCh2PF"),
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

akCsSoftDropCh2PFJetSequence_mc = cms.Sequence(
                                                  #akCsSoftDropCh2PFclean
                                                  #*
                                                  akCsSoftDropCh2PFmatch
                                                  #*
                                                  #akCsSoftDropCh2PFmatchGroomed
                                                  *
                                                  akCsSoftDropCh2PFparton
                                                  *
                                                  akCsSoftDropCh2PFcorr
                                                  *
                                                  #akCsSoftDropCh2PFJetID
                                                  #*
                                                  akCsSoftDropCh2PFPatJetFlavourIdLegacy
                                                  #*
			                          #akCsSoftDropCh2PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akCsSoftDropCh2PFJetTracksAssociatorAtVertex
                                                  *
                                                  akCsSoftDropCh2PFJetBtagging
                                                  *
                                                  akCsSoftDropCh2PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akCsSoftDropCh2PFpatJetsWithBtagging
                                                  *
                                                  akCsSoftDropCh2PFJetAnalyzer
                                                  )

akCsSoftDropCh2PFJetSequence_data = cms.Sequence(akCsSoftDropCh2PFcorr
                                                    *
                                                    #akCsSoftDropCh2PFJetID
                                                    #*
                                                    akCsSoftDropCh2PFJetTracksAssociatorAtVertex
                                                    *
                                                    akCsSoftDropCh2PFJetBtagging
                                                    *
                                                    akCsSoftDropCh2PFNjettiness 
                                                    *
                                                    akCsSoftDropCh2PFpatJetsWithBtagging
                                                    *
                                                    akCsSoftDropCh2PFJetAnalyzer
                                                    )

akCsSoftDropCh2PFJetSequence_jec = cms.Sequence(akCsSoftDropCh2PFJetSequence_mc)
akCsSoftDropCh2PFJetSequence_mb = cms.Sequence(akCsSoftDropCh2PFJetSequence_mc)

akCsSoftDropCh2PFJetSequence = cms.Sequence(akCsSoftDropCh2PFJetSequence_mc)
akCsSoftDropCh2PFpatJetsWithBtagging.userData.userFloats.src += ['akCsSoftDropCh2PFJets:sym']
akCsSoftDropCh2PFpatJetsWithBtagging.userData.userInts.src += ['akCsSoftDropCh2PFJets:droppedBranches']
