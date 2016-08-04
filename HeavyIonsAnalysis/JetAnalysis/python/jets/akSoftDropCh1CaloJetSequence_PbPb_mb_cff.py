

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDropCh1Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh1CaloJets"),
    matched = cms.InputTag("ak1HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akSoftDropCh1CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh1HiGenJets"),
    matched = cms.InputTag("ak1HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akSoftDropCh1Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh1CaloJets")
                                                        )

akSoftDropCh1Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akSoftDropCh1CaloJets"),
    payload = "AK1Calo_offline"
    )

akSoftDropCh1CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akSoftDropCh1CaloJets'))

#akSoftDropCh1Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak1HiCleanedGenJets'))

akSoftDropCh1CalobTagger = bTaggers("akSoftDropCh1Calo",0.1)

#create objects locally since they dont load properly otherwise
#akSoftDropCh1Calomatch = akSoftDropCh1CalobTagger.match
akSoftDropCh1Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh1CaloJets"), matched = cms.InputTag("selectedPartons"))
akSoftDropCh1CaloPatJetFlavourAssociationLegacy = akSoftDropCh1CalobTagger.PatJetFlavourAssociationLegacy
akSoftDropCh1CaloPatJetPartons = akSoftDropCh1CalobTagger.PatJetPartons
akSoftDropCh1CaloJetTracksAssociatorAtVertex = akSoftDropCh1CalobTagger.JetTracksAssociatorAtVertex
akSoftDropCh1CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDropCh1CaloSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh1CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh1CaloSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh1CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh1CaloCombinedSecondaryVertexBJetTags = akSoftDropCh1CalobTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh1CaloCombinedSecondaryVertexV2BJetTags = akSoftDropCh1CalobTagger.CombinedSecondaryVertexV2BJetTags
akSoftDropCh1CaloJetBProbabilityBJetTags = akSoftDropCh1CalobTagger.JetBProbabilityBJetTags
akSoftDropCh1CaloSoftPFMuonByPtBJetTags = akSoftDropCh1CalobTagger.SoftPFMuonByPtBJetTags
akSoftDropCh1CaloSoftPFMuonByIP3dBJetTags = akSoftDropCh1CalobTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh1CaloTrackCountingHighEffBJetTags = akSoftDropCh1CalobTagger.TrackCountingHighEffBJetTags
akSoftDropCh1CaloTrackCountingHighPurBJetTags = akSoftDropCh1CalobTagger.TrackCountingHighPurBJetTags
akSoftDropCh1CaloPatJetPartonAssociationLegacy = akSoftDropCh1CalobTagger.PatJetPartonAssociationLegacy

akSoftDropCh1CaloImpactParameterTagInfos = akSoftDropCh1CalobTagger.ImpactParameterTagInfos
akSoftDropCh1CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh1CaloJetProbabilityBJetTags = akSoftDropCh1CalobTagger.JetProbabilityBJetTags

akSoftDropCh1CaloSecondaryVertexTagInfos = akSoftDropCh1CalobTagger.SecondaryVertexTagInfos
akSoftDropCh1CaloSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh1CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh1CaloSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh1CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh1CaloCombinedSecondaryVertexBJetTags = akSoftDropCh1CalobTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh1CaloCombinedSecondaryVertexV2BJetTags = akSoftDropCh1CalobTagger.CombinedSecondaryVertexV2BJetTags

akSoftDropCh1CaloSecondaryVertexNegativeTagInfos = akSoftDropCh1CalobTagger.SecondaryVertexNegativeTagInfos
akSoftDropCh1CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh1CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDropCh1CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh1CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDropCh1CaloNegativeCombinedSecondaryVertexBJetTags = akSoftDropCh1CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDropCh1CaloPositiveCombinedSecondaryVertexBJetTags = akSoftDropCh1CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDropCh1CaloNegativeCombinedSecondaryVertexV2BJetTags = akSoftDropCh1CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDropCh1CaloPositiveCombinedSecondaryVertexV2BJetTags = akSoftDropCh1CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDropCh1CaloSoftPFMuonsTagInfos = akSoftDropCh1CalobTagger.SoftPFMuonsTagInfos
akSoftDropCh1CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh1CaloSoftPFMuonBJetTags = akSoftDropCh1CalobTagger.SoftPFMuonBJetTags
akSoftDropCh1CaloSoftPFMuonByIP3dBJetTags = akSoftDropCh1CalobTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh1CaloSoftPFMuonByPtBJetTags = akSoftDropCh1CalobTagger.SoftPFMuonByPtBJetTags
akSoftDropCh1CaloNegativeSoftPFMuonByPtBJetTags = akSoftDropCh1CalobTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDropCh1CaloPositiveSoftPFMuonByPtBJetTags = akSoftDropCh1CalobTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDropCh1CaloPatJetFlavourIdLegacy = cms.Sequence(akSoftDropCh1CaloPatJetPartonAssociationLegacy*akSoftDropCh1CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akSoftDropCh1CaloPatJetFlavourAssociation = akSoftDropCh1CalobTagger.PatJetFlavourAssociation
#akSoftDropCh1CaloPatJetFlavourId = cms.Sequence(akSoftDropCh1CaloPatJetPartons*akSoftDropCh1CaloPatJetFlavourAssociation)

akSoftDropCh1CaloJetBtaggingIP       = cms.Sequence(akSoftDropCh1CaloImpactParameterTagInfos *
            (akSoftDropCh1CaloTrackCountingHighEffBJetTags +
             akSoftDropCh1CaloTrackCountingHighPurBJetTags +
             akSoftDropCh1CaloJetProbabilityBJetTags +
             akSoftDropCh1CaloJetBProbabilityBJetTags 
            )
            )

akSoftDropCh1CaloJetBtaggingSV = cms.Sequence(akSoftDropCh1CaloImpactParameterTagInfos
            *
            akSoftDropCh1CaloSecondaryVertexTagInfos
            * (akSoftDropCh1CaloSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh1CaloSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh1CaloCombinedSecondaryVertexBJetTags+
                akSoftDropCh1CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh1CaloJetBtaggingNegSV = cms.Sequence(akSoftDropCh1CaloImpactParameterTagInfos
            *
            akSoftDropCh1CaloSecondaryVertexNegativeTagInfos
            * (akSoftDropCh1CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh1CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh1CaloNegativeCombinedSecondaryVertexBJetTags+
                akSoftDropCh1CaloPositiveCombinedSecondaryVertexBJetTags+
                akSoftDropCh1CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akSoftDropCh1CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh1CaloJetBtaggingMu = cms.Sequence(akSoftDropCh1CaloSoftPFMuonsTagInfos * (akSoftDropCh1CaloSoftPFMuonBJetTags
                +
                akSoftDropCh1CaloSoftPFMuonByIP3dBJetTags
                +
                akSoftDropCh1CaloSoftPFMuonByPtBJetTags
                +
                akSoftDropCh1CaloNegativeSoftPFMuonByPtBJetTags
                +
                akSoftDropCh1CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akSoftDropCh1CaloJetBtagging = cms.Sequence(akSoftDropCh1CaloJetBtaggingIP
            *akSoftDropCh1CaloJetBtaggingSV
            *akSoftDropCh1CaloJetBtaggingNegSV
#            *akSoftDropCh1CaloJetBtaggingMu
            )

akSoftDropCh1CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akSoftDropCh1CaloJets"),
        genJetMatch          = cms.InputTag("akSoftDropCh1Calomatch"),
        genPartonMatch       = cms.InputTag("akSoftDropCh1Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akSoftDropCh1Calocorr")),
        JetPartonMapSource   = cms.InputTag("akSoftDropCh1CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akSoftDropCh1CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akSoftDropCh1CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akSoftDropCh1CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akSoftDropCh1CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akSoftDropCh1CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akSoftDropCh1CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akSoftDropCh1CaloJetBProbabilityBJetTags"),
            cms.InputTag("akSoftDropCh1CaloJetProbabilityBJetTags"),
            #cms.InputTag("akSoftDropCh1CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akSoftDropCh1CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akSoftDropCh1CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akSoftDropCh1CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akSoftDropCh1CaloJetID"),
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

akSoftDropCh1CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akSoftDropCh1CaloJets"),
           	    R0  = cms.double( 0.1)
)
akSoftDropCh1CalopatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh1CaloNjettiness:tau1','akSoftDropCh1CaloNjettiness:tau2','akSoftDropCh1CaloNjettiness:tau3']

akSoftDropCh1CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akSoftDropCh1CalopatJetsWithBtagging"),
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
                                                             bTagJetName = cms.untracked.string("akSoftDropCh1Calo"),
                                                             jetName = cms.untracked.string("akSoftDropCh1Calo"),
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

akSoftDropCh1CaloJetSequence_mc = cms.Sequence(
                                                  #akSoftDropCh1Caloclean
                                                  #*
                                                  akSoftDropCh1Calomatch
                                                  #*
                                                  #akSoftDropCh1CalomatchGroomed
                                                  *
                                                  akSoftDropCh1Caloparton
                                                  *
                                                  akSoftDropCh1Calocorr
                                                  *
                                                  #akSoftDropCh1CaloJetID
                                                  #*
                                                  akSoftDropCh1CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akSoftDropCh1CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akSoftDropCh1CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akSoftDropCh1CaloJetBtagging
                                                  *
                                                  akSoftDropCh1CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akSoftDropCh1CalopatJetsWithBtagging
                                                  *
                                                  akSoftDropCh1CaloJetAnalyzer
                                                  )

akSoftDropCh1CaloJetSequence_data = cms.Sequence(akSoftDropCh1Calocorr
                                                    *
                                                    #akSoftDropCh1CaloJetID
                                                    #*
                                                    akSoftDropCh1CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akSoftDropCh1CaloJetBtagging
                                                    *
                                                    akSoftDropCh1CaloNjettiness 
                                                    *
                                                    akSoftDropCh1CalopatJetsWithBtagging
                                                    *
                                                    akSoftDropCh1CaloJetAnalyzer
                                                    )

akSoftDropCh1CaloJetSequence_jec = cms.Sequence(akSoftDropCh1CaloJetSequence_mc)
akSoftDropCh1CaloJetSequence_mb = cms.Sequence(akSoftDropCh1CaloJetSequence_mc)

akSoftDropCh1CaloJetSequence = cms.Sequence(akSoftDropCh1CaloJetSequence_mb)
akSoftDropCh1CalopatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh1CaloJets:sym']
akSoftDropCh1CalopatJetsWithBtagging.userData.userInts.src += ['akSoftDropCh1CaloJets:droppedBranches']
