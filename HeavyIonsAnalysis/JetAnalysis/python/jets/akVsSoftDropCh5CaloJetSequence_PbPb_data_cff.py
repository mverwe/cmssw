

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropCh5Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropCh5CaloJets"),
    matched = cms.InputTag("ak5HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.5
    )

akVsSoftDropCh5CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh5HiGenJets"),
    matched = cms.InputTag("ak5HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.5
    )

akVsSoftDropCh5Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh5CaloJets")
                                                        )

akVsSoftDropCh5Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropCh5CaloJets"),
    payload = "AK5Calo_offline"
    )

akVsSoftDropCh5CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropCh5CaloJets'))

#akVsSoftDropCh5Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak5HiSignalGenJets'))

akVsSoftDropCh5CalobTagger = bTaggers("akVsSoftDropCh5Calo",0.5)

#create objects locally since they dont load properly otherwise
#akVsSoftDropCh5Calomatch = akVsSoftDropCh5CalobTagger.match
akVsSoftDropCh5Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh5CaloJets"), matched = cms.InputTag("hiSignalGenParticles"))
akVsSoftDropCh5CaloPatJetFlavourAssociationLegacy = akVsSoftDropCh5CalobTagger.PatJetFlavourAssociationLegacy
akVsSoftDropCh5CaloPatJetPartons = akVsSoftDropCh5CalobTagger.PatJetPartons
akVsSoftDropCh5CaloJetTracksAssociatorAtVertex = akVsSoftDropCh5CalobTagger.JetTracksAssociatorAtVertex
akVsSoftDropCh5CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropCh5CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh5CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh5CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh5CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh5CaloCombinedSecondaryVertexBJetTags = akVsSoftDropCh5CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh5CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh5CalobTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropCh5CaloJetBProbabilityBJetTags = akVsSoftDropCh5CalobTagger.JetBProbabilityBJetTags
akVsSoftDropCh5CaloSoftPFMuonByPtBJetTags = akVsSoftDropCh5CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh5CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropCh5CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh5CaloTrackCountingHighEffBJetTags = akVsSoftDropCh5CalobTagger.TrackCountingHighEffBJetTags
akVsSoftDropCh5CaloTrackCountingHighPurBJetTags = akVsSoftDropCh5CalobTagger.TrackCountingHighPurBJetTags
akVsSoftDropCh5CaloPatJetPartonAssociationLegacy = akVsSoftDropCh5CalobTagger.PatJetPartonAssociationLegacy

akVsSoftDropCh5CaloImpactParameterTagInfos = akVsSoftDropCh5CalobTagger.ImpactParameterTagInfos
akVsSoftDropCh5CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh5CaloJetProbabilityBJetTags = akVsSoftDropCh5CalobTagger.JetProbabilityBJetTags

akVsSoftDropCh5CaloSecondaryVertexTagInfos = akVsSoftDropCh5CalobTagger.SecondaryVertexTagInfos
akVsSoftDropCh5CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh5CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh5CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh5CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh5CaloCombinedSecondaryVertexBJetTags = akVsSoftDropCh5CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh5CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh5CalobTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropCh5CaloSecondaryVertexNegativeTagInfos = akVsSoftDropCh5CalobTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropCh5CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh5CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh5CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh5CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh5CaloNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropCh5CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropCh5CaloPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropCh5CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropCh5CaloNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh5CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropCh5CaloPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh5CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropCh5CaloSoftPFMuonsTagInfos = akVsSoftDropCh5CalobTagger.SoftPFMuonsTagInfos
akVsSoftDropCh5CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh5CaloSoftPFMuonBJetTags = akVsSoftDropCh5CalobTagger.SoftPFMuonBJetTags
akVsSoftDropCh5CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropCh5CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh5CaloSoftPFMuonByPtBJetTags = akVsSoftDropCh5CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh5CaloNegativeSoftPFMuonByPtBJetTags = akVsSoftDropCh5CalobTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropCh5CaloPositiveSoftPFMuonByPtBJetTags = akVsSoftDropCh5CalobTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropCh5CaloPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropCh5CaloPatJetPartonAssociationLegacy*akVsSoftDropCh5CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropCh5CaloPatJetFlavourAssociation = akVsSoftDropCh5CalobTagger.PatJetFlavourAssociation
#akVsSoftDropCh5CaloPatJetFlavourId = cms.Sequence(akVsSoftDropCh5CaloPatJetPartons*akVsSoftDropCh5CaloPatJetFlavourAssociation)

akVsSoftDropCh5CaloJetBtaggingIP       = cms.Sequence(akVsSoftDropCh5CaloImpactParameterTagInfos *
            (akVsSoftDropCh5CaloTrackCountingHighEffBJetTags +
             akVsSoftDropCh5CaloTrackCountingHighPurBJetTags +
             akVsSoftDropCh5CaloJetProbabilityBJetTags +
             akVsSoftDropCh5CaloJetBProbabilityBJetTags 
            )
            )

akVsSoftDropCh5CaloJetBtaggingSV = cms.Sequence(akVsSoftDropCh5CaloImpactParameterTagInfos
            *
            akVsSoftDropCh5CaloSecondaryVertexTagInfos
            * (akVsSoftDropCh5CaloSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh5CaloSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh5CaloCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh5CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh5CaloJetBtaggingNegSV = cms.Sequence(akVsSoftDropCh5CaloImpactParameterTagInfos
            *
            akVsSoftDropCh5CaloSecondaryVertexNegativeTagInfos
            * (akVsSoftDropCh5CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh5CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh5CaloNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh5CaloPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh5CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropCh5CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh5CaloJetBtaggingMu = cms.Sequence(akVsSoftDropCh5CaloSoftPFMuonsTagInfos * (akVsSoftDropCh5CaloSoftPFMuonBJetTags
                +
                akVsSoftDropCh5CaloSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropCh5CaloSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh5CaloNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh5CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropCh5CaloJetBtagging = cms.Sequence(akVsSoftDropCh5CaloJetBtaggingIP
            *akVsSoftDropCh5CaloJetBtaggingSV
            *akVsSoftDropCh5CaloJetBtaggingNegSV
#            *akVsSoftDropCh5CaloJetBtaggingMu
            )

akVsSoftDropCh5CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropCh5CaloJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropCh5Calomatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropCh5Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropCh5Calocorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropCh5CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropCh5CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropCh5CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropCh5CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh5CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropCh5CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropCh5CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropCh5CaloJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropCh5CaloJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropCh5CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropCh5CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropCh5CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh5CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropCh5CaloJetID"),
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

akVsSoftDropCh5CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropCh5CaloJets"),
           	    R0  = cms.double( 0.5)
)
akVsSoftDropCh5CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh5CaloNjettiness:tau1','akVsSoftDropCh5CaloNjettiness:tau2','akVsSoftDropCh5CaloNjettiness:tau3']

akVsSoftDropCh5CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropCh5CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak5HiSignalGenJets',#'ak5HiGenJets',
                                                             rParam = 0.5,
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
                                                             bTagJetName = cms.untracked.string("akVsSoftDropCh5Calo"),
                                                             jetName = cms.untracked.string("akVsSoftDropCh5Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropCh5GenJets"),
                                                             doGenTaus = False,
                                                             genTau1 = cms.InputTag("akSoftDropCh5GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropCh5GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropCh5GenNjettiness","tau3"),
                                                             doGenSym = True,
                                                             genSym = cms.InputTag("akSoftDropCh5GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropCh5GenJets","droppedBranches")
                                                             )

akVsSoftDropCh5CaloJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropCh5Caloclean
                                                  #*
                                                  akVsSoftDropCh5Calomatch
                                                  #*
                                                  #akVsSoftDropCh5CalomatchGroomed
                                                  *
                                                  akVsSoftDropCh5Caloparton
                                                  *
                                                  akVsSoftDropCh5Calocorr
                                                  *
                                                  #akVsSoftDropCh5CaloJetID
                                                  #*
                                                  akVsSoftDropCh5CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropCh5CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropCh5CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropCh5CaloJetBtagging
                                                  *
                                                  akVsSoftDropCh5CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropCh5CalopatJetsWithBtagging
                                                  *
                                                  akVsSoftDropCh5CaloJetAnalyzer
                                                  )

akVsSoftDropCh5CaloJetSequence_data = cms.Sequence(akVsSoftDropCh5Calocorr
                                                    *
                                                    #akVsSoftDropCh5CaloJetID
                                                    #*
                                                    akVsSoftDropCh5CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropCh5CaloJetBtagging
                                                    *
                                                    akVsSoftDropCh5CaloNjettiness 
                                                    *
                                                    akVsSoftDropCh5CalopatJetsWithBtagging
                                                    *
                                                    akVsSoftDropCh5CaloJetAnalyzer
                                                    )

akVsSoftDropCh5CaloJetSequence_jec = cms.Sequence(akVsSoftDropCh5CaloJetSequence_mc)
akVsSoftDropCh5CaloJetSequence_mb = cms.Sequence(akVsSoftDropCh5CaloJetSequence_mc)

akVsSoftDropCh5CaloJetSequence = cms.Sequence(akVsSoftDropCh5CaloJetSequence_data)
akVsSoftDropCh5CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh5CaloJets:sym']
akVsSoftDropCh5CalopatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropCh5CaloJets:droppedBranches']
