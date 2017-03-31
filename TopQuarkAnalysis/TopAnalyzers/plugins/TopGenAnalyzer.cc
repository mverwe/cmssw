// -*- C++ -*-
//
// Package:    TopQuarkAnalysis/TopAnalyzers
// Class:      TopGenAnalyzer
// 
/**\class TopAnalyzers TopGenAnalyzer.cc TopQuarkAnalysis/TopAnalyzers/plugins/TopGenAnalyzer.cc

   Description: extract gen level info about top event

   Implementation:
   Uses PseudoTop as input
*/
//
// Original Author:  Marta Verweij
//         Created:  Thu, 30 Mar 2017 14:48:19 GMT
//
//


// system include files
#include <memory>
#include <sstream>
#include <string>
#include <vector>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "DataFormats/JetReco/interface/GenJetCollection.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
//#include "DataFormats/PatCandidates/interface/Jet.h"

#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

// root include files
#include "TLorentzVector.h"
#include "TTree.h"

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class TopGenAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
public:
  explicit TopGenAnalyzer(const edm::ParameterSet&);
  ~TopGenAnalyzer();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


private:
  virtual void beginJob() override;
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;

  // ----------member data ---------------------------
  edm::EDGetTokenT<reco::GenParticleCollection> pseudoTopToken_;

  //output
  TTree *tree_;
  edm::Service<TFileService> fs_;

  struct GENTOP {
    std::vector<int> gtop_id;
    std::vector<double> gtop_pt;
    std::vector<double> gtop_eta;
    std::vector<double> gtop_phi;
    std::vector<double> gtop_mass;
    std::vector<std::vector<int>> gtop_daughterArr;
  };

  GENTOP topObj_;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
TopGenAnalyzer::TopGenAnalyzer(const edm::ParameterSet& iConfig) :
  //pseudoTopToken_(consumes<reco::GenParticleCollection>(edm::InputTag("pseudoTop")))
  pseudoTopToken_(consumes<reco::GenParticleCollection>(iConfig.getParameter<edm::InputTag>("pseudoTop")))

{
  //now do what ever initialization is needed
  usesResource("TFileService");

}


TopGenAnalyzer::~TopGenAnalyzer()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
TopGenAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

  //clear vectors in tree
  topObj_.gtop_id.clear();
  topObj_.gtop_pt.clear();
  topObj_.gtop_eta.clear();
  topObj_.gtop_phi.clear();
  topObj_.gtop_mass.clear();
  topObj_.gtop_daughterArr.clear();

  //pseudo-tops 
  edm::Handle<reco::GenParticleCollection> pseudoTop;
  iEvent.getByToken(pseudoTopToken_,pseudoTop);

  std::cout << "analyze gen level top " << pseudoTop->size() << std::endl;
  
  for (size_t i = 0; i < pseudoTop->size(); ++i) {
    const reco::GenParticle & genIt = (*pseudoTop)[i];
    topObj_.gtop_id.push_back(genIt.pdgId()*1000);
    topObj_.gtop_pt.push_back(genIt.pt());
    topObj_.gtop_eta.push_back(genIt.eta());
    topObj_.gtop_phi.push_back(genIt.phi());
    topObj_.gtop_mass.push_back(genIt.mass());

    std::cout << "pdf: " << genIt.pdgId() << "  nDaughters: " << genIt.numberOfDaughters() << "  collisionsId: " << genIt.collisionId() << std::endl;

    std::vector<int> daughterArr;
    for(unsigned int idx=0; idx<genIt.numberOfDaughters(); idx++) {
      double ptd = genIt.daughter(idx)->pt();
      double phid = genIt.daughter(idx)->phi();
      double etad = genIt.daughter(idx)->eta();

      for (size_t j = 0; j < pseudoTop->size(); ++j) {
        const reco::GenParticle & genJt = (*pseudoTop)[j];
        if(fabs(ptd-genJt.pt())<0.001
           && fabs(etad-genJt.eta())<0.001
           && fabs(phid-genJt.phi())<0.001
           )
          daughterArr.push_back(j);
      }
    }
    topObj_.gtop_daughterArr.push_back(daughterArr);
  }

  tree_->Fill();

}


// ------------ method called once each job just before starting event loop  ------------
void 
TopGenAnalyzer::beginJob()
{
  TString topTagTitle = "PseudoTop Gen analysis tree";
  tree_ = fs_->make<TTree>("t",topTagTitle.Data());
  tree_->Branch("gtop_id",&(topObj_.gtop_id));
  tree_->Branch("gtop_pt",&(topObj_.gtop_pt));
  tree_->Branch("gtop_eta",&(topObj_.gtop_eta));
  tree_->Branch("gtop_phi",&(topObj_.gtop_phi));
  tree_->Branch("gtop_mass",&(topObj_.gtop_mass));
  tree_->Branch("gtop_daughterArr",&(topObj_.gtop_daughterArr));
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TopGenAnalyzer::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TopGenAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TopGenAnalyzer);
