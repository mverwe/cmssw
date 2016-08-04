

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDropCh4PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh4PFJets"),
    matched = cms.InputTag("ak4GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.4
    )

akSoftDropCh4PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh4GenJets"),
    matched = cms.InputTag("ak4GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.4
    )

akSoftDropCh4PFparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh4PFJets")
                                                        )

akSoftDropCh4PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akSoftDropCh4PFJets"),
    payload = "AK4PF_offline"
    )

akSoftDropCh4PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akSoftDropCh4CaloJets'))

#akSoftDropCh4PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak4GenJets'))

akSoftDropCh4PFbTagger = bTaggers("akSoftDropCh4PF",0.4)

#create objects locally since they dont load properly otherwise
#akSoftDropCh4PFmatch = akSoftDropCh4PFbTagger.match
akSoftDropCh4PFparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh4PFJets"), matched = cms.InputTag("genParticles"))
akSoftDropCh4PFPatJetFlavourAssociationLegacy = akSoftDropCh4PFbTagger.PatJetFlavourAssociationLegacy
akSoftDropCh4PFPatJetPartons = akSoftDropCh4PFbTagger.PatJetPartons
akSoftDropCh4PFJetTracksAssociatorAtVertex = akSoftDropCh4PFbTagger.JetTracksAssociatorAtVertex
akSoftDropCh4PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDropCh4PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh4PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh4PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh4PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh4PFCombinedSecondaryVertexBJetTags = akSoftDropCh4PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh4PFCombinedSecondaryVertexV2BJetTags = akSoftDropCh4PFbTagger.CombinedSecondaryVertexV2BJetTags
akSoftDropCh4PFJetBProbabilityBJetTags = akSoftDropCh4PFbTagger.JetBProbabilityBJetTags
akSoftDropCh4PFSoftPFMuonByPtBJetTags = akSoftDropCh4PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropCh4PFSoftPFMuonByIP3dBJetTags = akSoftDropCh4PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh4PFTrackCountingHighEffBJetTags = akSoftDropCh4PFbTagger.TrackCountingHighEffBJetTags
akSoftDropCh4PFTrackCountingHighPurBJetTags = akSoftDropCh4PFbTagger.TrackCountingHighPurBJetTags
akSoftDropCh4PFPatJetPartonAssociationLegacy = akSoftDropCh4PFbTagger.PatJetPartonAssociationLegacy

akSoftDropCh4PFImpactParameterTagInfos = akSoftDropCh4PFbTagger.ImpactParameterTagInfos
akSoftDropCh4PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh4PFJetProbabilityBJetTags = akSoftDropCh4PFbTagger.JetProbabilityBJetTags

akSoftDropCh4PFSecondaryVertexTagInfos = akSoftDropCh4PFbTagger.SecondaryVertexTagInfos
akSoftDropCh4PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh4PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh4PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh4PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh4PFCombinedSecondaryVertexBJetTags = akSoftDropCh4PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh4PFCombinedSecondaryVertexV2BJetTags = akSoftDropCh4PFbTagger.CombinedSecondaryVertexV2BJetTags

akSoftDropCh4PFSecondaryVertexNegativeTagInfos = akSoftDropCh4PFbTagger.SecondaryVertexNegativeTagInfos
akSoftDropCh4PFNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh4PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDropCh4PFNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh4PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDropCh4PFNegativeCombinedSecondaryVertexBJetTags = akSoftDropCh4PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDropCh4PFPositiveCombinedSecondaryVertexBJetTags = akSoftDropCh4PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDropCh4PFNegativeCombinedSecondaryVertexV2BJetTags = akSoftDropCh4PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDropCh4PFPositiveCombinedSecondaryVertexV2BJetTags = akSoftDropCh4PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDropCh4PFSoftPFMuonsTagInfos = akSoftDropCh4PFbTagger.SoftPFMuonsTagInfos
akSoftDropCh4PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh4PFSoftPFMuonBJetTags = akSoftDropCh4PFbTagger.SoftPFMuonBJetTags
akSoftDropCh4PFSoftPFMuonByIP3dBJetTags = akSoftDropCh4PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh4PFSoftPFMuonByPtBJetTags = akSoftDropCh4PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropCh4PFNegativeSoftPFMuonByPtBJetTags = akSoftDropCh4PFbTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDropCh4PFPositiveSoftPFMuonByPtBJetTags = akSoftDropCh4PFbTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDropCh4PFPatJetFlavourIdLegacy = cms.Sequence(akSoftDropCh4PFPatJetPartonAssociationLegacy*akSoftDropCh4PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akSoftDropCh4PFPatJetFlavourAssociation = akSoftDropCh4PFbTagger.PatJetFlavourAssociation
#akSoftDropCh4PFPatJetFlavourId = cms.Sequence(akSoftDropCh4PFPatJetPartons*akSoftDropCh4PFPatJetFlavourAssociation)

akSoftDropCh4PFJetBtaggingIP       = cms.Sequence(akSoftDropCh4PFImpactParameterTagInfos *
            (akSoftDropCh4PFTrackCountingHighEffBJetTags +
             akSoftDropCh4PFTrackCountingHighPurBJetTags +
             akSoftDropCh4PFJetProbabilityBJetTags +
             akSoftDropCh4PFJetBProbabilityBJetTags 
            )
            )

akSoftDropCh4PFJetBtaggingSV = cms.Sequence(akSoftDropCh4PFImpactParameterTagInfos
            *
            akSoftDropCh4PFSecondaryVertexTagInfos
            * (akSoftDropCh4PFSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh4PFSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh4PFCombinedSecondaryVertexBJetTags+
                akSoftDropCh4PFCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh4PFJetBtaggingNegSV = cms.Sequence(akSoftDropCh4PFImpactParameterTagInfos
            *
            akSoftDropCh4PFSecondaryVertexNegativeTagInfos
            * (akSoftDropCh4PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh4PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh4PFNegativeCombinedSecondaryVertexBJetTags+
                akSoftDropCh4PFPositiveCombinedSecondaryVertexBJetTags+
                akSoftDropCh4PFNegativeCombinedSecondaryVertexV2BJetTags+
                akSoftDropCh4PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh4PFJetBtaggingMu = cms.Sequence(akSoftDropCh4PFSoftPFMuonsTagInfos * (akSoftDropCh4PFSoftPFMuonBJetTags
                +
                akSoftDropCh4PFSoftPFMuonByIP3dBJetTags
                +
                akSoftDropCh4PFSoftPFMuonByPtBJetTags
                +
                akSoftDropCh4PFNegativeSoftPFMuonByPtBJetTags
                +
                akSoftDropCh4PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akSoftDropCh4PFJetBtagging = cms.Sequence(akSoftDropCh4PFJetBtaggingIP
            *akSoftDropCh4PFJetBtaggingSV
            *akSoftDropCh4PFJetBtaggingNegSV
#            *akSoftDropCh4PFJetBtaggingMu
            )

akSoftDropCh4PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akSoftDropCh4PFJets"),
        genJetMatch          = cms.InputTag("akSoftDropCh4PFmatch"),
        genPartonMatch       = cms.InputTag("akSoftDropCh4PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akSoftDropCh4PFcorr")),
        JetPartonMapSource   = cms.InputTag("akSoftDropCh4PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akSoftDropCh4PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akSoftDropCh4PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akSoftDropCh4PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akSoftDropCh4PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akSoftDropCh4PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akSoftDropCh4PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akSoftDropCh4PFJetBProbabilityBJetTags"),
            cms.InputTag("akSoftDropCh4PFJetProbabilityBJetTags"),
            #cms.InputTag("akSoftDropCh4PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akSoftDropCh4PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akSoftDropCh4PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akSoftDropCh4PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akSoftDropCh4PFJetID"),
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

akSoftDropCh4PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akSoftDropCh4PFJets"),
           	    R0  = cms.double( 0.4)
)
akSoftDropCh4PFpatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh4PFNjettiness:tau1','akSoftDropCh4PFNjettiness:tau2','akSoftDropCh4PFNjettiness:tau3']

akSoftDropCh4PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akSoftDropCh4PFpatJetsWithBtagging"),
                                                             genjetTag = 'ak4GenJets',#'ak4GenJets',
                                                             rParam = 0.4,
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
                                                             bTagJetName = cms.untracked.string("akSoftDropCh4PF"),
                                                             jetName = cms.untracked.string("akSoftDropCh4PF"),
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

akSoftDropCh4PFJetSequence_mc = cms.Sequence(
                                                  #akSoftDropCh4PFclean
                                                  #*
                                                  akSoftDropCh4PFmatch
                                                  #*
                                                  #akSoftDropCh4PFmatchGroomed
                                                  *
                                                  akSoftDropCh4PFparton
                                                  *
                                                  akSoftDropCh4PFcorr
                                                  *
                                                  #akSoftDropCh4PFJetID
                                                  #*
                                                  akSoftDropCh4PFPatJetFlavourIdLegacy
                                                  #*
			                          #akSoftDropCh4PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akSoftDropCh4PFJetTracksAssociatorAtVertex
                                                  *
                                                  akSoftDropCh4PFJetBtagging
                                                  *
                                                  akSoftDropCh4PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akSoftDropCh4PFpatJetsWithBtagging
                                                  *
                                                  akSoftDropCh4PFJetAnalyzer
                                                  )

akSoftDropCh4PFJetSequence_data = cms.Sequence(akSoftDropCh4PFcorr
                                                    *
                                                    #akSoftDropCh4PFJetID
                                                    #*
                                                    akSoftDropCh4PFJetTracksAssociatorAtVertex
                                                    *
                                                    akSoftDropCh4PFJetBtagging
                                                    *
                                                    akSoftDropCh4PFNjettiness 
                                                    *
                                                    akSoftDropCh4PFpatJetsWithBtagging
                                                    *
                                                    akSoftDropCh4PFJetAnalyzer
                                                    )

akSoftDropCh4PFJetSequence_jec = cms.Sequence(akSoftDropCh4PFJetSequence_mc)
akSoftDropCh4PFJetSequence_mb = cms.Sequence(akSoftDropCh4PFJetSequence_mc)

akSoftDropCh4PFJetSequence = cms.Sequence(akSoftDropCh4PFJetSequence_mc)
akSoftDropCh4PFpatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh4PFJets:sym']
akSoftDropCh4PFpatJetsWithBtagging.userData.userInts.src += ['akSoftDropCh4PFJets:droppedBranches']
