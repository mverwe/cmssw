

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akCsSoftDropCh4PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akCsSoftDropCh4PFJets"),
    matched = cms.InputTag("ak4HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.4
    )

akCsSoftDropCh4PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh4HiGenJets"),
    matched = cms.InputTag("ak4HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.4
    )

akCsSoftDropCh4PFparton = patJetPartonMatch.clone(src = cms.InputTag("akCsSoftDropCh4PFJets")
                                                        )

akCsSoftDropCh4PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akCsSoftDropCh4PFJets"),
    payload = "AK4PF_offline"
    )

akCsSoftDropCh4PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akCsSoftDropCh4CaloJets'))

#akCsSoftDropCh4PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak4HiSignalGenJets'))

akCsSoftDropCh4PFbTagger = bTaggers("akCsSoftDropCh4PF",0.4)

#create objects locally since they dont load properly otherwise
#akCsSoftDropCh4PFmatch = akCsSoftDropCh4PFbTagger.match
akCsSoftDropCh4PFparton = patJetPartonMatch.clone(src = cms.InputTag("akCsSoftDropCh4PFJets"), matched = cms.InputTag("hiSignalGenParticles"))
akCsSoftDropCh4PFPatJetFlavourAssociationLegacy = akCsSoftDropCh4PFbTagger.PatJetFlavourAssociationLegacy
akCsSoftDropCh4PFPatJetPartons = akCsSoftDropCh4PFbTagger.PatJetPartons
akCsSoftDropCh4PFJetTracksAssociatorAtVertex = akCsSoftDropCh4PFbTagger.JetTracksAssociatorAtVertex
akCsSoftDropCh4PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akCsSoftDropCh4PFSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropCh4PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akCsSoftDropCh4PFSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropCh4PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akCsSoftDropCh4PFCombinedSecondaryVertexBJetTags = akCsSoftDropCh4PFbTagger.CombinedSecondaryVertexBJetTags
akCsSoftDropCh4PFCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh4PFbTagger.CombinedSecondaryVertexV2BJetTags
akCsSoftDropCh4PFJetBProbabilityBJetTags = akCsSoftDropCh4PFbTagger.JetBProbabilityBJetTags
akCsSoftDropCh4PFSoftPFMuonByPtBJetTags = akCsSoftDropCh4PFbTagger.SoftPFMuonByPtBJetTags
akCsSoftDropCh4PFSoftPFMuonByIP3dBJetTags = akCsSoftDropCh4PFbTagger.SoftPFMuonByIP3dBJetTags
akCsSoftDropCh4PFTrackCountingHighEffBJetTags = akCsSoftDropCh4PFbTagger.TrackCountingHighEffBJetTags
akCsSoftDropCh4PFTrackCountingHighPurBJetTags = akCsSoftDropCh4PFbTagger.TrackCountingHighPurBJetTags
akCsSoftDropCh4PFPatJetPartonAssociationLegacy = akCsSoftDropCh4PFbTagger.PatJetPartonAssociationLegacy

akCsSoftDropCh4PFImpactParameterTagInfos = akCsSoftDropCh4PFbTagger.ImpactParameterTagInfos
akCsSoftDropCh4PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akCsSoftDropCh4PFJetProbabilityBJetTags = akCsSoftDropCh4PFbTagger.JetProbabilityBJetTags

akCsSoftDropCh4PFSecondaryVertexTagInfos = akCsSoftDropCh4PFbTagger.SecondaryVertexTagInfos
akCsSoftDropCh4PFSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropCh4PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akCsSoftDropCh4PFSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropCh4PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akCsSoftDropCh4PFCombinedSecondaryVertexBJetTags = akCsSoftDropCh4PFbTagger.CombinedSecondaryVertexBJetTags
akCsSoftDropCh4PFCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh4PFbTagger.CombinedSecondaryVertexV2BJetTags

akCsSoftDropCh4PFSecondaryVertexNegativeTagInfos = akCsSoftDropCh4PFbTagger.SecondaryVertexNegativeTagInfos
akCsSoftDropCh4PFNegativeSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropCh4PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akCsSoftDropCh4PFNegativeSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropCh4PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akCsSoftDropCh4PFNegativeCombinedSecondaryVertexBJetTags = akCsSoftDropCh4PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akCsSoftDropCh4PFPositiveCombinedSecondaryVertexBJetTags = akCsSoftDropCh4PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akCsSoftDropCh4PFNegativeCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh4PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akCsSoftDropCh4PFPositiveCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh4PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akCsSoftDropCh4PFSoftPFMuonsTagInfos = akCsSoftDropCh4PFbTagger.SoftPFMuonsTagInfos
akCsSoftDropCh4PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akCsSoftDropCh4PFSoftPFMuonBJetTags = akCsSoftDropCh4PFbTagger.SoftPFMuonBJetTags
akCsSoftDropCh4PFSoftPFMuonByIP3dBJetTags = akCsSoftDropCh4PFbTagger.SoftPFMuonByIP3dBJetTags
akCsSoftDropCh4PFSoftPFMuonByPtBJetTags = akCsSoftDropCh4PFbTagger.SoftPFMuonByPtBJetTags
akCsSoftDropCh4PFNegativeSoftPFMuonByPtBJetTags = akCsSoftDropCh4PFbTagger.NegativeSoftPFMuonByPtBJetTags
akCsSoftDropCh4PFPositiveSoftPFMuonByPtBJetTags = akCsSoftDropCh4PFbTagger.PositiveSoftPFMuonByPtBJetTags
akCsSoftDropCh4PFPatJetFlavourIdLegacy = cms.Sequence(akCsSoftDropCh4PFPatJetPartonAssociationLegacy*akCsSoftDropCh4PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akCsSoftDropCh4PFPatJetFlavourAssociation = akCsSoftDropCh4PFbTagger.PatJetFlavourAssociation
#akCsSoftDropCh4PFPatJetFlavourId = cms.Sequence(akCsSoftDropCh4PFPatJetPartons*akCsSoftDropCh4PFPatJetFlavourAssociation)

akCsSoftDropCh4PFJetBtaggingIP       = cms.Sequence(akCsSoftDropCh4PFImpactParameterTagInfos *
            (akCsSoftDropCh4PFTrackCountingHighEffBJetTags +
             akCsSoftDropCh4PFTrackCountingHighPurBJetTags +
             akCsSoftDropCh4PFJetProbabilityBJetTags +
             akCsSoftDropCh4PFJetBProbabilityBJetTags 
            )
            )

akCsSoftDropCh4PFJetBtaggingSV = cms.Sequence(akCsSoftDropCh4PFImpactParameterTagInfos
            *
            akCsSoftDropCh4PFSecondaryVertexTagInfos
            * (akCsSoftDropCh4PFSimpleSecondaryVertexHighEffBJetTags+
                akCsSoftDropCh4PFSimpleSecondaryVertexHighPurBJetTags+
                akCsSoftDropCh4PFCombinedSecondaryVertexBJetTags+
                akCsSoftDropCh4PFCombinedSecondaryVertexV2BJetTags
              )
            )

akCsSoftDropCh4PFJetBtaggingNegSV = cms.Sequence(akCsSoftDropCh4PFImpactParameterTagInfos
            *
            akCsSoftDropCh4PFSecondaryVertexNegativeTagInfos
            * (akCsSoftDropCh4PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akCsSoftDropCh4PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akCsSoftDropCh4PFNegativeCombinedSecondaryVertexBJetTags+
                akCsSoftDropCh4PFPositiveCombinedSecondaryVertexBJetTags+
                akCsSoftDropCh4PFNegativeCombinedSecondaryVertexV2BJetTags+
                akCsSoftDropCh4PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akCsSoftDropCh4PFJetBtaggingMu = cms.Sequence(akCsSoftDropCh4PFSoftPFMuonsTagInfos * (akCsSoftDropCh4PFSoftPFMuonBJetTags
                +
                akCsSoftDropCh4PFSoftPFMuonByIP3dBJetTags
                +
                akCsSoftDropCh4PFSoftPFMuonByPtBJetTags
                +
                akCsSoftDropCh4PFNegativeSoftPFMuonByPtBJetTags
                +
                akCsSoftDropCh4PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akCsSoftDropCh4PFJetBtagging = cms.Sequence(akCsSoftDropCh4PFJetBtaggingIP
            *akCsSoftDropCh4PFJetBtaggingSV
            *akCsSoftDropCh4PFJetBtaggingNegSV
#            *akCsSoftDropCh4PFJetBtaggingMu
            )

akCsSoftDropCh4PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akCsSoftDropCh4PFJets"),
        genJetMatch          = cms.InputTag("akCsSoftDropCh4PFmatch"),
        genPartonMatch       = cms.InputTag("akCsSoftDropCh4PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akCsSoftDropCh4PFcorr")),
        JetPartonMapSource   = cms.InputTag("akCsSoftDropCh4PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akCsSoftDropCh4PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akCsSoftDropCh4PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akCsSoftDropCh4PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akCsSoftDropCh4PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akCsSoftDropCh4PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akCsSoftDropCh4PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akCsSoftDropCh4PFJetBProbabilityBJetTags"),
            cms.InputTag("akCsSoftDropCh4PFJetProbabilityBJetTags"),
            #cms.InputTag("akCsSoftDropCh4PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akCsSoftDropCh4PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akCsSoftDropCh4PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akCsSoftDropCh4PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akCsSoftDropCh4PFJetID"),
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

akCsSoftDropCh4PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akCsSoftDropCh4PFJets"),
           	    R0  = cms.double( 0.4)
)
akCsSoftDropCh4PFpatJetsWithBtagging.userData.userFloats.src += ['akCsSoftDropCh4PFNjettiness:tau1','akCsSoftDropCh4PFNjettiness:tau2','akCsSoftDropCh4PFNjettiness:tau3']

akCsSoftDropCh4PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akCsSoftDropCh4PFpatJetsWithBtagging"),
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
                                                             bTagJetName = cms.untracked.string("akCsSoftDropCh4PF"),
                                                             jetName = cms.untracked.string("akCsSoftDropCh4PF"),
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

akCsSoftDropCh4PFJetSequence_mc = cms.Sequence(
                                                  #akCsSoftDropCh4PFclean
                                                  #*
                                                  akCsSoftDropCh4PFmatch
                                                  #*
                                                  #akCsSoftDropCh4PFmatchGroomed
                                                  *
                                                  akCsSoftDropCh4PFparton
                                                  *
                                                  akCsSoftDropCh4PFcorr
                                                  *
                                                  #akCsSoftDropCh4PFJetID
                                                  #*
                                                  akCsSoftDropCh4PFPatJetFlavourIdLegacy
                                                  #*
			                          #akCsSoftDropCh4PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akCsSoftDropCh4PFJetTracksAssociatorAtVertex
                                                  *
                                                  akCsSoftDropCh4PFJetBtagging
                                                  *
                                                  akCsSoftDropCh4PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akCsSoftDropCh4PFpatJetsWithBtagging
                                                  *
                                                  akCsSoftDropCh4PFJetAnalyzer
                                                  )

akCsSoftDropCh4PFJetSequence_data = cms.Sequence(akCsSoftDropCh4PFcorr
                                                    *
                                                    #akCsSoftDropCh4PFJetID
                                                    #*
                                                    akCsSoftDropCh4PFJetTracksAssociatorAtVertex
                                                    *
                                                    akCsSoftDropCh4PFJetBtagging
                                                    *
                                                    akCsSoftDropCh4PFNjettiness 
                                                    *
                                                    akCsSoftDropCh4PFpatJetsWithBtagging
                                                    *
                                                    akCsSoftDropCh4PFJetAnalyzer
                                                    )

akCsSoftDropCh4PFJetSequence_jec = cms.Sequence(akCsSoftDropCh4PFJetSequence_mc)
akCsSoftDropCh4PFJetSequence_mb = cms.Sequence(akCsSoftDropCh4PFJetSequence_mc)

akCsSoftDropCh4PFJetSequence = cms.Sequence(akCsSoftDropCh4PFJetSequence_data)
akCsSoftDropCh4PFpatJetsWithBtagging.userData.userFloats.src += ['akCsSoftDropCh4PFJets:sym']
akCsSoftDropCh4PFpatJetsWithBtagging.userData.userInts.src += ['akCsSoftDropCh4PFJets:droppedBranches']
