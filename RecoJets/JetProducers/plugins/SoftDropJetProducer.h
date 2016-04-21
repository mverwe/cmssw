#ifndef RecoJets_JetProducers_SoftDropJetProducer_h
#define RecoJets_JetProducers_SoftDropJetProducer_h

/* *********************************************************
  \class SoftDropJetProducer

  \brief Jet producer to produce SoftDrop jets

  \author   Marta Verweij
  \version  

         Notes on implementation:

         Allows to use soft drop only on charged particle flow candidates
         Stores additional information about soft dropped branches

 ************************************************************/


#include "RecoJets/JetProducers/plugins/VirtualJetProducer.h"

namespace cms
{
  class SoftDropJetProducer : public VirtualJetProducer
  {
  public:
    // typedefs
    //    typedef fastjet::ClusterSequencePtr         transformer;
    //typedef std::unique_ptr<transformer> transformer_ptr;
    typedef std::vector<ClusterSequencePtr> clusterSequence_coll;

    SoftDropJetProducer(const edm::ParameterSet& ps);

    virtual ~SoftDropJetProducer() {}

    virtual void produce( edm::Event & iEvent, const edm::EventSetup & iSetup );

  protected:
    void writeSoftDropJets(  edm::Event & iEvent, edm::EventSetup const& iSetup);
    
  protected:

    virtual void runAlgorithm( edm::Event& iEvent, const edm::EventSetup& iSetup );

    double zCut_;               /// for pruning OR soft drop: constituent minimum pt fraction of parent cluster
    double beta_;               /// for soft drop : beta (angular exponent)
    double R0_;                 /// for soft drop : R0 (angular distance normalization - should be set to jet radius in most cases)
    bool   useOnlyCharged_;     /// run soft drop only on charged constituents

    JetDefPtr                       fjJetDefinitionRecluster_; // fastjet jet definition for reclustering
    ClusterSequencePtr              fjClusterSeqRecluster_;    // fastjet cluster sequence for reclustering
  };
}
#endif
