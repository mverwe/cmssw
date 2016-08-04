

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPuSoftDropCh6Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPuSoftDropCh6CaloJets"),
    matched = cms.InputTag("ak6GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.6
    )

akPuSoftDropCh6CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh6GenJets"),
    matched = cms.InputTag("ak6GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.6
    )

akPuSoftDropCh6Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh6CaloJets")
                                                        )

akPuSoftDropCh6Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akPuSoftDropCh6CaloJets"),
    payload = "AKPu6Calo_offline"
    )

akPuSoftDropCh6CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akPuSoftDropCh6CaloJets'))

#akPuSoftDropCh6Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak6GenJets'))

akPuSoftDropCh6CalobTagger = bTaggers("akPuSoftDropCh6Calo",0.6)

#create objects locally since they dont load properly otherwise
#akPuSoftDropCh6Calomatch = akPuSoftDropCh6CalobTagger.match
akPuSoftDropCh6Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh6CaloJets"), matched = cms.InputTag("genParticles"))
akPuSoftDropCh6CaloPatJetFlavourAssociationLegacy = akPuSoftDropCh6CalobTagger.PatJetFlavourAssociationLegacy
akPuSoftDropCh6CaloPatJetPartons = akPuSoftDropCh6CalobTagger.PatJetPartons
akPuSoftDropCh6CaloJetTracksAssociatorAtVertex = akPuSoftDropCh6CalobTagger.JetTracksAssociatorAtVertex
akPuSoftDropCh6CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPuSoftDropCh6CaloSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh6CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh6CaloSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh6CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh6CaloCombinedSecondaryVertexBJetTags = akPuSoftDropCh6CalobTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh6CaloCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh6CalobTagger.CombinedSecondaryVertexV2BJetTags
akPuSoftDropCh6CaloJetBProbabilityBJetTags = akPuSoftDropCh6CalobTagger.JetBProbabilityBJetTags
akPuSoftDropCh6CaloSoftPFMuonByPtBJetTags = akPuSoftDropCh6CalobTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh6CaloSoftPFMuonByIP3dBJetTags = akPuSoftDropCh6CalobTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh6CaloTrackCountingHighEffBJetTags = akPuSoftDropCh6CalobTagger.TrackCountingHighEffBJetTags
akPuSoftDropCh6CaloTrackCountingHighPurBJetTags = akPuSoftDropCh6CalobTagger.TrackCountingHighPurBJetTags
akPuSoftDropCh6CaloPatJetPartonAssociationLegacy = akPuSoftDropCh6CalobTagger.PatJetPartonAssociationLegacy

akPuSoftDropCh6CaloImpactParameterTagInfos = akPuSoftDropCh6CalobTagger.ImpactParameterTagInfos
akPuSoftDropCh6CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh6CaloJetProbabilityBJetTags = akPuSoftDropCh6CalobTagger.JetProbabilityBJetTags

akPuSoftDropCh6CaloSecondaryVertexTagInfos = akPuSoftDropCh6CalobTagger.SecondaryVertexTagInfos
akPuSoftDropCh6CaloSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh6CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh6CaloSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh6CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh6CaloCombinedSecondaryVertexBJetTags = akPuSoftDropCh6CalobTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh6CaloCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh6CalobTagger.CombinedSecondaryVertexV2BJetTags

akPuSoftDropCh6CaloSecondaryVertexNegativeTagInfos = akPuSoftDropCh6CalobTagger.SecondaryVertexNegativeTagInfos
akPuSoftDropCh6CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh6CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh6CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh6CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh6CaloNegativeCombinedSecondaryVertexBJetTags = akPuSoftDropCh6CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akPuSoftDropCh6CaloPositiveCombinedSecondaryVertexBJetTags = akPuSoftDropCh6CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akPuSoftDropCh6CaloNegativeCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh6CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPuSoftDropCh6CaloPositiveCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh6CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPuSoftDropCh6CaloSoftPFMuonsTagInfos = akPuSoftDropCh6CalobTagger.SoftPFMuonsTagInfos
akPuSoftDropCh6CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh6CaloSoftPFMuonBJetTags = akPuSoftDropCh6CalobTagger.SoftPFMuonBJetTags
akPuSoftDropCh6CaloSoftPFMuonByIP3dBJetTags = akPuSoftDropCh6CalobTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh6CaloSoftPFMuonByPtBJetTags = akPuSoftDropCh6CalobTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh6CaloNegativeSoftPFMuonByPtBJetTags = akPuSoftDropCh6CalobTagger.NegativeSoftPFMuonByPtBJetTags
akPuSoftDropCh6CaloPositiveSoftPFMuonByPtBJetTags = akPuSoftDropCh6CalobTagger.PositiveSoftPFMuonByPtBJetTags
akPuSoftDropCh6CaloPatJetFlavourIdLegacy = cms.Sequence(akPuSoftDropCh6CaloPatJetPartonAssociationLegacy*akPuSoftDropCh6CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akPuSoftDropCh6CaloPatJetFlavourAssociation = akPuSoftDropCh6CalobTagger.PatJetFlavourAssociation
#akPuSoftDropCh6CaloPatJetFlavourId = cms.Sequence(akPuSoftDropCh6CaloPatJetPartons*akPuSoftDropCh6CaloPatJetFlavourAssociation)

akPuSoftDropCh6CaloJetBtaggingIP       = cms.Sequence(akPuSoftDropCh6CaloImpactParameterTagInfos *
            (akPuSoftDropCh6CaloTrackCountingHighEffBJetTags +
             akPuSoftDropCh6CaloTrackCountingHighPurBJetTags +
             akPuSoftDropCh6CaloJetProbabilityBJetTags +
             akPuSoftDropCh6CaloJetBProbabilityBJetTags 
            )
            )

akPuSoftDropCh6CaloJetBtaggingSV = cms.Sequence(akPuSoftDropCh6CaloImpactParameterTagInfos
            *
            akPuSoftDropCh6CaloSecondaryVertexTagInfos
            * (akPuSoftDropCh6CaloSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh6CaloSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh6CaloCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh6CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh6CaloJetBtaggingNegSV = cms.Sequence(akPuSoftDropCh6CaloImpactParameterTagInfos
            *
            akPuSoftDropCh6CaloSecondaryVertexNegativeTagInfos
            * (akPuSoftDropCh6CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh6CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh6CaloNegativeCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh6CaloPositiveCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh6CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akPuSoftDropCh6CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh6CaloJetBtaggingMu = cms.Sequence(akPuSoftDropCh6CaloSoftPFMuonsTagInfos * (akPuSoftDropCh6CaloSoftPFMuonBJetTags
                +
                akPuSoftDropCh6CaloSoftPFMuonByIP3dBJetTags
                +
                akPuSoftDropCh6CaloSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh6CaloNegativeSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh6CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akPuSoftDropCh6CaloJetBtagging = cms.Sequence(akPuSoftDropCh6CaloJetBtaggingIP
            *akPuSoftDropCh6CaloJetBtaggingSV
            *akPuSoftDropCh6CaloJetBtaggingNegSV
#            *akPuSoftDropCh6CaloJetBtaggingMu
            )

akPuSoftDropCh6CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akPuSoftDropCh6CaloJets"),
        genJetMatch          = cms.InputTag("akPuSoftDropCh6Calomatch"),
        genPartonMatch       = cms.InputTag("akPuSoftDropCh6Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPuSoftDropCh6Calocorr")),
        JetPartonMapSource   = cms.InputTag("akPuSoftDropCh6CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akPuSoftDropCh6CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPuSoftDropCh6CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akPuSoftDropCh6CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh6CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPuSoftDropCh6CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPuSoftDropCh6CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akPuSoftDropCh6CaloJetBProbabilityBJetTags"),
            cms.InputTag("akPuSoftDropCh6CaloJetProbabilityBJetTags"),
            #cms.InputTag("akPuSoftDropCh6CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akPuSoftDropCh6CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akPuSoftDropCh6CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh6CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPuSoftDropCh6CaloJetID"),
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

akPuSoftDropCh6CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akPuSoftDropCh6CaloJets"),
           	    R0  = cms.double( 0.6)
)
akPuSoftDropCh6CalopatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh6CaloNjettiness:tau1','akPuSoftDropCh6CaloNjettiness:tau2','akPuSoftDropCh6CaloNjettiness:tau3']

akPuSoftDropCh6CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPuSoftDropCh6CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak6GenJets',#'ak6GenJets',
                                                             rParam = 0.6,
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
                                                             bTagJetName = cms.untracked.string("akPuSoftDropCh6Calo"),
                                                             jetName = cms.untracked.string("akPuSoftDropCh6Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(False),
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

akPuSoftDropCh6CaloJetSequence_mc = cms.Sequence(
                                                  #akPuSoftDropCh6Caloclean
                                                  #*
                                                  akPuSoftDropCh6Calomatch
                                                  #*
                                                  #akPuSoftDropCh6CalomatchGroomed
                                                  *
                                                  akPuSoftDropCh6Caloparton
                                                  *
                                                  akPuSoftDropCh6Calocorr
                                                  *
                                                  #akPuSoftDropCh6CaloJetID
                                                  #*
                                                  akPuSoftDropCh6CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akPuSoftDropCh6CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akPuSoftDropCh6CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akPuSoftDropCh6CaloJetBtagging
                                                  *
                                                  akPuSoftDropCh6CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akPuSoftDropCh6CalopatJetsWithBtagging
                                                  *
                                                  akPuSoftDropCh6CaloJetAnalyzer
                                                  )

akPuSoftDropCh6CaloJetSequence_data = cms.Sequence(akPuSoftDropCh6Calocorr
                                                    *
                                                    #akPuSoftDropCh6CaloJetID
                                                    #*
                                                    akPuSoftDropCh6CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akPuSoftDropCh6CaloJetBtagging
                                                    *
                                                    akPuSoftDropCh6CaloNjettiness 
                                                    *
                                                    akPuSoftDropCh6CalopatJetsWithBtagging
                                                    *
                                                    akPuSoftDropCh6CaloJetAnalyzer
                                                    )

akPuSoftDropCh6CaloJetSequence_jec = cms.Sequence(akPuSoftDropCh6CaloJetSequence_mc)
akPuSoftDropCh6CaloJetSequence_mb = cms.Sequence(akPuSoftDropCh6CaloJetSequence_mc)

akPuSoftDropCh6CaloJetSequence = cms.Sequence(akPuSoftDropCh6CaloJetSequence_jec)
akPuSoftDropCh6CaloJetAnalyzer.genPtMin = cms.untracked.double(1)
akPuSoftDropCh6CaloJetAnalyzer.jetPtMin = cms.double(1)
akPuSoftDropCh6CalopatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh6CaloJets:sym']
akPuSoftDropCh6CalopatJetsWithBtagging.userData.userInts.src += ['akPuSoftDropCh6CaloJets:droppedBranches']
