

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropCh6Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropCh6CaloJets"),
    matched = cms.InputTag("ak6HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.6
    )

akVsSoftDropCh6CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh6HiGenJets"),
    matched = cms.InputTag("ak6HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.6
    )

akVsSoftDropCh6Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh6CaloJets")
                                                        )

akVsSoftDropCh6Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropCh6CaloJets"),
    payload = "AK6Calo_offline"
    )

akVsSoftDropCh6CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropCh6CaloJets'))

#akVsSoftDropCh6Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak6HiCleanedGenJets'))

akVsSoftDropCh6CalobTagger = bTaggers("akVsSoftDropCh6Calo",0.6)

#create objects locally since they dont load properly otherwise
#akVsSoftDropCh6Calomatch = akVsSoftDropCh6CalobTagger.match
akVsSoftDropCh6Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh6CaloJets"), matched = cms.InputTag("selectedPartons"))
akVsSoftDropCh6CaloPatJetFlavourAssociationLegacy = akVsSoftDropCh6CalobTagger.PatJetFlavourAssociationLegacy
akVsSoftDropCh6CaloPatJetPartons = akVsSoftDropCh6CalobTagger.PatJetPartons
akVsSoftDropCh6CaloJetTracksAssociatorAtVertex = akVsSoftDropCh6CalobTagger.JetTracksAssociatorAtVertex
akVsSoftDropCh6CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropCh6CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh6CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh6CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh6CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh6CaloCombinedSecondaryVertexBJetTags = akVsSoftDropCh6CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh6CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh6CalobTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropCh6CaloJetBProbabilityBJetTags = akVsSoftDropCh6CalobTagger.JetBProbabilityBJetTags
akVsSoftDropCh6CaloSoftPFMuonByPtBJetTags = akVsSoftDropCh6CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh6CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropCh6CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh6CaloTrackCountingHighEffBJetTags = akVsSoftDropCh6CalobTagger.TrackCountingHighEffBJetTags
akVsSoftDropCh6CaloTrackCountingHighPurBJetTags = akVsSoftDropCh6CalobTagger.TrackCountingHighPurBJetTags
akVsSoftDropCh6CaloPatJetPartonAssociationLegacy = akVsSoftDropCh6CalobTagger.PatJetPartonAssociationLegacy

akVsSoftDropCh6CaloImpactParameterTagInfos = akVsSoftDropCh6CalobTagger.ImpactParameterTagInfos
akVsSoftDropCh6CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh6CaloJetProbabilityBJetTags = akVsSoftDropCh6CalobTagger.JetProbabilityBJetTags

akVsSoftDropCh6CaloSecondaryVertexTagInfos = akVsSoftDropCh6CalobTagger.SecondaryVertexTagInfos
akVsSoftDropCh6CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh6CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh6CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh6CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh6CaloCombinedSecondaryVertexBJetTags = akVsSoftDropCh6CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh6CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh6CalobTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropCh6CaloSecondaryVertexNegativeTagInfos = akVsSoftDropCh6CalobTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropCh6CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh6CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh6CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh6CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh6CaloNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropCh6CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropCh6CaloPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropCh6CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropCh6CaloNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh6CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropCh6CaloPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh6CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropCh6CaloSoftPFMuonsTagInfos = akVsSoftDropCh6CalobTagger.SoftPFMuonsTagInfos
akVsSoftDropCh6CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh6CaloSoftPFMuonBJetTags = akVsSoftDropCh6CalobTagger.SoftPFMuonBJetTags
akVsSoftDropCh6CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropCh6CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh6CaloSoftPFMuonByPtBJetTags = akVsSoftDropCh6CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh6CaloNegativeSoftPFMuonByPtBJetTags = akVsSoftDropCh6CalobTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropCh6CaloPositiveSoftPFMuonByPtBJetTags = akVsSoftDropCh6CalobTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropCh6CaloPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropCh6CaloPatJetPartonAssociationLegacy*akVsSoftDropCh6CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropCh6CaloPatJetFlavourAssociation = akVsSoftDropCh6CalobTagger.PatJetFlavourAssociation
#akVsSoftDropCh6CaloPatJetFlavourId = cms.Sequence(akVsSoftDropCh6CaloPatJetPartons*akVsSoftDropCh6CaloPatJetFlavourAssociation)

akVsSoftDropCh6CaloJetBtaggingIP       = cms.Sequence(akVsSoftDropCh6CaloImpactParameterTagInfos *
            (akVsSoftDropCh6CaloTrackCountingHighEffBJetTags +
             akVsSoftDropCh6CaloTrackCountingHighPurBJetTags +
             akVsSoftDropCh6CaloJetProbabilityBJetTags +
             akVsSoftDropCh6CaloJetBProbabilityBJetTags 
            )
            )

akVsSoftDropCh6CaloJetBtaggingSV = cms.Sequence(akVsSoftDropCh6CaloImpactParameterTagInfos
            *
            akVsSoftDropCh6CaloSecondaryVertexTagInfos
            * (akVsSoftDropCh6CaloSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh6CaloSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh6CaloCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh6CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh6CaloJetBtaggingNegSV = cms.Sequence(akVsSoftDropCh6CaloImpactParameterTagInfos
            *
            akVsSoftDropCh6CaloSecondaryVertexNegativeTagInfos
            * (akVsSoftDropCh6CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh6CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh6CaloNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh6CaloPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh6CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropCh6CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh6CaloJetBtaggingMu = cms.Sequence(akVsSoftDropCh6CaloSoftPFMuonsTagInfos * (akVsSoftDropCh6CaloSoftPFMuonBJetTags
                +
                akVsSoftDropCh6CaloSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropCh6CaloSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh6CaloNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh6CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropCh6CaloJetBtagging = cms.Sequence(akVsSoftDropCh6CaloJetBtaggingIP
            *akVsSoftDropCh6CaloJetBtaggingSV
            *akVsSoftDropCh6CaloJetBtaggingNegSV
#            *akVsSoftDropCh6CaloJetBtaggingMu
            )

akVsSoftDropCh6CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropCh6CaloJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropCh6Calomatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropCh6Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropCh6Calocorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropCh6CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropCh6CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropCh6CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropCh6CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh6CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropCh6CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropCh6CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropCh6CaloJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropCh6CaloJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropCh6CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropCh6CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropCh6CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh6CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropCh6CaloJetID"),
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

akVsSoftDropCh6CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropCh6CaloJets"),
           	    R0  = cms.double( 0.6)
)
akVsSoftDropCh6CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh6CaloNjettiness:tau1','akVsSoftDropCh6CaloNjettiness:tau2','akVsSoftDropCh6CaloNjettiness:tau3']

akVsSoftDropCh6CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropCh6CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak6HiCleanedGenJets',#'ak6HiGenJets',
                                                             rParam = 0.6,
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
                                                             bTagJetName = cms.untracked.string("akVsSoftDropCh6Calo"),
                                                             jetName = cms.untracked.string("akVsSoftDropCh6Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropCh6GenJets"),
                                                             doGenTaus = False,
                                                             genTau1 = cms.InputTag("akSoftDropCh6GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropCh6GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropCh6GenNjettiness","tau3"),
                                                             doGenSym = True,
                                                             genSym = cms.InputTag("akSoftDropCh6GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropCh6GenJets","droppedBranches")
                                                             )

akVsSoftDropCh6CaloJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropCh6Caloclean
                                                  #*
                                                  akVsSoftDropCh6Calomatch
                                                  #*
                                                  #akVsSoftDropCh6CalomatchGroomed
                                                  *
                                                  akVsSoftDropCh6Caloparton
                                                  *
                                                  akVsSoftDropCh6Calocorr
                                                  *
                                                  #akVsSoftDropCh6CaloJetID
                                                  #*
                                                  akVsSoftDropCh6CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropCh6CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropCh6CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropCh6CaloJetBtagging
                                                  *
                                                  akVsSoftDropCh6CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropCh6CalopatJetsWithBtagging
                                                  *
                                                  akVsSoftDropCh6CaloJetAnalyzer
                                                  )

akVsSoftDropCh6CaloJetSequence_data = cms.Sequence(akVsSoftDropCh6Calocorr
                                                    *
                                                    #akVsSoftDropCh6CaloJetID
                                                    #*
                                                    akVsSoftDropCh6CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropCh6CaloJetBtagging
                                                    *
                                                    akVsSoftDropCh6CaloNjettiness 
                                                    *
                                                    akVsSoftDropCh6CalopatJetsWithBtagging
                                                    *
                                                    akVsSoftDropCh6CaloJetAnalyzer
                                                    )

akVsSoftDropCh6CaloJetSequence_jec = cms.Sequence(akVsSoftDropCh6CaloJetSequence_mc)
akVsSoftDropCh6CaloJetSequence_mb = cms.Sequence(akVsSoftDropCh6CaloJetSequence_mc)

akVsSoftDropCh6CaloJetSequence = cms.Sequence(akVsSoftDropCh6CaloJetSequence_mb)
akVsSoftDropCh6CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh6CaloJets:sym']
akVsSoftDropCh6CalopatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropCh6CaloJets:droppedBranches']
