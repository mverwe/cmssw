

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDropCh5Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh5CaloJets"),
    matched = cms.InputTag("ak5HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.5
    )

akSoftDropCh5CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh5HiGenJets"),
    matched = cms.InputTag("ak5HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.5
    )

akSoftDropCh5Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh5CaloJets")
                                                        )

akSoftDropCh5Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akSoftDropCh5CaloJets"),
    payload = "AK5Calo_offline"
    )

akSoftDropCh5CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akSoftDropCh5CaloJets'))

#akSoftDropCh5Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak5HiSignalGenJets'))

akSoftDropCh5CalobTagger = bTaggers("akSoftDropCh5Calo",0.5)

#create objects locally since they dont load properly otherwise
#akSoftDropCh5Calomatch = akSoftDropCh5CalobTagger.match
akSoftDropCh5Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh5CaloJets"), matched = cms.InputTag("hiSignalGenParticles"))
akSoftDropCh5CaloPatJetFlavourAssociationLegacy = akSoftDropCh5CalobTagger.PatJetFlavourAssociationLegacy
akSoftDropCh5CaloPatJetPartons = akSoftDropCh5CalobTagger.PatJetPartons
akSoftDropCh5CaloJetTracksAssociatorAtVertex = akSoftDropCh5CalobTagger.JetTracksAssociatorAtVertex
akSoftDropCh5CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDropCh5CaloSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh5CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh5CaloSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh5CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh5CaloCombinedSecondaryVertexBJetTags = akSoftDropCh5CalobTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh5CaloCombinedSecondaryVertexV2BJetTags = akSoftDropCh5CalobTagger.CombinedSecondaryVertexV2BJetTags
akSoftDropCh5CaloJetBProbabilityBJetTags = akSoftDropCh5CalobTagger.JetBProbabilityBJetTags
akSoftDropCh5CaloSoftPFMuonByPtBJetTags = akSoftDropCh5CalobTagger.SoftPFMuonByPtBJetTags
akSoftDropCh5CaloSoftPFMuonByIP3dBJetTags = akSoftDropCh5CalobTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh5CaloTrackCountingHighEffBJetTags = akSoftDropCh5CalobTagger.TrackCountingHighEffBJetTags
akSoftDropCh5CaloTrackCountingHighPurBJetTags = akSoftDropCh5CalobTagger.TrackCountingHighPurBJetTags
akSoftDropCh5CaloPatJetPartonAssociationLegacy = akSoftDropCh5CalobTagger.PatJetPartonAssociationLegacy

akSoftDropCh5CaloImpactParameterTagInfos = akSoftDropCh5CalobTagger.ImpactParameterTagInfos
akSoftDropCh5CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh5CaloJetProbabilityBJetTags = akSoftDropCh5CalobTagger.JetProbabilityBJetTags

akSoftDropCh5CaloSecondaryVertexTagInfos = akSoftDropCh5CalobTagger.SecondaryVertexTagInfos
akSoftDropCh5CaloSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh5CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh5CaloSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh5CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh5CaloCombinedSecondaryVertexBJetTags = akSoftDropCh5CalobTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh5CaloCombinedSecondaryVertexV2BJetTags = akSoftDropCh5CalobTagger.CombinedSecondaryVertexV2BJetTags

akSoftDropCh5CaloSecondaryVertexNegativeTagInfos = akSoftDropCh5CalobTagger.SecondaryVertexNegativeTagInfos
akSoftDropCh5CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh5CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDropCh5CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh5CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDropCh5CaloNegativeCombinedSecondaryVertexBJetTags = akSoftDropCh5CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDropCh5CaloPositiveCombinedSecondaryVertexBJetTags = akSoftDropCh5CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDropCh5CaloNegativeCombinedSecondaryVertexV2BJetTags = akSoftDropCh5CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDropCh5CaloPositiveCombinedSecondaryVertexV2BJetTags = akSoftDropCh5CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDropCh5CaloSoftPFMuonsTagInfos = akSoftDropCh5CalobTagger.SoftPFMuonsTagInfos
akSoftDropCh5CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh5CaloSoftPFMuonBJetTags = akSoftDropCh5CalobTagger.SoftPFMuonBJetTags
akSoftDropCh5CaloSoftPFMuonByIP3dBJetTags = akSoftDropCh5CalobTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh5CaloSoftPFMuonByPtBJetTags = akSoftDropCh5CalobTagger.SoftPFMuonByPtBJetTags
akSoftDropCh5CaloNegativeSoftPFMuonByPtBJetTags = akSoftDropCh5CalobTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDropCh5CaloPositiveSoftPFMuonByPtBJetTags = akSoftDropCh5CalobTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDropCh5CaloPatJetFlavourIdLegacy = cms.Sequence(akSoftDropCh5CaloPatJetPartonAssociationLegacy*akSoftDropCh5CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akSoftDropCh5CaloPatJetFlavourAssociation = akSoftDropCh5CalobTagger.PatJetFlavourAssociation
#akSoftDropCh5CaloPatJetFlavourId = cms.Sequence(akSoftDropCh5CaloPatJetPartons*akSoftDropCh5CaloPatJetFlavourAssociation)

akSoftDropCh5CaloJetBtaggingIP       = cms.Sequence(akSoftDropCh5CaloImpactParameterTagInfos *
            (akSoftDropCh5CaloTrackCountingHighEffBJetTags +
             akSoftDropCh5CaloTrackCountingHighPurBJetTags +
             akSoftDropCh5CaloJetProbabilityBJetTags +
             akSoftDropCh5CaloJetBProbabilityBJetTags 
            )
            )

akSoftDropCh5CaloJetBtaggingSV = cms.Sequence(akSoftDropCh5CaloImpactParameterTagInfos
            *
            akSoftDropCh5CaloSecondaryVertexTagInfos
            * (akSoftDropCh5CaloSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh5CaloSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh5CaloCombinedSecondaryVertexBJetTags+
                akSoftDropCh5CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh5CaloJetBtaggingNegSV = cms.Sequence(akSoftDropCh5CaloImpactParameterTagInfos
            *
            akSoftDropCh5CaloSecondaryVertexNegativeTagInfos
            * (akSoftDropCh5CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh5CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh5CaloNegativeCombinedSecondaryVertexBJetTags+
                akSoftDropCh5CaloPositiveCombinedSecondaryVertexBJetTags+
                akSoftDropCh5CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akSoftDropCh5CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh5CaloJetBtaggingMu = cms.Sequence(akSoftDropCh5CaloSoftPFMuonsTagInfos * (akSoftDropCh5CaloSoftPFMuonBJetTags
                +
                akSoftDropCh5CaloSoftPFMuonByIP3dBJetTags
                +
                akSoftDropCh5CaloSoftPFMuonByPtBJetTags
                +
                akSoftDropCh5CaloNegativeSoftPFMuonByPtBJetTags
                +
                akSoftDropCh5CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akSoftDropCh5CaloJetBtagging = cms.Sequence(akSoftDropCh5CaloJetBtaggingIP
            *akSoftDropCh5CaloJetBtaggingSV
            *akSoftDropCh5CaloJetBtaggingNegSV
#            *akSoftDropCh5CaloJetBtaggingMu
            )

akSoftDropCh5CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akSoftDropCh5CaloJets"),
        genJetMatch          = cms.InputTag("akSoftDropCh5Calomatch"),
        genPartonMatch       = cms.InputTag("akSoftDropCh5Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akSoftDropCh5Calocorr")),
        JetPartonMapSource   = cms.InputTag("akSoftDropCh5CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akSoftDropCh5CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akSoftDropCh5CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akSoftDropCh5CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akSoftDropCh5CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akSoftDropCh5CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akSoftDropCh5CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akSoftDropCh5CaloJetBProbabilityBJetTags"),
            cms.InputTag("akSoftDropCh5CaloJetProbabilityBJetTags"),
            #cms.InputTag("akSoftDropCh5CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akSoftDropCh5CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akSoftDropCh5CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akSoftDropCh5CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akSoftDropCh5CaloJetID"),
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

akSoftDropCh5CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akSoftDropCh5CaloJets"),
           	    R0  = cms.double( 0.5)
)
akSoftDropCh5CalopatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh5CaloNjettiness:tau1','akSoftDropCh5CaloNjettiness:tau2','akSoftDropCh5CaloNjettiness:tau3']

akSoftDropCh5CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akSoftDropCh5CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak5HiSignalGenJets',#'ak5HiGenJets',
                                                             rParam = 0.5,
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
                                                             bTagJetName = cms.untracked.string("akSoftDropCh5Calo"),
                                                             jetName = cms.untracked.string("akSoftDropCh5Calo"),
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

akSoftDropCh5CaloJetSequence_mc = cms.Sequence(
                                                  #akSoftDropCh5Caloclean
                                                  #*
                                                  akSoftDropCh5Calomatch
                                                  #*
                                                  #akSoftDropCh5CalomatchGroomed
                                                  *
                                                  akSoftDropCh5Caloparton
                                                  *
                                                  akSoftDropCh5Calocorr
                                                  *
                                                  #akSoftDropCh5CaloJetID
                                                  #*
                                                  akSoftDropCh5CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akSoftDropCh5CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akSoftDropCh5CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akSoftDropCh5CaloJetBtagging
                                                  *
                                                  akSoftDropCh5CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akSoftDropCh5CalopatJetsWithBtagging
                                                  *
                                                  akSoftDropCh5CaloJetAnalyzer
                                                  )

akSoftDropCh5CaloJetSequence_data = cms.Sequence(akSoftDropCh5Calocorr
                                                    *
                                                    #akSoftDropCh5CaloJetID
                                                    #*
                                                    akSoftDropCh5CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akSoftDropCh5CaloJetBtagging
                                                    *
                                                    akSoftDropCh5CaloNjettiness 
                                                    *
                                                    akSoftDropCh5CalopatJetsWithBtagging
                                                    *
                                                    akSoftDropCh5CaloJetAnalyzer
                                                    )

akSoftDropCh5CaloJetSequence_jec = cms.Sequence(akSoftDropCh5CaloJetSequence_mc)
akSoftDropCh5CaloJetSequence_mb = cms.Sequence(akSoftDropCh5CaloJetSequence_mc)

akSoftDropCh5CaloJetSequence = cms.Sequence(akSoftDropCh5CaloJetSequence_mc)
akSoftDropCh5CalopatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh5CaloJets:sym']
akSoftDropCh5CalopatJetsWithBtagging.userData.userInts.src += ['akSoftDropCh5CaloJets:droppedBranches']
