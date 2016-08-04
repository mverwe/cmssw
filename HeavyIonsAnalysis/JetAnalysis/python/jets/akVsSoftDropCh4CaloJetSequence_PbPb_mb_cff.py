

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropCh4Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropCh4CaloJets"),
    matched = cms.InputTag("ak4HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.4
    )

akVsSoftDropCh4CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh4HiGenJets"),
    matched = cms.InputTag("ak4HiCleanedGenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.4
    )

akVsSoftDropCh4Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh4CaloJets")
                                                        )

akVsSoftDropCh4Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropCh4CaloJets"),
    payload = "AK4Calo_offline"
    )

akVsSoftDropCh4CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropCh4CaloJets'))

#akVsSoftDropCh4Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak4HiCleanedGenJets'))

akVsSoftDropCh4CalobTagger = bTaggers("akVsSoftDropCh4Calo",0.4)

#create objects locally since they dont load properly otherwise
#akVsSoftDropCh4Calomatch = akVsSoftDropCh4CalobTagger.match
akVsSoftDropCh4Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh4CaloJets"), matched = cms.InputTag("selectedPartons"))
akVsSoftDropCh4CaloPatJetFlavourAssociationLegacy = akVsSoftDropCh4CalobTagger.PatJetFlavourAssociationLegacy
akVsSoftDropCh4CaloPatJetPartons = akVsSoftDropCh4CalobTagger.PatJetPartons
akVsSoftDropCh4CaloJetTracksAssociatorAtVertex = akVsSoftDropCh4CalobTagger.JetTracksAssociatorAtVertex
akVsSoftDropCh4CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropCh4CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh4CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh4CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh4CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh4CaloCombinedSecondaryVertexBJetTags = akVsSoftDropCh4CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh4CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh4CalobTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropCh4CaloJetBProbabilityBJetTags = akVsSoftDropCh4CalobTagger.JetBProbabilityBJetTags
akVsSoftDropCh4CaloSoftPFMuonByPtBJetTags = akVsSoftDropCh4CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh4CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropCh4CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh4CaloTrackCountingHighEffBJetTags = akVsSoftDropCh4CalobTagger.TrackCountingHighEffBJetTags
akVsSoftDropCh4CaloTrackCountingHighPurBJetTags = akVsSoftDropCh4CalobTagger.TrackCountingHighPurBJetTags
akVsSoftDropCh4CaloPatJetPartonAssociationLegacy = akVsSoftDropCh4CalobTagger.PatJetPartonAssociationLegacy

akVsSoftDropCh4CaloImpactParameterTagInfos = akVsSoftDropCh4CalobTagger.ImpactParameterTagInfos
akVsSoftDropCh4CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh4CaloJetProbabilityBJetTags = akVsSoftDropCh4CalobTagger.JetProbabilityBJetTags

akVsSoftDropCh4CaloSecondaryVertexTagInfos = akVsSoftDropCh4CalobTagger.SecondaryVertexTagInfos
akVsSoftDropCh4CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh4CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh4CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh4CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh4CaloCombinedSecondaryVertexBJetTags = akVsSoftDropCh4CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh4CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh4CalobTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropCh4CaloSecondaryVertexNegativeTagInfos = akVsSoftDropCh4CalobTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropCh4CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh4CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh4CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh4CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh4CaloNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropCh4CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropCh4CaloPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropCh4CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropCh4CaloNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh4CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropCh4CaloPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh4CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropCh4CaloSoftPFMuonsTagInfos = akVsSoftDropCh4CalobTagger.SoftPFMuonsTagInfos
akVsSoftDropCh4CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh4CaloSoftPFMuonBJetTags = akVsSoftDropCh4CalobTagger.SoftPFMuonBJetTags
akVsSoftDropCh4CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropCh4CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh4CaloSoftPFMuonByPtBJetTags = akVsSoftDropCh4CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh4CaloNegativeSoftPFMuonByPtBJetTags = akVsSoftDropCh4CalobTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropCh4CaloPositiveSoftPFMuonByPtBJetTags = akVsSoftDropCh4CalobTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropCh4CaloPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropCh4CaloPatJetPartonAssociationLegacy*akVsSoftDropCh4CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropCh4CaloPatJetFlavourAssociation = akVsSoftDropCh4CalobTagger.PatJetFlavourAssociation
#akVsSoftDropCh4CaloPatJetFlavourId = cms.Sequence(akVsSoftDropCh4CaloPatJetPartons*akVsSoftDropCh4CaloPatJetFlavourAssociation)

akVsSoftDropCh4CaloJetBtaggingIP       = cms.Sequence(akVsSoftDropCh4CaloImpactParameterTagInfos *
            (akVsSoftDropCh4CaloTrackCountingHighEffBJetTags +
             akVsSoftDropCh4CaloTrackCountingHighPurBJetTags +
             akVsSoftDropCh4CaloJetProbabilityBJetTags +
             akVsSoftDropCh4CaloJetBProbabilityBJetTags 
            )
            )

akVsSoftDropCh4CaloJetBtaggingSV = cms.Sequence(akVsSoftDropCh4CaloImpactParameterTagInfos
            *
            akVsSoftDropCh4CaloSecondaryVertexTagInfos
            * (akVsSoftDropCh4CaloSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh4CaloSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh4CaloCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh4CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh4CaloJetBtaggingNegSV = cms.Sequence(akVsSoftDropCh4CaloImpactParameterTagInfos
            *
            akVsSoftDropCh4CaloSecondaryVertexNegativeTagInfos
            * (akVsSoftDropCh4CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh4CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh4CaloNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh4CaloPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh4CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropCh4CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh4CaloJetBtaggingMu = cms.Sequence(akVsSoftDropCh4CaloSoftPFMuonsTagInfos * (akVsSoftDropCh4CaloSoftPFMuonBJetTags
                +
                akVsSoftDropCh4CaloSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropCh4CaloSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh4CaloNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh4CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropCh4CaloJetBtagging = cms.Sequence(akVsSoftDropCh4CaloJetBtaggingIP
            *akVsSoftDropCh4CaloJetBtaggingSV
            *akVsSoftDropCh4CaloJetBtaggingNegSV
#            *akVsSoftDropCh4CaloJetBtaggingMu
            )

akVsSoftDropCh4CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropCh4CaloJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropCh4Calomatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropCh4Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropCh4Calocorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropCh4CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropCh4CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropCh4CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropCh4CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh4CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropCh4CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropCh4CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropCh4CaloJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropCh4CaloJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropCh4CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropCh4CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropCh4CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh4CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropCh4CaloJetID"),
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

akVsSoftDropCh4CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropCh4CaloJets"),
           	    R0  = cms.double( 0.4)
)
akVsSoftDropCh4CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh4CaloNjettiness:tau1','akVsSoftDropCh4CaloNjettiness:tau2','akVsSoftDropCh4CaloNjettiness:tau3']

akVsSoftDropCh4CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropCh4CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak4HiCleanedGenJets',#'ak4HiGenJets',
                                                             rParam = 0.4,
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
                                                             bTagJetName = cms.untracked.string("akVsSoftDropCh4Calo"),
                                                             jetName = cms.untracked.string("akVsSoftDropCh4Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
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

akVsSoftDropCh4CaloJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropCh4Caloclean
                                                  #*
                                                  akVsSoftDropCh4Calomatch
                                                  #*
                                                  #akVsSoftDropCh4CalomatchGroomed
                                                  *
                                                  akVsSoftDropCh4Caloparton
                                                  *
                                                  akVsSoftDropCh4Calocorr
                                                  *
                                                  #akVsSoftDropCh4CaloJetID
                                                  #*
                                                  akVsSoftDropCh4CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropCh4CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropCh4CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropCh4CaloJetBtagging
                                                  *
                                                  akVsSoftDropCh4CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropCh4CalopatJetsWithBtagging
                                                  *
                                                  akVsSoftDropCh4CaloJetAnalyzer
                                                  )

akVsSoftDropCh4CaloJetSequence_data = cms.Sequence(akVsSoftDropCh4Calocorr
                                                    *
                                                    #akVsSoftDropCh4CaloJetID
                                                    #*
                                                    akVsSoftDropCh4CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropCh4CaloJetBtagging
                                                    *
                                                    akVsSoftDropCh4CaloNjettiness 
                                                    *
                                                    akVsSoftDropCh4CalopatJetsWithBtagging
                                                    *
                                                    akVsSoftDropCh4CaloJetAnalyzer
                                                    )

akVsSoftDropCh4CaloJetSequence_jec = cms.Sequence(akVsSoftDropCh4CaloJetSequence_mc)
akVsSoftDropCh4CaloJetSequence_mb = cms.Sequence(akVsSoftDropCh4CaloJetSequence_mc)

akVsSoftDropCh4CaloJetSequence = cms.Sequence(akVsSoftDropCh4CaloJetSequence_mb)
akVsSoftDropCh4CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh4CaloJets:sym']
akVsSoftDropCh4CalopatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropCh4CaloJets:droppedBranches']
