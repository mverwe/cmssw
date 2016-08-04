

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akSoftDropCh3Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh3CaloJets"),
    matched = cms.InputTag("ak3GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.3
    )

akSoftDropCh3CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh3GenJets"),
    matched = cms.InputTag("ak3GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.3
    )

akSoftDropCh3Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh3CaloJets")
                                                        )

akSoftDropCh3Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akSoftDropCh3CaloJets"),
    payload = "AK3Calo_offline"
    )

akSoftDropCh3CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akSoftDropCh3CaloJets'))

#akSoftDropCh3Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak3GenJets'))

akSoftDropCh3CalobTagger = bTaggers("akSoftDropCh3Calo",0.3)

#create objects locally since they dont load properly otherwise
#akSoftDropCh3Calomatch = akSoftDropCh3CalobTagger.match
akSoftDropCh3Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akSoftDropCh3CaloJets"), matched = cms.InputTag("genParticles"))
akSoftDropCh3CaloPatJetFlavourAssociationLegacy = akSoftDropCh3CalobTagger.PatJetFlavourAssociationLegacy
akSoftDropCh3CaloPatJetPartons = akSoftDropCh3CalobTagger.PatJetPartons
akSoftDropCh3CaloJetTracksAssociatorAtVertex = akSoftDropCh3CalobTagger.JetTracksAssociatorAtVertex
akSoftDropCh3CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akSoftDropCh3CaloSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh3CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh3CaloSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh3CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh3CaloCombinedSecondaryVertexBJetTags = akSoftDropCh3CalobTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh3CaloCombinedSecondaryVertexV2BJetTags = akSoftDropCh3CalobTagger.CombinedSecondaryVertexV2BJetTags
akSoftDropCh3CaloJetBProbabilityBJetTags = akSoftDropCh3CalobTagger.JetBProbabilityBJetTags
akSoftDropCh3CaloSoftPFMuonByPtBJetTags = akSoftDropCh3CalobTagger.SoftPFMuonByPtBJetTags
akSoftDropCh3CaloSoftPFMuonByIP3dBJetTags = akSoftDropCh3CalobTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh3CaloTrackCountingHighEffBJetTags = akSoftDropCh3CalobTagger.TrackCountingHighEffBJetTags
akSoftDropCh3CaloTrackCountingHighPurBJetTags = akSoftDropCh3CalobTagger.TrackCountingHighPurBJetTags
akSoftDropCh3CaloPatJetPartonAssociationLegacy = akSoftDropCh3CalobTagger.PatJetPartonAssociationLegacy

akSoftDropCh3CaloImpactParameterTagInfos = akSoftDropCh3CalobTagger.ImpactParameterTagInfos
akSoftDropCh3CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh3CaloJetProbabilityBJetTags = akSoftDropCh3CalobTagger.JetProbabilityBJetTags

akSoftDropCh3CaloSecondaryVertexTagInfos = akSoftDropCh3CalobTagger.SecondaryVertexTagInfos
akSoftDropCh3CaloSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh3CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akSoftDropCh3CaloSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh3CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akSoftDropCh3CaloCombinedSecondaryVertexBJetTags = akSoftDropCh3CalobTagger.CombinedSecondaryVertexBJetTags
akSoftDropCh3CaloCombinedSecondaryVertexV2BJetTags = akSoftDropCh3CalobTagger.CombinedSecondaryVertexV2BJetTags

akSoftDropCh3CaloSecondaryVertexNegativeTagInfos = akSoftDropCh3CalobTagger.SecondaryVertexNegativeTagInfos
akSoftDropCh3CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akSoftDropCh3CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akSoftDropCh3CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akSoftDropCh3CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akSoftDropCh3CaloNegativeCombinedSecondaryVertexBJetTags = akSoftDropCh3CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akSoftDropCh3CaloPositiveCombinedSecondaryVertexBJetTags = akSoftDropCh3CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akSoftDropCh3CaloNegativeCombinedSecondaryVertexV2BJetTags = akSoftDropCh3CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akSoftDropCh3CaloPositiveCombinedSecondaryVertexV2BJetTags = akSoftDropCh3CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akSoftDropCh3CaloSoftPFMuonsTagInfos = akSoftDropCh3CalobTagger.SoftPFMuonsTagInfos
akSoftDropCh3CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akSoftDropCh3CaloSoftPFMuonBJetTags = akSoftDropCh3CalobTagger.SoftPFMuonBJetTags
akSoftDropCh3CaloSoftPFMuonByIP3dBJetTags = akSoftDropCh3CalobTagger.SoftPFMuonByIP3dBJetTags
akSoftDropCh3CaloSoftPFMuonByPtBJetTags = akSoftDropCh3CalobTagger.SoftPFMuonByPtBJetTags
akSoftDropCh3CaloNegativeSoftPFMuonByPtBJetTags = akSoftDropCh3CalobTagger.NegativeSoftPFMuonByPtBJetTags
akSoftDropCh3CaloPositiveSoftPFMuonByPtBJetTags = akSoftDropCh3CalobTagger.PositiveSoftPFMuonByPtBJetTags
akSoftDropCh3CaloPatJetFlavourIdLegacy = cms.Sequence(akSoftDropCh3CaloPatJetPartonAssociationLegacy*akSoftDropCh3CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akSoftDropCh3CaloPatJetFlavourAssociation = akSoftDropCh3CalobTagger.PatJetFlavourAssociation
#akSoftDropCh3CaloPatJetFlavourId = cms.Sequence(akSoftDropCh3CaloPatJetPartons*akSoftDropCh3CaloPatJetFlavourAssociation)

akSoftDropCh3CaloJetBtaggingIP       = cms.Sequence(akSoftDropCh3CaloImpactParameterTagInfos *
            (akSoftDropCh3CaloTrackCountingHighEffBJetTags +
             akSoftDropCh3CaloTrackCountingHighPurBJetTags +
             akSoftDropCh3CaloJetProbabilityBJetTags +
             akSoftDropCh3CaloJetBProbabilityBJetTags 
            )
            )

akSoftDropCh3CaloJetBtaggingSV = cms.Sequence(akSoftDropCh3CaloImpactParameterTagInfos
            *
            akSoftDropCh3CaloSecondaryVertexTagInfos
            * (akSoftDropCh3CaloSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh3CaloSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh3CaloCombinedSecondaryVertexBJetTags+
                akSoftDropCh3CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh3CaloJetBtaggingNegSV = cms.Sequence(akSoftDropCh3CaloImpactParameterTagInfos
            *
            akSoftDropCh3CaloSecondaryVertexNegativeTagInfos
            * (akSoftDropCh3CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akSoftDropCh3CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akSoftDropCh3CaloNegativeCombinedSecondaryVertexBJetTags+
                akSoftDropCh3CaloPositiveCombinedSecondaryVertexBJetTags+
                akSoftDropCh3CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akSoftDropCh3CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akSoftDropCh3CaloJetBtaggingMu = cms.Sequence(akSoftDropCh3CaloSoftPFMuonsTagInfos * (akSoftDropCh3CaloSoftPFMuonBJetTags
                +
                akSoftDropCh3CaloSoftPFMuonByIP3dBJetTags
                +
                akSoftDropCh3CaloSoftPFMuonByPtBJetTags
                +
                akSoftDropCh3CaloNegativeSoftPFMuonByPtBJetTags
                +
                akSoftDropCh3CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akSoftDropCh3CaloJetBtagging = cms.Sequence(akSoftDropCh3CaloJetBtaggingIP
            *akSoftDropCh3CaloJetBtaggingSV
            *akSoftDropCh3CaloJetBtaggingNegSV
#            *akSoftDropCh3CaloJetBtaggingMu
            )

akSoftDropCh3CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akSoftDropCh3CaloJets"),
        genJetMatch          = cms.InputTag("akSoftDropCh3Calomatch"),
        genPartonMatch       = cms.InputTag("akSoftDropCh3Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akSoftDropCh3Calocorr")),
        JetPartonMapSource   = cms.InputTag("akSoftDropCh3CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akSoftDropCh3CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akSoftDropCh3CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akSoftDropCh3CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akSoftDropCh3CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akSoftDropCh3CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akSoftDropCh3CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akSoftDropCh3CaloJetBProbabilityBJetTags"),
            cms.InputTag("akSoftDropCh3CaloJetProbabilityBJetTags"),
            #cms.InputTag("akSoftDropCh3CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akSoftDropCh3CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akSoftDropCh3CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akSoftDropCh3CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akSoftDropCh3CaloJetID"),
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

akSoftDropCh3CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akSoftDropCh3CaloJets"),
           	    R0  = cms.double( 0.3)
)
akSoftDropCh3CalopatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh3CaloNjettiness:tau1','akSoftDropCh3CaloNjettiness:tau2','akSoftDropCh3CaloNjettiness:tau3']

akSoftDropCh3CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akSoftDropCh3CalopatJetsWithBtagging"),
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
                                                             bTagJetName = cms.untracked.string("akSoftDropCh3Calo"),
                                                             jetName = cms.untracked.string("akSoftDropCh3Calo"),
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

akSoftDropCh3CaloJetSequence_mc = cms.Sequence(
                                                  #akSoftDropCh3Caloclean
                                                  #*
                                                  akSoftDropCh3Calomatch
                                                  #*
                                                  #akSoftDropCh3CalomatchGroomed
                                                  *
                                                  akSoftDropCh3Caloparton
                                                  *
                                                  akSoftDropCh3Calocorr
                                                  *
                                                  #akSoftDropCh3CaloJetID
                                                  #*
                                                  akSoftDropCh3CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akSoftDropCh3CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akSoftDropCh3CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akSoftDropCh3CaloJetBtagging
                                                  *
                                                  akSoftDropCh3CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akSoftDropCh3CalopatJetsWithBtagging
                                                  *
                                                  akSoftDropCh3CaloJetAnalyzer
                                                  )

akSoftDropCh3CaloJetSequence_data = cms.Sequence(akSoftDropCh3Calocorr
                                                    *
                                                    #akSoftDropCh3CaloJetID
                                                    #*
                                                    akSoftDropCh3CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akSoftDropCh3CaloJetBtagging
                                                    *
                                                    akSoftDropCh3CaloNjettiness 
                                                    *
                                                    akSoftDropCh3CalopatJetsWithBtagging
                                                    *
                                                    akSoftDropCh3CaloJetAnalyzer
                                                    )

akSoftDropCh3CaloJetSequence_jec = cms.Sequence(akSoftDropCh3CaloJetSequence_mc)
akSoftDropCh3CaloJetSequence_mb = cms.Sequence(akSoftDropCh3CaloJetSequence_mc)

akSoftDropCh3CaloJetSequence = cms.Sequence(akSoftDropCh3CaloJetSequence_jec)
akSoftDropCh3CaloJetAnalyzer.genPtMin = cms.untracked.double(1)
akSoftDropCh3CaloJetAnalyzer.jetPtMin = cms.double(1)
akSoftDropCh3CalopatJetsWithBtagging.userData.userFloats.src += ['akSoftDropCh3CaloJets:sym']
akSoftDropCh3CalopatJetsWithBtagging.userData.userInts.src += ['akSoftDropCh3CaloJets:droppedBranches']
