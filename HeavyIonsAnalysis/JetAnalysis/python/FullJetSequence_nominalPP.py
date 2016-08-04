import FWCore.ParameterSet.Config as cms

### PP RECO does not include R=3 or R=5 jets.
### re-RECO is only possible for PF, RECO is missing calotowers
from RecoJets.JetProducers.ak5PFJets_cfi import ak5PFJets
ak5PFJets.doAreaFastjet = True
ak3PFJets = ak5PFJets.clone(rParam = 0.3)
from RecoJets.JetProducers.ak5GenJets_cfi import ak5GenJets
ak3GenJets = ak5GenJets.clone(rParam = 0.3)
ak4GenJets = ak5GenJets.clone(rParam = 0.4)

#Njettiness gen jets
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness
ak3GenNjettiness = Njettiness.clone(
                    src = cms.InputTag("ak3GenJets"),
                    R0  = cms.double( 0.3)
)
ak4GenNjettiness = Njettiness.clone(
                    src = cms.InputTag("ak4GenJets"),
                    R0  = cms.double( 0.4)
)
ak5GenNjettiness = Njettiness.clone(
                    src = cms.InputTag("ak5GenJets"),
                    R0  = cms.double( 0.5)
)

#SoftDrop PF jets
from HeavyIonsAnalysis.JetAnalysis.akSoftDrop4PFJets_cfi import akSoftDrop4PFJets, akSoftDropCh4PFJets
from RecoJets.JetProducers.PFJetParameters_cfi import *
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *
akSoftDrop4PFJets.zcut = cms.double(0.1)
akSoftDropCh4PFJets.zcut = cms.double(0.1)
akSoftDrop5PFJets = akSoftDrop4PFJets.clone(rParam = cms.double(0.5), R0 = cms.double(0.5))
akSoftDropCh5PFJets = akSoftDropCh4PFJets.clone(rParam = cms.double(0.5), R0 = cms.double(0.5))

akSoftDropZCut0004PFJets = akSoftDrop4PFJets.clone(zcut = cms.double(0.0))
akSoftDropChZCut0004PFJets = akSoftDropCh4PFJets.clone(zcut = cms.double(0.0))
akSoftDropZCut0005PFJets = akSoftDrop5PFJets.clone(zcut = cms.double(0.0))
akSoftDropChZCut0005PFJets = akSoftDropCh5PFJets.clone(zcut = cms.double(0.0))

from HeavyIonsAnalysis.JetAnalysis.akSoftDrop4GenJets_cfi import akSoftDrop4GenJets, akSoftDropCh4GenJets
akSoftDrop4GenJets.zcut = cms.double(0.1)
akSoftDropCh4GenJets.zcut = cms.double(0.1)
akSoftDrop5GenJets = akSoftDrop4GenJets.clone(rParam = 0.5)
akSoftDropCh5GenJets = akSoftDropCh4GenJets.clone(rParam = 0.5)

akSoftDropZCut0004GenJets = akSoftDrop4GenJets.clone(zcut = cms.double(0.0))
akSoftDropChZCut0004GenJets = akSoftDropCh4GenJets.clone(zcut = cms.double(0.0))
akSoftDropZCut0005GenJets = akSoftDrop5GenJets.clone(zcut = cms.double(0.0))
akSoftDropChZCut0005GenJets = akSoftDropCh5GenJets.clone(zcut = cms.double(0.0))

#from HeavyIonsAnalysis.JetAnalysis.akSD4GenJets_cfi import akSD4GenJets
#akSD5GenJets = akSD4GenJets.clone(rParam = 0.5)

#Filter PF jets
akFilter4PFJets = cms.EDProducer(
    "FastjetJetProducer",
    PFJetParameters,
    AnomalousCellParameters,
    jetAlgorithm = cms.string("AntiKt"),
    rParam       = cms.double(0.4),
    useFiltering = cms.bool(True),
    nFilt = cms.int32(4),
    rFilt = cms.double(0.15),
    useExplicitGhosts = cms.bool(True),
    writeCompound = cms.bool(True),
    jetCollInstanceName=cms.string("SubJets")
)
akFilter5PFJets = akFilter4PFJets.clone(rParam = cms.double(0.5))

from RecoJets.Configuration.GenJetParticles_cff import *
from RecoHI.HiJetAlgos.HiGenJets_cff import *
from HeavyIonsAnalysis.JetAnalysis.makePartons_cff import myPartons

from HeavyIonsAnalysis.JetAnalysis.jets.ak3PFJetSequence_pp_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.ak4PFJetSequence_pp_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.ak5PFJetSequence_pp_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.ak4CaloJetSequence_pp_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akSoftDrop4PFJetSequence_pp_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akSoftDrop5PFJetSequence_pp_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akSoftDropCh4PFJetSequence_pp_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akSoftDropCh5PFJetSequence_pp_mc_cff import *

from HeavyIonsAnalysis.JetAnalysis.jets.akSoftDropZCut0004PFJetSequence_pp_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akSoftDropZCut0005PFJetSequence_pp_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akSoftDropChZCut0004PFJetSequence_pp_mc_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akSoftDropChZCut0005PFJetSequence_pp_mc_cff import *

highPurityTracks = cms.EDFilter("TrackSelector",
                                src = cms.InputTag("generalTracks"),
                                cut = cms.string('quality("highPurity")')
)

# Other radii jets and calo jets need to be reconstructed
jetSequences = cms.Sequence(
    myPartons +
    genParticlesForJets +
    ak3GenJets +
    ak4GenJets +
    ak5GenJets +
    ak3GenNjettiness +
    ak4GenNjettiness +
    ak5GenNjettiness +
    ak3PFJets +
    ak5PFJets +
    akSoftDrop4PFJets +
    akSoftDrop5PFJets +
    akSoftDropCh4PFJets +
    akSoftDropCh5PFJets +
    akSoftDropZCut0004PFJets +
    akSoftDropZCut0005PFJets +
    akSoftDropChZCut0004PFJets +
    akSoftDropChZCut0005PFJets +
    akFilter4PFJets +
    akFilter5PFJets +
    akSoftDrop4GenJets +
    akSoftDrop5GenJets +
    akSoftDropCh4GenJets +
    akSoftDropCh5GenJets +
    akSoftDropZCut0004GenJets +
    akSoftDropZCut0005GenJets +
    akSoftDropChZCut0004GenJets +
    akSoftDropChZCut0005GenJets +
    highPurityTracks +
    ak3PFJetSequence +
    ak4PFJetSequence +
    ak5PFJetSequence +
    #ak4CaloJetSequence +
    akSoftDrop4PFJetSequence +
    akSoftDrop5PFJetSequence +
    akSoftDropCh4PFJetSequence +
    akSoftDropCh5PFJetSequence +
    akSoftDropZCut0004PFJetSequence +
    akSoftDropZCut0005PFJetSequence +
    akSoftDropChZCut0004PFJetSequence +
    akSoftDropChZCut0005PFJetSequence
)
