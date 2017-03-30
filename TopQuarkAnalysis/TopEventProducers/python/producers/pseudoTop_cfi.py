import FWCore.ParameterSet.Config as cms

pseudoTop = cms.EDProducer("PseudoTopProducer",
    src = cms.InputTag("genParticles2HepMC:unsmeared"),
    
    projection = cms.string("PseudoTop"),
    
    maxEta = cms.double(5.), # HF range. Maximum 6.0 on MiniAOD
    
    leptonConeSize = cms.double(0.1),
    minLeptonPt = cms.double(15.),
    maxLeptonEta = cms.double(2.5),
    
    jetConeSize = cms.double(0.4),
    minJetPt = cms.double(30.),
    maxJetEta = cms.double(2.4),
    
    fatJetConeSize = cms.double(0.8),
    minFatJetPt = cms.double(400.),
    maxFatJetEta = cms.double(2.4),
    
    wMass = cms.double(80.4),
    tMass = cms.double(172.5),

    minLeptonPtDilepton = cms.double(20),
    maxLeptonEtaDilepton = cms.double(2.4),
    minDileptonMassDilepton = cms.double(20),
    minLeptonPtSemilepton = cms.double(20),
    maxLeptonEtaSemilepton = cms.double(2.4),
    minVetoLeptonPtSemilepton = cms.double(15),
    maxVetoLeptonEtaSemilepton = cms.double(2.5),
    minMETSemiLepton = cms.double(30),
    minMtWSemiLepton = cms.double(30),
    
    runTopReconstruction = cms.bool(True),
)
