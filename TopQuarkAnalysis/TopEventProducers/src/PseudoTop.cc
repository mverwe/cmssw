#include "TopQuarkAnalysis/TopEventProducers/interface/PseudoTop.hh"
//#include "Rivet/Config/RivetCommon.hh"
#include "Rivet/Tools/ParticleIdUtils.hh"

using namespace Rivet;

void PseudoTop::project(const Event& event) {
  // Leptons : do the lepton clustering anti-kt R=0.1 using stable photons and leptons not from hadron decay
  // Neutrinos : neutrinos not from hadron decay
  // MET : vector sum of all invisible particles in x-y plane 
  // Jets : anti-kt clustering using all particles excluding neutrinos and particles used in lepton clustering
  //        add ghost B hadrons during the jet clustering to identify B jets.

  // W->lv : dressed lepton and neutrino pairs
  // W->jj : light flavored dijet
  // W candidate : select lv or jj pairs which minimise |mW1-80.4|+|mW2-80.4|
  //               lepton-neutrino pair will be selected with higher priority

  // t->Wb : W candidate + b jet
  // t candidate : select Wb pairs which minimise |mtop1-172.5|+|mtop2-172.5|

  _isValid = false;
  _theParticles.clear();
  _wDecays1.clear();
  _wDecays2.clear();
  _jets.clear();
  _bjets.clear();
  _ljets.clear();
  _leptons.clear();
  _neutrinos.clear();
  _mode1 = _mode2 = CH_HADRON;
  
  // Get analysis objects from projections
  
  _leptons = applyProjection<DressedLeptons>(event, "DressedLeptons").dressedLeptons();

  Cut jet_cut = (Cuts::abseta < _jetMaxEta) and (Cuts::pT > _jetMinPt*GeV);
  _jets = applyProjection<FastJets>(event, "Jets").jetsByPt(jet_cut);
  for (const Jet& jet : _jets) {
    if (jet.bTagged()) _bjets.push_back(jet);
    else               _ljets.push_back(jet);
  }
  
  _neutrinos = applyProjection<PromptFinalState>(event, "PromptNeutrinos").particlesByPt();
  
  _met = -applyProjection<MissingMomentum>(event, "MET").vectorEt();

  // All building blocks are ready. Continue to pseudo-W and pseudo-top combination

  if (not _runTopReconstruction) return;
  
  if (_bjets.size() < 2) return; // Ignore single top for now

  if ( _leptons.size() == 2 and _neutrinos.size() >= 2 ) {
    // Start from dilepton channel
    const int q1 = _leptons.at(0).charge();
    const int q2 = _leptons.at(1).charge();
    if ( q1*q2 > 0 ) return;

    const auto& lepton1 = q1 > 0 ? _leptons.at(0) : _leptons.at(1);
    const auto& lepton2 = q1 > 0 ? _leptons.at(1) : _leptons.at(0);

    if ( lepton1.pt() < _minLeptonPtDilepton or std::abs(lepton1.eta()) > _maxLeptonEtaDilepton ) return;
    if ( lepton2.pt() < _minLeptonPtDilepton or std::abs(lepton2.eta()) > _maxLeptonEtaDilepton ) return;
    if ( (lepton1.momentum()+lepton2.momentum()).mass() < _minDileptonMassDilepton ) return;

    double dm = 1e9;
    int selNu1 = -1, selNu2 = -1;
    for ( int i=0; i<2; ++i ) { // Consider leading 2 neutrinos. Neutrino vector is already sorted by pT
      const double dm1 = std::abs((lepton1.momentum()+_neutrinos.at(i).momentum()).mass()-_wMass);
      for ( int j=0; j<2; ++j ) {
        if ( i == j ) continue;
        const double dm2 = std::abs((lepton2.momentum()+_neutrinos.at(j).momentum()).mass()-_wMass);
        const double newDm = dm1+dm2;

        if ( newDm < dm ) { dm = newDm; selNu1 = i; selNu2 = j; }
      }
    }
    if ( dm >= 1e9 ) return;

    const auto& nu1 = _neutrinos.at(selNu1);
    const auto& nu2 = _neutrinos.at(selNu2);
    const auto w1LVec = lepton1.momentum()+nu1.momentum();
    const auto w2LVec = lepton2.momentum()+nu2.momentum();

    // Contiue to top quarks
    dm = 1e9; // Reset once again for top combination.
    int selB1 = -1, selB2 = -1;
    for ( unsigned int i=0; i<_bjets.size(); ++i ) {
      const auto& bjet1 = _bjets.at(i);
      if ( deltaR(bjet1.momentum(), lepton1.momentum()) < 0.4 ) continue;
      if ( deltaR(bjet1.momentum(), lepton2.momentum()) < 0.4 ) continue;

      const double dm1 = std::abs((w1LVec+bjet1.momentum()).mass()-_tMass);
      for ( unsigned int j=0; j<_bjets.size(); ++j ) {
        if ( i == j ) continue;
        const auto& bjet2 = _bjets.at(j);
        if ( deltaR(bjet2.momentum(), lepton1.momentum()) < 0.4 ) continue;
        if ( deltaR(bjet2.momentum(), lepton2.momentum()) < 0.4 ) continue;
        const double dm2 = std::abs((w2LVec+bjet2.momentum()).mass()-_tMass);
        const double newDm = dm1+dm2;

        if ( newDm < dm ) { dm = newDm; selB1 = i; selB2 = j; }
      }
    }
    if ( dm >= 1e9 ) return;

    _b1 = Particle(q1*5, _bjets.at(selB1).momentum());
    _t1 = Particle(q1*6, w1LVec + _b1.momentum());
    _w1 = Particle(q1*24, w1LVec);

    _b2 = Particle(q2*5, _bjets.at(selB2).momentum());
    _t2 = Particle(q2*6, w2LVec + _b2.momentum());
    _w2 = Particle(q2*24, w2LVec);

    _wDecays1.push_back(lepton1);
    _wDecays1.push_back(_neutrinos.at(selNu1));
    _wDecays2.push_back(lepton2);
    _wDecays2.push_back(_neutrinos.at(selNu2));

    _mode1 = std::abs(lepton1.pdgId()) == 13 ? CH_MUON : CH_ELECTRON;
    _mode2 = std::abs(lepton2.pdgId()) == 13 ? CH_MUON : CH_ELECTRON;
  }
  else if ( _leptons.size() >= 1 and _neutrinos.size() >= 1 and _ljets.size() >= 2 ) {
    const auto& lepton = _leptons.at(0);
    if ( lepton.pt() < _minLeptonPtSemilepton or std::abs(lepton.eta()) > _maxLeptonEtaSemilepton ) return;

    // Skip event if there are veto leptons
    bool hasVetoLepton = false;
    for ( auto vetoLeptonItr = _leptons.begin()+1; vetoLeptonItr != _leptons.end(); ++vetoLeptonItr ) {
      if ( vetoLeptonItr->pt() > _minVetoLeptonPtSemilepton and
          std::abs(vetoLeptonItr->eta()) < _maxVetoLeptonEtaSemilepton ) {
        hasVetoLepton = true;
      }
    }
    if ( hasVetoLepton ) return;

    // MET and neutrino reconstruction
    double metX = _met.x(), metY = _met.y();
    const double metPt = _met.perp();
    if ( metPt < _minMETSemiLepton ) return;

    const double mtW = std::sqrt( 2*lepton.pt()*metPt*cos(lepton.phi()-atan2(metX, metY)) );
    if ( mtW < _minMtWSemiLepton ) return;

    // Solve pz to give wMass_^2 = (lepE+energy)^2 - (lepPx+metX)^2 - (lepPy+metY)^2 - (lepPz+pz)^2
    // -> (wMass_^2)/2 = lepE*sqrt(metPt^2+pz^2) - lepPx*metX - lepPy*metY - lepPz*pz
    // -> C := (wMass_^2)/2 + lepPx*metX + lepPy*metY
    // -> lepE^2*(metPt^2+pz^2) = C^2 + 2*C*lepPz*pz + lepPz^2*pz^2
    // -> (lepE^2-lepPz^2)*pz^2 - 2*C*lepPz*pz - C^2 + lepE^2*metPt^2 = 0
    // -> lepPt^2*pz^2 - 2*C*lepPz*pz - C^2 + lepE^2*metPt^2 = 0
    const double lpz = lepton.pz(), le = lepton.energy(), lpt = lepton.pt();
    const double cf = (_wMass*_wMass)/2 + lepton.px()*metX + lepton.py()*metY;
    const double det = cf*cf*lpz*lpz - lpt*lpt*(le*le*metPt*metPt - cf*cf);
    if ( det < 0 ) return;
    const double pz = (cf*lpz + (cf < 0 ? -sqrt(det) : sqrt(det)))/lpt/lpt;
    const FourMomentum nu1P4(std::hypot(metPt, pz), metX, metY, pz);
    const auto w1LVec = lepton.momentum()+nu1P4;

    // Continue to build leptonic pseudo top
    double minDR = 1e9;
    int selB1 = -1;
    for ( size_t i=0; i<_bjets.size(); ++i ) {
      const auto bjet = _bjets.at(i);
      if ( deltaR(bjet.momentum(), lepton.momentum()) < 0.4 ) continue;
      const double dR = deltaR(bjet.momentum(), w1LVec);
      if ( dR < minDR ) { selB1 = i; minDR = dR; }
    }
    if ( selB1 == -1 ) return;

    // Build hadronic pseudo W, take leading two jets (ljetIdxs are (implicitly) sorted by pT)
    int selJ1 = -1, selJ2 = -1;
    for ( size_t i=0; i<_ljets.size(); ++i ) {
      const auto ljet = _ljets.at(i);
      if ( deltaR(ljet.momentum(), lepton.momentum()) < 0.4 ) continue;
      if ( selJ1 < 0 ) selJ1 = i;
      else if ( selJ2 < 0 ) selJ2 = i;
      else break;
    }
    if ( selJ1 < 0 or selJ2 < 0 ) return;
    const auto& wJet1 = _ljets.at(selJ1);
    const auto& wJet2 = _ljets.at(selJ2);
    const auto w2LVec = wJet1.momentum() + wJet2.momentum();

    // Contiue to top quarks
    double dm = 1e9;
    int selB2 = -1;
    for ( size_t i=0; i<_bjets.size(); ++i ) {
      if ( int(i) == selB1 ) continue;
      const auto& bjet = _bjets.at(i);
      if ( deltaR(bjet.momentum(), lepton.momentum()) < 0.4 ) continue;
      const double newDm = std::abs((w2LVec+bjet.momentum()).mass()-_tMass);
      if ( newDm < dm ) { dm = newDm; selB2 = i; }
    }
    if ( dm >= 1e9 ) return;

    const int q = lepton.charge();

    _b1 = Particle(q*5, _bjets.at(selB1).momentum());
    _t1 = Particle(q*6, w1LVec + _b1.momentum());
    _w1 = Particle(q*24, w1LVec);

    _b2 = Particle(-q*5, _bjets.at(selB2).momentum());
    _t2 = Particle(-q*6, w2LVec + _b2.momentum());
    _w2 = Particle(-q*24, w2LVec);

    _wDecays1.push_back(lepton);
    _wDecays1.push_back(Particle(q*(std::abs(lepton.pdgId())+1), nu1P4));
    _wDecays2.push_back(Particle(-2*q, wJet1));
    _wDecays2.push_back(Particle(q, wJet2));

    _mode1 = std::abs(lepton.pdgId()) == 13 ? CH_MUON : CH_ELECTRON;
  }

  _isValid = true;
}

