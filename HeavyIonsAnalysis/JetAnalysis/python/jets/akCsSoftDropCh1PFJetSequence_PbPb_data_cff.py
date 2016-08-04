

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akCsSoftDropCh1PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akCsSoftDropCh1PFJets"),
    matched = cms.InputTag("ak1HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akCsSoftDropCh1PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh1HiGenJets"),
    matched = cms.InputTag("ak1HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akCsSoftDropCh1PFparton = patJetPartonMatch.clone(src = cms.InputTag("akCsSoftDropCh1PFJets")
                                                        )

akCsSoftDropCh1PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akCsSoftDropCh1PFJets"),
    payload = "AK1PF_offline"
    )

akCsSoftDropCh1PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akCsSoftDropCh1CaloJets'))

#akCsSoftDropCh1PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak1HiSignalGenJets'))

akCsSoftDropCh1PFbTagger = bTaggers("akCsSoftDropCh1PF",0.1)

#create objects locally since they dont load properly otherwise
#akCsSoftDropCh1PFmatch = akCsSoftDropCh1PFbTagger.match
akCsSoftDropCh1PFparton = patJetPartonMatch.clone(src = cms.InputTag("akCsSoftDropCh1PFJets"), matched = cms.InputTag("hiSignalGenParticles"))
akCsSoftDropCh1PFPatJetFlavourAssociationLegacy = akCsSoftDropCh1PFbTagger.PatJetFlavourAssociationLegacy
akCsSoftDropCh1PFPatJetPartons = akCsSoftDropCh1PFbTagger.PatJetPartons
akCsSoftDropCh1PFJetTracksAssociatorAtVertex = akCsSoftDropCh1PFbTagger.JetTracksAssociatorAtVertex
akCsSoftDropCh1PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akCsSoftDropCh1PFSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropCh1PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akCsSoftDropCh1PFSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropCh1PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akCsSoftDropCh1PFCombinedSecondaryVertexBJetTags = akCsSoftDropCh1PFbTagger.CombinedSecondaryVertexBJetTags
akCsSoftDropCh1PFCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh1PFbTagger.CombinedSecondaryVertexV2BJetTags
akCsSoftDropCh1PFJetBProbabilityBJetTags = akCsSoftDropCh1PFbTagger.JetBProbabilityBJetTags
akCsSoftDropCh1PFSoftPFMuonByPtBJetTags = akCsSoftDropCh1PFbTagger.SoftPFMuonByPtBJetTags
akCsSoftDropCh1PFSoftPFMuonByIP3dBJetTags = akCsSoftDropCh1PFbTagger.SoftPFMuonByIP3dBJetTags
akCsSoftDropCh1PFTrackCountingHighEffBJetTags = akCsSoftDropCh1PFbTagger.TrackCountingHighEffBJetTags
akCsSoftDropCh1PFTrackCountingHighPurBJetTags = akCsSoftDropCh1PFbTagger.TrackCountingHighPurBJetTags
akCsSoftDropCh1PFPatJetPartonAssociationLegacy = akCsSoftDropCh1PFbTagger.PatJetPartonAssociationLegacy

akCsSoftDropCh1PFImpactParameterTagInfos = akCsSoftDropCh1PFbTagger.ImpactParameterTagInfos
akCsSoftDropCh1PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akCsSoftDropCh1PFJetProbabilityBJetTags = akCsSoftDropCh1PFbTagger.JetProbabilityBJetTags

akCsSoftDropCh1PFSecondaryVertexTagInfos = akCsSoftDropCh1PFbTagger.SecondaryVertexTagInfos
akCsSoftDropCh1PFSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropCh1PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akCsSoftDropCh1PFSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropCh1PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akCsSoftDropCh1PFCombinedSecondaryVertexBJetTags = akCsSoftDropCh1PFbTagger.CombinedSecondaryVertexBJetTags
akCsSoftDropCh1PFCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh1PFbTagger.CombinedSecondaryVertexV2BJetTags

akCsSoftDropCh1PFSecondaryVertexNegativeTagInfos = akCsSoftDropCh1PFbTagger.SecondaryVertexNegativeTagInfos
akCsSoftDropCh1PFNegativeSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropCh1PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akCsSoftDropCh1PFNegativeSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropCh1PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akCsSoftDropCh1PFNegativeCombinedSecondaryVertexBJetTags = akCsSoftDropCh1PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akCsSoftDropCh1PFPositiveCombinedSecondaryVertexBJetTags = akCsSoftDropCh1PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akCsSoftDropCh1PFNegativeCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh1PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akCsSoftDropCh1PFPositiveCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh1PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akCsSoftDropCh1PFSoftPFMuonsTagInfos = akCsSoftDropCh1PFbTagger.SoftPFMuonsTagInfos
akCsSoftDropCh1PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akCsSoftDropCh1PFSoftPFMuonBJetTags = akCsSoftDropCh1PFbTagger.SoftPFMuonBJetTags
akCsSoftDropCh1PFSoftPFMuonByIP3dBJetTags = akCsSoftDropCh1PFbTagger.SoftPFMuonByIP3dBJetTags
akCsSoftDropCh1PFSoftPFMuonByPtBJetTags = akCsSoftDropCh1PFbTagger.SoftPFMuonByPtBJetTags
akCsSoftDropCh1PFNegativeSoftPFMuonByPtBJetTags = akCsSoftDropCh1PFbTagger.NegativeSoftPFMuonByPtBJetTags
akCsSoftDropCh1PFPositiveSoftPFMuonByPtBJetTags = akCsSoftDropCh1PFbTagger.PositiveSoftPFMuonByPtBJetTags
akCsSoftDropCh1PFPatJetFlavourIdLegacy = cms.Sequence(akCsSoftDropCh1PFPatJetPartonAssociationLegacy*akCsSoftDropCh1PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akCsSoftDropCh1PFPatJetFlavourAssociation = akCsSoftDropCh1PFbTagger.PatJetFlavourAssociation
#akCsSoftDropCh1PFPatJetFlavourId = cms.Sequence(akCsSoftDropCh1PFPatJetPartons*akCsSoftDropCh1PFPatJetFlavourAssociation)

akCsSoftDropCh1PFJetBtaggingIP       = cms.Sequence(akCsSoftDropCh1PFImpactParameterTagInfos *
            (akCsSoftDropCh1PFTrackCountingHighEffBJetTags +
             akCsSoftDropCh1PFTrackCountingHighPurBJetTags +
             akCsSoftDropCh1PFJetProbabilityBJetTags +
             akCsSoftDropCh1PFJetBProbabilityBJetTags 
            )
            )

akCsSoftDropCh1PFJetBtaggingSV = cms.Sequence(akCsSoftDropCh1PFImpactParameterTagInfos
            *
            akCsSoftDropCh1PFSecondaryVertexTagInfos
            * (akCsSoftDropCh1PFSimpleSecondaryVertexHighEffBJetTags+
                akCsSoftDropCh1PFSimpleSecondaryVertexHighPurBJetTags+
                akCsSoftDropCh1PFCombinedSecondaryVertexBJetTags+
                akCsSoftDropCh1PFCombinedSecondaryVertexV2BJetTags
              )
            )

akCsSoftDropCh1PFJetBtaggingNegSV = cms.Sequence(akCsSoftDropCh1PFImpactParameterTagInfos
            *
            akCsSoftDropCh1PFSecondaryVertexNegativeTagInfos
            * (akCsSoftDropCh1PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akCsSoftDropCh1PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akCsSoftDropCh1PFNegativeCombinedSecondaryVertexBJetTags+
                akCsSoftDropCh1PFPositiveCombinedSecondaryVertexBJetTags+
                akCsSoftDropCh1PFNegativeCombinedSecondaryVertexV2BJetTags+
                akCsSoftDropCh1PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akCsSoftDropCh1PFJetBtaggingMu = cms.Sequence(akCsSoftDropCh1PFSoftPFMuonsTagInfos * (akCsSoftDropCh1PFSoftPFMuonBJetTags
                +
                akCsSoftDropCh1PFSoftPFMuonByIP3dBJetTags
                +
                akCsSoftDropCh1PFSoftPFMuonByPtBJetTags
                +
                akCsSoftDropCh1PFNegativeSoftPFMuonByPtBJetTags
                +
                akCsSoftDropCh1PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akCsSoftDropCh1PFJetBtagging = cms.Sequence(akCsSoftDropCh1PFJetBtaggingIP
            *akCsSoftDropCh1PFJetBtaggingSV
            *akCsSoftDropCh1PFJetBtaggingNegSV
#            *akCsSoftDropCh1PFJetBtaggingMu
            )

akCsSoftDropCh1PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akCsSoftDropCh1PFJets"),
        genJetMatch          = cms.InputTag("akCsSoftDropCh1PFmatch"),
        genPartonMatch       = cms.InputTag("akCsSoftDropCh1PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akCsSoftDropCh1PFcorr")),
        JetPartonMapSource   = cms.InputTag("akCsSoftDropCh1PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akCsSoftDropCh1PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akCsSoftDropCh1PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akCsSoftDropCh1PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akCsSoftDropCh1PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akCsSoftDropCh1PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akCsSoftDropCh1PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akCsSoftDropCh1PFJetBProbabilityBJetTags"),
            cms.InputTag("akCsSoftDropCh1PFJetProbabilityBJetTags"),
            #cms.InputTag("akCsSoftDropCh1PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akCsSoftDropCh1PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akCsSoftDropCh1PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akCsSoftDropCh1PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akCsSoftDropCh1PFJetID"),
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

akCsSoftDropCh1PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akCsSoftDropCh1PFJets"),
           	    R0  = cms.double( 0.1)
)
akCsSoftDropCh1PFpatJetsWithBtagging.userData.userFloats.src += ['akCsSoftDropCh1PFNjettiness:tau1','akCsSoftDropCh1PFNjettiness:tau2','akCsSoftDropCh1PFNjettiness:tau3']

akCsSoftDropCh1PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akCsSoftDropCh1PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak1HiSignalGenJets',#'ak1HiGenJets',
                                                             rParam = 0.1,
                                                             matchJets = cms.untracked.bool(False),
                                                             matchTag = 'patJetsWithBtagging',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("hiGeneralTracks"),
                                                             fillGenJets = False,
                                                             isMC = False,
							     doSubEvent = False,
                                                             useHepMC = cms.untracked.bool(False),
							     genParticles = cms.untracked.InputTag("genParticles"),
							     eventInfoTag = cms.InputTag("generator"),
                                                             doLifeTimeTagging = cms.untracked.bool(True),
                                                             doLifeTimeTaggingExtras = cms.untracked.bool(False),
                                                             bTagJetName = cms.untracked.string("akCsSoftDropCh1PF"),
                                                             jetName = cms.untracked.string("akCsSoftDropCh1PF"),
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

akCsSoftDropCh1PFJetSequence_mc = cms.Sequence(
                                                  #akCsSoftDropCh1PFclean
                                                  #*
                                                  akCsSoftDropCh1PFmatch
                                                  #*
                                                  #akCsSoftDropCh1PFmatchGroomed
                                                  *
                                                  akCsSoftDropCh1PFparton
                                                  *
                                                  akCsSoftDropCh1PFcorr
                                                  *
                                                  #akCsSoftDropCh1PFJetID
                                                  #*
                                                  akCsSoftDropCh1PFPatJetFlavourIdLegacy
                                                  #*
			                          #akCsSoftDropCh1PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akCsSoftDropCh1PFJetTracksAssociatorAtVertex
                                                  *
                                                  akCsSoftDropCh1PFJetBtagging
                                                  *
                                                  akCsSoftDropCh1PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akCsSoftDropCh1PFpatJetsWithBtagging
                                                  *
                                                  akCsSoftDropCh1PFJetAnalyzer
                                                  )

akCsSoftDropCh1PFJetSequence_data = cms.Sequence(akCsSoftDropCh1PFcorr
                                                    *
                                                    #akCsSoftDropCh1PFJetID
                                                    #*
                                                    akCsSoftDropCh1PFJetTracksAssociatorAtVertex
                                                    *
                                                    akCsSoftDropCh1PFJetBtagging
                                                    *
                                                    akCsSoftDropCh1PFNjettiness 
                                                    *
                                                    akCsSoftDropCh1PFpatJetsWithBtagging
                                                    *
                                                    akCsSoftDropCh1PFJetAnalyzer
                                                    )

akCsSoftDropCh1PFJetSequence_jec = cms.Sequence(akCsSoftDropCh1PFJetSequence_mc)
akCsSoftDropCh1PFJetSequence_mb = cms.Sequence(akCsSoftDropCh1PFJetSequence_mc)

akCsSoftDropCh1PFJetSequence = cms.Sequence(akCsSoftDropCh1PFJetSequence_data)
akCsSoftDropCh1PFpatJetsWithBtagging.userData.userFloats.src += ['akCsSoftDropCh1PFJets:sym']
akCsSoftDropCh1PFpatJetsWithBtagging.userData.userInts.src += ['akCsSoftDropCh1PFJets:droppedBranches']
