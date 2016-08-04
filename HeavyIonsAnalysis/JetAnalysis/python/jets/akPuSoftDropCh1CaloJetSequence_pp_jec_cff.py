

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPuSoftDropCh1Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPuSoftDropCh1CaloJets"),
    matched = cms.InputTag("ak1GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akPuSoftDropCh1CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("akSoftDropCh1GenJets"),
    matched = cms.InputTag("ak1GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akPuSoftDropCh1Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh1CaloJets")
                                                        )

akPuSoftDropCh1Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akPuSoftDropCh1CaloJets"),
    payload = "AKPu1Calo_offline"
    )

akPuSoftDropCh1CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akPuSoftDropCh1CaloJets'))

#akPuSoftDropCh1Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak1GenJets'))

akPuSoftDropCh1CalobTagger = bTaggers("akPuSoftDropCh1Calo",0.1)

#create objects locally since they dont load properly otherwise
#akPuSoftDropCh1Calomatch = akPuSoftDropCh1CalobTagger.match
akPuSoftDropCh1Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPuSoftDropCh1CaloJets"), matched = cms.InputTag("genParticles"))
akPuSoftDropCh1CaloPatJetFlavourAssociationLegacy = akPuSoftDropCh1CalobTagger.PatJetFlavourAssociationLegacy
akPuSoftDropCh1CaloPatJetPartons = akPuSoftDropCh1CalobTagger.PatJetPartons
akPuSoftDropCh1CaloJetTracksAssociatorAtVertex = akPuSoftDropCh1CalobTagger.JetTracksAssociatorAtVertex
akPuSoftDropCh1CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPuSoftDropCh1CaloSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh1CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh1CaloSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh1CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh1CaloCombinedSecondaryVertexBJetTags = akPuSoftDropCh1CalobTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh1CaloCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh1CalobTagger.CombinedSecondaryVertexV2BJetTags
akPuSoftDropCh1CaloJetBProbabilityBJetTags = akPuSoftDropCh1CalobTagger.JetBProbabilityBJetTags
akPuSoftDropCh1CaloSoftPFMuonByPtBJetTags = akPuSoftDropCh1CalobTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh1CaloSoftPFMuonByIP3dBJetTags = akPuSoftDropCh1CalobTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh1CaloTrackCountingHighEffBJetTags = akPuSoftDropCh1CalobTagger.TrackCountingHighEffBJetTags
akPuSoftDropCh1CaloTrackCountingHighPurBJetTags = akPuSoftDropCh1CalobTagger.TrackCountingHighPurBJetTags
akPuSoftDropCh1CaloPatJetPartonAssociationLegacy = akPuSoftDropCh1CalobTagger.PatJetPartonAssociationLegacy

akPuSoftDropCh1CaloImpactParameterTagInfos = akPuSoftDropCh1CalobTagger.ImpactParameterTagInfos
akPuSoftDropCh1CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh1CaloJetProbabilityBJetTags = akPuSoftDropCh1CalobTagger.JetProbabilityBJetTags

akPuSoftDropCh1CaloSecondaryVertexTagInfos = akPuSoftDropCh1CalobTagger.SecondaryVertexTagInfos
akPuSoftDropCh1CaloSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh1CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh1CaloSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh1CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh1CaloCombinedSecondaryVertexBJetTags = akPuSoftDropCh1CalobTagger.CombinedSecondaryVertexBJetTags
akPuSoftDropCh1CaloCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh1CalobTagger.CombinedSecondaryVertexV2BJetTags

akPuSoftDropCh1CaloSecondaryVertexNegativeTagInfos = akPuSoftDropCh1CalobTagger.SecondaryVertexNegativeTagInfos
akPuSoftDropCh1CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akPuSoftDropCh1CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPuSoftDropCh1CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akPuSoftDropCh1CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPuSoftDropCh1CaloNegativeCombinedSecondaryVertexBJetTags = akPuSoftDropCh1CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akPuSoftDropCh1CaloPositiveCombinedSecondaryVertexBJetTags = akPuSoftDropCh1CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akPuSoftDropCh1CaloNegativeCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh1CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPuSoftDropCh1CaloPositiveCombinedSecondaryVertexV2BJetTags = akPuSoftDropCh1CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPuSoftDropCh1CaloSoftPFMuonsTagInfos = akPuSoftDropCh1CalobTagger.SoftPFMuonsTagInfos
akPuSoftDropCh1CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPuSoftDropCh1CaloSoftPFMuonBJetTags = akPuSoftDropCh1CalobTagger.SoftPFMuonBJetTags
akPuSoftDropCh1CaloSoftPFMuonByIP3dBJetTags = akPuSoftDropCh1CalobTagger.SoftPFMuonByIP3dBJetTags
akPuSoftDropCh1CaloSoftPFMuonByPtBJetTags = akPuSoftDropCh1CalobTagger.SoftPFMuonByPtBJetTags
akPuSoftDropCh1CaloNegativeSoftPFMuonByPtBJetTags = akPuSoftDropCh1CalobTagger.NegativeSoftPFMuonByPtBJetTags
akPuSoftDropCh1CaloPositiveSoftPFMuonByPtBJetTags = akPuSoftDropCh1CalobTagger.PositiveSoftPFMuonByPtBJetTags
akPuSoftDropCh1CaloPatJetFlavourIdLegacy = cms.Sequence(akPuSoftDropCh1CaloPatJetPartonAssociationLegacy*akPuSoftDropCh1CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub, but keep it here for reference
#akPuSoftDropCh1CaloPatJetFlavourAssociation = akPuSoftDropCh1CalobTagger.PatJetFlavourAssociation
#akPuSoftDropCh1CaloPatJetFlavourId = cms.Sequence(akPuSoftDropCh1CaloPatJetPartons*akPuSoftDropCh1CaloPatJetFlavourAssociation)

akPuSoftDropCh1CaloJetBtaggingIP       = cms.Sequence(akPuSoftDropCh1CaloImpactParameterTagInfos *
            (akPuSoftDropCh1CaloTrackCountingHighEffBJetTags +
             akPuSoftDropCh1CaloTrackCountingHighPurBJetTags +
             akPuSoftDropCh1CaloJetProbabilityBJetTags +
             akPuSoftDropCh1CaloJetBProbabilityBJetTags 
            )
            )

akPuSoftDropCh1CaloJetBtaggingSV = cms.Sequence(akPuSoftDropCh1CaloImpactParameterTagInfos
            *
            akPuSoftDropCh1CaloSecondaryVertexTagInfos
            * (akPuSoftDropCh1CaloSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh1CaloSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh1CaloCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh1CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh1CaloJetBtaggingNegSV = cms.Sequence(akPuSoftDropCh1CaloImpactParameterTagInfos
            *
            akPuSoftDropCh1CaloSecondaryVertexNegativeTagInfos
            * (akPuSoftDropCh1CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akPuSoftDropCh1CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akPuSoftDropCh1CaloNegativeCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh1CaloPositiveCombinedSecondaryVertexBJetTags+
                akPuSoftDropCh1CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akPuSoftDropCh1CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akPuSoftDropCh1CaloJetBtaggingMu = cms.Sequence(akPuSoftDropCh1CaloSoftPFMuonsTagInfos * (akPuSoftDropCh1CaloSoftPFMuonBJetTags
                +
                akPuSoftDropCh1CaloSoftPFMuonByIP3dBJetTags
                +
                akPuSoftDropCh1CaloSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh1CaloNegativeSoftPFMuonByPtBJetTags
                +
                akPuSoftDropCh1CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akPuSoftDropCh1CaloJetBtagging = cms.Sequence(akPuSoftDropCh1CaloJetBtaggingIP
            *akPuSoftDropCh1CaloJetBtaggingSV
            *akPuSoftDropCh1CaloJetBtaggingNegSV
#            *akPuSoftDropCh1CaloJetBtaggingMu
            )

akPuSoftDropCh1CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akPuSoftDropCh1CaloJets"),
        genJetMatch          = cms.InputTag("akPuSoftDropCh1Calomatch"),
        genPartonMatch       = cms.InputTag("akPuSoftDropCh1Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPuSoftDropCh1Calocorr")),
        JetPartonMapSource   = cms.InputTag("akPuSoftDropCh1CaloPatJetFlavourAssociationLegacy"),
	JetFlavourInfoSource   = cms.InputTag("akPuSoftDropCh1CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPuSoftDropCh1CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = True,
        discriminatorSources = cms.VInputTag(cms.InputTag("akPuSoftDropCh1CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh1CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPuSoftDropCh1CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPuSoftDropCh1CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akPuSoftDropCh1CaloJetBProbabilityBJetTags"),
            cms.InputTag("akPuSoftDropCh1CaloJetProbabilityBJetTags"),
            #cms.InputTag("akPuSoftDropCh1CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akPuSoftDropCh1CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akPuSoftDropCh1CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akPuSoftDropCh1CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPuSoftDropCh1CaloJetID"),
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

akPuSoftDropCh1CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akPuSoftDropCh1CaloJets"),
           	    R0  = cms.double( 0.1)
)
akPuSoftDropCh1CalopatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh1CaloNjettiness:tau1','akPuSoftDropCh1CaloNjettiness:tau2','akPuSoftDropCh1CaloNjettiness:tau3']

akPuSoftDropCh1CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPuSoftDropCh1CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak1GenJets',#'ak1GenJets',
                                                             rParam = 0.1,
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
                                                             bTagJetName = cms.untracked.string("akPuSoftDropCh1Calo"),
                                                             jetName = cms.untracked.string("akPuSoftDropCh1Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(False),
							     doSubJets = cms.untracked.bool(True),
                                                             doGenSubJets = cms.untracked.bool(True),     
                                                             subjetGenTag = cms.untracked.InputTag("akSoftDropCh1GenJets"),
                                                             doGenTaus = False,
                                                             genTau1 = cms.InputTag("akSoftDropCh1GenNjettiness","tau1"),
                                                             genTau2 = cms.InputTag("akSoftDropCh1GenNjettiness","tau2"),
                                                             genTau3 = cms.InputTag("akSoftDropCh1GenNjettiness","tau3"),
                                                             doGenSym = True,
                                                             genSym = cms.InputTag("akSoftDropCh1GenJets","sym"),
                                                             genDroppedBranches = cms.InputTag("akSoftDropCh1GenJets","droppedBranches")
                                                             )

akPuSoftDropCh1CaloJetSequence_mc = cms.Sequence(
                                                  #akPuSoftDropCh1Caloclean
                                                  #*
                                                  akPuSoftDropCh1Calomatch
                                                  #*
                                                  #akPuSoftDropCh1CalomatchGroomed
                                                  *
                                                  akPuSoftDropCh1Caloparton
                                                  *
                                                  akPuSoftDropCh1Calocorr
                                                  *
                                                  #akPuSoftDropCh1CaloJetID
                                                  #*
                                                  akPuSoftDropCh1CaloPatJetFlavourIdLegacy
                                                  #*
			                          #akPuSoftDropCh1CaloPatJetFlavourId  # Use legacy algo till PU implemented
                                                  *
                                                  akPuSoftDropCh1CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akPuSoftDropCh1CaloJetBtagging
                                                  *
                                                  akPuSoftDropCh1CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akPuSoftDropCh1CalopatJetsWithBtagging
                                                  *
                                                  akPuSoftDropCh1CaloJetAnalyzer
                                                  )

akPuSoftDropCh1CaloJetSequence_data = cms.Sequence(akPuSoftDropCh1Calocorr
                                                    *
                                                    #akPuSoftDropCh1CaloJetID
                                                    #*
                                                    akPuSoftDropCh1CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akPuSoftDropCh1CaloJetBtagging
                                                    *
                                                    akPuSoftDropCh1CaloNjettiness 
                                                    *
                                                    akPuSoftDropCh1CalopatJetsWithBtagging
                                                    *
                                                    akPuSoftDropCh1CaloJetAnalyzer
                                                    )

akPuSoftDropCh1CaloJetSequence_jec = cms.Sequence(akPuSoftDropCh1CaloJetSequence_mc)
akPuSoftDropCh1CaloJetSequence_mb = cms.Sequence(akPuSoftDropCh1CaloJetSequence_mc)

akPuSoftDropCh1CaloJetSequence = cms.Sequence(akPuSoftDropCh1CaloJetSequence_jec)
akPuSoftDropCh1CaloJetAnalyzer.genPtMin = cms.untracked.double(1)
akPuSoftDropCh1CaloJetAnalyzer.jetPtMin = cms.double(1)
akPuSoftDropCh1CalopatJetsWithBtagging.userData.userFloats.src += ['akPuSoftDropCh1CaloJets:sym']
akPuSoftDropCh1CalopatJetsWithBtagging.userData.userInts.src += ['akPuSoftDropCh1CaloJets:droppedBranches']
