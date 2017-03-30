#ifndef TopQuarkAnalysis_TopEventProducers_RivetWrapper_H
#define TopQuarkAnalysis_TopEventProducers_RivetWrapper_H

#include "Rivet/Analysis.hh"

#include "TopQuarkAnalysis/TopEventProducers/interface/PseudoTop.hh"

namespace Rivet {

  class RivetWrapper : public Analysis {
    public:
      RivetWrapper() : Analysis("RivetWrapper") {
      }

      // addProjection() is protected, so we need to register the PseudoTop projection here
      void init(const edm::ParameterSet& pset) {
        _allowProjReg = true;
        addProjection(PseudoTop(pset), "PseudoTop");
      };

      // Do nothing here
      void analyze(const Event& event) {};

      // Do nothing here
      void finalize() {};

  };

}

#endif
