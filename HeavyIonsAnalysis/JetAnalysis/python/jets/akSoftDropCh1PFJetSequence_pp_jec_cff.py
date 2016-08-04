

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDropCh1PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh1PFJets"),
    matched = cms.InputTag("ak1GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akSoftDropCh1PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh1GenJets"),
    matched = cms.InputTag("ak1GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akSoftDropCh1PFparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh1PFJets")
                                                        )

akSoftDropCh1PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akSoftDropCh1PFJets"),
    payload = "AK1PF_offline"
    )

akSoftDropCh1PFJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akSoftDropCh1CaloJets'))

#akSoftDropCh1PFclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak1GenJets'))

akSoftDropCh1PFbTagger = bTaggers("akSoftDropCh1PF",0.1)

#create objects locally since they dont load properly otherwise
#akSoftDropCh1PFmatch = akSoftDropCh1PFbTagger.match
akSoftDropCh1PFparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh1PFJets"), matched = cms.InputTag("genParticles"))
akSoftDropCh1PFPatJetFlavourAssociationLegacy = akSoftDropCh1PFbTagger.PatJetFlavourAssociationLegacy
akSoftDropCh1PFPatJetPartons = akSoftDropCh1PFbTagger.PatJetPartons
akSoftDropCh1PFJetTracksAssociatorAtVertex = akSoftDropCh1PFbTagger.JetTracksAssociatorAtVertex
akSoftDropCh1PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDropCh1PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh1PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh1PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh1PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh1PFCombinedSecondaryVertexBJetTags = akSoftDropCh1PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh1PFCombinedSecondaryVertexV2BJetTags = akSoftDropCh1PFbTagger.CombinedSecondaryVertexV2BJetTags
akSoftDropCh1PFJetBProbabilityBJetTags = akSoftDropCh1PFbTagger.JetBProbabilityBJetTags
akSoftDropCh1PFSoftPFMuonByPtBJetTags = akSoftDropCh1PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropCh1PFSoftPFMuonByIP3dBJetTags = akSoftDropCh1PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh1PFTrackCountingHighEffBJetTags = akSoftDropCh1PFbTagger.TrackCountingHighEffBJetTags
akSoftDropCh1PFTrackCountingHighPurBJetTags = akSoftDropCh1PFbTagger.TrackCountingHighPurBJetTags
akSoftDropCh1PFPatJetPartonAssociationLegacy = akSoftDropCh1PFbTagger.PatJetPartonAssociationLegacy

akSoftDropCh1PFImpactParameterTagInfos = akSoftDropCh1PFbTagger.ImpactParameterTagInfos
akSoftDropCh1PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh1PFJetProbabilityBJetTags = akSoftDropCh1PFbTagger.JetProbabilityBJetTags

akSoftDropCh1PFSecondaryVertexTagInfos = akSoftDropCh1PFbTagger.SecondaryVertexTagInfos
akSoftDropCh1PFSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh1PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh1PFSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh1PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh1PFCombinedSecondaryVertexBJetTags = akSoftDropCh1PFbTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh1PFCombinedSecondaryVertexV2BJetTags = akSoftDropCh1PFbTagger.CombinedSecondaryVertexV2BJetTags

akSoftDropCh1PFSecondaryVertexNegativeTagInfos = akSoftDropCh1PFbTagger.SecondaryVertexNegativeTagInfos
akSoftDropCh1PFNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh1PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDropCh1PFNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh1PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDropCh1PFNegativeCombinedSecondaryVertexBJetTags = akSoftDropCh1PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDropCh1PFPositiveCombinedSecondaryVertexBJetTags = akSoftDropCh1PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDropCh1PFNegativeCombinedSecondaryVertexV2BJetTags = akSoftDropCh1PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDropCh1PFPositiveCombinedSecondaryVertexV2BJetTags = akSoftDropCh1PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDropCh1PFSoftPFMuonsTagInfos = akSoftDropCh1PFbTagger.SoftPFMuonsTagInfos
akSoftDropCh1PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh1PFSoftPFMuonBJetTags = akSoftDropCh1PFbTagger.SoftPFMuonBJetTags
akSoftDropCh1PFSoftPFMuonByIP3dBJetTags = akSoftDropCh1PFbTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh1PFSoftPFMuonByPtBJetTags = akSoftDropCh1PFbTagger.SoftPFMuonByPtBJetTags
akSoftDropCh1PFNegativeSoftPFMuonByPtBJetTags = akSoftDropCh1PFbTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDropCh1PFPositiveSoftPFMuonByPtBJetTags = akSoftDropCh1PFbTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDropCh1PFPatJetFlavourIdLegacy = cms.Sequence(akSoftDropCh1PFPatJetPartonAssociationLegacy*akSoftDropCh1PFPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akSoftDropCh1PFPatJetFlavourAssociation = akSoftDropCh1PFbTagger.PatJetFlavourAssociation
#akSoftDropCh1PFPatJetFlavourId = cms.Sequence(akSoftDropCh1PFPatJetPartons*akSoftDropCh1PFPatJetFlavourAssociation)

akSoftDropCh1PFJetBtaggingIP       = cms.Sequence(akSoftDropCh1PFImpactParameterTagInfos *
            (akSoftDropCh1PFTrackCountingHighEffBJetTags +
             akSoftDropCh1PFTrackCountingHighPurBJetTags +
             akSoftDropCh1PFJetProbabilityBJetTags +
             akSoftDropCh1PFJetBProbabilityBJetTags 
            )
            )

akSoftDropCh1PFJetBtaggingSV = cms.Sequence(akSoftDropCh1PFImpactParameterTagInfos
            *
            akSoftDropCh1PFSecondaryVertexTagInfos
            * (akSoftDropCh1PFSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh1PFSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh1PFCombinedSecondaryVertexBJetTags+
                akSoftDropCh1PFCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh1PFJetBtaggingNegSV = cms.Sequence(akSoftDropCh1PFImpactParameterTagInfos
            *
            akSoftDropCh1PFSecondaryVertexNegativeTagInfos
            * (akSoftDropCh1PFNegativeSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh1PFNegativeSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh1PFNegativeCombinedSecondaryVertexBJetTags+
                akSoftDropCh1PFPositiveCombinedSecondaryVertexBJetTags+
                akSoftDropCh1PFNegativeCombinedSecondaryVertexV2BJetTags+
                akSoftDropCh1PFPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh1PFJetBtaggingMu = cms.Sequence(akSoftDropCh1PFSoftPFMuonsTagInfos * (akSoftDropCh1PFSoftPFMuonBJetTags
                +
                akSoftDropCh1PFSoftPFMuonByIP3dBJetTags
                +
                akSoftDropCh1PFSoftPFMuonByPtBJetTags
                +
                akSoftDropCh1PFNegativeSoftPFMuonByPtBJetTags
                +
                akSoftDropCh1PFPositiveSoftPFMuonByPtBJetTags
              )
            )

akSoftDropCh1PFJetBtagging = cms.Sequence(akSoftDropCh1PFJetBtaggingIP
            *akSoftDropCh1PFJetBtaggingSV
            *akSoftDropCh1PFJetBtaggingNegSV
#            *akSoftDropCh1PFJetBtaggingMu
            )

akSoftDropCh1PFpatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akSoftDropCh1PFJets"),
        genJetMatch          = cms.InputTag("akSoftDropCh1PFmatch"),
        genPartonMatch       = cms.InputTag("akSoftDropCh1PFparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akSoftDropCh1PFcorr")),
        JetPartonMapSource   = cms.InputTag("akSoftDropCh1PFPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akSoftDropCh1PFPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akSoftDropCh1PFJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akSoftDropCh1PFSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akSoftDropCh1PFSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akSoftDropCh1PFCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akSoftDropCh1PFCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akSoftDropCh1PFJetBProbabilityBJetTags"),
            cms.InputTag("akSoftDropCh1PFJetProbabilityBJetTags"),
            #cms.InputTag("akSoftDropCh1PFSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akSoftDropCh1PFSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akSoftDropCh1PFTrackCountingHighEffBJetTags"),
            cms.InputTag("akSoftDropCh1PFTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akSoftDropCh1PFJetID"),
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

akSoftDropCh1PFNjettiness = Njettiness.clone(
		    src = cms.InputTag("akSoftDropCh1PFJets"),
           	    R0  = cms.double( 0.1)
)
akSoftDropCh1PFpatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh1PFNjettiness:tau1','akSoftDropCh1PFNjettiness:tau2','akSoftDropCh1PFNjettiness:tau3']

akSoftDropCh1PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akSoftDropCh1PFpatJetsWithBtagging"),
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
                                                             bTagJetName = cms.untracked.string("akSoftDropCh1PF"),
                                                             jetName = cms.untracked.string("akSoftDropCh1PF"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(False),
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

akSoftDropCh1PFJetSequence_mc = cms.Sequence(
                                                  #akSoftDropCh1PFclean
                                                  #*
                                                  akSoftDropCh1PFmatch
                                                  #*
                                                  #akSoftDropCh1PFmatchGroomed
                                                  *
                                                  akSoftDropCh1PFparton
                                                  *
                                                  akSoftDropCh1PFcorr
                                                  *
                                                  #akSoftDropCh1PFJetID
                                                  #*
                                                  akSoftDropCh1PFPatJetFlavourIdLegacy
                                                  #*
			                          #akSoftDropCh1PFPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akSoftDropCh1PFJetTracksAssociatorAtVertex
                                                  *
                                                  akSoftDropCh1PFJetBtagging
                                                  *
                                                  akSoftDropCh1PFNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akSoftDropCh1PFpatJetsWithBtagging
                                                  *
                                                  akSoftDropCh1PFJetAnalyzer
                                                  )

akSoftDropCh1PFJetSequence_data = cms.Sequence(akSoftDropCh1PFcorr
                                                    *
                                                    #akSoftDropCh1PFJetID
                                                    #*
                                                    akSoftDropCh1PFJetTracksAssociatorAtVertex
                                                    *
                                                    akSoftDropCh1PFJetBtagging
                                                    *
                                                    akSoftDropCh1PFNjettiness 
                                                    *
                                                    akSoftDropCh1PFpatJetsWithBtagging
                                                    *
                                                    akSoftDropCh1PFJetAnalyzer
                                                    )

akSoftDropCh1PFJetSequence_jec = cms.Sequence(akSoftDropCh1PFJetSequence_mc)
akSoftDropCh1PFJetSequence_mb = cms.Sequence(akSoftDropCh1PFJetSequence_mc)

akSoftDropCh1PFJetSequence = cms.Sequence(akSoftDropCh1PFJetSequence_jec)
akSoftDropCh1PFJetAnalyzer.genPtMin = cms.untracked.double(1)
akSoftDropCh1PFJetAnalyzer.jetPtMin = cms.double(1)
akSoftDropCh1PFpatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh1PFJets:sym']
akSoftDropCh1PFpatJetsWithBtagging.userData.userInts.src += ['akSoftDropCh1PFJets:droppedBranches']
