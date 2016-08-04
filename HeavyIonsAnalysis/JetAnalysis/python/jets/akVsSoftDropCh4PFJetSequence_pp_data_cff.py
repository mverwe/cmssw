

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropCh4PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropCh4PFJets"),
    matched = cms.InputTag("ak4GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.4
    )

akVsSoftDropCh4PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh4GenJets"),
    matched = cms.InputTag("ak4GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.4
    )

akVsSoftDropCh4PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh4PFJets")
                                                        )

akVsSoftDropCh4PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropCh4PFJets"),
    payload = "AK4PF_offline"
    )

akVsSoftDropCh4PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropCh4CaloJets'))

#akVsSoftDropCh4PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak4GenJets'))

akVsSoftDropCh4PFbTagger = bTaggers("akVsSoftDropCh4PF",0.4)

#create objects locally since they dont load properly otherwise
#akVsSoftDropCh4PFmatch = akVsSoftDropCh4PFbTagger.match
akVsSoftDropCh4PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh4PFJets"), matched = cms.InputTag("genParticles"))
akVsSoftDropCh4PFPatJetFlavourAssociationLegacy = akVsSoftDropCh4PFbTagger.PatJetFlavourAssociationLegacy
akVsSoftDropCh4PFPatJetPartons = akVsSoftDropCh4PFbTagger.PatJetPartons
akVsSoftDropCh4PFJetTracksAssociatorAtVertex = akVsSoftDropCh4PFbTagger.JetTracksAssociatorAtVertex
akVsSoftDropCh4PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropCh4PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh4PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh4PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh4PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh4PFCombinedSecondaryVertexBJetTags = akVsSoftDropCh4PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh4PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh4PFbTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropCh4PFJetBProbabilityBJetTags = akVsSoftDropCh4PFbTagger.JetBProbabilityBJetTags
akVsSoftDropCh4PFSoftPFMuonByPtBJetTags = akVsSoftDropCh4PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh4PFSoftPFMuonByIP3dBJetTags = akVsSoftDropCh4PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh4PFTrackCountingHighEffBJetTags = akVsSoftDropCh4PFbTagger.TrackCountingHighEffBJetTags
akVsSoftDropCh4PFTrackCountingHighPurBJetTags = akVsSoftDropCh4PFbTagger.TrackCountingHighPurBJetTags
akVsSoftDropCh4PFPatJetPartonAssociationLegacy = akVsSoftDropCh4PFbTagger.PatJetPartonAssociationLegacy

akVsSoftDropCh4PFImpactParameterTagInfos = akVsSoftDropCh4PFbTagger.ImpactParameterTagInfos
akVsSoftDropCh4PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh4PFJetProbabilityBJetTags = akVsSoftDropCh4PFbTagger.JetProbabilityBJetTags

akVsSoftDropCh4PFSecondaryVertexTagInfos = akVsSoftDropCh4PFbTagger.SecondaryVertexTagInfos
akVsSoftDropCh4PFSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh4PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh4PFSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh4PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh4PFCombinedSecondaryVertexBJetTags = akVsSoftDropCh4PFbTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh4PFCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh4PFbTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropCh4PFSecondaryVertexNegativeTagInfos = akVsSoftDropCh4PFbTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropCh4PFNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh4PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh4PFNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh4PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh4PFNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropCh4PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropCh4PFPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropCh4PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropCh4PFNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh4PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropCh4PFPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh4PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropCh4PFSoftPFMuonsTagInfos = akVsSoftDropCh4PFbTagger.SoftPFMuonsTagInfos
akVsSoftDropCh4PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh4PFSoftPFMuonBJetTags = akVsSoftDropCh4PFbTagger.SoftPFMuonBJetTags
akVsSoftDropCh4PFSoftPFMuonByIP3dBJetTags = akVsSoftDropCh4PFbTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh4PFSoftPFMuonByPtBJetTags = akVsSoftDropCh4PFbTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh4PFNegativeSoftPFMuonByPtBJetTags = akVsSoftDropCh4PFbTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropCh4PFPositiveSoftPFMuonByPtBJetTags = akVsSoftDropCh4PFbTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropCh4PFPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropCh4PFPatJetPartonAssociationLegacy*akVsSoftDropCh4PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropCh4PFPatJetFlavourAssociation = akVsSoftDropCh4PFbTagger.PatJetFlavourAssociation
#akVsSoftDropCh4PFPatJetFlavourId = cms.Sequence(akVsSoftDropCh4PFPatJetPartons*akVsSoftDropCh4PFPatJetFlavourAssociation)

akVsSoftDropCh4PFJetBtaggingIP       = cms.Sequence(akVsSoftDropCh4PFImpactParameterTagInfos *
            (akVsSoftDropCh4PFTrackCountingHighEffBJetTags +
             akVsSoftDropCh4PFTrackCountingHighPurBJetTags +
             akVsSoftDropCh4PFJetProbabilityBJetTags +
             akVsSoftDropCh4PFJetBProbabilityBJetTags 
            )
            )

akVsSoftDropCh4PFJetBtaggingSV = cms.Sequence(akVsSoftDropCh4PFImpactParameterTagInfos
            *
            akVsSoftDropCh4PFSecondaryVertexTagInfos
            * (akVsSoftDropCh4PFSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh4PFSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh4PFCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh4PFCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh4PFJetBtaggingNegSV = cms.Sequence(akVsSoftDropCh4PFImpactParameterTagInfos
            *
            akVsSoftDropCh4PFSecondaryVertexNegativeTagInfos
            * (akVsSoftDropCh4PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh4PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh4PFNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh4PFPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh4PFNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropCh4PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh4PFJetBtaggingMu = cms.Sequence(akVsSoftDropCh4PFSoftPFMuonsTagInfos * (akVsSoftDropCh4PFSoftPFMuonBJetTags
                +
                akVsSoftDropCh4PFSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropCh4PFSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh4PFNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh4PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropCh4PFJetBtagging = cms.Sequence(akVsSoftDropCh4PFJetBtaggingIP
            *akVsSoftDropCh4PFJetBtaggingSV
            *akVsSoftDropCh4PFJetBtaggingNegSV
#            *akVsSoftDropCh4PFJetBtaggingMu
            )

akVsSoftDropCh4PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropCh4PFJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropCh4PFmatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropCh4PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropCh4PFcorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropCh4PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropCh4PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropCh4PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropCh4PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh4PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropCh4PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropCh4PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropCh4PFJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropCh4PFJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropCh4PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropCh4PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropCh4PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh4PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropCh4PFJetID"),
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

akVsSoftDropCh4PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropCh4PFJets"),
           	    R0  = cms.double( 0.4)
)
akVsSoftDropCh4PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh4PFNjettiness:tau1','akVsSoftDropCh4PFNjettiness:tau2','akVsSoftDropCh4PFNjettiness:tau3']

akVsSoftDropCh4PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropCh4PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak4GenJets',#'ak4GenJets',
                                                             rParam = 0.4,
                                                             matchJets = cms.untracked.bool(False),
                                                             matchTag = 'patJetsWithBtagging',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("generalTracks"),
                                                             fillGenJets = False,
                                                             isMC = False,
							     doSubEvent = False,
                                                             useHepMC = cms.untracked.bool(False),
							     genParticles = cms.untracked.InputTag("genParticles"),
							     eventInfoTag = cms.InputTag("generator"),
                                                             doLifeTimeTagging = cms.untracked.bool(True),
                                                             doLifeTimeTaggingExtras = cms.untracked.bool(False),
                                                             bTagJetName = cms.untracked.string("akVsSoftDropCh4PF"),
                                                             jetName = cms.untracked.string("akVsSoftDropCh4PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(False),
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

akVsSoftDropCh4PFJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropCh4PFclean
                                                  #*
                                                  akVsSoftDropCh4PFmatch
                                                  #*
                                                  #akVsSoftDropCh4PFmatchGroomed
                                                  *
                                                  akVsSoftDropCh4PFparton
                                                  *
                                                  akVsSoftDropCh4PFcorr
                                                  *
                                                  #akVsSoftDropCh4PFJetID
                                                  #*
                                                  akVsSoftDropCh4PFPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropCh4PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropCh4PFJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropCh4PFJetBtagging
                                                  *
                                                  akVsSoftDropCh4PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropCh4PFpatJetsWithBtagging
                                                  *
                                                  akVsSoftDropCh4PFJetAnalyzer
                                                  )

akVsSoftDropCh4PFJetSequence_data = cms.Sequence(akVsSoftDropCh4PFcorr
                                                    *
                                                    #akVsSoftDropCh4PFJetID
                                                    #*
                                                    akVsSoftDropCh4PFJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropCh4PFJetBtagging
                                                    *
                                                    akVsSoftDropCh4PFNjettiness 
                                                    *
                                                    akVsSoftDropCh4PFpatJetsWithBtagging
                                                    *
                                                    akVsSoftDropCh4PFJetAnalyzer
                                                    )

akVsSoftDropCh4PFJetSequence_jec = cms.Sequence(akVsSoftDropCh4PFJetSequence_mc)
akVsSoftDropCh4PFJetSequence_mb = cms.Sequence(akVsSoftDropCh4PFJetSequence_mc)

akVsSoftDropCh4PFJetSequence = cms.Sequence(akVsSoftDropCh4PFJetSequence_data)
akVsSoftDropCh4PFpatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh4PFJets:sym']
akVsSoftDropCh4PFpatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropCh4PFJets:droppedBranches']
