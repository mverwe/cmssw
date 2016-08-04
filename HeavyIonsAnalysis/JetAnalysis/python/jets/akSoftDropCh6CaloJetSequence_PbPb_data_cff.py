

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDropCh6Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh6CaloJets"),
    matched = cms.InputTag("ak6HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.6
    )

akSoftDropCh6CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh6HiGenJets"),
    matched = cms.InputTag("ak6HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.6
    )

akSoftDropCh6Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh6CaloJets")
                                                        )

akSoftDropCh6Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akSoftDropCh6CaloJets"),
    payload = "AK6Calo_offline"
    )

akSoftDropCh6CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akSoftDropCh6CaloJets'))

#akSoftDropCh6Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak6HiSignalGenJets'))

akSoftDropCh6CalobTagger = bTaggers("akSoftDropCh6Calo",0.6)

#create objects locally since they dont load properly otherwise
#akSoftDropCh6Calomatch = akSoftDropCh6CalobTagger.match
akSoftDropCh6Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh6CaloJets"), matched = cms.InputTag("hiSignalGenParticles"))
akSoftDropCh6CaloPatJetFlavourAssociationLegacy = akSoftDropCh6CalobTagger.PatJetFlavourAssociationLegacy
akSoftDropCh6CaloPatJetPartons = akSoftDropCh6CalobTagger.PatJetPartons
akSoftDropCh6CaloJetTracksAssociatorAtVertex = akSoftDropCh6CalobTagger.JetTracksAssociatorAtVertex
akSoftDropCh6CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDropCh6CaloSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh6CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh6CaloSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh6CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh6CaloCombinedSecondaryVertexBJetTags = akSoftDropCh6CalobTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh6CaloCombinedSecondaryVertexV2BJetTags = akSoftDropCh6CalobTagger.CombinedSecondaryVertexV2BJetTags
akSoftDropCh6CaloJetBProbabilityBJetTags = akSoftDropCh6CalobTagger.JetBProbabilityBJetTags
akSoftDropCh6CaloSoftPFMuonByPtBJetTags = akSoftDropCh6CalobTagger.SoftPFMuonByPtBJetTags
akSoftDropCh6CaloSoftPFMuonByIP3dBJetTags = akSoftDropCh6CalobTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh6CaloTrackCountingHighEffBJetTags = akSoftDropCh6CalobTagger.TrackCountingHighEffBJetTags
akSoftDropCh6CaloTrackCountingHighPurBJetTags = akSoftDropCh6CalobTagger.TrackCountingHighPurBJetTags
akSoftDropCh6CaloPatJetPartonAssociationLegacy = akSoftDropCh6CalobTagger.PatJetPartonAssociationLegacy

akSoftDropCh6CaloImpactParameterTagInfos = akSoftDropCh6CalobTagger.ImpactParameterTagInfos
akSoftDropCh6CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh6CaloJetProbabilityBJetTags = akSoftDropCh6CalobTagger.JetProbabilityBJetTags

akSoftDropCh6CaloSecondaryVertexTagInfos = akSoftDropCh6CalobTagger.SecondaryVertexTagInfos
akSoftDropCh6CaloSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh6CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh6CaloSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh6CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh6CaloCombinedSecondaryVertexBJetTags = akSoftDropCh6CalobTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh6CaloCombinedSecondaryVertexV2BJetTags = akSoftDropCh6CalobTagger.CombinedSecondaryVertexV2BJetTags

akSoftDropCh6CaloSecondaryVertexNegativeTagInfos = akSoftDropCh6CalobTagger.SecondaryVertexNegativeTagInfos
akSoftDropCh6CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh6CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDropCh6CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh6CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDropCh6CaloNegativeCombinedSecondaryVertexBJetTags = akSoftDropCh6CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDropCh6CaloPositiveCombinedSecondaryVertexBJetTags = akSoftDropCh6CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDropCh6CaloNegativeCombinedSecondaryVertexV2BJetTags = akSoftDropCh6CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDropCh6CaloPositiveCombinedSecondaryVertexV2BJetTags = akSoftDropCh6CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDropCh6CaloSoftPFMuonsTagInfos = akSoftDropCh6CalobTagger.SoftPFMuonsTagInfos
akSoftDropCh6CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh6CaloSoftPFMuonBJetTags = akSoftDropCh6CalobTagger.SoftPFMuonBJetTags
akSoftDropCh6CaloSoftPFMuonByIP3dBJetTags = akSoftDropCh6CalobTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh6CaloSoftPFMuonByPtBJetTags = akSoftDropCh6CalobTagger.SoftPFMuonByPtBJetTags
akSoftDropCh6CaloNegativeSoftPFMuonByPtBJetTags = akSoftDropCh6CalobTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDropCh6CaloPositiveSoftPFMuonByPtBJetTags = akSoftDropCh6CalobTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDropCh6CaloPatJetFlavourIdLegacy = cms.Sequence(akSoftDropCh6CaloPatJetPartonAssociationLegacy*akSoftDropCh6CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akSoftDropCh6CaloPatJetFlavourAssociation = akSoftDropCh6CalobTagger.PatJetFlavourAssociation
#akSoftDropCh6CaloPatJetFlavourId = cms.Sequence(akSoftDropCh6CaloPatJetPartons*akSoftDropCh6CaloPatJetFlavourAssociation)

akSoftDropCh6CaloJetBtaggingIP       = cms.Sequence(akSoftDropCh6CaloImpactParameterTagInfos *
            (akSoftDropCh6CaloTrackCountingHighEffBJetTags +
             akSoftDropCh6CaloTrackCountingHighPurBJetTags +
             akSoftDropCh6CaloJetProbabilityBJetTags +
             akSoftDropCh6CaloJetBProbabilityBJetTags 
            )
            )

akSoftDropCh6CaloJetBtaggingSV = cms.Sequence(akSoftDropCh6CaloImpactParameterTagInfos
            *
            akSoftDropCh6CaloSecondaryVertexTagInfos
            * (akSoftDropCh6CaloSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh6CaloSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh6CaloCombinedSecondaryVertexBJetTags+
                akSoftDropCh6CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh6CaloJetBtaggingNegSV = cms.Sequence(akSoftDropCh6CaloImpactParameterTagInfos
            *
            akSoftDropCh6CaloSecondaryVertexNegativeTagInfos
            * (akSoftDropCh6CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh6CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh6CaloNegativeCombinedSecondaryVertexBJetTags+
                akSoftDropCh6CaloPositiveCombinedSecondaryVertexBJetTags+
                akSoftDropCh6CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akSoftDropCh6CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh6CaloJetBtaggingMu = cms.Sequence(akSoftDropCh6CaloSoftPFMuonsTagInfos * (akSoftDropCh6CaloSoftPFMuonBJetTags
                +
                akSoftDropCh6CaloSoftPFMuonByIP3dBJetTags
                +
                akSoftDropCh6CaloSoftPFMuonByPtBJetTags
                +
                akSoftDropCh6CaloNegativeSoftPFMuonByPtBJetTags
                +
                akSoftDropCh6CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akSoftDropCh6CaloJetBtagging = cms.Sequence(akSoftDropCh6CaloJetBtaggingIP
            *akSoftDropCh6CaloJetBtaggingSV
            *akSoftDropCh6CaloJetBtaggingNegSV
#            *akSoftDropCh6CaloJetBtaggingMu
            )

akSoftDropCh6CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akSoftDropCh6CaloJets"),
        genJetMatch          = cms.InputTag("akSoftDropCh6Calomatch"),
        genPartonMatch       = cms.InputTag("akSoftDropCh6Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akSoftDropCh6Calocorr")),
        JetPartonMapSource   = cms.InputTag("akSoftDropCh6CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akSoftDropCh6CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akSoftDropCh6CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akSoftDropCh6CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akSoftDropCh6CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akSoftDropCh6CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akSoftDropCh6CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akSoftDropCh6CaloJetBProbabilityBJetTags"),
            cms.InputTag("akSoftDropCh6CaloJetProbabilityBJetTags"),
            #cms.InputTag("akSoftDropCh6CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akSoftDropCh6CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akSoftDropCh6CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akSoftDropCh6CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akSoftDropCh6CaloJetID"),
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

akSoftDropCh6CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akSoftDropCh6CaloJets"),
           	    R0  = cms.double( 0.6)
)
akSoftDropCh6CalopatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh6CaloNjettiness:tau1','akSoftDropCh6CaloNjettiness:tau2','akSoftDropCh6CaloNjettiness:tau3']

akSoftDropCh6CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akSoftDropCh6CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak6HiSignalGenJets',#'ak6HiGenJets',
                                                             rParam = 0.6,
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
                                                             bTagJetName = cms.untracked.string("akSoftDropCh6Calo"),
                                                             jetName = cms.untracked.string("akSoftDropCh6Calo"),
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

akSoftDropCh6CaloJetSequence_mc = cms.Sequence(
                                                  #akSoftDropCh6Caloclean
                                                  #*
                                                  akSoftDropCh6Calomatch
                                                  #*
                                                  #akSoftDropCh6CalomatchGroomed
                                                  *
                                                  akSoftDropCh6Caloparton
                                                  *
                                                  akSoftDropCh6Calocorr
                                                  *
                                                  #akSoftDropCh6CaloJetID
                                                  #*
                                                  akSoftDropCh6CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akSoftDropCh6CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akSoftDropCh6CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akSoftDropCh6CaloJetBtagging
                                                  *
                                                  akSoftDropCh6CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akSoftDropCh6CalopatJetsWithBtagging
                                                  *
                                                  akSoftDropCh6CaloJetAnalyzer
                                                  )

akSoftDropCh6CaloJetSequence_data = cms.Sequence(akSoftDropCh6Calocorr
                                                    *
                                                    #akSoftDropCh6CaloJetID
                                                    #*
                                                    akSoftDropCh6CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akSoftDropCh6CaloJetBtagging
                                                    *
                                                    akSoftDropCh6CaloNjettiness 
                                                    *
                                                    akSoftDropCh6CalopatJetsWithBtagging
                                                    *
                                                    akSoftDropCh6CaloJetAnalyzer
                                                    )

akSoftDropCh6CaloJetSequence_jec = cms.Sequence(akSoftDropCh6CaloJetSequence_mc)
akSoftDropCh6CaloJetSequence_mb = cms.Sequence(akSoftDropCh6CaloJetSequence_mc)

akSoftDropCh6CaloJetSequence = cms.Sequence(akSoftDropCh6CaloJetSequence_data)
akSoftDropCh6CalopatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh6CaloJets:sym']
akSoftDropCh6CalopatJetsWithBtagging.userData.userInts.src += ['akSoftDropCh6CaloJets:droppedBranches']
