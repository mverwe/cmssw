import FWCore.ParameterSet.Config as cms

topGenAnalyzer = cms.EDAnalyzer('TopGenAnalyzer',
                                pseudoTop = cms.InputTag("pseudoTop")
)
