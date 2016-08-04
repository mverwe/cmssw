

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropCh1Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropCh1CaloJets"),
    matched = cms.InputTag("ak1HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akVsSoftDropCh1CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh1HiGenJets"),
    matched = cms.InputTag("ak1HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.1
    )

akVsSoftDropCh1Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh1CaloJets")
                                                        )

akVsSoftDropCh1Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropCh1CaloJets"),
    payload = "AK1Calo_offline"
    )

akVsSoftDropCh1CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropCh1CaloJets'))

#akVsSoftDropCh1Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak1HiCleanedGenJets'))

akVsSoftDropCh1CalobTagger = bTaggers("akVsSoftDropCh1Calo",0.1)

#create objects locally since they dont load properly otherwise
#akVsSoftDropCh1Calomatch = akVsSoftDropCh1CalobTagger.match
akVsSoftDropCh1Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh1CaloJets"), matched = cms.InputTag("selectedPartons"))
akVsSoftDropCh1CaloPatJetFlavourAssociationLegacy = akVsSoftDropCh1CalobTagger.PatJetFlavourAssociationLegacy
akVsSoftDropCh1CaloPatJetPartons = akVsSoftDropCh1CalobTagger.PatJetPartons
akVsSoftDropCh1CaloJetTracksAssociatorAtVertex = akVsSoftDropCh1CalobTagger.JetTracksAssociatorAtVertex
akVsSoftDropCh1CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropCh1CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh1CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh1CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh1CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh1CaloCombinedSecondaryVertexBJetTags = akVsSoftDropCh1CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh1CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh1CalobTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropCh1CaloJetBProbabilityBJetTags = akVsSoftDropCh1CalobTagger.JetBProbabilityBJetTags
akVsSoftDropCh1CaloSoftPFMuonByPtBJetTags = akVsSoftDropCh1CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh1CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropCh1CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh1CaloTrackCountingHighEffBJetTags = akVsSoftDropCh1CalobTagger.TrackCountingHighEffBJetTags
akVsSoftDropCh1CaloTrackCountingHighPurBJetTags = akVsSoftDropCh1CalobTagger.TrackCountingHighPurBJetTags
akVsSoftDropCh1CaloPatJetPartonAssociationLegacy = akVsSoftDropCh1CalobTagger.PatJetPartonAssociationLegacy

akVsSoftDropCh1CaloImpactParameterTagInfos = akVsSoftDropCh1CalobTagger.ImpactParameterTagInfos
akVsSoftDropCh1CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh1CaloJetProbabilityBJetTags = akVsSoftDropCh1CalobTagger.JetProbabilityBJetTags

akVsSoftDropCh1CaloSecondaryVertexTagInfos = akVsSoftDropCh1CalobTagger.SecondaryVertexTagInfos
akVsSoftDropCh1CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh1CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh1CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh1CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh1CaloCombinedSecondaryVertexBJetTags = akVsSoftDropCh1CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh1CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh1CalobTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropCh1CaloSecondaryVertexNegativeTagInfos = akVsSoftDropCh1CalobTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropCh1CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh1CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh1CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh1CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh1CaloNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropCh1CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropCh1CaloPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropCh1CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropCh1CaloNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh1CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropCh1CaloPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh1CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropCh1CaloSoftPFMuonsTagInfos = akVsSoftDropCh1CalobTagger.SoftPFMuonsTagInfos
akVsSoftDropCh1CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh1CaloSoftPFMuonBJetTags = akVsSoftDropCh1CalobTagger.SoftPFMuonBJetTags
akVsSoftDropCh1CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropCh1CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh1CaloSoftPFMuonByPtBJetTags = akVsSoftDropCh1CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh1CaloNegativeSoftPFMuonByPtBJetTags = akVsSoftDropCh1CalobTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropCh1CaloPositiveSoftPFMuonByPtBJetTags = akVsSoftDropCh1CalobTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropCh1CaloPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropCh1CaloPatJetPartonAssociationLegacy*akVsSoftDropCh1CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropCh1CaloPatJetFlavourAssociation = akVsSoftDropCh1CalobTagger.PatJetFlavourAssociation
#akVsSoftDropCh1CaloPatJetFlavourId = cms.Sequence(akVsSoftDropCh1CaloPatJetPartons*akVsSoftDropCh1CaloPatJetFlavourAssociation)

akVsSoftDropCh1CaloJetBtaggingIP       = cms.Sequence(akVsSoftDropCh1CaloImpactParameterTagInfos *
            (akVsSoftDropCh1CaloTrackCountingHighEffBJetTags +
             akVsSoftDropCh1CaloTrackCountingHighPurBJetTags +
             akVsSoftDropCh1CaloJetProbabilityBJetTags +
             akVsSoftDropCh1CaloJetBProbabilityBJetTags 
            )
            )

akVsSoftDropCh1CaloJetBtaggingSV = cms.Sequence(akVsSoftDropCh1CaloImpactParameterTagInfos
            *
            akVsSoftDropCh1CaloSecondaryVertexTagInfos
            * (akVsSoftDropCh1CaloSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh1CaloSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh1CaloCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh1CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh1CaloJetBtaggingNegSV = cms.Sequence(akVsSoftDropCh1CaloImpactParameterTagInfos
            *
            akVsSoftDropCh1CaloSecondaryVertexNegativeTagInfos
            * (akVsSoftDropCh1CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh1CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh1CaloNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh1CaloPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh1CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropCh1CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh1CaloJetBtaggingMu = cms.Sequence(akVsSoftDropCh1CaloSoftPFMuonsTagInfos * (akVsSoftDropCh1CaloSoftPFMuonBJetTags
                +
                akVsSoftDropCh1CaloSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropCh1CaloSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh1CaloNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh1CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropCh1CaloJetBtagging = cms.Sequence(akVsSoftDropCh1CaloJetBtaggingIP
            *akVsSoftDropCh1CaloJetBtaggingSV
            *akVsSoftDropCh1CaloJetBtaggingNegSV
#            *akVsSoftDropCh1CaloJetBtaggingMu
            )

akVsSoftDropCh1CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropCh1CaloJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropCh1Calomatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropCh1Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropCh1Calocorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropCh1CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropCh1CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropCh1CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropCh1CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh1CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropCh1CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropCh1CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropCh1CaloJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropCh1CaloJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropCh1CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropCh1CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropCh1CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh1CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropCh1CaloJetID"),
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

akVsSoftDropCh1CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropCh1CaloJets"),
           	    R0  = cms.double( 0.1)
)
akVsSoftDropCh1CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh1CaloNjettiness:tau1','akVsSoftDropCh1CaloNjettiness:tau2','akVsSoftDropCh1CaloNjettiness:tau3']

akVsSoftDropCh1CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropCh1CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak1HiCleanedGenJets',#'ak1HiGenJets',
                                                             rParam = 0.1,
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
                                                             bTagJetName = cms.untracked.string("akVsSoftDropCh1Calo"),
                                                             jetName = cms.untracked.string("akVsSoftDropCh1Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
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

akVsSoftDropCh1CaloJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropCh1Caloclean
                                                  #*
                                                  akVsSoftDropCh1Calomatch
                                                  #*
                                                  #akVsSoftDropCh1CalomatchGroomed
                                                  *
                                                  akVsSoftDropCh1Caloparton
                                                  *
                                                  akVsSoftDropCh1Calocorr
                                                  *
                                                  #akVsSoftDropCh1CaloJetID
                                                  #*
                                                  akVsSoftDropCh1CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropCh1CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropCh1CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropCh1CaloJetBtagging
                                                  *
                                                  akVsSoftDropCh1CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropCh1CalopatJetsWithBtagging
                                                  *
                                                  akVsSoftDropCh1CaloJetAnalyzer
                                                  )

akVsSoftDropCh1CaloJetSequence_data = cms.Sequence(akVsSoftDropCh1Calocorr
                                                    *
                                                    #akVsSoftDropCh1CaloJetID
                                                    #*
                                                    akVsSoftDropCh1CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropCh1CaloJetBtagging
                                                    *
                                                    akVsSoftDropCh1CaloNjettiness 
                                                    *
                                                    akVsSoftDropCh1CalopatJetsWithBtagging
                                                    *
                                                    akVsSoftDropCh1CaloJetAnalyzer
                                                    )

akVsSoftDropCh1CaloJetSequence_jec = cms.Sequence(akVsSoftDropCh1CaloJetSequence_mc)
akVsSoftDropCh1CaloJetSequence_mb = cms.Sequence(akVsSoftDropCh1CaloJetSequence_mc)

akVsSoftDropCh1CaloJetSequence = cms.Sequence(akVsSoftDropCh1CaloJetSequence_mb)
akVsSoftDropCh1CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh1CaloJets:sym']
akVsSoftDropCh1CalopatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropCh1CaloJets:droppedBranches']
