

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropCh5PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropCh5PFJets"),
    matched = cms.InputTag("ak5HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.5
    )

akVsSoftDropCh5PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh5HiGenJets"),
    matched = cms.InputTag("ak5HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.5
    )

akVsSoftDropCh5PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh5PFJets")
                                                        )

akVsSoftDropCh5PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropCh5PFJets"),
    payload = "AK5PF_offline"
    )

akVsSoftDropCh5PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropCh5CaloJets'))

#akVsSoftDropCh5PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak5HiSignalGenJets'))

akVsSoftDropCh5PFbTagger = bTaggers("akVsSoftDropCh5PF",0.5)

#create objects locally since they dont load properly otherwise
#akVsSoftDropCh5PFmatch = akVsSoftDropCh5PFbTagger.match
akVsSoftDropCh5PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh5PFJets"), matched = cms.InputTag("hiSignalGenParticles"))
akVsSoftDropCh5PFPatJetFlavourAssociationLegacy = akVsSoftDropCh5PFbTagger.PatJetFlavourAssociationLegacy
akVsSoftDropCh5PFPatJetPartons = akVsSoftDropCh5PFbTagger.PatJetPartons
akVsSoftDropCh5PFJetTracksAssociatorAtVertex = akVsSoftDropCh5PFbTagger.JetTracksAssociatorAtVertex
akVsSoftDropCh5PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropCh5PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh5PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh5PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh5PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh5PFCombinedSecondaryVertexBJetTags = akVsSoftDropCh5PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh5PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh5PFbTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropCh5PFJetBProbabilityBJetTags = akVsSoftDropCh5PFbTagger.JetBProbabilityBJetTags
akVsSoftDropCh5PFSoftPFMuonByPtBJetTags = akVsSoftDropCh5PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh5PFSoftPFMuonByIP3dBJetTags = akVsSoftDropCh5PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh5PFTrackCountingHighEffBJetTags = akVsSoftDropCh5PFbTagger.TrackCountingHighEffBJetTags
akVsSoftDropCh5PFTrackCountingHighPurBJetTags = akVsSoftDropCh5PFbTagger.TrackCountingHighPurBJetTags
akVsSoftDropCh5PFPatJetPartonAssociationLegacy = akVsSoftDropCh5PFbTagger.PatJetPartonAssociationLegacy

akVsSoftDropCh5PFImpactParameterTagInfos = akVsSoftDropCh5PFbTagger.ImpactParameterTagInfos
akVsSoftDropCh5PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh5PFJetProbabilityBJetTags = akVsSoftDropCh5PFbTagger.JetProbabilityBJetTags

akVsSoftDropCh5PFSecondaryVertexTagInfos = akVsSoftDropCh5PFbTagger.SecondaryVertexTagInfos
akVsSoftDropCh5PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh5PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh5PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh5PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh5PFCombinedSecondaryVertexBJetTags = akVsSoftDropCh5PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh5PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh5PFbTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropCh5PFSecondaryVertexNegativeTagInfos = akVsSoftDropCh5PFbTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropCh5PFNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh5PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh5PFNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh5PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh5PFNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropCh5PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropCh5PFPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropCh5PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropCh5PFNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh5PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropCh5PFPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh5PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropCh5PFSoftPFMuonsTagInfos = akVsSoftDropCh5PFbTagger.SoftPFMuonsTagInfos
akVsSoftDropCh5PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh5PFSoftPFMuonBJetTags = akVsSoftDropCh5PFbTagger.SoftPFMuonBJetTags
akVsSoftDropCh5PFSoftPFMuonByIP3dBJetTags = akVsSoftDropCh5PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh5PFSoftPFMuonByPtBJetTags = akVsSoftDropCh5PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh5PFNegativeSoftPFMuonByPtBJetTags = akVsSoftDropCh5PFbTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropCh5PFPositiveSoftPFMuonByPtBJetTags = akVsSoftDropCh5PFbTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropCh5PFPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropCh5PFPatJetPartonAssociationLegacy*akVsSoftDropCh5PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropCh5PFPatJetFlavourAssociation = akVsSoftDropCh5PFbTagger.PatJetFlavourAssociation
#akVsSoftDropCh5PFPatJetFlavourId = cms.Sequence(akVsSoftDropCh5PFPatJetPartons*akVsSoftDropCh5PFPatJetFlavourAssociation)

akVsSoftDropCh5PFJetBtaggingIP       = cms.Sequence(akVsSoftDropCh5PFImpactParameterTagInfos *
            (akVsSoftDropCh5PFTrackCountingHighEffBJetTags +
             akVsSoftDropCh5PFTrackCountingHighPurBJetTags +
             akVsSoftDropCh5PFJetProbabilityBJetTags +
             akVsSoftDropCh5PFJetBProbabilityBJetTags 
            )
            )

akVsSoftDropCh5PFJetBtaggingSV = cms.Sequence(akVsSoftDropCh5PFImpactParameterTagInfos
            *
            akVsSoftDropCh5PFSecondaryVertexTagInfos
            * (akVsSoftDropCh5PFSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh5PFSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh5PFCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh5PFCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh5PFJetBtaggingNegSV = cms.Sequence(akVsSoftDropCh5PFImpactParameterTagInfos
            *
            akVsSoftDropCh5PFSecondaryVertexNegativeTagInfos
            * (akVsSoftDropCh5PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh5PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh5PFNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh5PFPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh5PFNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropCh5PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh5PFJetBtaggingMu = cms.Sequence(akVsSoftDropCh5PFSoftPFMuonsTagInfos * (akVsSoftDropCh5PFSoftPFMuonBJetTags
                +
                akVsSoftDropCh5PFSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropCh5PFSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh5PFNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh5PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropCh5PFJetBtagging = cms.Sequence(akVsSoftDropCh5PFJetBtaggingIP
            *akVsSoftDropCh5PFJetBtaggingSV
            *akVsSoftDropCh5PFJetBtaggingNegSV
#            *akVsSoftDropCh5PFJetBtaggingMu
            )

akVsSoftDropCh5PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropCh5PFJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropCh5PFmatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropCh5PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropCh5PFcorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropCh5PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropCh5PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropCh5PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropCh5PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh5PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropCh5PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropCh5PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropCh5PFJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropCh5PFJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropCh5PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropCh5PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropCh5PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh5PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropCh5PFJetID"),
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

akVsSoftDropCh5PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropCh5PFJets"),
           	    R0  = cms.double( 0.5)
)
akVsSoftDropCh5PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh5PFNjettiness:tau1','akVsSoftDropCh5PFNjettiness:tau2','akVsSoftDropCh5PFNjettiness:tau3']

akVsSoftDropCh5PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropCh5PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak5HiSignalGenJets',#'ak5HiGenJets',
                                                             rParam = 0.5,
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
                                                             bTagJetName = cms.untracked.string("akVsSoftDropCh5PF"),
                                                             jetName = cms.untracked.string("akVsSoftDropCh5PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
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

akVsSoftDropCh5PFJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropCh5PFclean
                                                  #*
                                                  akVsSoftDropCh5PFmatch
                                                  #*
                                                  #akVsSoftDropCh5PFmatchGroomed
                                                  *
                                                  akVsSoftDropCh5PFparton
                                                  *
                                                  akVsSoftDropCh5PFcorr
                                                  *
                                                  #akVsSoftDropCh5PFJetID
                                                  #*
                                                  akVsSoftDropCh5PFPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropCh5PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropCh5PFJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropCh5PFJetBtagging
                                                  *
                                                  akVsSoftDropCh5PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropCh5PFpatJetsWithBtagging
                                                  *
                                                  akVsSoftDropCh5PFJetAnalyzer
                                                  )

akVsSoftDropCh5PFJetSequence_data = cms.Sequence(akVsSoftDropCh5PFcorr
                                                    *
                                                    #akVsSoftDropCh5PFJetID
                                                    #*
                                                    akVsSoftDropCh5PFJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropCh5PFJetBtagging
                                                    *
                                                    akVsSoftDropCh5PFNjettiness 
                                                    *
                                                    akVsSoftDropCh5PFpatJetsWithBtagging
                                                    *
                                                    akVsSoftDropCh5PFJetAnalyzer
                                                    )

akVsSoftDropCh5PFJetSequence_jec = cms.Sequence(akVsSoftDropCh5PFJetSequence_mc)
akVsSoftDropCh5PFJetSequence_mb = cms.Sequence(akVsSoftDropCh5PFJetSequence_mc)

akVsSoftDropCh5PFJetSequence = cms.Sequence(akVsSoftDropCh5PFJetSequence_jec)
akVsSoftDropCh5PFJetAnalyzer.genPtMin = cms.untracked.double(1)
akVsSoftDropCh5PFJetAnalyzer.jetPtMin = cms.double(1)
akVsSoftDropCh5PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh5PFJets:sym']
akVsSoftDropCh5PFpatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropCh5PFJets:droppedBranches']
