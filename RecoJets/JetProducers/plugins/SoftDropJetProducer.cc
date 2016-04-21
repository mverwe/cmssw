#include "FWCore/Framework/interface/MakerMacros.h"
#include "RecoJets/JetProducers/plugins/SoftDropJetProducer.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "RecoJets/JetProducers/interface/JetSpecific.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"

#include "fastjet/contrib/SoftDrop.hh"

#include <iostream>
#include <memory>
#include <algorithm>
#include <limits>
#include <cmath>

using namespace std;
using namespace reco;
using namespace edm;
using namespace cms;

SoftDropJetProducer::SoftDropJetProducer(edm::ParameterSet const& iConfig):
  VirtualJetProducer( iConfig ),
  zCut_(-1.0),
  beta_(-1.0),
  R0_(-1.0),
  useOnlyCharged_(false)
{
  //get soft drop settings
  zCut_ = iConfig.getParameter<double>("zcut");
  beta_ = iConfig.getParameter<double>("beta");
  R0_ = iConfig.getParameter<double>("R0");
  useOnlyCharged_ = iConfig.getParameter<bool>("useOnlyCharged");
}

void SoftDropJetProducer::produce( edm::Event & iEvent, const edm::EventSetup & iSetup )
{
  // use the default production from one collection
  VirtualJetProducer::produce( iEvent, iSetup );
  //use runAlgorithm of this class


  // fjClusterSeq_ retains quite a lot of memory - about 1 to 7Mb at 200 pileup
  // depending on the exact configuration; and there are 24 FastjetJetProducers in the
  // sequence so this adds up to about 60 Mb. It's allocated every time runAlgorithm
  // is called, so safe to delete here.
  fjClusterSeq_.reset();
  fjClusterSeqRecluster_.reset();
}

//______________________________________________________________________________
void SoftDropJetProducer::runAlgorithm( edm::Event & iEvent, edm::EventSetup const& iSetup)
{
  std::cout << "SoftDropProducer::runAlgorithm begin" << std::endl;

  if ( !doAreaFastjet_ && !doRhoFastjet_) {
    fjClusterSeq_ = ClusterSequencePtr( new fastjet::ClusterSequence( fjInputs_, *fjJetDefinition_ ) );
  } else if (voronoiRfact_ <= 0) {
    fjClusterSeq_ = ClusterSequencePtr( new fastjet::ClusterSequenceArea( fjInputs_, *fjJetDefinition_ , *fjAreaDefinition_ ) );
  } else {
    fjClusterSeq_ = ClusterSequencePtr( new fastjet::ClusterSequenceVoronoiArea( fjInputs_, *fjJetDefinition_ , fastjet::VoronoiAreaSpec(voronoiRfact_) ) );
  }
  
  std::vector<fastjet::PseudoJet> origJets = fastjet::sorted_by_pt(fjClusterSeq_->inclusive_jets(jetPtMin_));
  fastjet::contrib::SoftDrop * sdr = new fastjet::contrib::SoftDrop(beta_, zCut_, R0_ );
  sdr->set_verbose_structure(true);
  
  for ( std::vector<fastjet::PseudoJet>::const_iterator ijet = origJets.begin(),
          ijetEnd = origJets.end(); ijet != ijetEnd; ++ijet ) {
    fastjet::PseudoJet transformedJet = *ijet;
    if ( transformedJet == 0 ) continue;
    transformedJet = (*sdr)(transformedJet);
    //fjJets_.push_back( transformedJet );

    double sym = transformedJet.structure_of<fastjet::contrib::SoftDrop>().symmetry();
    std::cout << "sym: " << sym << std::endl;
    int ndrop = transformedJet.structure_of<fastjet::contrib::SoftDrop>().dropped_count();
    std::cout << "#dropped branches: " << ndrop << std::endl;
    std::vector<double> dropped_symmetry = transformedJet.structure_of<fastjet::contrib::SoftDrop>().dropped_symmetry();
    std::cout << "dropped_symmetry.size() " << dropped_symmetry.size() << std::endl;
    for ( std::vector<double>::const_iterator dsym = dropped_symmetry.begin();
            dsym != dropped_symmetry.end(); ++dsym )
      std::cout << "dropped symmetry: " << (*dsym) << std::endl;
  }

  std::cout << "recluster manual" << std::endl;

  //select requested particle types and recluster with CA infinite radius
  //fjJetDefinitionRecluster_ = JetDefPtr(new fastjet::JetDefinition(fastjet::antikt_algorithm,rParam_));
  
  fjJets_.clear();
  
  static const reco::PFCandidate dummySinceTranslateIsNotStatic;
  clusterSequence_coll clusterSequences;
  for ( std::vector<fastjet::PseudoJet>::const_iterator ijet = origJets.begin(),
          ijetEnd = origJets.end(); ijet != ijetEnd; ++ijet ) {
    fjClusterSeqRecluster_.reset();
    std::vector<fastjet::PseudoJet> inputsRecluster;
    //    inputsRecluster.clear();
    std::vector<fastjet::PseudoJet> particles, ghosts;
    fastjet::SelectorIsPureGhost().sift(ijet->constituents(), ghosts, particles);
    for ( std::vector<fastjet::PseudoJet>::const_iterator ipart = particles.begin();
          ipart != particles.end(); ++ipart ) {
      auto orig = inputs_[(*ipart).user_index()];
      auto id = dummySinceTranslateIsNotStatic.translatePdgIdToType(orig->pdgId());
      bool passed  = false;
      if(useOnlyCharged_) {
        if(id==1) passed = true;
      } else
        passed = true;
      
      if(passed) inputsRecluster.push_back(*ipart);
    }

    //recluster with selected particles
    //fjJetDefinitionRecluster_ = JetDefPtr(new fastjet::JetDefinition(fastjet::antikt_algorithm,rParam_));
    fjJetDefinitionRecluster_ = JetDefPtr(new fastjet::JetDefinition(fastjet::cambridge_algorithm,999.));
    //fjJetDefinitionRecluster_ = JetDefPtr(new fastjet::JetDefinition(fastjet::cambridge_algorithm,fastjet::JetDefinition::max_allowable_R));
    if ( !doAreaFastjet_ && !doRhoFastjet_) {
      fjClusterSeqRecluster_ = ClusterSequencePtr( new fastjet::ClusterSequence( inputsRecluster, *fjJetDefinitionRecluster_ ) );
    } else if (voronoiRfact_ <= 0) {
      fjClusterSeqRecluster_ = ClusterSequencePtr( new fastjet::ClusterSequenceArea( inputsRecluster, *fjJetDefinitionRecluster_ , *fjAreaDefinition_ ) );
    } else {
      fjClusterSeqRecluster_ = ClusterSequencePtr( new fastjet::ClusterSequenceVoronoiArea( inputsRecluster, *fjJetDefinitionRecluster_ , fastjet::VoronoiAreaSpec(voronoiRfact_) ) );
    }
    clusterSequences.push_back(fjClusterSeqRecluster_);

    std::vector<fastjet::PseudoJet> tempJets = fastjet::sorted_by_pt(fjClusterSeqRecluster_->inclusive_jets(jetPtMin_));
    if(tempJets.size()<1) continue;
    std::cout << "got reclusted CA jet" << std::endl;
    
    fastjet::contrib::SoftDrop * sd = new fastjet::contrib::SoftDrop(beta_, zCut_, R0_ );
    sd->set_verbose_structure(true);

    fastjet::PseudoJet transformedJet = tempJets[0];
    if ( transformedJet == 0 ) {
      //fjClusterSeqRecluster_->delete_self_when_unused();
      if(sd) { delete sd; sd = 0;}
      continue;
    }
    if(!transformedJet.has_valid_cluster_sequence()) {
      std::cout << "transformedJet does not have a valid cluster sequence" << std::endl;
    }

    transformedJet = (*sd)(transformedJet);
    fjJets_.push_back( transformedJet ); //put CA reclusterd jet after softDrop into vector which will be written to event

    double sym = transformedJet.structure_of<fastjet::contrib::SoftDrop>().symmetry();
    std::cout << "sym: " << sym << std::endl;
    int ndrop = transformedJet.structure_of<fastjet::contrib::SoftDrop>().dropped_count();
    std::cout << "#dropped branches: " << ndrop << std::endl;
    std::vector<double> dropped_symmetry = transformedJet.structure_of<fastjet::contrib::SoftDrop>().dropped_symmetry();
    std::cout << "dropped_symmetry.size() " << dropped_symmetry.size() << std::endl;
    for ( std::vector<double>::const_iterator dsym = dropped_symmetry.begin();
          dsym != dropped_symmetry.end(); ++dsym )
      std::cout << "dropped symmetry: " << (*dsym) << std::endl;

    if(sd) { delete sd; sd = 0;}
    //    fjClusterSeqRecluster_->delete_self_when_unused();
    
  }//anti-kt original jet loop
  
  //fjJets_ = fastjet::sorted_by_pt(fjClusterSeq_->inclusive_jets(jetPtMin_));
  
  // fastjet::RecursiveSymmetryCutBase rc(fastjet::SymmetryMeasure::scalar_z,  // the default SymmetryMeasure
  //                                      std::numeric_limits<double>::infinity(), // default is no mass drop
  //                                      fastjet::RecursionChoice::larger_pt, // the default RecursionChoice
  //                                      subtractor);
  // rc.set_grooming_mode();

  //  PseudoJet piece1, piece2;
  //  while (subjet.has_parents(piece1, piece2)) {
  //  double sym;
  //  double pt1 = piece1.pt();
  //  double pt2 = piece2.pt();
  //  make sure denominator is non-zero
  //  sym = pt1 + pt2;
  //  if (sym == 0) return PseudoJet(); 
  //  sym = std::min(pt1, pt2) / sym;
  // }

  std::cout << "SoftDropProducer::runAlgorithm end" << std::endl;
  
}

void SoftDropJetProducer::writeSoftDropJets(  edm::Event & iEvent, edm::EventSetup const& iSetup)
{
  VirtualJetProducer::writeJetsWithConstituents(iEvent,iSetup);
}


////////////////////////////////////////////////////////////////////////////////
// define as cmssw plugin
////////////////////////////////////////////////////////////////////////////////

DEFINE_FWK_MODULE(SoftDropJetProducer);
