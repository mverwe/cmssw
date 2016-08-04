

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akCsSoftDropCh6PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akCsSoftDropCh6PFJets"),
    matched = cms.InputTag("ak6HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.6
    )

akCsSoftDropCh6PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh6HiGenJets"),
    matched = cms.InputTag("ak6HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.6
    )

akCsSoftDropCh6PFparton = patJetPartonMatch.clone(src = cms.InputTag("akCsSoftDropCh6PFJets")
                                                        )

akCsSoftDropCh6PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akCsSoftDropCh6PFJets"),
    payload = "AK6PF_offline"
    )

akCsSoftDropCh6PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akCsSoftDropCh6CaloJets'))

#akCsSoftDropCh6PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak6HiSignalGenJets'))

akCsSoftDropCh6PFbTagger = bTaggers("akCsSoftDropCh6PF",0.6)

#create objects locally since they dont load properly otherwise
#akCsSoftDropCh6PFmatch = akCsSoftDropCh6PFbTagger.match
akCsSoftDropCh6PFparton = patJetPartonMatch.clone(src = cms.InputTag("akCsSoftDropCh6PFJets"), matched = cms.InputTag("hiSignalGenParticles"))
akCsSoftDropCh6PFPatJetFlavourAssociationLegacy = akCsSoftDropCh6PFbTagger.PatJetFlavourAssociationLegacy
akCsSoftDropCh6PFPatJetPartons = akCsSoftDropCh6PFbTagger.PatJetPartons
akCsSoftDropCh6PFJetTracksAssociatorAtVertex = akCsSoftDropCh6PFbTagger.JetTracksAssociatorAtVertex
akCsSoftDropCh6PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akCsSoftDropCh6PFSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropCh6PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akCsSoftDropCh6PFSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropCh6PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akCsSoftDropCh6PFCombinedSecondaryVertexBJetTags = akCsSoftDropCh6PFbTagger.CombinedSecondaryVertexBJetTags
akCsSoftDropCh6PFCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh6PFbTagger.CombinedSecondaryVertexV2BJetTags
akCsSoftDropCh6PFJetBProbabilityBJetTags = akCsSoftDropCh6PFbTagger.JetBProbabilityBJetTags
akCsSoftDropCh6PFSoftPFMuonByPtBJetTags = akCsSoftDropCh6PFbTagger.SoftPFMuonByPtBJetTags
akCsSoftDropCh6PFSoftPFMuonByIP3dBJetTags = akCsSoftDropCh6PFbTagger.SoftPFMuonByIP3dBJetTags
akCsSoftDropCh6PFTrackCountingHighEffBJetTags = akCsSoftDropCh6PFbTagger.TrackCountingHighEffBJetTags
akCsSoftDropCh6PFTrackCountingHighPurBJetTags = akCsSoftDropCh6PFbTagger.TrackCountingHighPurBJetTags
akCsSoftDropCh6PFPatJetPartonAssociationLegacy = akCsSoftDropCh6PFbTagger.PatJetPartonAssociationLegacy

akCsSoftDropCh6PFImpactParameterTagInfos = akCsSoftDropCh6PFbTagger.ImpactParameterTagInfos
akCsSoftDropCh6PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akCsSoftDropCh6PFJetProbabilityBJetTags = akCsSoftDropCh6PFbTagger.JetProbabilityBJetTags

akCsSoftDropCh6PFSecondaryVertexTagInfos = akCsSoftDropCh6PFbTagger.SecondaryVertexTagInfos
akCsSoftDropCh6PFSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropCh6PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akCsSoftDropCh6PFSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropCh6PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akCsSoftDropCh6PFCombinedSecondaryVertexBJetTags = akCsSoftDropCh6PFbTagger.CombinedSecondaryVertexBJetTags
akCsSoftDropCh6PFCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh6PFbTagger.CombinedSecondaryVertexV2BJetTags

akCsSoftDropCh6PFSecondaryVertexNegativeTagInfos = akCsSoftDropCh6PFbTagger.SecondaryVertexNegativeTagInfos
akCsSoftDropCh6PFNegativeSimpleSecondaryVertexHighEffBJetTags = akCsSoftDropCh6PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akCsSoftDropCh6PFNegativeSimpleSecondaryVertexHighPurBJetTags = akCsSoftDropCh6PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akCsSoftDropCh6PFNegativeCombinedSecondaryVertexBJetTags = akCsSoftDropCh6PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akCsSoftDropCh6PFPositiveCombinedSecondaryVertexBJetTags = akCsSoftDropCh6PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akCsSoftDropCh6PFNegativeCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh6PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akCsSoftDropCh6PFPositiveCombinedSecondaryVertexV2BJetTags = akCsSoftDropCh6PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akCsSoftDropCh6PFSoftPFMuonsTagInfos = akCsSoftDropCh6PFbTagger.SoftPFMuonsTagInfos
akCsSoftDropCh6PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akCsSoftDropCh6PFSoftPFMuonBJetTags = akCsSoftDropCh6PFbTagger.SoftPFMuonBJetTags
akCsSoftDropCh6PFSoftPFMuonByIP3dBJetTags = akCsSoftDropCh6PFbTagger.SoftPFMuonByIP3dBJetTags
akCsSoftDropCh6PFSoftPFMuonByPtBJetTags = akCsSoftDropCh6PFbTagger.SoftPFMuonByPtBJetTags
akCsSoftDropCh6PFNegativeSoftPFMuonByPtBJetTags = akCsSoftDropCh6PFbTagger.NegativeSoftPFMuonByPtBJetTags
akCsSoftDropCh6PFPositiveSoftPFMuonByPtBJetTags = akCsSoftDropCh6PFbTagger.PositiveSoftPFMuonByPtBJetTags
akCsSoftDropCh6PFPatJetFlavourIdLegacy = cms.Sequence(akCsSoftDropCh6PFPatJetPartonAssociationLegacy*akCsSoftDropCh6PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akCsSoftDropCh6PFPatJetFlavourAssociation = akCsSoftDropCh6PFbTagger.PatJetFlavourAssociation
#akCsSoftDropCh6PFPatJetFlavourId = cms.Sequence(akCsSoftDropCh6PFPatJetPartons*akCsSoftDropCh6PFPatJetFlavourAssociation)

akCsSoftDropCh6PFJetBtaggingIP       = cms.Sequence(akCsSoftDropCh6PFImpactParameterTagInfos *
            (akCsSoftDropCh6PFTrackCountingHighEffBJetTags +
             akCsSoftDropCh6PFTrackCountingHighPurBJetTags +
             akCsSoftDropCh6PFJetProbabilityBJetTags +
             akCsSoftDropCh6PFJetBProbabilityBJetTags 
            )
            )

akCsSoftDropCh6PFJetBtaggingSV = cms.Sequence(akCsSoftDropCh6PFImpactParameterTagInfos
            *
            akCsSoftDropCh6PFSecondaryVertexTagInfos
            * (akCsSoftDropCh6PFSimpleSecondaryVertexHighEffBJetTags+
                akCsSoftDropCh6PFSimpleSecondaryVertexHighPurBJetTags+
                akCsSoftDropCh6PFCombinedSecondaryVertexBJetTags+
                akCsSoftDropCh6PFCombinedSecondaryVertexV2BJetTags
              )
            )

akCsSoftDropCh6PFJetBtaggingNegSV = cms.Sequence(akCsSoftDropCh6PFImpactParameterTagInfos
            *
            akCsSoftDropCh6PFSecondaryVertexNegativeTagInfos
            * (akCsSoftDropCh6PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akCsSoftDropCh6PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akCsSoftDropCh6PFNegativeCombinedSecondaryVertexBJetTags+
                akCsSoftDropCh6PFPositiveCombinedSecondaryVertexBJetTags+
                akCsSoftDropCh6PFNegativeCombinedSecondaryVertexV2BJetTags+
                akCsSoftDropCh6PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akCsSoftDropCh6PFJetBtaggingMu = cms.Sequence(akCsSoftDropCh6PFSoftPFMuonsTagInfos * (akCsSoftDropCh6PFSoftPFMuonBJetTags
                +
                akCsSoftDropCh6PFSoftPFMuonByIP3dBJetTags
                +
                akCsSoftDropCh6PFSoftPFMuonByPtBJetTags
                +
                akCsSoftDropCh6PFNegativeSoftPFMuonByPtBJetTags
                +
                akCsSoftDropCh6PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akCsSoftDropCh6PFJetBtagging = cms.Sequence(akCsSoftDropCh6PFJetBtaggingIP
            *akCsSoftDropCh6PFJetBtaggingSV
            *akCsSoftDropCh6PFJetBtaggingNegSV
#            *akCsSoftDropCh6PFJetBtaggingMu
            )

akCsSoftDropCh6PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akCsSoftDropCh6PFJets"),
        genJetMatch          = cms.InputTag("akCsSoftDropCh6PFmatch"),
        genPartonMatch       = cms.InputTag("akCsSoftDropCh6PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akCsSoftDropCh6PFcorr")),
        JetPartonMapSource   = cms.InputTag("akCsSoftDropCh6PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akCsSoftDropCh6PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akCsSoftDropCh6PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akCsSoftDropCh6PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akCsSoftDropCh6PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akCsSoftDropCh6PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akCsSoftDropCh6PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akCsSoftDropCh6PFJetBProbabilityBJetTags"),
            cms.InputTag("akCsSoftDropCh6PFJetProbabilityBJetTags"),
            #cms.InputTag("akCsSoftDropCh6PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akCsSoftDropCh6PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akCsSoftDropCh6PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akCsSoftDropCh6PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akCsSoftDropCh6PFJetID"),
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

akCsSoftDropCh6PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akCsSoftDropCh6PFJets"),
           	    R0  = cms.double( 0.6)
)
akCsSoftDropCh6PFpatJetsWithBtagging.userData.userFloats.src += ['akCsSoftDropCh6PFNjettiness:tau1','akCsSoftDropCh6PFNjettiness:tau2','akCsSoftDropCh6PFNjettiness:tau3']

akCsSoftDropCh6PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akCsSoftDropCh6PFpatJetsWithBtagging"),
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
                                                             bTagJetName = cms.untracked.string("akCsSoftDropCh6PF"),
                                                             jetName = cms.untracked.string("akCsSoftDropCh6PF"),
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

akCsSoftDropCh6PFJetSequence_mc = cms.Sequence(
                                                  #akCsSoftDropCh6PFclean
                                                  #*
                                                  akCsSoftDropCh6PFmatch
                                                  #*
                                                  #akCsSoftDropCh6PFmatchGroomed
                                                  *
                                                  akCsSoftDropCh6PFparton
                                                  *
                                                  akCsSoftDropCh6PFcorr
                                                  *
                                                  #akCsSoftDropCh6PFJetID
                                                  #*
                                                  akCsSoftDropCh6PFPatJetFlavourIdLegacy
                                                  #*
			                          #akCsSoftDropCh6PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akCsSoftDropCh6PFJetTracksAssociatorAtVertex
                                                  *
                                                  akCsSoftDropCh6PFJetBtagging
                                                  *
                                                  akCsSoftDropCh6PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akCsSoftDropCh6PFpatJetsWithBtagging
                                                  *
                                                  akCsSoftDropCh6PFJetAnalyzer
                                                  )

akCsSoftDropCh6PFJetSequence_data = cms.Sequence(akCsSoftDropCh6PFcorr
                                                    *
                                                    #akCsSoftDropCh6PFJetID
                                                    #*
                                                    akCsSoftDropCh6PFJetTracksAssociatorAtVertex
                                                    *
                                                    akCsSoftDropCh6PFJetBtagging
                                                    *
                                                    akCsSoftDropCh6PFNjettiness 
                                                    *
                                                    akCsSoftDropCh6PFpatJetsWithBtagging
                                                    *
                                                    akCsSoftDropCh6PFJetAnalyzer
                                                    )

akCsSoftDropCh6PFJetSequence_jec = cms.Sequence(akCsSoftDropCh6PFJetSequence_mc)
akCsSoftDropCh6PFJetSequence_mb = cms.Sequence(akCsSoftDropCh6PFJetSequence_mc)

akCsSoftDropCh6PFJetSequence = cms.Sequence(akCsSoftDropCh6PFJetSequence_mc)
akCsSoftDropCh6PFpatJetsWithBtagging.userData.userFloats.src += ['akCsSoftDropCh6PFJets:sym']
akCsSoftDropCh6PFpatJetsWithBtagging.userData.userInts.src += ['akCsSoftDropCh6PFJets:droppedBranches']
