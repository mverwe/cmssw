

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPuSoftDropCh2Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPuSoftDropCh2CaloJets"),
    matched = cms.InputTag("ak2HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.2
    )

akPuSoftDropCh2CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh2HiGenJets"),
    matched = cms.InputTag("ak2HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.2
    )

akPuSoftDropCh2Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh2CaloJets")
                                                        )

akPuSoftDropCh2Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akPuSoftDropCh2CaloJets"),
    payload = "AKPu2Calo_offline"
    )

akPuSoftDropCh2CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akPuSoftDropCh2CaloJets'))

#akPuSoftDropCh2Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak2HiSignalGenJets'))

akPuSoftDropCh2CalobTagger = bTaggers("akPuSoftDropCh2Calo",0.2)

#create objects locally since they dont load properly otherwise
#akPuSoftDropCh2Calomatch = akPuSoftDropCh2CalobTagger.match
akPuSoftDropCh2Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh2CaloJets"), matched = cms.InputTag("hiSignalGenParticles"))
akPuSoftDropCh2CaloPatJetFlavourAssociationLegacy = akPuSoftDropCh2CalobTagger.PatJetFlavourAssociationLegacy
akPuSoftDropCh2CaloPatJetPartons = akPuSoftDropCh2CalobTagger.PatJetPartons
akPuSoftDropCh2CaloJetTracksAssociatorAtVertex = akPuSoftDropCh2CalobTagger.JetTracksAssociatorAtVertex
akPuSoftDropCh2CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPuSoftDropCh2CaloSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh2CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh2CaloSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh2CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh2CaloCombinedSecondaryVertexBJetTags = akPuSoftDropCh2CalobTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh2CaloCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh2CalobTagger.CombinedSecondaryVertexV2BJetTags
akPuSoftDropCh2CaloJetBProbabilityBJetTags = akPuSoftDropCh2CalobTagger.JetBProbabilityBJetTags
akPuSoftDropCh2CaloSoftPFMuonByPtBJetTags = akPuSoftDropCh2CalobTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh2CaloSoftPFMuonByIP3dBJetTags = akPuSoftDropCh2CalobTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh2CaloTrackCountingHighEffBJetTags = akPuSoftDropCh2CalobTagger.TrackCountingHighEffBJetTags
akPuSoftDropCh2CaloTrackCountingHighPurBJetTags = akPuSoftDropCh2CalobTagger.TrackCountingHighPurBJetTags
akPuSoftDropCh2CaloPatJetPartonAssociationLegacy = akPuSoftDropCh2CalobTagger.PatJetPartonAssociationLegacy

akPuSoftDropCh2CaloImpactParameterTagInfos = akPuSoftDropCh2CalobTagger.ImpactParameterTagInfos
akPuSoftDropCh2CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh2CaloJetProbabilityBJetTags = akPuSoftDropCh2CalobTagger.JetProbabilityBJetTags

akPuSoftDropCh2CaloSecondaryVertexTagInfos = akPuSoftDropCh2CalobTagger.SecondaryVertexTagInfos
akPuSoftDropCh2CaloSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh2CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh2CaloSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh2CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh2CaloCombinedSecondaryVertexBJetTags = akPuSoftDropCh2CalobTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh2CaloCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh2CalobTagger.CombinedSecondaryVertexV2BJetTags

akPuSoftDropCh2CaloSecondaryVertexNegativeTagInfos = akPuSoftDropCh2CalobTagger.SecondaryVertexNegativeTagInfos
akPuSoftDropCh2CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh2CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh2CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh2CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh2CaloNegativeCombinedSecondaryVertexBJetTags = akPuSoftDropCh2CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akPuSoftDropCh2CaloPositiveCombinedSecondaryVertexBJetTags = akPuSoftDropCh2CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akPuSoftDropCh2CaloNegativeCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh2CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPuSoftDropCh2CaloPositiveCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh2CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPuSoftDropCh2CaloSoftPFMuonsTagInfos = akPuSoftDropCh2CalobTagger.SoftPFMuonsTagInfos
akPuSoftDropCh2CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh2CaloSoftPFMuonBJetTags = akPuSoftDropCh2CalobTagger.SoftPFMuonBJetTags
akPuSoftDropCh2CaloSoftPFMuonByIP3dBJetTags = akPuSoftDropCh2CalobTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh2CaloSoftPFMuonByPtBJetTags = akPuSoftDropCh2CalobTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh2CaloNegativeSoftPFMuonByPtBJetTags = akPuSoftDropCh2CalobTagger.NegativeSoftPFMuonByPtBJetTags
akPuSoftDropCh2CaloPositiveSoftPFMuonByPtBJetTags = akPuSoftDropCh2CalobTagger.PositiveSoftPFMuonByPtBJetTags
akPuSoftDropCh2CaloPatJetFlavourIdLegacy = cms.Sequence(akPuSoftDropCh2CaloPatJetPartonAssociationLegacy*akPuSoftDropCh2CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akPuSoftDropCh2CaloPatJetFlavourAssociation = akPuSoftDropCh2CalobTagger.PatJetFlavourAssociation
#akPuSoftDropCh2CaloPatJetFlavourId = cms.Sequence(akPuSoftDropCh2CaloPatJetPartons*akPuSoftDropCh2CaloPatJetFlavourAssociation)

akPuSoftDropCh2CaloJetBtaggingIP       = cms.Sequence(akPuSoftDropCh2CaloImpactParameterTagInfos *
            (akPuSoftDropCh2CaloTrackCountingHighEffBJetTags +
             akPuSoftDropCh2CaloTrackCountingHighPurBJetTags +
             akPuSoftDropCh2CaloJetProbabilityBJetTags +
             akPuSoftDropCh2CaloJetBProbabilityBJetTags 
            )
            )

akPuSoftDropCh2CaloJetBtaggingSV = cms.Sequence(akPuSoftDropCh2CaloImpactParameterTagInfos
            *
            akPuSoftDropCh2CaloSecondaryVertexTagInfos
            * (akPuSoftDropCh2CaloSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh2CaloSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh2CaloCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh2CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh2CaloJetBtaggingNegSV = cms.Sequence(akPuSoftDropCh2CaloImpactParameterTagInfos
            *
            akPuSoftDropCh2CaloSecondaryVertexNegativeTagInfos
            * (akPuSoftDropCh2CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh2CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh2CaloNegativeCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh2CaloPositiveCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh2CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akPuSoftDropCh2CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh2CaloJetBtaggingMu = cms.Sequence(akPuSoftDropCh2CaloSoftPFMuonsTagInfos * (akPuSoftDropCh2CaloSoftPFMuonBJetTags
                +
                akPuSoftDropCh2CaloSoftPFMuonByIP3dBJetTags
                +
                akPuSoftDropCh2CaloSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh2CaloNegativeSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh2CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akPuSoftDropCh2CaloJetBtagging = cms.Sequence(akPuSoftDropCh2CaloJetBtaggingIP
            *akPuSoftDropCh2CaloJetBtaggingSV
            *akPuSoftDropCh2CaloJetBtaggingNegSV
#            *akPuSoftDropCh2CaloJetBtaggingMu
            )

akPuSoftDropCh2CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akPuSoftDropCh2CaloJets"),
        genJetMatch          = cms.InputTag("akPuSoftDropCh2Calomatch"),
        genPartonMatch       = cms.InputTag("akPuSoftDropCh2Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPuSoftDropCh2Calocorr")),
        JetPartonMapSource   = cms.InputTag("akPuSoftDropCh2CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akPuSoftDropCh2CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPuSoftDropCh2CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akPuSoftDropCh2CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh2CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPuSoftDropCh2CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPuSoftDropCh2CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akPuSoftDropCh2CaloJetBProbabilityBJetTags"),
            cms.InputTag("akPuSoftDropCh2CaloJetProbabilityBJetTags"),
            #cms.InputTag("akPuSoftDropCh2CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akPuSoftDropCh2CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akPuSoftDropCh2CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh2CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPuSoftDropCh2CaloJetID"),
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

akPuSoftDropCh2CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akPuSoftDropCh2CaloJets"),
           	    R0  = cms.double( 0.2)
)
akPuSoftDropCh2CalopatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh2CaloNjettiness:tau1','akPuSoftDropCh2CaloNjettiness:tau2','akPuSoftDropCh2CaloNjettiness:tau3']

akPuSoftDropCh2CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPuSoftDropCh2CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak2HiSignalGenJets',#'ak2HiGenJets',
                                                             rParam = 0.2,
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
                                                             bTagJetName = cms.untracked.string("akPuSoftDropCh2Calo"),
                                                             jetName = cms.untracked.string("akPuSoftDropCh2Calo"),
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

akPuSoftDropCh2CaloJetSequence_mc = cms.Sequence(
                                                  #akPuSoftDropCh2Caloclean
                                                  #*
                                                  akPuSoftDropCh2Calomatch
                                                  #*
                                                  #akPuSoftDropCh2CalomatchGroomed
                                                  *
                                                  akPuSoftDropCh2Caloparton
                                                  *
                                                  akPuSoftDropCh2Calocorr
                                                  *
                                                  #akPuSoftDropCh2CaloJetID
                                                  #*
                                                  akPuSoftDropCh2CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akPuSoftDropCh2CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akPuSoftDropCh2CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akPuSoftDropCh2CaloJetBtagging
                                                  *
                                                  akPuSoftDropCh2CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akPuSoftDropCh2CalopatJetsWithBtagging
                                                  *
                                                  akPuSoftDropCh2CaloJetAnalyzer
                                                  )

akPuSoftDropCh2CaloJetSequence_data = cms.Sequence(akPuSoftDropCh2Calocorr
                                                    *
                                                    #akPuSoftDropCh2CaloJetID
                                                    #*
                                                    akPuSoftDropCh2CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akPuSoftDropCh2CaloJetBtagging
                                                    *
                                                    akPuSoftDropCh2CaloNjettiness 
                                                    *
                                                    akPuSoftDropCh2CalopatJetsWithBtagging
                                                    *
                                                    akPuSoftDropCh2CaloJetAnalyzer
                                                    )

akPuSoftDropCh2CaloJetSequence_jec = cms.Sequence(akPuSoftDropCh2CaloJetSequence_mc)
akPuSoftDropCh2CaloJetSequence_mb = cms.Sequence(akPuSoftDropCh2CaloJetSequence_mc)

akPuSoftDropCh2CaloJetSequence = cms.Sequence(akPuSoftDropCh2CaloJetSequence_jec)
akPuSoftDropCh2CaloJetAnalyzer.genPtMin = cms.untracked.double(1)
akPuSoftDropCh2CaloJetAnalyzer.jetPtMin = cms.double(1)
akPuSoftDropCh2CalopatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh2CaloJets:sym']
akPuSoftDropCh2CalopatJetsWithBtagging.userData.userInts.src += ['akPuSoftDropCh2CaloJets:droppedBranches']
