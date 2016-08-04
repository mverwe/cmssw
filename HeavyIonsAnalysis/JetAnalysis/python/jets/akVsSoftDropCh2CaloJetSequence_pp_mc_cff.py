

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropCh2Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropCh2CaloJets"),
    matched = cms.InputTag("ak2GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.2
    )

akVsSoftDropCh2CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh2GenJets"),
    matched = cms.InputTag("ak2GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.2
    )

akVsSoftDropCh2Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh2CaloJets")
                                                        )

akVsSoftDropCh2Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropCh2CaloJets"),
    payload = "AK2Calo_offline"
    )

akVsSoftDropCh2CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropCh2CaloJets'))

#akVsSoftDropCh2Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak2GenJets'))

akVsSoftDropCh2CalobTagger = bTaggers("akVsSoftDropCh2Calo",0.2)

#create objects locally since they dont load properly otherwise
#akVsSoftDropCh2Calomatch = akVsSoftDropCh2CalobTagger.match
akVsSoftDropCh2Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh2CaloJets"), matched = cms.InputTag("genParticles"))
akVsSoftDropCh2CaloPatJetFlavourAssociationLegacy = akVsSoftDropCh2CalobTagger.PatJetFlavourAssociationLegacy
akVsSoftDropCh2CaloPatJetPartons = akVsSoftDropCh2CalobTagger.PatJetPartons
akVsSoftDropCh2CaloJetTracksAssociatorAtVertex = akVsSoftDropCh2CalobTagger.JetTracksAssociatorAtVertex
akVsSoftDropCh2CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropCh2CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh2CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh2CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh2CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh2CaloCombinedSecondaryVertexBJetTags = akVsSoftDropCh2CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh2CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh2CalobTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropCh2CaloJetBProbabilityBJetTags = akVsSoftDropCh2CalobTagger.JetBProbabilityBJetTags
akVsSoftDropCh2CaloSoftPFMuonByPtBJetTags = akVsSoftDropCh2CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh2CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropCh2CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh2CaloTrackCountingHighEffBJetTags = akVsSoftDropCh2CalobTagger.TrackCountingHighEffBJetTags
akVsSoftDropCh2CaloTrackCountingHighPurBJetTags = akVsSoftDropCh2CalobTagger.TrackCountingHighPurBJetTags
akVsSoftDropCh2CaloPatJetPartonAssociationLegacy = akVsSoftDropCh2CalobTagger.PatJetPartonAssociationLegacy

akVsSoftDropCh2CaloImpactParameterTagInfos = akVsSoftDropCh2CalobTagger.ImpactParameterTagInfos
akVsSoftDropCh2CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh2CaloJetProbabilityBJetTags = akVsSoftDropCh2CalobTagger.JetProbabilityBJetTags

akVsSoftDropCh2CaloSecondaryVertexTagInfos = akVsSoftDropCh2CalobTagger.SecondaryVertexTagInfos
akVsSoftDropCh2CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh2CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh2CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh2CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh2CaloCombinedSecondaryVertexBJetTags = akVsSoftDropCh2CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh2CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh2CalobTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropCh2CaloSecondaryVertexNegativeTagInfos = akVsSoftDropCh2CalobTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropCh2CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh2CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh2CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh2CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh2CaloNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropCh2CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropCh2CaloPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropCh2CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropCh2CaloNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh2CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropCh2CaloPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh2CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropCh2CaloSoftPFMuonsTagInfos = akVsSoftDropCh2CalobTagger.SoftPFMuonsTagInfos
akVsSoftDropCh2CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh2CaloSoftPFMuonBJetTags = akVsSoftDropCh2CalobTagger.SoftPFMuonBJetTags
akVsSoftDropCh2CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropCh2CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh2CaloSoftPFMuonByPtBJetTags = akVsSoftDropCh2CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh2CaloNegativeSoftPFMuonByPtBJetTags = akVsSoftDropCh2CalobTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropCh2CaloPositiveSoftPFMuonByPtBJetTags = akVsSoftDropCh2CalobTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropCh2CaloPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropCh2CaloPatJetPartonAssociationLegacy*akVsSoftDropCh2CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropCh2CaloPatJetFlavourAssociation = akVsSoftDropCh2CalobTagger.PatJetFlavourAssociation
#akVsSoftDropCh2CaloPatJetFlavourId = cms.Sequence(akVsSoftDropCh2CaloPatJetPartons*akVsSoftDropCh2CaloPatJetFlavourAssociation)

akVsSoftDropCh2CaloJetBtaggingIP       = cms.Sequence(akVsSoftDropCh2CaloImpactParameterTagInfos *
            (akVsSoftDropCh2CaloTrackCountingHighEffBJetTags +
             akVsSoftDropCh2CaloTrackCountingHighPurBJetTags +
             akVsSoftDropCh2CaloJetProbabilityBJetTags +
             akVsSoftDropCh2CaloJetBProbabilityBJetTags 
            )
            )

akVsSoftDropCh2CaloJetBtaggingSV = cms.Sequence(akVsSoftDropCh2CaloImpactParameterTagInfos
            *
            akVsSoftDropCh2CaloSecondaryVertexTagInfos
            * (akVsSoftDropCh2CaloSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh2CaloSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh2CaloCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh2CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh2CaloJetBtaggingNegSV = cms.Sequence(akVsSoftDropCh2CaloImpactParameterTagInfos
            *
            akVsSoftDropCh2CaloSecondaryVertexNegativeTagInfos
            * (akVsSoftDropCh2CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh2CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh2CaloNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh2CaloPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh2CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropCh2CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh2CaloJetBtaggingMu = cms.Sequence(akVsSoftDropCh2CaloSoftPFMuonsTagInfos * (akVsSoftDropCh2CaloSoftPFMuonBJetTags
                +
                akVsSoftDropCh2CaloSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropCh2CaloSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh2CaloNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh2CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropCh2CaloJetBtagging = cms.Sequence(akVsSoftDropCh2CaloJetBtaggingIP
            *akVsSoftDropCh2CaloJetBtaggingSV
            *akVsSoftDropCh2CaloJetBtaggingNegSV
#            *akVsSoftDropCh2CaloJetBtaggingMu
            )

akVsSoftDropCh2CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropCh2CaloJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropCh2Calomatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropCh2Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropCh2Calocorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropCh2CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropCh2CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropCh2CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropCh2CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh2CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropCh2CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropCh2CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropCh2CaloJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropCh2CaloJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropCh2CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropCh2CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropCh2CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh2CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropCh2CaloJetID"),
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

akVsSoftDropCh2CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropCh2CaloJets"),
           	    R0  = cms.double( 0.2)
)
akVsSoftDropCh2CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh2CaloNjettiness:tau1','akVsSoftDropCh2CaloNjettiness:tau2','akVsSoftDropCh2CaloNjettiness:tau3']

akVsSoftDropCh2CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropCh2CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak2GenJets',#'ak2GenJets',
                                                             rParam = 0.2,
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
                                                             bTagJetName = cms.untracked.string("akVsSoftDropCh2Calo"),
                                                             jetName = cms.untracked.string("akVsSoftDropCh2Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(False),
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

akVsSoftDropCh2CaloJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropCh2Caloclean
                                                  #*
                                                  akVsSoftDropCh2Calomatch
                                                  #*
                                                  #akVsSoftDropCh2CalomatchGroomed
                                                  *
                                                  akVsSoftDropCh2Caloparton
                                                  *
                                                  akVsSoftDropCh2Calocorr
                                                  *
                                                  #akVsSoftDropCh2CaloJetID
                                                  #*
                                                  akVsSoftDropCh2CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropCh2CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropCh2CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropCh2CaloJetBtagging
                                                  *
                                                  akVsSoftDropCh2CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropCh2CalopatJetsWithBtagging
                                                  *
                                                  akVsSoftDropCh2CaloJetAnalyzer
                                                  )

akVsSoftDropCh2CaloJetSequence_data = cms.Sequence(akVsSoftDropCh2Calocorr
                                                    *
                                                    #akVsSoftDropCh2CaloJetID
                                                    #*
                                                    akVsSoftDropCh2CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropCh2CaloJetBtagging
                                                    *
                                                    akVsSoftDropCh2CaloNjettiness 
                                                    *
                                                    akVsSoftDropCh2CalopatJetsWithBtagging
                                                    *
                                                    akVsSoftDropCh2CaloJetAnalyzer
                                                    )

akVsSoftDropCh2CaloJetSequence_jec = cms.Sequence(akVsSoftDropCh2CaloJetSequence_mc)
akVsSoftDropCh2CaloJetSequence_mb = cms.Sequence(akVsSoftDropCh2CaloJetSequence_mc)

akVsSoftDropCh2CaloJetSequence = cms.Sequence(akVsSoftDropCh2CaloJetSequence_mc)
akVsSoftDropCh2CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh2CaloJets:sym']
akVsSoftDropCh2CalopatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropCh2CaloJets:droppedBranches']
