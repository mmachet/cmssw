// -*- C++ -*-
//
// Package:    IsolatedEcalPixelTrackCandidateProducer
// Class:      IsolatedEcalPixelTrackCandidateProducer
// 
/**\class IsolatedEcalPixelTrackCandidateProducer IsolatedEcalPixelTrackCandidateProducer.cc Calibration/HcalIsolatedTrackReco/src/IsolatedEcalPixelTrackCandidateProducer.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Ruchi Gupta
//         Created:  Thu Feb 11 17:21:58 MSD 2014
// $Id: IsolatedEcalPixelTrackCandidateProducer.cc,v 1.0 2014/02/11 22:25:52 wmtan Exp $
//
//

//#define DebugLog
// system include files
#include <memory>

// user include files

#include "FWCore/Framework/interface/EventSetup.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "DataFormats/Common/interface/Ref.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"

#include "Calibration/HcalIsolatedTrackReco/interface/IsolatedEcalPixelTrackCandidateProducer.h"

IsolatedEcalPixelTrackCandidateProducer::IsolatedEcalPixelTrackCandidateProducer(const edm::ParameterSet& conf) {

  coneSizeEta0_    = conf.getParameter<double>("EcalConeSizeEta0");
  coneSizeEta1_    = conf.getParameter<double>("EcalConeSizeEta1");
  hitCountEthr_    = conf.getParameter<double>("ECHitCountEnergyThreshold");
  hitEthr_         = conf.getParameter<double>("ECHitEnergyThreshold");
  tok_trigcand = consumes<trigger::TriggerFilterObjectWithRefs>(conf.getParameter<edm::InputTag>("filterLabel"));
  tok_eb = consumes<EcalRecHitCollection>(conf.getParameter<edm::InputTag>("EBRecHitSource"));
  tok_ee = consumes<EcalRecHitCollection>(conf.getParameter<edm::InputTag>("EERecHitSource"));

   //register your products
  produces< reco::IsolatedPixelTrackCandidateCollection >();
}

IsolatedEcalPixelTrackCandidateProducer::~IsolatedEcalPixelTrackCandidateProducer() { }

// ------------ method called to produce the data  ------------
void IsolatedEcalPixelTrackCandidateProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {
#ifdef DebugLog
  std::cout << "==============Inside IsolatedEcalPixelTrackCandidateProducer" << std::endl;
#endif
  edm::ESHandle<CaloGeometry> pG;
  iSetup.get<CaloGeometryRecord>().get(pG);
  const CaloGeometry* geo = pG.product();

  edm::Handle<EcalRecHitCollection> ecalEB;
  iEvent.getByToken(tok_eb,ecalEB);

  edm::Handle<EcalRecHitCollection> ecalEE;
  iEvent.getByToken(tok_ee,ecalEE);
#ifdef DebugLog
  std::cout << "ecal Collections isValid: " << ecalEB.isValid() << "/" << ecalEE.isValid() << std::endl;
#endif

  edm::Handle<trigger::TriggerFilterObjectWithRefs> trigCand;
  iEvent.getByToken(tok_trigcand,trigCand);

  std::vector< edm::Ref<reco::IsolatedPixelTrackCandidateCollection> > isoPixTrackRefs;
  trigCand->getObjects(trigger::TriggerTrack, isoPixTrackRefs);
  int nCand=isoPixTrackRefs.size();  

  reco::IsolatedPixelTrackCandidateCollection * iptcCollection=new reco::IsolatedPixelTrackCandidateCollection;
#ifdef DebugLog
  std::cout << "coneSize_ " << coneSizeEta0_ << "/"<< coneSizeEta1_ << " hitCountEthr_ " << hitCountEthr_ << " hitEthr_ " << hitEthr_ << std::endl;
#endif
  for (int p=0; p<nCand; p++) {
    int    nhitIn(0), nhitOut(0);
    double inEnergy(0), outEnergy(0);
    std::pair<double,double> etaPhi(isoPixTrackRefs[p]->track()->eta(), isoPixTrackRefs[p]->track()->phi());
    if (isoPixTrackRefs[p]->etaPhiEcal()) etaPhi = isoPixTrackRefs[p]->EtaPhiEcal();
    double etaAbs = std::abs(etaPhi.first);
    double coneSize_ = (etaAbs > 1.5) ? coneSizeEta1_ : (coneSizeEta0_*(1.5-etaAbs)+coneSizeEta1_*etaAbs)/1.5;
#ifdef DebugLog
    std::cout << "Track: eta/phi " << etaPhi.first << "/" << etaPhi.second << " pt:" << isoPixTrackRefs[p]->track()->pt() << " cone " << coneSize_ << std::endl;
    std::cout << "rechit size EB/EE : " << ecalEB->size() << "/" << ecalEE->size() << " coneSize_: " <<  coneSize_ << std::endl;
#endif
    if (etaAbs<1.7) {
      for (EcalRecHitCollection::const_iterator eItr=ecalEB->begin(); eItr!=ecalEB->end(); eItr++) {
	GlobalPoint pos = geo->getPosition(eItr->detid());
	double      R   = reco::deltaR(pos.eta(),pos.phi(),etaPhi.first,etaPhi.second);
	if (R < coneSize_) {
	  nhitIn++;
	  inEnergy += (eItr->energy());
	  if (eItr->energy() > hitCountEthr_) nhitOut++;
	  if (eItr->energy() > hitEthr_)      outEnergy += (eItr->energy());
#ifdef DebugLog
	  std::cout << "Rechit Close to the track has energy " << eItr->energy()
		    << " eta/phi: " << pos.eta() << "/" << pos.phi() << " deltaR: " << R << std::endl;
#endif
	}
      }
    }
    if (etaAbs>1.25) {
      for (EcalRecHitCollection::const_iterator eItr=ecalEE->begin(); eItr!=ecalEE->end(); eItr++) {
	GlobalPoint pos = geo->getPosition(eItr->detid());
	double      R   = reco::deltaR(pos.eta(),pos.phi(),etaPhi.first,etaPhi.second);
	if (R < coneSize_) {
	  nhitIn++;
	  inEnergy += (eItr->energy());
	  if (eItr->energy() > hitCountEthr_) nhitOut++;
	  if (eItr->energy() > hitEthr_)      outEnergy += (eItr->energy());
#ifdef DebugLog
	  std::cout << "Rechit Close to the track has energy " << eItr->energy()
		    << " eta/phi: " << pos.eta() << "/" << pos.phi() << " deltaR: " << R << std::endl;
#endif
	}
      }
    }
#ifdef DebugLog
    std::cout << "nhitIn:" << nhitIn << " inEnergy:" << inEnergy << " nhitOut:" << nhitOut << " outEnergy:" << outEnergy << std::endl;
#endif
    reco::IsolatedPixelTrackCandidate newca(*isoPixTrackRefs[p]);
    newca.SetEnergyIn(inEnergy);
    newca.SetEnergyOut(outEnergy);
    newca.SetNHitIn(nhitIn);
    newca.SetNHitOut(nhitOut);
    iptcCollection->push_back(newca);	
  }
#ifdef DebugLog
  std::cout << "ncand:" << nCand << " outcollction size:" << iptcCollection->size() << std::endl;
#endif
  std::auto_ptr<reco::IsolatedPixelTrackCandidateCollection> outCollection(iptcCollection);
  iEvent.put(outCollection);
}
// ------------ method called once each job just before starting event loop  ------------
void IsolatedEcalPixelTrackCandidateProducer::beginJob() { }

// ------------ method called once each job just after ending the event loop  ------------
void IsolatedEcalPixelTrackCandidateProducer::endJob() { }
