

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDropCh2Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh2CaloJets"),
    matched = cms.InputTag("ak2HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.2
    )

akSoftDropCh2CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh2HiGenJets"),
    matched = cms.InputTag("ak2HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.2
    )

akSoftDropCh2Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh2CaloJets")
                                                        )

akSoftDropCh2Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akSoftDropCh2CaloJets"),
    payload = "AK2Calo_offline"
    )

akSoftDropCh2CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akSoftDropCh2CaloJets'))

#akSoftDropCh2Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak2HiSignalGenJets'))

akSoftDropCh2CalobTagger = bTaggers("akSoftDropCh2Calo",0.2)

#create objects locally since they dont load properly otherwise
#akSoftDropCh2Calomatch = akSoftDropCh2CalobTagger.match
akSoftDropCh2Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh2CaloJets"), matched = cms.InputTag("hiSignalGenParticles"))
akSoftDropCh2CaloPatJetFlavourAssociationLegacy = akSoftDropCh2CalobTagger.PatJetFlavourAssociationLegacy
akSoftDropCh2CaloPatJetPartons = akSoftDropCh2CalobTagger.PatJetPartons
akSoftDropCh2CaloJetTracksAssociatorAtVertex = akSoftDropCh2CalobTagger.JetTracksAssociatorAtVertex
akSoftDropCh2CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDropCh2CaloSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh2CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh2CaloSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh2CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh2CaloCombinedSecondaryVertexBJetTags = akSoftDropCh2CalobTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh2CaloCombinedSecondaryVertexV2BJetTags = akSoftDropCh2CalobTagger.CombinedSecondaryVertexV2BJetTags
akSoftDropCh2CaloJetBProbabilityBJetTags = akSoftDropCh2CalobTagger.JetBProbabilityBJetTags
akSoftDropCh2CaloSoftPFMuonByPtBJetTags = akSoftDropCh2CalobTagger.SoftPFMuonByPtBJetTags
akSoftDropCh2CaloSoftPFMuonByIP3dBJetTags = akSoftDropCh2CalobTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh2CaloTrackCountingHighEffBJetTags = akSoftDropCh2CalobTagger.TrackCountingHighEffBJetTags
akSoftDropCh2CaloTrackCountingHighPurBJetTags = akSoftDropCh2CalobTagger.TrackCountingHighPurBJetTags
akSoftDropCh2CaloPatJetPartonAssociationLegacy = akSoftDropCh2CalobTagger.PatJetPartonAssociationLegacy

akSoftDropCh2CaloImpactParameterTagInfos = akSoftDropCh2CalobTagger.ImpactParameterTagInfos
akSoftDropCh2CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh2CaloJetProbabilityBJetTags = akSoftDropCh2CalobTagger.JetProbabilityBJetTags

akSoftDropCh2CaloSecondaryVertexTagInfos = akSoftDropCh2CalobTagger.SecondaryVertexTagInfos
akSoftDropCh2CaloSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh2CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh2CaloSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh2CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh2CaloCombinedSecondaryVertexBJetTags = akSoftDropCh2CalobTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh2CaloCombinedSecondaryVertexV2BJetTags = akSoftDropCh2CalobTagger.CombinedSecondaryVertexV2BJetTags

akSoftDropCh2CaloSecondaryVertexNegativeTagInfos = akSoftDropCh2CalobTagger.SecondaryVertexNegativeTagInfos
akSoftDropCh2CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh2CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDropCh2CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh2CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDropCh2CaloNegativeCombinedSecondaryVertexBJetTags = akSoftDropCh2CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDropCh2CaloPositiveCombinedSecondaryVertexBJetTags = akSoftDropCh2CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDropCh2CaloNegativeCombinedSecondaryVertexV2BJetTags = akSoftDropCh2CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDropCh2CaloPositiveCombinedSecondaryVertexV2BJetTags = akSoftDropCh2CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDropCh2CaloSoftPFMuonsTagInfos = akSoftDropCh2CalobTagger.SoftPFMuonsTagInfos
akSoftDropCh2CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh2CaloSoftPFMuonBJetTags = akSoftDropCh2CalobTagger.SoftPFMuonBJetTags
akSoftDropCh2CaloSoftPFMuonByIP3dBJetTags = akSoftDropCh2CalobTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh2CaloSoftPFMuonByPtBJetTags = akSoftDropCh2CalobTagger.SoftPFMuonByPtBJetTags
akSoftDropCh2CaloNegativeSoftPFMuonByPtBJetTags = akSoftDropCh2CalobTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDropCh2CaloPositiveSoftPFMuonByPtBJetTags = akSoftDropCh2CalobTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDropCh2CaloPatJetFlavourIdLegacy = cms.Sequence(akSoftDropCh2CaloPatJetPartonAssociationLegacy*akSoftDropCh2CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akSoftDropCh2CaloPatJetFlavourAssociation = akSoftDropCh2CalobTagger.PatJetFlavourAssociation
#akSoftDropCh2CaloPatJetFlavourId = cms.Sequence(akSoftDropCh2CaloPatJetPartons*akSoftDropCh2CaloPatJetFlavourAssociation)

akSoftDropCh2CaloJetBtaggingIP       = cms.Sequence(akSoftDropCh2CaloImpactParameterTagInfos *
            (akSoftDropCh2CaloTrackCountingHighEffBJetTags +
             akSoftDropCh2CaloTrackCountingHighPurBJetTags +
             akSoftDropCh2CaloJetProbabilityBJetTags +
             akSoftDropCh2CaloJetBProbabilityBJetTags 
            )
            )

akSoftDropCh2CaloJetBtaggingSV = cms.Sequence(akSoftDropCh2CaloImpactParameterTagInfos
            *
            akSoftDropCh2CaloSecondaryVertexTagInfos
            * (akSoftDropCh2CaloSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh2CaloSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh2CaloCombinedSecondaryVertexBJetTags+
                akSoftDropCh2CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh2CaloJetBtaggingNegSV = cms.Sequence(akSoftDropCh2CaloImpactParameterTagInfos
            *
            akSoftDropCh2CaloSecondaryVertexNegativeTagInfos
            * (akSoftDropCh2CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh2CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh2CaloNegativeCombinedSecondaryVertexBJetTags+
                akSoftDropCh2CaloPositiveCombinedSecondaryVertexBJetTags+
                akSoftDropCh2CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akSoftDropCh2CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh2CaloJetBtaggingMu = cms.Sequence(akSoftDropCh2CaloSoftPFMuonsTagInfos * (akSoftDropCh2CaloSoftPFMuonBJetTags
                +
                akSoftDropCh2CaloSoftPFMuonByIP3dBJetTags
                +
                akSoftDropCh2CaloSoftPFMuonByPtBJetTags
                +
                akSoftDropCh2CaloNegativeSoftPFMuonByPtBJetTags
                +
                akSoftDropCh2CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akSoftDropCh2CaloJetBtagging = cms.Sequence(akSoftDropCh2CaloJetBtaggingIP
            *akSoftDropCh2CaloJetBtaggingSV
            *akSoftDropCh2CaloJetBtaggingNegSV
#            *akSoftDropCh2CaloJetBtaggingMu
            )

akSoftDropCh2CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akSoftDropCh2CaloJets"),
        genJetMatch          = cms.InputTag("akSoftDropCh2Calomatch"),
        genPartonMatch       = cms.InputTag("akSoftDropCh2Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akSoftDropCh2Calocorr")),
        JetPartonMapSource   = cms.InputTag("akSoftDropCh2CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akSoftDropCh2CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akSoftDropCh2CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akSoftDropCh2CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akSoftDropCh2CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akSoftDropCh2CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akSoftDropCh2CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akSoftDropCh2CaloJetBProbabilityBJetTags"),
            cms.InputTag("akSoftDropCh2CaloJetProbabilityBJetTags"),
            #cms.InputTag("akSoftDropCh2CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akSoftDropCh2CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akSoftDropCh2CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akSoftDropCh2CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akSoftDropCh2CaloJetID"),
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

akSoftDropCh2CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akSoftDropCh2CaloJets"),
           	    R0  = cms.double( 0.2)
)
akSoftDropCh2CalopatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh2CaloNjettiness:tau1','akSoftDropCh2CaloNjettiness:tau2','akSoftDropCh2CaloNjettiness:tau3']

akSoftDropCh2CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akSoftDropCh2CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak2HiSignalGenJets',#'ak2HiGenJets',
                                                             rParam = 0.2,
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
                                                             bTagJetName = cms.untracked.string("akSoftDropCh2Calo"),
                                                             jetName = cms.untracked.string("akSoftDropCh2Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropCh2GenJets"),
                                                             doGenTaus = False,
                                                             genTau1 = cms.InputTag("akSoftDropCh2GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropCh2GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropCh2GenNjettiness","tau3"),
                                                             doGenSym = True,
                                                             genSym = cms.InputTag("akSoftDropCh2GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropCh2GenJets","droppedBranches")
                                                             )

akSoftDropCh2CaloJetSequence_mc = cms.Sequence(
                                                  #akSoftDropCh2Caloclean
                                                  #*
                                                  akSoftDropCh2Calomatch
                                                  #*
                                                  #akSoftDropCh2CalomatchGroomed
                                                  *
                                                  akSoftDropCh2Caloparton
                                                  *
                                                  akSoftDropCh2Calocorr
                                                  *
                                                  #akSoftDropCh2CaloJetID
                                                  #*
                                                  akSoftDropCh2CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akSoftDropCh2CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akSoftDropCh2CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akSoftDropCh2CaloJetBtagging
                                                  *
                                                  akSoftDropCh2CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akSoftDropCh2CalopatJetsWithBtagging
                                                  *
                                                  akSoftDropCh2CaloJetAnalyzer
                                                  )

akSoftDropCh2CaloJetSequence_data = cms.Sequence(akSoftDropCh2Calocorr
                                                    *
                                                    #akSoftDropCh2CaloJetID
                                                    #*
                                                    akSoftDropCh2CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akSoftDropCh2CaloJetBtagging
                                                    *
                                                    akSoftDropCh2CaloNjettiness 
                                                    *
                                                    akSoftDropCh2CalopatJetsWithBtagging
                                                    *
                                                    akSoftDropCh2CaloJetAnalyzer
                                                    )

akSoftDropCh2CaloJetSequence_jec = cms.Sequence(akSoftDropCh2CaloJetSequence_mc)
akSoftDropCh2CaloJetSequence_mb = cms.Sequence(akSoftDropCh2CaloJetSequence_mc)

akSoftDropCh2CaloJetSequence = cms.Sequence(akSoftDropCh2CaloJetSequence_data)
akSoftDropCh2CalopatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh2CaloJets:sym']
akSoftDropCh2CalopatJetsWithBtagging.userData.userInts.src += ['akSoftDropCh2CaloJets:droppedBranches']
