

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPuSoftDropCh4PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPuSoftDropCh4PFJets"),
    matched = cms.InputTag("ak4HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.4
    )

akPuSoftDropCh4PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh4HiGenJets"),
    matched = cms.InputTag("ak4HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.4
    )

akPuSoftDropCh4PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh4PFJets")
                                                        )

akPuSoftDropCh4PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akPuSoftDropCh4PFJets"),
    payload = "AKPu4PF_offline"
    )

akPuSoftDropCh4PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akPuSoftDropCh4CaloJets'))

#akPuSoftDropCh4PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak4HiSignalGenJets'))

akPuSoftDropCh4PFbTagger = bTaggers("akPuSoftDropCh4PF",0.4)

#create objects locally since they dont load properly otherwise
#akPuSoftDropCh4PFmatch = akPuSoftDropCh4PFbTagger.match
akPuSoftDropCh4PFparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh4PFJets"), matched = cms.InputTag("hiSignalGenParticles"))
akPuSoftDropCh4PFPatJetFlavourAssociationLegacy = akPuSoftDropCh4PFbTagger.PatJetFlavourAssociationLegacy
akPuSoftDropCh4PFPatJetPartons = akPuSoftDropCh4PFbTagger.PatJetPartons
akPuSoftDropCh4PFJetTracksAssociatorAtVertex = akPuSoftDropCh4PFbTagger.JetTracksAssociatorAtVertex
akPuSoftDropCh4PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPuSoftDropCh4PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh4PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh4PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh4PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh4PFCombinedSecondaryVertexBJetTags = akPuSoftDropCh4PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh4PFCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh4PFbTagger.CombinedSecondaryVertexV2BJetTags
akPuSoftDropCh4PFJetBProbabilityBJetTags = akPuSoftDropCh4PFbTagger.JetBProbabilityBJetTags
akPuSoftDropCh4PFSoftPFMuonByPtBJetTags = akPuSoftDropCh4PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh4PFSoftPFMuonByIP3dBJetTags = akPuSoftDropCh4PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh4PFTrackCountingHighEffBJetTags = akPuSoftDropCh4PFbTagger.TrackCountingHighEffBJetTags
akPuSoftDropCh4PFTrackCountingHighPurBJetTags = akPuSoftDropCh4PFbTagger.TrackCountingHighPurBJetTags
akPuSoftDropCh4PFPatJetPartonAssociationLegacy = akPuSoftDropCh4PFbTagger.PatJetPartonAssociationLegacy

akPuSoftDropCh4PFImpactParameterTagInfos = akPuSoftDropCh4PFbTagger.ImpactParameterTagInfos
akPuSoftDropCh4PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh4PFJetProbabilityBJetTags = akPuSoftDropCh4PFbTagger.JetProbabilityBJetTags

akPuSoftDropCh4PFSecondaryVertexTagInfos = akPuSoftDropCh4PFbTagger.SecondaryVertexTagInfos
akPuSoftDropCh4PFSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh4PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh4PFSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh4PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh4PFCombinedSecondaryVertexBJetTags = akPuSoftDropCh4PFbTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh4PFCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh4PFbTagger.CombinedSecondaryVertexV2BJetTags

akPuSoftDropCh4PFSecondaryVertexNegativeTagInfos = akPuSoftDropCh4PFbTagger.SecondaryVertexNegativeTagInfos
akPuSoftDropCh4PFNegativeSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh4PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh4PFNegativeSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh4PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh4PFNegativeCombinedSecondaryVertexBJetTags = akPuSoftDropCh4PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akPuSoftDropCh4PFPositiveCombinedSecondaryVertexBJetTags = akPuSoftDropCh4PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akPuSoftDropCh4PFNegativeCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh4PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPuSoftDropCh4PFPositiveCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh4PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPuSoftDropCh4PFSoftPFMuonsTagInfos = akPuSoftDropCh4PFbTagger.SoftPFMuonsTagInfos
akPuSoftDropCh4PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh4PFSoftPFMuonBJetTags = akPuSoftDropCh4PFbTagger.SoftPFMuonBJetTags
akPuSoftDropCh4PFSoftPFMuonByIP3dBJetTags = akPuSoftDropCh4PFbTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh4PFSoftPFMuonByPtBJetTags = akPuSoftDropCh4PFbTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh4PFNegativeSoftPFMuonByPtBJetTags = akPuSoftDropCh4PFbTagger.NegativeSoftPFMuonByPtBJetTags
akPuSoftDropCh4PFPositiveSoftPFMuonByPtBJetTags = akPuSoftDropCh4PFbTagger.PositiveSoftPFMuonByPtBJetTags
akPuSoftDropCh4PFPatJetFlavourIdLegacy = cms.Sequence(akPuSoftDropCh4PFPatJetPartonAssociationLegacy*akPuSoftDropCh4PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akPuSoftDropCh4PFPatJetFlavourAssociation = akPuSoftDropCh4PFbTagger.PatJetFlavourAssociation
#akPuSoftDropCh4PFPatJetFlavourId = cms.Sequence(akPuSoftDropCh4PFPatJetPartons*akPuSoftDropCh4PFPatJetFlavourAssociation)

akPuSoftDropCh4PFJetBtaggingIP       = cms.Sequence(akPuSoftDropCh4PFImpactParameterTagInfos *
            (akPuSoftDropCh4PFTrackCountingHighEffBJetTags +
             akPuSoftDropCh4PFTrackCountingHighPurBJetTags +
             akPuSoftDropCh4PFJetProbabilityBJetTags +
             akPuSoftDropCh4PFJetBProbabilityBJetTags 
            )
            )

akPuSoftDropCh4PFJetBtaggingSV = cms.Sequence(akPuSoftDropCh4PFImpactParameterTagInfos
            *
            akPuSoftDropCh4PFSecondaryVertexTagInfos
            * (akPuSoftDropCh4PFSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh4PFSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh4PFCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh4PFCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh4PFJetBtaggingNegSV = cms.Sequence(akPuSoftDropCh4PFImpactParameterTagInfos
            *
            akPuSoftDropCh4PFSecondaryVertexNegativeTagInfos
            * (akPuSoftDropCh4PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh4PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh4PFNegativeCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh4PFPositiveCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh4PFNegativeCombinedSecondaryVertexV2BJetTags+
                akPuSoftDropCh4PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh4PFJetBtaggingMu = cms.Sequence(akPuSoftDropCh4PFSoftPFMuonsTagInfos * (akPuSoftDropCh4PFSoftPFMuonBJetTags
                +
                akPuSoftDropCh4PFSoftPFMuonByIP3dBJetTags
                +
                akPuSoftDropCh4PFSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh4PFNegativeSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh4PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akPuSoftDropCh4PFJetBtagging = cms.Sequence(akPuSoftDropCh4PFJetBtaggingIP
            *akPuSoftDropCh4PFJetBtaggingSV
            *akPuSoftDropCh4PFJetBtaggingNegSV
#            *akPuSoftDropCh4PFJetBtaggingMu
            )

akPuSoftDropCh4PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akPuSoftDropCh4PFJets"),
        genJetMatch          = cms.InputTag("akPuSoftDropCh4PFmatch"),
        genPartonMatch       = cms.InputTag("akPuSoftDropCh4PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPuSoftDropCh4PFcorr")),
        JetPartonMapSource   = cms.InputTag("akPuSoftDropCh4PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akPuSoftDropCh4PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPuSoftDropCh4PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akPuSoftDropCh4PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh4PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPuSoftDropCh4PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPuSoftDropCh4PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akPuSoftDropCh4PFJetBProbabilityBJetTags"),
            cms.InputTag("akPuSoftDropCh4PFJetProbabilityBJetTags"),
            #cms.InputTag("akPuSoftDropCh4PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akPuSoftDropCh4PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akPuSoftDropCh4PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh4PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPuSoftDropCh4PFJetID"),
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

akPuSoftDropCh4PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akPuSoftDropCh4PFJets"),
           	    R0  = cms.double( 0.4)
)
akPuSoftDropCh4PFpatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh4PFNjettiness:tau1','akPuSoftDropCh4PFNjettiness:tau2','akPuSoftDropCh4PFNjettiness:tau3']

akPuSoftDropCh4PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPuSoftDropCh4PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak4HiSignalGenJets',#'ak4HiGenJets',
                                                             rParam = 0.4,
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
                                                             bTagJetName = cms.untracked.string("akPuSoftDropCh4PF"),
                                                             jetName = cms.untracked.string("akPuSoftDropCh4PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropCh4GenJets"),
                                                             doGenTaus = False,
                                                             genTau1 = cms.InputTag("akSoftDropCh4GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropCh4GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropCh4GenNjettiness","tau3"),
                                                             doGenSym = True,
                                                             genSym = cms.InputTag("akSoftDropCh4GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropCh4GenJets","droppedBranches")
                                                             )

akPuSoftDropCh4PFJetSequence_mc = cms.Sequence(
                                                  #akPuSoftDropCh4PFclean
                                                  #*
                                                  akPuSoftDropCh4PFmatch
                                                  #*
                                                  #akPuSoftDropCh4PFmatchGroomed
                                                  *
                                                  akPuSoftDropCh4PFparton
                                                  *
                                                  akPuSoftDropCh4PFcorr
                                                  *
                                                  #akPuSoftDropCh4PFJetID
                                                  #*
                                                  akPuSoftDropCh4PFPatJetFlavourIdLegacy
                                                  #*
			                          #akPuSoftDropCh4PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akPuSoftDropCh4PFJetTracksAssociatorAtVertex
                                                  *
                                                  akPuSoftDropCh4PFJetBtagging
                                                  *
                                                  akPuSoftDropCh4PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akPuSoftDropCh4PFpatJetsWithBtagging
                                                  *
                                                  akPuSoftDropCh4PFJetAnalyzer
                                                  )

akPuSoftDropCh4PFJetSequence_data = cms.Sequence(akPuSoftDropCh4PFcorr
                                                    *
                                                    #akPuSoftDropCh4PFJetID
                                                    #*
                                                    akPuSoftDropCh4PFJetTracksAssociatorAtVertex
                                                    *
                                                    akPuSoftDropCh4PFJetBtagging
                                                    *
                                                    akPuSoftDropCh4PFNjettiness 
                                                    *
                                                    akPuSoftDropCh4PFpatJetsWithBtagging
                                                    *
                                                    akPuSoftDropCh4PFJetAnalyzer
                                                    )

akPuSoftDropCh4PFJetSequence_jec = cms.Sequence(akPuSoftDropCh4PFJetSequence_mc)
akPuSoftDropCh4PFJetSequence_mb = cms.Sequence(akPuSoftDropCh4PFJetSequence_mc)

akPuSoftDropCh4PFJetSequence = cms.Sequence(akPuSoftDropCh4PFJetSequence_data)
akPuSoftDropCh4PFpatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh4PFJets:sym']
akPuSoftDropCh4PFpatJetsWithBtagging.userData.userInts.src += ['akPuSoftDropCh4PFJets:droppedBranches']
