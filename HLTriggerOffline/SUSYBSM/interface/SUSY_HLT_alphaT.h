#ifndef SUSY_HLT_alphaT_H
#define SUSY_HLT_alphaT_H

//event
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"

//DQM
#include "DQMServices/Core/interface/DQMEDAnalyzer.h"
#include "DQMServices/Core/interface/DQMStore.h"
#include "DQMServices/Core/interface/MonitorElement.h"

//Muon
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"


// MET
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETCollection.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/CaloMETCollection.h"

// Jets
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/JetReco/interface/CaloJet.h"

// Trigger
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/HLTReco/interface/TriggerEventWithRefs.h"
#include "DataFormats/HLTReco/interface/TriggerEventWithRefs.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"

#include "HLTrigger/JetMET/interface/AlphaT.h"

class SUSY_HLT_alphaT: public DQMEDAnalyzer{

  public:
  SUSY_HLT_alphaT(const edm::ParameterSet& ps);
  virtual ~SUSY_HLT_alphaT();

  protected:
  void dqmBeginRun(edm::Run const &, edm::EventSetup const &) override;
  void bookHistograms(DQMStore::IBooker &, edm::Run const &, edm::EventSetup const &) override;
  void analyze(edm::Event const& e, edm::EventSetup const& eSetup);
  void beginLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& eSetup) ;
  void endLuminosityBlock(edm::LuminosityBlock const& lumi, edm::EventSetup const& eSetup);
  void endRun(edm::Run const& run, edm::EventSetup const& eSetup);

  private:
  //histos booking function
  void bookHistos(DQMStore::IBooker &);
  
  //variables from config file
  //edm::EDGetTokenT<reco::PFMETCollection> thePfMETCollection_;
  edm::EDGetTokenT<reco::CaloMETCollection> theCaloMETCollection_;
  //edm::EDGetTokenT<reco::PFJetCollection> thePfJetCollection_;
  edm::EDGetTokenT<reco::CaloJetCollection> theCaloJetCollection_;
  edm::EDGetTokenT<edm::TriggerResults> triggerResults_;
  edm::EDGetTokenT<trigger::TriggerEvent> theTrigSummary_;


  HLTConfigProvider fHltConfig;

  std::string HLTProcess_;
  std::string triggerPath_;
  std::string triggerPathAuxiliaryForMuon_;
  std::string triggerPathAuxiliaryForHadronic_;
  edm::InputTag triggerFilter_;
  double ptThrJet_;
  double etaThrJet_;
  double alphaTThrTurnon_;
  double htThrTurnon_;
  
  // Histograms
  MonitorElement* h_triggerHt;
  //MonitorElement* h_triggerMht;
  MonitorElement* h_triggerAlphaT;
  MonitorElement* h_triggerAlphaT_triggerHt;
  MonitorElement* h_alphaTTurnOn_num;
  MonitorElement* h_alphaTTurnOn_den;
  MonitorElement* h_htTurnOn_num;
  MonitorElement* h_htTurnOn_den;

};

#endif
