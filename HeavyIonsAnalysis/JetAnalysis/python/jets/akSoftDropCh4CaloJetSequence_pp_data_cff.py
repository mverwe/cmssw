

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDropCh4Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh4CaloJets"),
    matched = cms.InputTag("ak4GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.4
    )

akSoftDropCh4CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh4GenJets"),
    matched = cms.InputTag("ak4GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.4
    )

akSoftDropCh4Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh4CaloJets")
                                                        )

akSoftDropCh4Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akSoftDropCh4CaloJets"),
    payload = "AK4Calo_offline"
    )

akSoftDropCh4CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akSoftDropCh4CaloJets'))

#akSoftDropCh4Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak4GenJets'))

akSoftDropCh4CalobTagger = bTaggers("akSoftDropCh4Calo",0.4)

#create objects locally since they dont load properly otherwise
#akSoftDropCh4Calomatch = akSoftDropCh4CalobTagger.match
akSoftDropCh4Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh4CaloJets"), matched = cms.InputTag("genParticles"))
akSoftDropCh4CaloPatJetFlavourAssociationLegacy = akSoftDropCh4CalobTagger.PatJetFlavourAssociationLegacy
akSoftDropCh4CaloPatJetPartons = akSoftDropCh4CalobTagger.PatJetPartons
akSoftDropCh4CaloJetTracksAssociatorAtVertex = akSoftDropCh4CalobTagger.JetTracksAssociatorAtVertex
akSoftDropCh4CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDropCh4CaloSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh4CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh4CaloSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh4CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh4CaloCombinedSecondaryVertexBJetTags = akSoftDropCh4CalobTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh4CaloCombinedSecondaryVertexV2BJetTags = akSoftDropCh4CalobTagger.CombinedSecondaryVertexV2BJetTags
akSoftDropCh4CaloJetBProbabilityBJetTags = akSoftDropCh4CalobTagger.JetBProbabilityBJetTags
akSoftDropCh4CaloSoftPFMuonByPtBJetTags = akSoftDropCh4CalobTagger.SoftPFMuonByPtBJetTags
akSoftDropCh4CaloSoftPFMuonByIP3dBJetTags = akSoftDropCh4CalobTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh4CaloTrackCountingHighEffBJetTags = akSoftDropCh4CalobTagger.TrackCountingHighEffBJetTags
akSoftDropCh4CaloTrackCountingHighPurBJetTags = akSoftDropCh4CalobTagger.TrackCountingHighPurBJetTags
akSoftDropCh4CaloPatJetPartonAssociationLegacy = akSoftDropCh4CalobTagger.PatJetPartonAssociationLegacy

akSoftDropCh4CaloImpactParameterTagInfos = akSoftDropCh4CalobTagger.ImpactParameterTagInfos
akSoftDropCh4CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh4CaloJetProbabilityBJetTags = akSoftDropCh4CalobTagger.JetProbabilityBJetTags

akSoftDropCh4CaloSecondaryVertexTagInfos = akSoftDropCh4CalobTagger.SecondaryVertexTagInfos
akSoftDropCh4CaloSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh4CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh4CaloSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh4CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh4CaloCombinedSecondaryVertexBJetTags = akSoftDropCh4CalobTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh4CaloCombinedSecondaryVertexV2BJetTags = akSoftDropCh4CalobTagger.CombinedSecondaryVertexV2BJetTags

akSoftDropCh4CaloSecondaryVertexNegativeTagInfos = akSoftDropCh4CalobTagger.SecondaryVertexNegativeTagInfos
akSoftDropCh4CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh4CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDropCh4CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh4CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDropCh4CaloNegativeCombinedSecondaryVertexBJetTags = akSoftDropCh4CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDropCh4CaloPositiveCombinedSecondaryVertexBJetTags = akSoftDropCh4CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDropCh4CaloNegativeCombinedSecondaryVertexV2BJetTags = akSoftDropCh4CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDropCh4CaloPositiveCombinedSecondaryVertexV2BJetTags = akSoftDropCh4CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDropCh4CaloSoftPFMuonsTagInfos = akSoftDropCh4CalobTagger.SoftPFMuonsTagInfos
akSoftDropCh4CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh4CaloSoftPFMuonBJetTags = akSoftDropCh4CalobTagger.SoftPFMuonBJetTags
akSoftDropCh4CaloSoftPFMuonByIP3dBJetTags = akSoftDropCh4CalobTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh4CaloSoftPFMuonByPtBJetTags = akSoftDropCh4CalobTagger.SoftPFMuonByPtBJetTags
akSoftDropCh4CaloNegativeSoftPFMuonByPtBJetTags = akSoftDropCh4CalobTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDropCh4CaloPositiveSoftPFMuonByPtBJetTags = akSoftDropCh4CalobTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDropCh4CaloPatJetFlavourIdLegacy = cms.Sequence(akSoftDropCh4CaloPatJetPartonAssociationLegacy*akSoftDropCh4CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akSoftDropCh4CaloPatJetFlavourAssociation = akSoftDropCh4CalobTagger.PatJetFlavourAssociation
#akSoftDropCh4CaloPatJetFlavourId = cms.Sequence(akSoftDropCh4CaloPatJetPartons*akSoftDropCh4CaloPatJetFlavourAssociation)

akSoftDropCh4CaloJetBtaggingIP       = cms.Sequence(akSoftDropCh4CaloImpactParameterTagInfos *
            (akSoftDropCh4CaloTrackCountingHighEffBJetTags +
             akSoftDropCh4CaloTrackCountingHighPurBJetTags +
             akSoftDropCh4CaloJetProbabilityBJetTags +
             akSoftDropCh4CaloJetBProbabilityBJetTags 
            )
            )

akSoftDropCh4CaloJetBtaggingSV = cms.Sequence(akSoftDropCh4CaloImpactParameterTagInfos
            *
            akSoftDropCh4CaloSecondaryVertexTagInfos
            * (akSoftDropCh4CaloSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh4CaloSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh4CaloCombinedSecondaryVertexBJetTags+
                akSoftDropCh4CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh4CaloJetBtaggingNegSV = cms.Sequence(akSoftDropCh4CaloImpactParameterTagInfos
            *
            akSoftDropCh4CaloSecondaryVertexNegativeTagInfos
            * (akSoftDropCh4CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh4CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh4CaloNegativeCombinedSecondaryVertexBJetTags+
                akSoftDropCh4CaloPositiveCombinedSecondaryVertexBJetTags+
                akSoftDropCh4CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akSoftDropCh4CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh4CaloJetBtaggingMu = cms.Sequence(akSoftDropCh4CaloSoftPFMuonsTagInfos * (akSoftDropCh4CaloSoftPFMuonBJetTags
                +
                akSoftDropCh4CaloSoftPFMuonByIP3dBJetTags
                +
                akSoftDropCh4CaloSoftPFMuonByPtBJetTags
                +
                akSoftDropCh4CaloNegativeSoftPFMuonByPtBJetTags
                +
                akSoftDropCh4CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akSoftDropCh4CaloJetBtagging = cms.Sequence(akSoftDropCh4CaloJetBtaggingIP
            *akSoftDropCh4CaloJetBtaggingSV
            *akSoftDropCh4CaloJetBtaggingNegSV
#            *akSoftDropCh4CaloJetBtaggingMu
            )

akSoftDropCh4CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akSoftDropCh4CaloJets"),
        genJetMatch          = cms.InputTag("akSoftDropCh4Calomatch"),
        genPartonMatch       = cms.InputTag("akSoftDropCh4Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akSoftDropCh4Calocorr")),
        JetPartonMapSource   = cms.InputTag("akSoftDropCh4CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akSoftDropCh4CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akSoftDropCh4CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akSoftDropCh4CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akSoftDropCh4CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akSoftDropCh4CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akSoftDropCh4CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akSoftDropCh4CaloJetBProbabilityBJetTags"),
            cms.InputTag("akSoftDropCh4CaloJetProbabilityBJetTags"),
            #cms.InputTag("akSoftDropCh4CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akSoftDropCh4CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akSoftDropCh4CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akSoftDropCh4CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akSoftDropCh4CaloJetID"),
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

akSoftDropCh4CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akSoftDropCh4CaloJets"),
           	    R0  = cms.double( 0.4)
)
akSoftDropCh4CalopatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh4CaloNjettiness:tau1','akSoftDropCh4CaloNjettiness:tau2','akSoftDropCh4CaloNjettiness:tau3']

akSoftDropCh4CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akSoftDropCh4CalopatJetsWithBtagging"),
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
                                                             bTagJetName = cms.untracked.string("akSoftDropCh4Calo"),
                                                             jetName = cms.untracked.string("akSoftDropCh4Calo"),
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

akSoftDropCh4CaloJetSequence_mc = cms.Sequence(
                                                  #akSoftDropCh4Caloclean
                                                  #*
                                                  akSoftDropCh4Calomatch
                                                  #*
                                                  #akSoftDropCh4CalomatchGroomed
                                                  *
                                                  akSoftDropCh4Caloparton
                                                  *
                                                  akSoftDropCh4Calocorr
                                                  *
                                                  #akSoftDropCh4CaloJetID
                                                  #*
                                                  akSoftDropCh4CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akSoftDropCh4CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akSoftDropCh4CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akSoftDropCh4CaloJetBtagging
                                                  *
                                                  akSoftDropCh4CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akSoftDropCh4CalopatJetsWithBtagging
                                                  *
                                                  akSoftDropCh4CaloJetAnalyzer
                                                  )

akSoftDropCh4CaloJetSequence_data = cms.Sequence(akSoftDropCh4Calocorr
                                                    *
                                                    #akSoftDropCh4CaloJetID
                                                    #*
                                                    akSoftDropCh4CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akSoftDropCh4CaloJetBtagging
                                                    *
                                                    akSoftDropCh4CaloNjettiness 
                                                    *
                                                    akSoftDropCh4CalopatJetsWithBtagging
                                                    *
                                                    akSoftDropCh4CaloJetAnalyzer
                                                    )

akSoftDropCh4CaloJetSequence_jec = cms.Sequence(akSoftDropCh4CaloJetSequence_mc)
akSoftDropCh4CaloJetSequence_mb = cms.Sequence(akSoftDropCh4CaloJetSequence_mc)

akSoftDropCh4CaloJetSequence = cms.Sequence(akSoftDropCh4CaloJetSequence_data)
akSoftDropCh4CalopatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh4CaloJets:sym']
akSoftDropCh4CalopatJetsWithBtagging.userData.userInts.src += ['akSoftDropCh4CaloJets:droppedBranches']
