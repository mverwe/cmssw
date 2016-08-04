

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akVsSoftDropCh3Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVsSoftDropCh3CaloJets"),
    matched = cms.InputTag("ak3GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.3
    )

akVsSoftDropCh3CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh3GenJets"),
    matched = cms.InputTag("ak3GenJets"),
    resolveByMatchQuality = cms.bool(True),
    maxDeltaR = 0.3
    )

akVsSoftDropCh3Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh3CaloJets")
                                                        )

akVsSoftDropCh3Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akVsSoftDropCh3CaloJets"),
    payload = "AK3Calo_offline"
    )

akVsSoftDropCh3CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akVsSoftDropCh3CaloJets'))

#akVsSoftDropCh3Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak3GenJets'))

akVsSoftDropCh3CalobTagger = bTaggers("akVsSoftDropCh3Calo",0.3)

#create objects locally since they dont load properly otherwise
#akVsSoftDropCh3Calomatch = akVsSoftDropCh3CalobTagger.match
akVsSoftDropCh3Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akVsSoftDropCh3CaloJets"), matched = cms.InputTag("genParticles"))
akVsSoftDropCh3CaloPatJetFlavourAssociationLegacy = akVsSoftDropCh3CalobTagger.PatJetFlavourAssociationLegacy
akVsSoftDropCh3CaloPatJetPartons = akVsSoftDropCh3CalobTagger.PatJetPartons
akVsSoftDropCh3CaloJetTracksAssociatorAtVertex = akVsSoftDropCh3CalobTagger.JetTracksAssociatorAtVertex
akVsSoftDropCh3CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akVsSoftDropCh3CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh3CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh3CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh3CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh3CaloCombinedSecondaryVertexBJetTags = akVsSoftDropCh3CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh3CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh3CalobTagger.CombinedSecondaryVertexV2BJetTags
akVsSoftDropCh3CaloJetBProbabilityBJetTags = akVsSoftDropCh3CalobTagger.JetBProbabilityBJetTags
akVsSoftDropCh3CaloSoftPFMuonByPtBJetTags = akVsSoftDropCh3CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh3CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropCh3CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh3CaloTrackCountingHighEffBJetTags = akVsSoftDropCh3CalobTagger.TrackCountingHighEffBJetTags
akVsSoftDropCh3CaloTrackCountingHighPurBJetTags = akVsSoftDropCh3CalobTagger.TrackCountingHighPurBJetTags
akVsSoftDropCh3CaloPatJetPartonAssociationLegacy = akVsSoftDropCh3CalobTagger.PatJetPartonAssociationLegacy

akVsSoftDropCh3CaloImpactParameterTagInfos = akVsSoftDropCh3CalobTagger.ImpactParameterTagInfos
akVsSoftDropCh3CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh3CaloJetProbabilityBJetTags = akVsSoftDropCh3CalobTagger.JetProbabilityBJetTags

akVsSoftDropCh3CaloSecondaryVertexTagInfos = akVsSoftDropCh3CalobTagger.SecondaryVertexTagInfos
akVsSoftDropCh3CaloSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh3CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh3CaloSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh3CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh3CaloCombinedSecondaryVertexBJetTags = akVsSoftDropCh3CalobTagger.CombinedSecondaryVertexBJetTags
akVsSoftDropCh3CaloCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh3CalobTagger.CombinedSecondaryVertexV2BJetTags

akVsSoftDropCh3CaloSecondaryVertexNegativeTagInfos = akVsSoftDropCh3CalobTagger.SecondaryVertexNegativeTagInfos
akVsSoftDropCh3CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akVsSoftDropCh3CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akVsSoftDropCh3CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akVsSoftDropCh3CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akVsSoftDropCh3CaloNegativeCombinedSecondaryVertexBJetTags = akVsSoftDropCh3CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akVsSoftDropCh3CaloPositiveCombinedSecondaryVertexBJetTags = akVsSoftDropCh3CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akVsSoftDropCh3CaloNegativeCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh3CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akVsSoftDropCh3CaloPositiveCombinedSecondaryVertexV2BJetTags = akVsSoftDropCh3CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akVsSoftDropCh3CaloSoftPFMuonsTagInfos = akVsSoftDropCh3CalobTagger.SoftPFMuonsTagInfos
akVsSoftDropCh3CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akVsSoftDropCh3CaloSoftPFMuonBJetTags = akVsSoftDropCh3CalobTagger.SoftPFMuonBJetTags
akVsSoftDropCh3CaloSoftPFMuonByIP3dBJetTags = akVsSoftDropCh3CalobTagger.SoftPFMuonByIP3dBJetTags
akVsSoftDropCh3CaloSoftPFMuonByPtBJetTags = akVsSoftDropCh3CalobTagger.SoftPFMuonByPtBJetTags
akVsSoftDropCh3CaloNegativeSoftPFMuonByPtBJetTags = akVsSoftDropCh3CalobTagger.NegativeSoftPFMuonByPtBJetTags
akVsSoftDropCh3CaloPositiveSoftPFMuonByPtBJetTags = akVsSoftDropCh3CalobTagger.PositiveSoftPFMuonByPtBJetTags
akVsSoftDropCh3CaloPatJetFlavourIdLegacy = cms.Sequence(akVsSoftDropCh3CaloPatJetPartonAssociationLegacy*akVsSoftDropCh3CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akVsSoftDropCh3CaloPatJetFlavourAssociation = akVsSoftDropCh3CalobTagger.PatJetFlavourAssociation
#akVsSoftDropCh3CaloPatJetFlavourId = cms.Sequence(akVsSoftDropCh3CaloPatJetPartons*akVsSoftDropCh3CaloPatJetFlavourAssociation)

akVsSoftDropCh3CaloJetBtaggingIP       = cms.Sequence(akVsSoftDropCh3CaloImpactParameterTagInfos *
            (akVsSoftDropCh3CaloTrackCountingHighEffBJetTags +
             akVsSoftDropCh3CaloTrackCountingHighPurBJetTags +
             akVsSoftDropCh3CaloJetProbabilityBJetTags +
             akVsSoftDropCh3CaloJetBProbabilityBJetTags 
            )
            )

akVsSoftDropCh3CaloJetBtaggingSV = cms.Sequence(akVsSoftDropCh3CaloImpactParameterTagInfos
            *
            akVsSoftDropCh3CaloSecondaryVertexTagInfos
            * (akVsSoftDropCh3CaloSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh3CaloSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh3CaloCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh3CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh3CaloJetBtaggingNegSV = cms.Sequence(akVsSoftDropCh3CaloImpactParameterTagInfos
            *
            akVsSoftDropCh3CaloSecondaryVertexNegativeTagInfos
            * (akVsSoftDropCh3CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akVsSoftDropCh3CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akVsSoftDropCh3CaloNegativeCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh3CaloPositiveCombinedSecondaryVertexBJetTags+
                akVsSoftDropCh3CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akVsSoftDropCh3CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akVsSoftDropCh3CaloJetBtaggingMu = cms.Sequence(akVsSoftDropCh3CaloSoftPFMuonsTagInfos * (akVsSoftDropCh3CaloSoftPFMuonBJetTags
                +
                akVsSoftDropCh3CaloSoftPFMuonByIP3dBJetTags
                +
                akVsSoftDropCh3CaloSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh3CaloNegativeSoftPFMuonByPtBJetTags
                +
                akVsSoftDropCh3CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akVsSoftDropCh3CaloJetBtagging = cms.Sequence(akVsSoftDropCh3CaloJetBtaggingIP
            *akVsSoftDropCh3CaloJetBtaggingSV
            *akVsSoftDropCh3CaloJetBtaggingNegSV
#            *akVsSoftDropCh3CaloJetBtaggingMu
            )

akVsSoftDropCh3CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akVsSoftDropCh3CaloJets"),
        genJetMatch          = cms.InputTag("akVsSoftDropCh3Calomatch"),
        genPartonMatch       = cms.InputTag("akVsSoftDropCh3Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVsSoftDropCh3Calocorr")),
        JetPartonMapSource   = cms.InputTag("akVsSoftDropCh3CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akVsSoftDropCh3CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akVsSoftDropCh3CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akVsSoftDropCh3CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh3CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akVsSoftDropCh3CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akVsSoftDropCh3CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akVsSoftDropCh3CaloJetBProbabilityBJetTags"),
            cms.InputTag("akVsSoftDropCh3CaloJetProbabilityBJetTags"),
            #cms.InputTag("akVsSoftDropCh3CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akVsSoftDropCh3CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akVsSoftDropCh3CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akVsSoftDropCh3CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akVsSoftDropCh3CaloJetID"),
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

akVsSoftDropCh3CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akVsSoftDropCh3CaloJets"),
           	    R0  = cms.double( 0.3)
)
akVsSoftDropCh3CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh3CaloNjettiness:tau1','akVsSoftDropCh3CaloNjettiness:tau2','akVsSoftDropCh3CaloNjettiness:tau3']

akVsSoftDropCh3CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVsSoftDropCh3CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak3GenJets',#'ak3GenJets',
                                                             rParam = 0.3,
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
                                                             bTagJetName = cms.untracked.string("akVsSoftDropCh3Calo"),
                                                             jetName = cms.untracked.string("akVsSoftDropCh3Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(False),
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

akVsSoftDropCh3CaloJetSequence_mc = cms.Sequence(
                                                  #akVsSoftDropCh3Caloclean
                                                  #*
                                                  akVsSoftDropCh3Calomatch
                                                  #*
                                                  #akVsSoftDropCh3CalomatchGroomed
                                                  *
                                                  akVsSoftDropCh3Caloparton
                                                  *
                                                  akVsSoftDropCh3Calocorr
                                                  *
                                                  #akVsSoftDropCh3CaloJetID
                                                  #*
                                                  akVsSoftDropCh3CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akVsSoftDropCh3CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akVsSoftDropCh3CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akVsSoftDropCh3CaloJetBtagging
                                                  *
                                                  akVsSoftDropCh3CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akVsSoftDropCh3CalopatJetsWithBtagging
                                                  *
                                                  akVsSoftDropCh3CaloJetAnalyzer
                                                  )

akVsSoftDropCh3CaloJetSequence_data = cms.Sequence(akVsSoftDropCh3Calocorr
                                                    *
                                                    #akVsSoftDropCh3CaloJetID
                                                    #*
                                                    akVsSoftDropCh3CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akVsSoftDropCh3CaloJetBtagging
                                                    *
                                                    akVsSoftDropCh3CaloNjettiness 
                                                    *
                                                    akVsSoftDropCh3CalopatJetsWithBtagging
                                                    *
                                                    akVsSoftDropCh3CaloJetAnalyzer
                                                    )

akVsSoftDropCh3CaloJetSequence_jec = cms.Sequence(akVsSoftDropCh3CaloJetSequence_mc)
akVsSoftDropCh3CaloJetSequence_mb = cms.Sequence(akVsSoftDropCh3CaloJetSequence_mc)

akVsSoftDropCh3CaloJetSequence = cms.Sequence(akVsSoftDropCh3CaloJetSequence_jec)
akVsSoftDropCh3CaloJetAnalyzer.genPtMin = cms.untracked.double(1)
akVsSoftDropCh3CaloJetAnalyzer.jetPtMin = cms.double(1)
akVsSoftDropCh3CalopatJetsWithBtagging.userData.userFloats.src += ['akVsSoftDropCh3CaloJets:sym']
akVsSoftDropCh3CalopatJetsWithBtagging.userData.userInts.src += ['akVsSoftDropCh3CaloJets:droppedBranches']
