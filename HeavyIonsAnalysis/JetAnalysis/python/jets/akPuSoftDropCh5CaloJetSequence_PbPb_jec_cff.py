

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPuSoftDropCh5Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPuSoftDropCh5CaloJets"),
    matched = cms.InputTag("ak5HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.5
    )

akPuSoftDropCh5CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh5HiGenJets"),
    matched = cms.InputTag("ak5HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.5
    )

akPuSoftDropCh5Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh5CaloJets")
                                                        )

akPuSoftDropCh5Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akPuSoftDropCh5CaloJets"),
    payload = "AKPu5Calo_offline"
    )

akPuSoftDropCh5CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akPuSoftDropCh5CaloJets'))

#akPuSoftDropCh5Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak5HiSignalGenJets'))

akPuSoftDropCh5CalobTagger = bTaggers("akPuSoftDropCh5Calo",0.5)

#create objects locally since they dont load properly otherwise
#akPuSoftDropCh5Calomatch = akPuSoftDropCh5CalobTagger.match
akPuSoftDropCh5Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh5CaloJets"), matched = cms.InputTag("hiSignalGenParticles"))
akPuSoftDropCh5CaloPatJetFlavourAssociationLegacy = akPuSoftDropCh5CalobTagger.PatJetFlavourAssociationLegacy
akPuSoftDropCh5CaloPatJetPartons = akPuSoftDropCh5CalobTagger.PatJetPartons
akPuSoftDropCh5CaloJetTracksAssociatorAtVertex = akPuSoftDropCh5CalobTagger.JetTracksAssociatorAtVertex
akPuSoftDropCh5CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPuSoftDropCh5CaloSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh5CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh5CaloSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh5CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh5CaloCombinedSecondaryVertexBJetTags = akPuSoftDropCh5CalobTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh5CaloCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh5CalobTagger.CombinedSecondaryVertexV2BJetTags
akPuSoftDropCh5CaloJetBProbabilityBJetTags = akPuSoftDropCh5CalobTagger.JetBProbabilityBJetTags
akPuSoftDropCh5CaloSoftPFMuonByPtBJetTags = akPuSoftDropCh5CalobTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh5CaloSoftPFMuonByIP3dBJetTags = akPuSoftDropCh5CalobTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh5CaloTrackCountingHighEffBJetTags = akPuSoftDropCh5CalobTagger.TrackCountingHighEffBJetTags
akPuSoftDropCh5CaloTrackCountingHighPurBJetTags = akPuSoftDropCh5CalobTagger.TrackCountingHighPurBJetTags
akPuSoftDropCh5CaloPatJetPartonAssociationLegacy = akPuSoftDropCh5CalobTagger.PatJetPartonAssociationLegacy

akPuSoftDropCh5CaloImpactParameterTagInfos = akPuSoftDropCh5CalobTagger.ImpactParameterTagInfos
akPuSoftDropCh5CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh5CaloJetProbabilityBJetTags = akPuSoftDropCh5CalobTagger.JetProbabilityBJetTags

akPuSoftDropCh5CaloSecondaryVertexTagInfos = akPuSoftDropCh5CalobTagger.SecondaryVertexTagInfos
akPuSoftDropCh5CaloSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh5CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh5CaloSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh5CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh5CaloCombinedSecondaryVertexBJetTags = akPuSoftDropCh5CalobTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh5CaloCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh5CalobTagger.CombinedSecondaryVertexV2BJetTags

akPuSoftDropCh5CaloSecondaryVertexNegativeTagInfos = akPuSoftDropCh5CalobTagger.SecondaryVertexNegativeTagInfos
akPuSoftDropCh5CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh5CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh5CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh5CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh5CaloNegativeCombinedSecondaryVertexBJetTags = akPuSoftDropCh5CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akPuSoftDropCh5CaloPositiveCombinedSecondaryVertexBJetTags = akPuSoftDropCh5CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akPuSoftDropCh5CaloNegativeCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh5CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPuSoftDropCh5CaloPositiveCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh5CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPuSoftDropCh5CaloSoftPFMuonsTagInfos = akPuSoftDropCh5CalobTagger.SoftPFMuonsTagInfos
akPuSoftDropCh5CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh5CaloSoftPFMuonBJetTags = akPuSoftDropCh5CalobTagger.SoftPFMuonBJetTags
akPuSoftDropCh5CaloSoftPFMuonByIP3dBJetTags = akPuSoftDropCh5CalobTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh5CaloSoftPFMuonByPtBJetTags = akPuSoftDropCh5CalobTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh5CaloNegativeSoftPFMuonByPtBJetTags = akPuSoftDropCh5CalobTagger.NegativeSoftPFMuonByPtBJetTags
akPuSoftDropCh5CaloPositiveSoftPFMuonByPtBJetTags = akPuSoftDropCh5CalobTagger.PositiveSoftPFMuonByPtBJetTags
akPuSoftDropCh5CaloPatJetFlavourIdLegacy = cms.Sequence(akPuSoftDropCh5CaloPatJetPartonAssociationLegacy*akPuSoftDropCh5CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akPuSoftDropCh5CaloPatJetFlavourAssociation = akPuSoftDropCh5CalobTagger.PatJetFlavourAssociation
#akPuSoftDropCh5CaloPatJetFlavourId = cms.Sequence(akPuSoftDropCh5CaloPatJetPartons*akPuSoftDropCh5CaloPatJetFlavourAssociation)

akPuSoftDropCh5CaloJetBtaggingIP       = cms.Sequence(akPuSoftDropCh5CaloImpactParameterTagInfos *
            (akPuSoftDropCh5CaloTrackCountingHighEffBJetTags +
             akPuSoftDropCh5CaloTrackCountingHighPurBJetTags +
             akPuSoftDropCh5CaloJetProbabilityBJetTags +
             akPuSoftDropCh5CaloJetBProbabilityBJetTags 
            )
            )

akPuSoftDropCh5CaloJetBtaggingSV = cms.Sequence(akPuSoftDropCh5CaloImpactParameterTagInfos
            *
            akPuSoftDropCh5CaloSecondaryVertexTagInfos
            * (akPuSoftDropCh5CaloSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh5CaloSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh5CaloCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh5CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh5CaloJetBtaggingNegSV = cms.Sequence(akPuSoftDropCh5CaloImpactParameterTagInfos
            *
            akPuSoftDropCh5CaloSecondaryVertexNegativeTagInfos
            * (akPuSoftDropCh5CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh5CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh5CaloNegativeCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh5CaloPositiveCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh5CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akPuSoftDropCh5CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh5CaloJetBtaggingMu = cms.Sequence(akPuSoftDropCh5CaloSoftPFMuonsTagInfos * (akPuSoftDropCh5CaloSoftPFMuonBJetTags
                +
                akPuSoftDropCh5CaloSoftPFMuonByIP3dBJetTags
                +
                akPuSoftDropCh5CaloSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh5CaloNegativeSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh5CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akPuSoftDropCh5CaloJetBtagging = cms.Sequence(akPuSoftDropCh5CaloJetBtaggingIP
            *akPuSoftDropCh5CaloJetBtaggingSV
            *akPuSoftDropCh5CaloJetBtaggingNegSV
#            *akPuSoftDropCh5CaloJetBtaggingMu
            )

akPuSoftDropCh5CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akPuSoftDropCh5CaloJets"),
        genJetMatch          = cms.InputTag("akPuSoftDropCh5Calomatch"),
        genPartonMatch       = cms.InputTag("akPuSoftDropCh5Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPuSoftDropCh5Calocorr")),
        JetPartonMapSource   = cms.InputTag("akPuSoftDropCh5CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akPuSoftDropCh5CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPuSoftDropCh5CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akPuSoftDropCh5CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh5CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPuSoftDropCh5CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPuSoftDropCh5CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akPuSoftDropCh5CaloJetBProbabilityBJetTags"),
            cms.InputTag("akPuSoftDropCh5CaloJetProbabilityBJetTags"),
            #cms.InputTag("akPuSoftDropCh5CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akPuSoftDropCh5CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akPuSoftDropCh5CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh5CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPuSoftDropCh5CaloJetID"),
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

akPuSoftDropCh5CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akPuSoftDropCh5CaloJets"),
           	    R0  = cms.double( 0.5)
)
akPuSoftDropCh5CalopatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh5CaloNjettiness:tau1','akPuSoftDropCh5CaloNjettiness:tau2','akPuSoftDropCh5CaloNjettiness:tau3']

akPuSoftDropCh5CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPuSoftDropCh5CalopatJetsWithBtagging"),
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
                                                             bTagJetName = cms.untracked.string("akPuSoftDropCh5Calo"),
                                                             jetName = cms.untracked.string("akPuSoftDropCh5Calo"),
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

akPuSoftDropCh5CaloJetSequence_mc = cms.Sequence(
                                                  #akPuSoftDropCh5Caloclean
                                                  #*
                                                  akPuSoftDropCh5Calomatch
                                                  #*
                                                  #akPuSoftDropCh5CalomatchGroomed
                                                  *
                                                  akPuSoftDropCh5Caloparton
                                                  *
                                                  akPuSoftDropCh5Calocorr
                                                  *
                                                  #akPuSoftDropCh5CaloJetID
                                                  #*
                                                  akPuSoftDropCh5CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akPuSoftDropCh5CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akPuSoftDropCh5CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akPuSoftDropCh5CaloJetBtagging
                                                  *
                                                  akPuSoftDropCh5CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akPuSoftDropCh5CalopatJetsWithBtagging
                                                  *
                                                  akPuSoftDropCh5CaloJetAnalyzer
                                                  )

akPuSoftDropCh5CaloJetSequence_data = cms.Sequence(akPuSoftDropCh5Calocorr
                                                    *
                                                    #akPuSoftDropCh5CaloJetID
                                                    #*
                                                    akPuSoftDropCh5CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akPuSoftDropCh5CaloJetBtagging
                                                    *
                                                    akPuSoftDropCh5CaloNjettiness 
                                                    *
                                                    akPuSoftDropCh5CalopatJetsWithBtagging
                                                    *
                                                    akPuSoftDropCh5CaloJetAnalyzer
                                                    )

akPuSoftDropCh5CaloJetSequence_jec = cms.Sequence(akPuSoftDropCh5CaloJetSequence_mc)
akPuSoftDropCh5CaloJetSequence_mb = cms.Sequence(akPuSoftDropCh5CaloJetSequence_mc)

akPuSoftDropCh5CaloJetSequence = cms.Sequence(akPuSoftDropCh5CaloJetSequence_jec)
akPuSoftDropCh5CaloJetAnalyzer.genPtMin = cms.untracked.double(1)
akPuSoftDropCh5CaloJetAnalyzer.jetPtMin = cms.double(1)
akPuSoftDropCh5CalopatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh5CaloJets:sym']
akPuSoftDropCh5CalopatJetsWithBtagging.userData.userInts.src += ['akPuSoftDropCh5CaloJets:droppedBranches']
