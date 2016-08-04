

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPuSoftDropCh4Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPuSoftDropCh4CaloJets"),
    matched = cms.InputTag("ak4HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.4
    )

akPuSoftDropCh4CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh4HiGenJets"),
    matched = cms.InputTag("ak4HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.4
    )

akPuSoftDropCh4Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh4CaloJets")
                                                        )

akPuSoftDropCh4Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akPuSoftDropCh4CaloJets"),
    payload = "AKPu4Calo_offline"
    )

akPuSoftDropCh4CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akPuSoftDropCh4CaloJets'))

#akPuSoftDropCh4Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak4HiSignalGenJets'))

akPuSoftDropCh4CalobTagger = bTaggers("akPuSoftDropCh4Calo",0.4)

#create objects locally since they dont load properly otherwise
#akPuSoftDropCh4Calomatch = akPuSoftDropCh4CalobTagger.match
akPuSoftDropCh4Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh4CaloJets"), matched = cms.InputTag("hiSignalGenParticles"))
akPuSoftDropCh4CaloPatJetFlavourAssociationLegacy = akPuSoftDropCh4CalobTagger.PatJetFlavourAssociationLegacy
akPuSoftDropCh4CaloPatJetPartons = akPuSoftDropCh4CalobTagger.PatJetPartons
akPuSoftDropCh4CaloJetTracksAssociatorAtVertex = akPuSoftDropCh4CalobTagger.JetTracksAssociatorAtVertex
akPuSoftDropCh4CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPuSoftDropCh4CaloSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh4CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh4CaloSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh4CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh4CaloCombinedSecondaryVertexBJetTags = akPuSoftDropCh4CalobTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh4CaloCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh4CalobTagger.CombinedSecondaryVertexV2BJetTags
akPuSoftDropCh4CaloJetBProbabilityBJetTags = akPuSoftDropCh4CalobTagger.JetBProbabilityBJetTags
akPuSoftDropCh4CaloSoftPFMuonByPtBJetTags = akPuSoftDropCh4CalobTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh4CaloSoftPFMuonByIP3dBJetTags = akPuSoftDropCh4CalobTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh4CaloTrackCountingHighEffBJetTags = akPuSoftDropCh4CalobTagger.TrackCountingHighEffBJetTags
akPuSoftDropCh4CaloTrackCountingHighPurBJetTags = akPuSoftDropCh4CalobTagger.TrackCountingHighPurBJetTags
akPuSoftDropCh4CaloPatJetPartonAssociationLegacy = akPuSoftDropCh4CalobTagger.PatJetPartonAssociationLegacy

akPuSoftDropCh4CaloImpactParameterTagInfos = akPuSoftDropCh4CalobTagger.ImpactParameterTagInfos
akPuSoftDropCh4CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh4CaloJetProbabilityBJetTags = akPuSoftDropCh4CalobTagger.JetProbabilityBJetTags

akPuSoftDropCh4CaloSecondaryVertexTagInfos = akPuSoftDropCh4CalobTagger.SecondaryVertexTagInfos
akPuSoftDropCh4CaloSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh4CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh4CaloSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh4CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh4CaloCombinedSecondaryVertexBJetTags = akPuSoftDropCh4CalobTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh4CaloCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh4CalobTagger.CombinedSecondaryVertexV2BJetTags

akPuSoftDropCh4CaloSecondaryVertexNegativeTagInfos = akPuSoftDropCh4CalobTagger.SecondaryVertexNegativeTagInfos
akPuSoftDropCh4CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh4CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh4CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh4CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh4CaloNegativeCombinedSecondaryVertexBJetTags = akPuSoftDropCh4CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akPuSoftDropCh4CaloPositiveCombinedSecondaryVertexBJetTags = akPuSoftDropCh4CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akPuSoftDropCh4CaloNegativeCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh4CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPuSoftDropCh4CaloPositiveCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh4CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPuSoftDropCh4CaloSoftPFMuonsTagInfos = akPuSoftDropCh4CalobTagger.SoftPFMuonsTagInfos
akPuSoftDropCh4CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh4CaloSoftPFMuonBJetTags = akPuSoftDropCh4CalobTagger.SoftPFMuonBJetTags
akPuSoftDropCh4CaloSoftPFMuonByIP3dBJetTags = akPuSoftDropCh4CalobTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh4CaloSoftPFMuonByPtBJetTags = akPuSoftDropCh4CalobTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh4CaloNegativeSoftPFMuonByPtBJetTags = akPuSoftDropCh4CalobTagger.NegativeSoftPFMuonByPtBJetTags
akPuSoftDropCh4CaloPositiveSoftPFMuonByPtBJetTags = akPuSoftDropCh4CalobTagger.PositiveSoftPFMuonByPtBJetTags
akPuSoftDropCh4CaloPatJetFlavourIdLegacy = cms.Sequence(akPuSoftDropCh4CaloPatJetPartonAssociationLegacy*akPuSoftDropCh4CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akPuSoftDropCh4CaloPatJetFlavourAssociation = akPuSoftDropCh4CalobTagger.PatJetFlavourAssociation
#akPuSoftDropCh4CaloPatJetFlavourId = cms.Sequence(akPuSoftDropCh4CaloPatJetPartons*akPuSoftDropCh4CaloPatJetFlavourAssociation)

akPuSoftDropCh4CaloJetBtaggingIP       = cms.Sequence(akPuSoftDropCh4CaloImpactParameterTagInfos *
            (akPuSoftDropCh4CaloTrackCountingHighEffBJetTags +
             akPuSoftDropCh4CaloTrackCountingHighPurBJetTags +
             akPuSoftDropCh4CaloJetProbabilityBJetTags +
             akPuSoftDropCh4CaloJetBProbabilityBJetTags 
            )
            )

akPuSoftDropCh4CaloJetBtaggingSV = cms.Sequence(akPuSoftDropCh4CaloImpactParameterTagInfos
            *
            akPuSoftDropCh4CaloSecondaryVertexTagInfos
            * (akPuSoftDropCh4CaloSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh4CaloSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh4CaloCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh4CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh4CaloJetBtaggingNegSV = cms.Sequence(akPuSoftDropCh4CaloImpactParameterTagInfos
            *
            akPuSoftDropCh4CaloSecondaryVertexNegativeTagInfos
            * (akPuSoftDropCh4CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh4CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh4CaloNegativeCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh4CaloPositiveCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh4CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akPuSoftDropCh4CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh4CaloJetBtaggingMu = cms.Sequence(akPuSoftDropCh4CaloSoftPFMuonsTagInfos * (akPuSoftDropCh4CaloSoftPFMuonBJetTags
                +
                akPuSoftDropCh4CaloSoftPFMuonByIP3dBJetTags
                +
                akPuSoftDropCh4CaloSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh4CaloNegativeSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh4CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akPuSoftDropCh4CaloJetBtagging = cms.Sequence(akPuSoftDropCh4CaloJetBtaggingIP
            *akPuSoftDropCh4CaloJetBtaggingSV
            *akPuSoftDropCh4CaloJetBtaggingNegSV
#            *akPuSoftDropCh4CaloJetBtaggingMu
            )

akPuSoftDropCh4CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akPuSoftDropCh4CaloJets"),
        genJetMatch          = cms.InputTag("akPuSoftDropCh4Calomatch"),
        genPartonMatch       = cms.InputTag("akPuSoftDropCh4Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPuSoftDropCh4Calocorr")),
        JetPartonMapSource   = cms.InputTag("akPuSoftDropCh4CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akPuSoftDropCh4CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPuSoftDropCh4CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akPuSoftDropCh4CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh4CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPuSoftDropCh4CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPuSoftDropCh4CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akPuSoftDropCh4CaloJetBProbabilityBJetTags"),
            cms.InputTag("akPuSoftDropCh4CaloJetProbabilityBJetTags"),
            #cms.InputTag("akPuSoftDropCh4CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akPuSoftDropCh4CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akPuSoftDropCh4CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh4CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPuSoftDropCh4CaloJetID"),
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

akPuSoftDropCh4CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akPuSoftDropCh4CaloJets"),
           	    R0  = cms.double( 0.4)
)
akPuSoftDropCh4CalopatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh4CaloNjettiness:tau1','akPuSoftDropCh4CaloNjettiness:tau2','akPuSoftDropCh4CaloNjettiness:tau3']

akPuSoftDropCh4CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPuSoftDropCh4CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak4HiSignalGenJets',#'ak4HiGenJets',
                                                             rParam = 0.4,
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
                                                             bTagJetName = cms.untracked.string("akPuSoftDropCh4Calo"),
                                                             jetName = cms.untracked.string("akPuSoftDropCh4Calo"),
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

akPuSoftDropCh4CaloJetSequence_mc = cms.Sequence(
                                                  #akPuSoftDropCh4Caloclean
                                                  #*
                                                  akPuSoftDropCh4Calomatch
                                                  #*
                                                  #akPuSoftDropCh4CalomatchGroomed
                                                  *
                                                  akPuSoftDropCh4Caloparton
                                                  *
                                                  akPuSoftDropCh4Calocorr
                                                  *
                                                  #akPuSoftDropCh4CaloJetID
                                                  #*
                                                  akPuSoftDropCh4CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akPuSoftDropCh4CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akPuSoftDropCh4CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akPuSoftDropCh4CaloJetBtagging
                                                  *
                                                  akPuSoftDropCh4CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akPuSoftDropCh4CalopatJetsWithBtagging
                                                  *
                                                  akPuSoftDropCh4CaloJetAnalyzer
                                                  )

akPuSoftDropCh4CaloJetSequence_data = cms.Sequence(akPuSoftDropCh4Calocorr
                                                    *
                                                    #akPuSoftDropCh4CaloJetID
                                                    #*
                                                    akPuSoftDropCh4CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akPuSoftDropCh4CaloJetBtagging
                                                    *
                                                    akPuSoftDropCh4CaloNjettiness 
                                                    *
                                                    akPuSoftDropCh4CalopatJetsWithBtagging
                                                    *
                                                    akPuSoftDropCh4CaloJetAnalyzer
                                                    )

akPuSoftDropCh4CaloJetSequence_jec = cms.Sequence(akPuSoftDropCh4CaloJetSequence_mc)
akPuSoftDropCh4CaloJetSequence_mb = cms.Sequence(akPuSoftDropCh4CaloJetSequence_mc)

akPuSoftDropCh4CaloJetSequence = cms.Sequence(akPuSoftDropCh4CaloJetSequence_data)
akPuSoftDropCh4CalopatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh4CaloJets:sym']
akPuSoftDropCh4CalopatJetsWithBtagging.userData.userInts.src += ['akPuSoftDropCh4CaloJets:droppedBranches']
