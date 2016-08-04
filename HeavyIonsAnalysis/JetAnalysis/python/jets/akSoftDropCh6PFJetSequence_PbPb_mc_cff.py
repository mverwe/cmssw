

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDropCh6PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh6PFJets"),
    matched = cms.InputTag("ak6HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.6
    )

akSoftDropCh6PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh6HiGenJets"),
    matched = cms.InputTag("ak6HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.6
    )

akSoftDropCh6PFparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh6PFJets")
                                                        )

akSoftDropCh6PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akSoftDropCh6PFJets"),
    payload = "AK6PF_offline"
    )

akSoftDropCh6PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akSoftDropCh6CaloJets'))

#akSoftDropCh6PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak6HiSignalGenJets'))

akSoftDropCh6PFbTagger = bTaggers("akSoftDropCh6PF",0.6)

#create objects locally since they dont load properly otherwise
#akSoftDropCh6PFmatch = akSoftDropCh6PFbTagger.match
akSoftDropCh6PFparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh6PFJets"), matched = cms.InputTag("hiSignalGenParticles"))
akSoftDropCh6PFPatJetFlavourAssociationLegacy = akSoftDropCh6PFbTagger.PatJetFlavourAssociationLegacy
akSoftDropCh6PFPatJetPartons = akSoftDropCh6PFbTagger.PatJetPartons
akSoftDropCh6PFJetTracksAssociatorAtVertex = akSoftDropCh6PFbTagger.JetTracksAssociatorAtVertex
akSoftDropCh6PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDropCh6PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh6PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh6PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh6PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh6PFCombinedSecondaryVertexBJetTags = akSoftDropCh6PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh6PFCombinedSecondaryVertexV2BJetTags = akSoftDropCh6PFbTagger.CombinedSecondaryVertexV2BJetTags
akSoftDropCh6PFJetBProbabilityBJetTags = akSoftDropCh6PFbTagger.JetBProbabilityBJetTags
akSoftDropCh6PFSoftPFMuonByPtBJetTags = akSoftDropCh6PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropCh6PFSoftPFMuonByIP3dBJetTags = akSoftDropCh6PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh6PFTrackCountingHighEffBJetTags = akSoftDropCh6PFbTagger.TrackCountingHighEffBJetTags
akSoftDropCh6PFTrackCountingHighPurBJetTags = akSoftDropCh6PFbTagger.TrackCountingHighPurBJetTags
akSoftDropCh6PFPatJetPartonAssociationLegacy = akSoftDropCh6PFbTagger.PatJetPartonAssociationLegacy

akSoftDropCh6PFImpactParameterTagInfos = akSoftDropCh6PFbTagger.ImpactParameterTagInfos
akSoftDropCh6PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh6PFJetProbabilityBJetTags = akSoftDropCh6PFbTagger.JetProbabilityBJetTags

akSoftDropCh6PFSecondaryVertexTagInfos = akSoftDropCh6PFbTagger.SecondaryVertexTagInfos
akSoftDropCh6PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh6PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh6PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh6PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh6PFCombinedSecondaryVertexBJetTags = akSoftDropCh6PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh6PFCombinedSecondaryVertexV2BJetTags = akSoftDropCh6PFbTagger.CombinedSecondaryVertexV2BJetTags

akSoftDropCh6PFSecondaryVertexNegativeTagInfos = akSoftDropCh6PFbTagger.SecondaryVertexNegativeTagInfos
akSoftDropCh6PFNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh6PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDropCh6PFNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh6PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDropCh6PFNegativeCombinedSecondaryVertexBJetTags = akSoftDropCh6PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDropCh6PFPositiveCombinedSecondaryVertexBJetTags = akSoftDropCh6PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDropCh6PFNegativeCombinedSecondaryVertexV2BJetTags = akSoftDropCh6PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDropCh6PFPositiveCombinedSecondaryVertexV2BJetTags = akSoftDropCh6PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDropCh6PFSoftPFMuonsTagInfos = akSoftDropCh6PFbTagger.SoftPFMuonsTagInfos
akSoftDropCh6PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh6PFSoftPFMuonBJetTags = akSoftDropCh6PFbTagger.SoftPFMuonBJetTags
akSoftDropCh6PFSoftPFMuonByIP3dBJetTags = akSoftDropCh6PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh6PFSoftPFMuonByPtBJetTags = akSoftDropCh6PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropCh6PFNegativeSoftPFMuonByPtBJetTags = akSoftDropCh6PFbTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDropCh6PFPositiveSoftPFMuonByPtBJetTags = akSoftDropCh6PFbTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDropCh6PFPatJetFlavourIdLegacy = cms.Sequence(akSoftDropCh6PFPatJetPartonAssociationLegacy*akSoftDropCh6PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akSoftDropCh6PFPatJetFlavourAssociation = akSoftDropCh6PFbTagger.PatJetFlavourAssociation
#akSoftDropCh6PFPatJetFlavourId = cms.Sequence(akSoftDropCh6PFPatJetPartons*akSoftDropCh6PFPatJetFlavourAssociation)

akSoftDropCh6PFJetBtaggingIP       = cms.Sequence(akSoftDropCh6PFImpactParameterTagInfos *
            (akSoftDropCh6PFTrackCountingHighEffBJetTags +
             akSoftDropCh6PFTrackCountingHighPurBJetTags +
             akSoftDropCh6PFJetProbabilityBJetTags +
             akSoftDropCh6PFJetBProbabilityBJetTags 
            )
            )

akSoftDropCh6PFJetBtaggingSV = cms.Sequence(akSoftDropCh6PFImpactParameterTagInfos
            *
            akSoftDropCh6PFSecondaryVertexTagInfos
            * (akSoftDropCh6PFSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh6PFSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh6PFCombinedSecondaryVertexBJetTags+
                akSoftDropCh6PFCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh6PFJetBtaggingNegSV = cms.Sequence(akSoftDropCh6PFImpactParameterTagInfos
            *
            akSoftDropCh6PFSecondaryVertexNegativeTagInfos
            * (akSoftDropCh6PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh6PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh6PFNegativeCombinedSecondaryVertexBJetTags+
                akSoftDropCh6PFPositiveCombinedSecondaryVertexBJetTags+
                akSoftDropCh6PFNegativeCombinedSecondaryVertexV2BJetTags+
                akSoftDropCh6PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh6PFJetBtaggingMu = cms.Sequence(akSoftDropCh6PFSoftPFMuonsTagInfos * (akSoftDropCh6PFSoftPFMuonBJetTags
                +
                akSoftDropCh6PFSoftPFMuonByIP3dBJetTags
                +
                akSoftDropCh6PFSoftPFMuonByPtBJetTags
                +
                akSoftDropCh6PFNegativeSoftPFMuonByPtBJetTags
                +
                akSoftDropCh6PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akSoftDropCh6PFJetBtagging = cms.Sequence(akSoftDropCh6PFJetBtaggingIP
            *akSoftDropCh6PFJetBtaggingSV
            *akSoftDropCh6PFJetBtaggingNegSV
#            *akSoftDropCh6PFJetBtaggingMu
            )

akSoftDropCh6PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akSoftDropCh6PFJets"),
        genJetMatch          = cms.InputTag("akSoftDropCh6PFmatch"),
        genPartonMatch       = cms.InputTag("akSoftDropCh6PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akSoftDropCh6PFcorr")),
        JetPartonMapSource   = cms.InputTag("akSoftDropCh6PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akSoftDropCh6PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akSoftDropCh6PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akSoftDropCh6PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akSoftDropCh6PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akSoftDropCh6PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akSoftDropCh6PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akSoftDropCh6PFJetBProbabilityBJetTags"),
            cms.InputTag("akSoftDropCh6PFJetProbabilityBJetTags"),
            #cms.InputTag("akSoftDropCh6PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akSoftDropCh6PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akSoftDropCh6PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akSoftDropCh6PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akSoftDropCh6PFJetID"),
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

akSoftDropCh6PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akSoftDropCh6PFJets"),
           	    R0  = cms.double( 0.6)
)
akSoftDropCh6PFpatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh6PFNjettiness:tau1','akSoftDropCh6PFNjettiness:tau2','akSoftDropCh6PFNjettiness:tau3']

akSoftDropCh6PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akSoftDropCh6PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak6HiSignalGenJets',#'ak6HiGenJets',
                                                             rParam = 0.6,
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
                                                             bTagJetName = cms.untracked.string("akSoftDropCh6PF"),
                                                             jetName = cms.untracked.string("akSoftDropCh6PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropCh6GenJets"),
                                                             doGenTaus = False,
                                                             genTau1 = cms.InputTag("akSoftDropCh6GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropCh6GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropCh6GenNjettiness","tau3"),
                                                             doGenSym = True,
                                                             genSym = cms.InputTag("akSoftDropCh6GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropCh6GenJets","droppedBranches")
                                                             )

akSoftDropCh6PFJetSequence_mc = cms.Sequence(
                                                  #akSoftDropCh6PFclean
                                                  #*
                                                  akSoftDropCh6PFmatch
                                                  #*
                                                  #akSoftDropCh6PFmatchGroomed
                                                  *
                                                  akSoftDropCh6PFparton
                                                  *
                                                  akSoftDropCh6PFcorr
                                                  *
                                                  #akSoftDropCh6PFJetID
                                                  #*
                                                  akSoftDropCh6PFPatJetFlavourIdLegacy
                                                  #*
			                          #akSoftDropCh6PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akSoftDropCh6PFJetTracksAssociatorAtVertex
                                                  *
                                                  akSoftDropCh6PFJetBtagging
                                                  *
                                                  akSoftDropCh6PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akSoftDropCh6PFpatJetsWithBtagging
                                                  *
                                                  akSoftDropCh6PFJetAnalyzer
                                                  )

akSoftDropCh6PFJetSequence_data = cms.Sequence(akSoftDropCh6PFcorr
                                                    *
                                                    #akSoftDropCh6PFJetID
                                                    #*
                                                    akSoftDropCh6PFJetTracksAssociatorAtVertex
                                                    *
                                                    akSoftDropCh6PFJetBtagging
                                                    *
                                                    akSoftDropCh6PFNjettiness 
                                                    *
                                                    akSoftDropCh6PFpatJetsWithBtagging
                                                    *
                                                    akSoftDropCh6PFJetAnalyzer
                                                    )

akSoftDropCh6PFJetSequence_jec = cms.Sequence(akSoftDropCh6PFJetSequence_mc)
akSoftDropCh6PFJetSequence_mb = cms.Sequence(akSoftDropCh6PFJetSequence_mc)

akSoftDropCh6PFJetSequence = cms.Sequence(akSoftDropCh6PFJetSequence_mc)
akSoftDropCh6PFpatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh6PFJets:sym']
akSoftDropCh6PFpatJetsWithBtagging.userData.userInts.src += ['akSoftDropCh6PFJets:droppedBranches']
