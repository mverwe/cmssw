

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPuSoftDropCh1PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPuSoftDropCh1PFJets"),
    matched = cms.InputTag("ak1HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akPuSoftDropCh1PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh1HiGenJets"),
    matched = cms.InputTag("ak1HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akPuSoftDropCh1PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh1PFJets")
                                                        )

akPuSoftDropCh1PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akPuSoftDropCh1PFJets"),
    payload = "AKPu1PF_offline"
    )

akPuSoftDropCh1PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akPuSoftDropCh1CaloJets'))

#akPuSoftDropCh1PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak1HiSignalGenJets'))

akPuSoftDropCh1PFbTagger = bTaggers("akPuSoftDropCh1PF",0.1)

#create objects locally since they dont load properly otherwise
#akPuSoftDropCh1PFmatch = akPuSoftDropCh1PFbTagger.match
akPuSoftDropCh1PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh1PFJets"), matched = cms.InputTag("hiSignalGenParticles"))
akPuSoftDropCh1PFPatJetFlavourAssociationLegacy = akPuSoftDropCh1PFbTagger.PatJetFlavourAssociationLegacy
akPuSoftDropCh1PFPatJetPartons = akPuSoftDropCh1PFbTagger.PatJetPartons
akPuSoftDropCh1PFJetTracksAssociatorAtVertex = akPuSoftDropCh1PFbTagger.JetTracksAssociatorAtVertex
akPuSoftDropCh1PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPuSoftDropCh1PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh1PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh1PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh1PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh1PFCombinedSecondaryVertexBJetTags = akPuSoftDropCh1PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh1PFCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh1PFbTagger.CombinedSecondaryVertexV2BJetTags
akPuSoftDropCh1PFJetBProbabilityBJetTags = akPuSoftDropCh1PFbTagger.JetBProbabilityBJetTags
akPuSoftDropCh1PFSoftPFMuonByPtBJetTags = akPuSoftDropCh1PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh1PFSoftPFMuonByIP3dBJetTags = akPuSoftDropCh1PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh1PFTrackCountingHighEffBJetTags = akPuSoftDropCh1PFbTagger.TrackCountingHighEffBJetTags
akPuSoftDropCh1PFTrackCountingHighPurBJetTags = akPuSoftDropCh1PFbTagger.TrackCountingHighPurBJetTags
akPuSoftDropCh1PFPatJetPartonAssociationLegacy = akPuSoftDropCh1PFbTagger.PatJetPartonAssociationLegacy

akPuSoftDropCh1PFImpactParameterTagInfos = akPuSoftDropCh1PFbTagger.ImpactParameterTagInfos
akPuSoftDropCh1PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh1PFJetProbabilityBJetTags = akPuSoftDropCh1PFbTagger.JetProbabilityBJetTags

akPuSoftDropCh1PFSecondaryVertexTagInfos = akPuSoftDropCh1PFbTagger.SecondaryVertexTagInfos
akPuSoftDropCh1PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh1PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh1PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh1PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh1PFCombinedSecondaryVertexBJetTags = akPuSoftDropCh1PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh1PFCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh1PFbTagger.CombinedSecondaryVertexV2BJetTags

akPuSoftDropCh1PFSecondaryVertexNegativeTagInfos = akPuSoftDropCh1PFbTagger.SecondaryVertexNegativeTagInfos
akPuSoftDropCh1PFNegativeSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh1PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh1PFNegativeSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh1PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh1PFNegativeCombinedSecondaryVertexBJetTags = akPuSoftDropCh1PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akPuSoftDropCh1PFPositiveCombinedSecondaryVertexBJetTags = akPuSoftDropCh1PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akPuSoftDropCh1PFNegativeCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh1PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPuSoftDropCh1PFPositiveCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh1PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPuSoftDropCh1PFSoftPFMuonsTagInfos = akPuSoftDropCh1PFbTagger.SoftPFMuonsTagInfos
akPuSoftDropCh1PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh1PFSoftPFMuonBJetTags = akPuSoftDropCh1PFbTagger.SoftPFMuonBJetTags
akPuSoftDropCh1PFSoftPFMuonByIP3dBJetTags = akPuSoftDropCh1PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh1PFSoftPFMuonByPtBJetTags = akPuSoftDropCh1PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh1PFNegativeSoftPFMuonByPtBJetTags = akPuSoftDropCh1PFbTagger.NegativeSoftPFMuonByPtBJetTags
akPuSoftDropCh1PFPositiveSoftPFMuonByPtBJetTags = akPuSoftDropCh1PFbTagger.PositiveSoftPFMuonByPtBJetTags
akPuSoftDropCh1PFPatJetFlavourIdLegacy = cms.Sequence(akPuSoftDropCh1PFPatJetPartonAssociationLegacy*akPuSoftDropCh1PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akPuSoftDropCh1PFPatJetFlavourAssociation = akPuSoftDropCh1PFbTagger.PatJetFlavourAssociation
#akPuSoftDropCh1PFPatJetFlavourId = cms.Sequence(akPuSoftDropCh1PFPatJetPartons*akPuSoftDropCh1PFPatJetFlavourAssociation)

akPuSoftDropCh1PFJetBtaggingIP       = cms.Sequence(akPuSoftDropCh1PFImpactParameterTagInfos *
            (akPuSoftDropCh1PFTrackCountingHighEffBJetTags +
             akPuSoftDropCh1PFTrackCountingHighPurBJetTags +
             akPuSoftDropCh1PFJetProbabilityBJetTags +
             akPuSoftDropCh1PFJetBProbabilityBJetTags 
            )
            )

akPuSoftDropCh1PFJetBtaggingSV = cms.Sequence(akPuSoftDropCh1PFImpactParameterTagInfos
            *
            akPuSoftDropCh1PFSecondaryVertexTagInfos
            * (akPuSoftDropCh1PFSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh1PFSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh1PFCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh1PFCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh1PFJetBtaggingNegSV = cms.Sequence(akPuSoftDropCh1PFImpactParameterTagInfos
            *
            akPuSoftDropCh1PFSecondaryVertexNegativeTagInfos
            * (akPuSoftDropCh1PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh1PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh1PFNegativeCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh1PFPositiveCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh1PFNegativeCombinedSecondaryVertexV2BJetTags+
                akPuSoftDropCh1PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh1PFJetBtaggingMu = cms.Sequence(akPuSoftDropCh1PFSoftPFMuonsTagInfos * (akPuSoftDropCh1PFSoftPFMuonBJetTags
                +
                akPuSoftDropCh1PFSoftPFMuonByIP3dBJetTags
                +
                akPuSoftDropCh1PFSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh1PFNegativeSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh1PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akPuSoftDropCh1PFJetBtagging = cms.Sequence(akPuSoftDropCh1PFJetBtaggingIP
            *akPuSoftDropCh1PFJetBtaggingSV
            *akPuSoftDropCh1PFJetBtaggingNegSV
#            *akPuSoftDropCh1PFJetBtaggingMu
            )

akPuSoftDropCh1PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akPuSoftDropCh1PFJets"),
        genJetMatch          = cms.InputTag("akPuSoftDropCh1PFmatch"),
        genPartonMatch       = cms.InputTag("akPuSoftDropCh1PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPuSoftDropCh1PFcorr")),
        JetPartonMapSource   = cms.InputTag("akPuSoftDropCh1PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akPuSoftDropCh1PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPuSoftDropCh1PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akPuSoftDropCh1PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh1PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPuSoftDropCh1PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPuSoftDropCh1PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akPuSoftDropCh1PFJetBProbabilityBJetTags"),
            cms.InputTag("akPuSoftDropCh1PFJetProbabilityBJetTags"),
            #cms.InputTag("akPuSoftDropCh1PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akPuSoftDropCh1PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akPuSoftDropCh1PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh1PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPuSoftDropCh1PFJetID"),
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

akPuSoftDropCh1PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akPuSoftDropCh1PFJets"),
           	    R0  = cms.double( 0.1)
)
akPuSoftDropCh1PFpatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh1PFNjettiness:tau1','akPuSoftDropCh1PFNjettiness:tau2','akPuSoftDropCh1PFNjettiness:tau3']

akPuSoftDropCh1PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPuSoftDropCh1PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak1HiSignalGenJets',#'ak1HiGenJets',
                                                             rParam = 0.1,
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
                                                             bTagJetName = cms.untracked.string("akPuSoftDropCh1PF"),
                                                             jetName = cms.untracked.string("akPuSoftDropCh1PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropCh1GenJets"),
                                                             doGenTaus = False,
                                                             genTau1 = cms.InputTag("akSoftDropCh1GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropCh1GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropCh1GenNjettiness","tau3"),
                                                             doGenSym = True,
                                                             genSym = cms.InputTag("akSoftDropCh1GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropCh1GenJets","droppedBranches")
                                                             )

akPuSoftDropCh1PFJetSequence_mc = cms.Sequence(
                                                  #akPuSoftDropCh1PFclean
                                                  #*
                                                  akPuSoftDropCh1PFmatch
                                                  #*
                                                  #akPuSoftDropCh1PFmatchGroomed
                                                  *
                                                  akPuSoftDropCh1PFparton
                                                  *
                                                  akPuSoftDropCh1PFcorr
                                                  *
                                                  #akPuSoftDropCh1PFJetID
                                                  #*
                                                  akPuSoftDropCh1PFPatJetFlavourIdLegacy
                                                  #*
			                          #akPuSoftDropCh1PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akPuSoftDropCh1PFJetTracksAssociatorAtVertex
                                                  *
                                                  akPuSoftDropCh1PFJetBtagging
                                                  *
                                                  akPuSoftDropCh1PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akPuSoftDropCh1PFpatJetsWithBtagging
                                                  *
                                                  akPuSoftDropCh1PFJetAnalyzer
                                                  )

akPuSoftDropCh1PFJetSequence_data = cms.Sequence(akPuSoftDropCh1PFcorr
                                                    *
                                                    #akPuSoftDropCh1PFJetID
                                                    #*
                                                    akPuSoftDropCh1PFJetTracksAssociatorAtVertex
                                                    *
                                                    akPuSoftDropCh1PFJetBtagging
                                                    *
                                                    akPuSoftDropCh1PFNjettiness 
                                                    *
                                                    akPuSoftDropCh1PFpatJetsWithBtagging
                                                    *
                                                    akPuSoftDropCh1PFJetAnalyzer
                                                    )

akPuSoftDropCh1PFJetSequence_jec = cms.Sequence(akPuSoftDropCh1PFJetSequence_mc)
akPuSoftDropCh1PFJetSequence_mb = cms.Sequence(akPuSoftDropCh1PFJetSequence_mc)

akPuSoftDropCh1PFJetSequence = cms.Sequence(akPuSoftDropCh1PFJetSequence_jec)
akPuSoftDropCh1PFJetAnalyzer.genPtMin = cms.untracked.double(1)
akPuSoftDropCh1PFJetAnalyzer.jetPtMin = cms.double(1)
akPuSoftDropCh1PFpatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh1PFJets:sym']
akPuSoftDropCh1PFpatJetsWithBtagging.userData.userInts.src += ['akPuSoftDropCh1PFJets:droppedBranches']
