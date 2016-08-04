

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVs1PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs1PFJets"),
    matched = cms.InputTag("ak1GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akVs1PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak1GenJets"),
    matched = cms.InputTag("ak1GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akVs1PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVs1PFJets")
                                                        )

akVs1PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVs1PFJets"),
    payload = "AK1PF_offline"
    )

akVs1PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVs1CaloJets'))

#akVs1PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak1GenJets'))

akVs1PFbTagger = bTaggers("akVs1PF",0.1)

#create objects locally since they dont load properly otherwise
#akVs1PFmatch = akVs1PFbTagger.match
akVs1PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVs1PFJets"), matched = cms.InputTag("genParticles"))
akVs1PFPatJetFlavourAssociationLegacy = akVs1PFbTagger.PatJetFlavourAssociationLegacy
akVs1PFPatJetPartons = akVs1PFbTagger.PatJetPartons
akVs1PFJetTracksAssociatorAtVertex = akVs1PFbTagger.JetTracksAssociatorAtVertex
akVs1PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVs1PFSimpleSecondaryVertexHighEffBJetTags = akVs1PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVs1PFSimpleSecondaryVertexHighPurBJetTags = akVs1PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVs1PFCombinedSecondaryVertexBJetTags = akVs1PFbTagger.CombinedSecondaryVertexBJetTags
akVs1PFCombinedSecondaryVertexV2BJetTags = akVs1PFbTagger.CombinedSecondaryVertexV2BJetTags
akVs1PFJetBProbabilityBJetTags = akVs1PFbTagger.JetBProbabilityBJetTags
akVs1PFSoftPFMuonByPtBJetTags = akVs1PFbTagger.SoftPFMuonByPtBJetTags
akVs1PFSoftPFMuonByIP3dBJetTags = akVs1PFbTagger.SoftPFMuonByIP3dBJetTags
akVs1PFTrackCountingHighEffBJetTags = akVs1PFbTagger.TrackCountingHighEffBJetTags
akVs1PFTrackCountingHighPurBJetTags = akVs1PFbTagger.TrackCountingHighPurBJetTags
akVs1PFPatJetPartonAssociationLegacy = akVs1PFbTagger.PatJetPartonAssociationLegacy

akVs1PFImpactParameterTagInfos = akVs1PFbTagger.ImpactParameterTagInfos
akVs1PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVs1PFJetProbabilityBJetTags = akVs1PFbTagger.JetProbabilityBJetTags

akVs1PFSecondaryVertexTagInfos = akVs1PFbTagger.SecondaryVertexTagInfos
akVs1PFSimpleSecondaryVertexHighEffBJetTags = akVs1PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akVs1PFSimpleSecondaryVertexHighPurBJetTags = akVs1PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akVs1PFCombinedSecondaryVertexBJetTags = akVs1PFbTagger.CombinedSecondaryVertexBJetTags
akVs1PFCombinedSecondaryVertexV2BJetTags = akVs1PFbTagger.CombinedSecondaryVertexV2BJetTags

akVs1PFSecondaryVertexNegativeTagInfos = akVs1PFbTagger.SecondaryVertexNegativeTagInfos
akVs1PFNegativeSimpleSecondaryVertexHighEffBJetTags = akVs1PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVs1PFNegativeSimpleSecondaryVertexHighPurBJetTags = akVs1PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVs1PFNegativeCombinedSecondaryVertexBJetTags = akVs1PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akVs1PFPositiveCombinedSecondaryVertexBJetTags = akVs1PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akVs1PFNegativeCombinedSecondaryVertexV2BJetTags = akVs1PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVs1PFPositiveCombinedSecondaryVertexV2BJetTags = akVs1PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVs1PFSoftPFMuonsTagInfos = akVs1PFbTagger.SoftPFMuonsTagInfos
akVs1PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVs1PFSoftPFMuonBJetTags = akVs1PFbTagger.SoftPFMuonBJetTags
akVs1PFSoftPFMuonByIP3dBJetTags = akVs1PFbTagger.SoftPFMuonByIP3dBJetTags
akVs1PFSoftPFMuonByPtBJetTags = akVs1PFbTagger.SoftPFMuonByPtBJetTags
akVs1PFNegativeSoftPFMuonByPtBJetTags = akVs1PFbTagger.NegativeSoftPFMuonByPtBJetTags
akVs1PFPositiveSoftPFMuonByPtBJetTags = akVs1PFbTagger.PositiveSoftPFMuonByPtBJetTags
akVs1PFPatJetFlavourIdLegacy = cms.Sequence(akVs1PFPatJetPartonAssociationLegacy*akVs1PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVs1PFPatJetFlavourAssociation = akVs1PFbTagger.PatJetFlavourAssociation
#akVs1PFPatJetFlavourId = cms.Sequence(akVs1PFPatJetPartons*akVs1PFPatJetFlavourAssociation)

akVs1PFJetBtaggingIP       = cms.Sequence(akVs1PFImpactParameterTagInfos *
            (akVs1PFTrackCountingHighEffBJetTags +
             akVs1PFTrackCountingHighPurBJetTags +
             akVs1PFJetProbabilityBJetTags +
             akVs1PFJetBProbabilityBJetTags 
            )
            )

akVs1PFJetBtaggingSV = cms.Sequence(akVs1PFImpactParameterTagInfos
            *
            akVs1PFSecondaryVertexTagInfos
            * (akVs1PFSimpleSecondaryVertexHighEffBJetTags+
                akVs1PFSimpleSecondaryVertexHighPurBJetTags+
                akVs1PFCombinedSecondaryVertexBJetTags+
                akVs1PFCombinedSecondaryVertexV2BJetTags
              )
            )

akVs1PFJetBtaggingNegSV = cms.Sequence(akVs1PFImpactParameterTagInfos
            *
            akVs1PFSecondaryVertexNegativeTagInfos
            * (akVs1PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVs1PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVs1PFNegativeCombinedSecondaryVertexBJetTags+
                akVs1PFPositiveCombinedSecondaryVertexBJetTags+
                akVs1PFNegativeCombinedSecondaryVertexV2BJetTags+
                akVs1PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVs1PFJetBtaggingMu = cms.Sequence(akVs1PFSoftPFMuonsTagInfos * (akVs1PFSoftPFMuonBJetTags
                +
                akVs1PFSoftPFMuonByIP3dBJetTags
                +
                akVs1PFSoftPFMuonByPtBJetTags
                +
                akVs1PFNegativeSoftPFMuonByPtBJetTags
                +
                akVs1PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akVs1PFJetBtagging = cms.Sequence(akVs1PFJetBtaggingIP
            *akVs1PFJetBtaggingSV
            *akVs1PFJetBtaggingNegSV
#            *akVs1PFJetBtaggingMu
            )

akVs1PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVs1PFJets"),
        genJetMatch          = cms.InputTag("akVs1PFmatch"),
        genPartonMatch       = cms.InputTag("akVs1PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs1PFcorr")),
        JetPartonMapSource   = cms.InputTag("akVs1PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVs1PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVs1PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVs1PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVs1PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVs1PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVs1PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVs1PFJetBProbabilityBJetTags"),
            cms.InputTag("akVs1PFJetProbabilityBJetTags"),
            #cms.InputTag("akVs1PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVs1PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVs1PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akVs1PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVs1PFJetID"),
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

akVs1PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVs1PFJets"),
           	    R0  = cms.double( 0.1)
)
akVs1PFpatJetsWithBtagging.userData.userFloats.src += ['akVs1PFNjettiness:tau1','akVs1PFNjettiness:tau2','akVs1PFNjettiness:tau3']

akVs1PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs1PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak1GenJets',#'ak1GenJets',
                                                             rParam = 0.1,
                                                             matchJets = cms.untracked.bool(False),
                                                             matchTag = 'patJetsWithBtagging',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("generalTracks"),
                                                             fillGenJets = True,
                                                             isMC = True,
							     doSubEvent = True,
                                                             useHepMC = cms.untracked.bool(False),
							     genParticles = cms.untracked.InputTag("genParticles"),
							     eventInfoTag = cms.InputTag("generator"),
                                                             doLifeTimeTagging = cms.untracked.bool(True),
                                                             doLifeTimeTaggingExtras = cms.untracked.bool(False),
                                                             bTagJetName = cms.untracked.string("akVs1PF"),
                                                             jetName = cms.untracked.string("akVs1PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(False),
							     doSubJets = cms.untracked.bool(False),
                                                             doGenSubJets = cms.untracked.bool(False),     
                                                             subjetGenTag = cms.untracked.InputTag("ak1GenJets"),
                                                             doGenTaus = True,
                                                             genTau1 = cms.InputTag("ak1GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("ak1GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("ak1GenNjettiness","tau3"),
                                                             doGenSym = False,
                                                             genSym = cms.InputTag("ak1GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("ak1GenJets","droppedBranches")
                                                             )

akVs1PFJetSequence_mc = cms.Sequence(
                                                  #akVs1PFclean
                                                  #*
                                                  akVs1PFmatch
                                                  #*
                                                  #akVs1PFmatchGroomed
                                                  *
                                                  akVs1PFparton
                                                  *
                                                  akVs1PFcorr
                                                  *
                                                  #akVs1PFJetID
                                                  #*
                                                  akVs1PFPatJetFlavourIdLegacy
                                                  #*
			                          #akVs1PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVs1PFJetTracksAssociatorAtVertex
                                                  *
                                                  akVs1PFJetBtagging
                                                  *
                                                  akVs1PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVs1PFpatJetsWithBtagging
                                                  *
                                                  akVs1PFJetAnalyzer
                                                  )

akVs1PFJetSequence_data = cms.Sequence(akVs1PFcorr
                                                    *
                                                    #akVs1PFJetID
                                                    #*
                                                    akVs1PFJetTracksAssociatorAtVertex
                                                    *
                                                    akVs1PFJetBtagging
                                                    *
                                                    akVs1PFNjettiness 
                                                    *
                                                    akVs1PFpatJetsWithBtagging
                                                    *
                                                    akVs1PFJetAnalyzer
                                                    )

akVs1PFJetSequence_jec = cms.Sequence(akVs1PFJetSequence_mc)
akVs1PFJetSequence_mb = cms.Sequence(akVs1PFJetSequence_mc)

akVs1PFJetSequence = cms.Sequence(akVs1PFJetSequence_jec)
akVs1PFJetAnalyzer.genPtMin = cms.untracked.double(1)
akVs1PFJetAnalyzer.jetPtMin = cms.double(1)
