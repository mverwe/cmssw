

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPuSoftDropCh3Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPuSoftDropCh3CaloJets"),
    matched = cms.InputTag("ak3HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.3
    )

akPuSoftDropCh3CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh3HiGenJets"),
    matched = cms.InputTag("ak3HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.3
    )

akPuSoftDropCh3Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh3CaloJets")
                                                        )

akPuSoftDropCh3Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akPuSoftDropCh3CaloJets"),
    payload = "AKPu3Calo_offline"
    )

akPuSoftDropCh3CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akPuSoftDropCh3CaloJets'))

#akPuSoftDropCh3Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak3HiSignalGenJets'))

akPuSoftDropCh3CalobTagger = bTaggers("akPuSoftDropCh3Calo",0.3)

#create objects locally since they dont load properly otherwise
#akPuSoftDropCh3Calomatch = akPuSoftDropCh3CalobTagger.match
akPuSoftDropCh3Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh3CaloJets"), matched = cms.InputTag("hiSignalGenParticles"))
akPuSoftDropCh3CaloPatJetFlavourAssociationLegacy = akPuSoftDropCh3CalobTagger.PatJetFlavourAssociationLegacy
akPuSoftDropCh3CaloPatJetPartons = akPuSoftDropCh3CalobTagger.PatJetPartons
akPuSoftDropCh3CaloJetTracksAssociatorAtVertex = akPuSoftDropCh3CalobTagger.JetTracksAssociatorAtVertex
akPuSoftDropCh3CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPuSoftDropCh3CaloSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh3CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh3CaloSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh3CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh3CaloCombinedSecondaryVertexBJetTags = akPuSoftDropCh3CalobTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh3CaloCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh3CalobTagger.CombinedSecondaryVertexV2BJetTags
akPuSoftDropCh3CaloJetBProbabilityBJetTags = akPuSoftDropCh3CalobTagger.JetBProbabilityBJetTags
akPuSoftDropCh3CaloSoftPFMuonByPtBJetTags = akPuSoftDropCh3CalobTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh3CaloSoftPFMuonByIP3dBJetTags = akPuSoftDropCh3CalobTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh3CaloTrackCountingHighEffBJetTags = akPuSoftDropCh3CalobTagger.TrackCountingHighEffBJetTags
akPuSoftDropCh3CaloTrackCountingHighPurBJetTags = akPuSoftDropCh3CalobTagger.TrackCountingHighPurBJetTags
akPuSoftDropCh3CaloPatJetPartonAssociationLegacy = akPuSoftDropCh3CalobTagger.PatJetPartonAssociationLegacy

akPuSoftDropCh3CaloImpactParameterTagInfos = akPuSoftDropCh3CalobTagger.ImpactParameterTagInfos
akPuSoftDropCh3CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh3CaloJetProbabilityBJetTags = akPuSoftDropCh3CalobTagger.JetProbabilityBJetTags

akPuSoftDropCh3CaloSecondaryVertexTagInfos = akPuSoftDropCh3CalobTagger.SecondaryVertexTagInfos
akPuSoftDropCh3CaloSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh3CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh3CaloSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh3CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh3CaloCombinedSecondaryVertexBJetTags = akPuSoftDropCh3CalobTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh3CaloCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh3CalobTagger.CombinedSecondaryVertexV2BJetTags

akPuSoftDropCh3CaloSecondaryVertexNegativeTagInfos = akPuSoftDropCh3CalobTagger.SecondaryVertexNegativeTagInfos
akPuSoftDropCh3CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh3CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh3CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh3CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh3CaloNegativeCombinedSecondaryVertexBJetTags = akPuSoftDropCh3CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akPuSoftDropCh3CaloPositiveCombinedSecondaryVertexBJetTags = akPuSoftDropCh3CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akPuSoftDropCh3CaloNegativeCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh3CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPuSoftDropCh3CaloPositiveCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh3CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPuSoftDropCh3CaloSoftPFMuonsTagInfos = akPuSoftDropCh3CalobTagger.SoftPFMuonsTagInfos
akPuSoftDropCh3CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh3CaloSoftPFMuonBJetTags = akPuSoftDropCh3CalobTagger.SoftPFMuonBJetTags
akPuSoftDropCh3CaloSoftPFMuonByIP3dBJetTags = akPuSoftDropCh3CalobTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh3CaloSoftPFMuonByPtBJetTags = akPuSoftDropCh3CalobTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh3CaloNegativeSoftPFMuonByPtBJetTags = akPuSoftDropCh3CalobTagger.NegativeSoftPFMuonByPtBJetTags
akPuSoftDropCh3CaloPositiveSoftPFMuonByPtBJetTags = akPuSoftDropCh3CalobTagger.PositiveSoftPFMuonByPtBJetTags
akPuSoftDropCh3CaloPatJetFlavourIdLegacy = cms.Sequence(akPuSoftDropCh3CaloPatJetPartonAssociationLegacy*akPuSoftDropCh3CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akPuSoftDropCh3CaloPatJetFlavourAssociation = akPuSoftDropCh3CalobTagger.PatJetFlavourAssociation
#akPuSoftDropCh3CaloPatJetFlavourId = cms.Sequence(akPuSoftDropCh3CaloPatJetPartons*akPuSoftDropCh3CaloPatJetFlavourAssociation)

akPuSoftDropCh3CaloJetBtaggingIP       = cms.Sequence(akPuSoftDropCh3CaloImpactParameterTagInfos *
            (akPuSoftDropCh3CaloTrackCountingHighEffBJetTags +
             akPuSoftDropCh3CaloTrackCountingHighPurBJetTags +
             akPuSoftDropCh3CaloJetProbabilityBJetTags +
             akPuSoftDropCh3CaloJetBProbabilityBJetTags 
            )
            )

akPuSoftDropCh3CaloJetBtaggingSV = cms.Sequence(akPuSoftDropCh3CaloImpactParameterTagInfos
            *
            akPuSoftDropCh3CaloSecondaryVertexTagInfos
            * (akPuSoftDropCh3CaloSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh3CaloSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh3CaloCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh3CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh3CaloJetBtaggingNegSV = cms.Sequence(akPuSoftDropCh3CaloImpactParameterTagInfos
            *
            akPuSoftDropCh3CaloSecondaryVertexNegativeTagInfos
            * (akPuSoftDropCh3CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh3CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh3CaloNegativeCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh3CaloPositiveCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh3CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akPuSoftDropCh3CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh3CaloJetBtaggingMu = cms.Sequence(akPuSoftDropCh3CaloSoftPFMuonsTagInfos * (akPuSoftDropCh3CaloSoftPFMuonBJetTags
                +
                akPuSoftDropCh3CaloSoftPFMuonByIP3dBJetTags
                +
                akPuSoftDropCh3CaloSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh3CaloNegativeSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh3CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akPuSoftDropCh3CaloJetBtagging = cms.Sequence(akPuSoftDropCh3CaloJetBtaggingIP
            *akPuSoftDropCh3CaloJetBtaggingSV
            *akPuSoftDropCh3CaloJetBtaggingNegSV
#            *akPuSoftDropCh3CaloJetBtaggingMu
            )

akPuSoftDropCh3CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akPuSoftDropCh3CaloJets"),
        genJetMatch          = cms.InputTag("akPuSoftDropCh3Calomatch"),
        genPartonMatch       = cms.InputTag("akPuSoftDropCh3Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPuSoftDropCh3Calocorr")),
        JetPartonMapSource   = cms.InputTag("akPuSoftDropCh3CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akPuSoftDropCh3CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPuSoftDropCh3CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akPuSoftDropCh3CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh3CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPuSoftDropCh3CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPuSoftDropCh3CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akPuSoftDropCh3CaloJetBProbabilityBJetTags"),
            cms.InputTag("akPuSoftDropCh3CaloJetProbabilityBJetTags"),
            #cms.InputTag("akPuSoftDropCh3CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akPuSoftDropCh3CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akPuSoftDropCh3CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh3CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPuSoftDropCh3CaloJetID"),
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

akPuSoftDropCh3CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akPuSoftDropCh3CaloJets"),
           	    R0  = cms.double( 0.3)
)
akPuSoftDropCh3CalopatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh3CaloNjettiness:tau1','akPuSoftDropCh3CaloNjettiness:tau2','akPuSoftDropCh3CaloNjettiness:tau3']

akPuSoftDropCh3CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPuSoftDropCh3CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak3HiSignalGenJets',#'ak3HiGenJets',
                                                             rParam = 0.3,
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
                                                             bTagJetName = cms.untracked.string("akPuSoftDropCh3Calo"),
                                                             jetName = cms.untracked.string("akPuSoftDropCh3Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(True),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropCh3GenJets"),
                                                             doGenTaus = False,
                                                             genTau1 = cms.InputTag("akSoftDropCh3GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropCh3GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropCh3GenNjettiness","tau3"),
                                                             doGenSym = True,
                                                             genSym = cms.InputTag("akSoftDropCh3GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropCh3GenJets","droppedBranches")
                                                             )

akPuSoftDropCh3CaloJetSequence_mc = cms.Sequence(
                                                  #akPuSoftDropCh3Caloclean
                                                  #*
                                                  akPuSoftDropCh3Calomatch
                                                  #*
                                                  #akPuSoftDropCh3CalomatchGroomed
                                                  *
                                                  akPuSoftDropCh3Caloparton
                                                  *
                                                  akPuSoftDropCh3Calocorr
                                                  *
                                                  #akPuSoftDropCh3CaloJetID
                                                  #*
                                                  akPuSoftDropCh3CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akPuSoftDropCh3CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akPuSoftDropCh3CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akPuSoftDropCh3CaloJetBtagging
                                                  *
                                                  akPuSoftDropCh3CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akPuSoftDropCh3CalopatJetsWithBtagging
                                                  *
                                                  akPuSoftDropCh3CaloJetAnalyzer
                                                  )

akPuSoftDropCh3CaloJetSequence_data = cms.Sequence(akPuSoftDropCh3Calocorr
                                                    *
                                                    #akPuSoftDropCh3CaloJetID
                                                    #*
                                                    akPuSoftDropCh3CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akPuSoftDropCh3CaloJetBtagging
                                                    *
                                                    akPuSoftDropCh3CaloNjettiness 
                                                    *
                                                    akPuSoftDropCh3CalopatJetsWithBtagging
                                                    *
                                                    akPuSoftDropCh3CaloJetAnalyzer
                                                    )

akPuSoftDropCh3CaloJetSequence_jec = cms.Sequence(akPuSoftDropCh3CaloJetSequence_mc)
akPuSoftDropCh3CaloJetSequence_mb = cms.Sequence(akPuSoftDropCh3CaloJetSequence_mc)

akPuSoftDropCh3CaloJetSequence = cms.Sequence(akPuSoftDropCh3CaloJetSequence_mc)
akPuSoftDropCh3CalopatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh3CaloJets:sym']
akPuSoftDropCh3CalopatJetsWithBtagging.userData.userInts.src += ['akPuSoftDropCh3CaloJets:droppedBranches']
