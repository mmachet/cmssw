# /dev/CMSSW_3_1_0/pre11/HIon_V10/V2 (CMSSW_3_1_0)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "HLT2" )

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/dev/CMSSW_3_1_0/pre11/HIon_V10/V2')
)

process.maxEvents = cms.untracked.PSet(  input = cms.untracked.int32( 20 ) )
process.options = cms.untracked.PSet(  wantSummary = cms.untracked.bool( True ) )

process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring( 
#    '/store/relval/CMSSW_3_1_1/RelValZMM/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP31X_V1-v2/0002/408C5A4A-C56B-DE11-9587-000423D991F0.root'
#    '/store/relval/CMSSW_3_1_2/RelValHQ_MinBias_4TeV/GEN-SIM-RAW/MC_31X_V3-v3/0008/F8429DD8-2580-DE11-ACF4-000423D99B3E.root',
#    '/store/relval/CMSSW_3_1_2/RelValHQ_MinBias_4TeV/GEN-SIM-RAW/MC_31X_V3-v3/0008/F62AC2D0-2780-DE11-A019-000423D6CA02.root',
#    '/store/relval/CMSSW_3_1_2/RelValHQ_MinBias_4TeV/GEN-SIM-RAW/MC_31X_V3-v3/0008/E201CBFF-5480-DE11-88EC-000423D33970.root',
#    '/store/relval/CMSSW_3_1_2/RelValHQ_MinBias_4TeV/GEN-SIM-RAW/MC_31X_V3-v3/0008/D4173843-5680-DE11-930A-0019B9F70468.root',
#    '/store/relval/CMSSW_3_1_2/RelValHQ_MinBias_4TeV/GEN-SIM-RAW/MC_31X_V3-v3/0008/7E5B4174-3D80-DE11-9963-000423D33970.root',
#    '/store/relval/CMSSW_3_1_2/RelValHQ_MinBias_4TeV/GEN-SIM-RAW/MC_31X_V3-v3/0008/40E80FDB-2280-DE11-B732-000423D98750.root',
##    '/store/relval/CMSSW_3_1_2/RelValHQ_MinBias_4TeV/GEN-SIM-RAW/MC_31X_V3-v3/0008/3A4E3278-3080-DE11-B86F-000423D6CA02.root',
#    '/store/relval/CMSSW_3_1_2/RelValHQ_MinBias_4TeV/GEN-SIM-RAW/MC_31X_V3-v3/0008/226D07AF-2C80-DE11-B093-000423D94E70.root',
#    '/store/relval/CMSSW_3_1_2/RelValHQ_MinBias_4TeV/GEN-SIM-RAW/MC_31X_V3-v3/0008/0409B9E2-3280-DE11-AA72-001D09F2546F.root' 
      '/store/relval/CMSSW_3_1_2/RelValZMM/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP31X_V2-v1/0007/069E08CD-CD78-DE11-9EB7-001D09F25109.root'    
    )
)

process.l1GtTriggerMenuXml = cms.ESProducer( "L1GtTriggerMenuXmlProducer",
  TriggerMenuLuminosity = cms.string( "startup" ),
  DefXmlFile = cms.string( "L1Menu_Commissioning2009_v0_L1T_Scales_20080926_startup_Imp0.xml" ),
#  DefXmlFile = cms.string( "L1Menu_startup2_v2.xml" ),
  VmeXmlFile = cms.string( "" ),
  appendToDataLabel = cms.string( "" )
)

process.essourceSev = cms.ESSource( "EmptyESSource",
    recordName = cms.string( "HcalSeverityLevelComputerRcd" ),
    iovIsRunNotTime = cms.bool( True ),
    appendToDataLabel = cms.string( "" ),
    firstValid = cms.vuint32( 1 )
)
process.BTagRecord = cms.ESSource( "EmptyESSource",
    recordName = cms.string( "JetTagComputerRecord" ),
    iovIsRunNotTime = cms.bool( True ),
    appendToDataLabel = cms.string( "" ),
    firstValid = cms.vuint32( 1 )
)
process.GlobalTag = cms.ESSource( "PoolDBESSource",
    BlobStreamerName = cms.untracked.string( "TBufferBlobStreamingService" ),
    connect = cms.string( "frontier://FrontierProd/CMS_COND_31X_GLOBALTAG" ),
    globaltag = cms.string( "MC_31X_V1::All" ),
    appendToDataLabel = cms.string( "" ),
    DBParameters = cms.PSet( 
      authenticationPath = cms.untracked.string( "." ),
      messageLevel = cms.untracked.int32( 0 ),
      connectionTimeOut = cms.untracked.int32( 0 ),
      connectionRetrialPeriod = cms.untracked.int32( 10 ),
      connectionRetrialTimeOut = cms.untracked.int32( 60 ),
      enableConnectionSharing = cms.untracked.bool( True ),
      enableReadOnlySessionOnUpdateConnection = cms.untracked.bool( False ),
      enablePoolAutomaticCleanUp = cms.untracked.bool( False ),
      idleConnectionCleanupPeriod = cms.untracked.int32( 10 )
    ),
    toGet = cms.VPSet( 
    ),
    timetype = cms.string( "runnumber" )
)
process.HepPDTESSource = cms.ESSource( "HepPDTESSource",
    pdtFileName = cms.FileInPath( "SimGeneral/HepPDTESSource/data/pythiaparticle.tbl" ),
    appendToDataLabel = cms.string( "" )
)
process.L2RelativeCorrectionService = cms.ESSource( "L2RelativeCorrectionService",
    appendToDataLabel = cms.string( "" ),
    tagName = cms.string( "Summer08_L2Relative_IC5Calo" ),
    label = cms.string( "L2RelativeJetCorrector" )
)
process.MCJetCorrectorIcone5HF07 = cms.ESSource( "L2RelativeCorrectionService",
    appendToDataLabel = cms.string( "" ),
    tagName = cms.string( "HLT_L2Relative" ),
    label = cms.string( "MCJetCorrectorIcone5HF07" )
)
process.MCJetCorrectorIcone5Unit = cms.ESSource( "L2RelativeCorrectionService",
    appendToDataLabel = cms.string( "" ),
    tagName = cms.string( "HLT_L2RelativeFlat" ),
    label = cms.string( "MCJetCorrectorIcone5Unit" )
)
process.L3AbsoluteCorrectionService = cms.ESSource( "L3AbsoluteCorrectionService",
    appendToDataLabel = cms.string( "" ),
    tagName = cms.string( "Summer08_L3Absolute_IC5Calo" ),
    label = cms.string( "L3AbsoluteJetCorrector" )
)
process.MCJetCorrectorIcone5 = cms.ESSource( "JetCorrectionServiceChain",
    label = cms.string( "MCJetCorrectorIcone5" ),
    appendToDataLabel = cms.string( "" ),
    correctors = cms.vstring( 'L2RelativeJetCorrector',
      'L3AbsoluteJetCorrector' )
)
process.SiStripQualityFakeESSource = cms.ESSource( "SiStripQualityFakeESSource" )
process.XMLIdealGeometryESSource = cms.ESSource( "XMLIdealGeometryESSource",
    rootNodeName = cms.string( "cms:OCMS" ),
    appendToDataLabel = cms.string( "" ),
    geomXMLFiles = ( cms.vstring( 'Geometry/CMSCommonData/data/materials.xml',
      'Geometry/CMSCommonData/data/rotations.xml',
      'Geometry/CMSCommonData/data/extend/cmsextent.xml',
      'Geometry/CMSCommonData/data/cms.xml',
      'Geometry/CMSCommonData/data/cmsMother.xml',
      'Geometry/CMSCommonData/data/cmsTracker.xml',
      'Geometry/CMSCommonData/data/caloBase.xml',
      'Geometry/CMSCommonData/data/cmsCalo.xml',
      'Geometry/CMSCommonData/data/muonBase.xml',
      'Geometry/CMSCommonData/data/cmsMuon.xml',
      'Geometry/CMSCommonData/data/mgnt.xml',
      'Geometry/CMSCommonData/data/beampipe.xml',
      'Geometry/CMSCommonData/data/cmsBeam.xml',
      'Geometry/CMSCommonData/data/muonMB.xml',
      'Geometry/CMSCommonData/data/muonMagnet.xml',
      'Geometry/CMSCommonData/data/cavern.xml',
      'Geometry/TrackerCommonData/data/pixfwdMaterials.xml',
      'Geometry/TrackerCommonData/data/pixfwdCommon.xml',
      'Geometry/TrackerCommonData/data/pixfwdPlaq.xml',
      'Geometry/TrackerCommonData/data/pixfwdPlaq1x2.xml',
      'Geometry/TrackerCommonData/data/pixfwdPlaq1x5.xml',
      'Geometry/TrackerCommonData/data/pixfwdPlaq2x3.xml',
      'Geometry/TrackerCommonData/data/pixfwdPlaq2x4.xml',
      'Geometry/TrackerCommonData/data/pixfwdPlaq2x5.xml',
      'Geometry/TrackerCommonData/data/pixfwdPanelBase.xml',
      'Geometry/TrackerCommonData/data/pixfwdPanel.xml',
      'Geometry/TrackerCommonData/data/pixfwdBlade.xml',
      'Geometry/TrackerCommonData/data/pixfwdNipple.xml',
      'Geometry/TrackerCommonData/data/pixfwdDisk.xml',
      'Geometry/TrackerCommonData/data/pixfwdCylinder.xml',
      'Geometry/TrackerCommonData/data/pixfwd.xml',
      'Geometry/TrackerCommonData/data/pixbarmaterial.xml',
      'Geometry/TrackerCommonData/data/pixbarladder.xml',
      'Geometry/TrackerCommonData/data/pixbarladderfull.xml',
      'Geometry/TrackerCommonData/data/pixbarladderhalf.xml',
      'Geometry/TrackerCommonData/data/pixbarlayer.xml',
      'Geometry/TrackerCommonData/data/pixbarlayer0.xml',
      'Geometry/TrackerCommonData/data/pixbarlayer1.xml',
      'Geometry/TrackerCommonData/data/pixbarlayer2.xml',
      'Geometry/TrackerCommonData/data/pixbar.xml',
      'Geometry/TrackerCommonData/data/tibtidcommonmaterial.xml',
      'Geometry/TrackerCommonData/data/tibmaterial.xml',
      'Geometry/TrackerCommonData/data/tibmodpar.xml',
      'Geometry/TrackerCommonData/data/tibmodule0.xml',
      'Geometry/TrackerCommonData/data/tibmodule0a.xml',
      'Geometry/TrackerCommonData/data/tibmodule0b.xml',
      'Geometry/TrackerCommonData/data/tibmodule2.xml',
      'Geometry/TrackerCommonData/data/tibstringpar.xml',
      'Geometry/TrackerCommonData/data/tibstring0ll.xml',
      'Geometry/TrackerCommonData/data/tibstring0lr.xml',
      'Geometry/TrackerCommonData/data/tibstring0ul.xml',
      'Geometry/TrackerCommonData/data/tibstring0ur.xml',
      'Geometry/TrackerCommonData/data/tibstring0.xml',
      'Geometry/TrackerCommonData/data/tibstring1ll.xml',
      'Geometry/TrackerCommonData/data/tibstring1lr.xml',
      'Geometry/TrackerCommonData/data/tibstring1ul.xml',
      'Geometry/TrackerCommonData/data/tibstring1ur.xml',
      'Geometry/TrackerCommonData/data/tibstring1.xml',
      'Geometry/TrackerCommonData/data/tibstring2ll.xml',
      'Geometry/TrackerCommonData/data/tibstring2lr.xml',
      'Geometry/TrackerCommonData/data/tibstring2ul.xml',
      'Geometry/TrackerCommonData/data/tibstring2ur.xml',
      'Geometry/TrackerCommonData/data/tibstring2.xml',
      'Geometry/TrackerCommonData/data/tibstring3ll.xml',
      'Geometry/TrackerCommonData/data/tibstring3lr.xml',
      'Geometry/TrackerCommonData/data/tibstring3ul.xml',
      'Geometry/TrackerCommonData/data/tibstring3ur.xml',
      'Geometry/TrackerCommonData/data/tibstring3.xml',
      'Geometry/TrackerCommonData/data/tiblayerpar.xml',
      'Geometry/TrackerCommonData/data/tiblayer0.xml',
      'Geometry/TrackerCommonData/data/tiblayer1.xml',
      'Geometry/TrackerCommonData/data/tiblayer2.xml',
      'Geometry/TrackerCommonData/data/tiblayer3.xml',
      'Geometry/TrackerCommonData/data/tib.xml',
      'Geometry/TrackerCommonData/data/tidmaterial.xml',
      'Geometry/TrackerCommonData/data/tidmodpar.xml',
      'Geometry/TrackerCommonData/data/tidmodule0.xml',
      'Geometry/TrackerCommonData/data/tidmodule0r.xml',
      'Geometry/TrackerCommonData/data/tidmodule0l.xml',
      'Geometry/TrackerCommonData/data/tidmodule1.xml',
      'Geometry/TrackerCommonData/data/tidmodule1r.xml',
      'Geometry/TrackerCommonData/data/tidmodule1l.xml',
      'Geometry/TrackerCommonData/data/tidmodule2.xml',
      'Geometry/TrackerCommonData/data/tidringpar.xml',
      'Geometry/TrackerCommonData/data/tidring0.xml',
      'Geometry/TrackerCommonData/data/tidring0f.xml',
      'Geometry/TrackerCommonData/data/tidring0b.xml',
      'Geometry/TrackerCommonData/data/tidring1.xml',
      'Geometry/TrackerCommonData/data/tidring1f.xml',
      'Geometry/TrackerCommonData/data/tidring1b.xml',
      'Geometry/TrackerCommonData/data/tidring2.xml',
      'Geometry/TrackerCommonData/data/tid.xml',
      'Geometry/TrackerCommonData/data/tidf.xml',
      'Geometry/TrackerCommonData/data/tidb.xml',
      'Geometry/TrackerCommonData/data/tibtidservices.xml',
      'Geometry/TrackerCommonData/data/tibtidservicesf.xml',
      'Geometry/TrackerCommonData/data/tibtidservicesb.xml',
      'Geometry/TrackerCommonData/data/tobmaterial.xml',
      'Geometry/TrackerCommonData/data/tobmodpar.xml',
      'Geometry/TrackerCommonData/data/tobmodule0.xml',
      'Geometry/TrackerCommonData/data/tobmodule2.xml',
      'Geometry/TrackerCommonData/data/tobmodule4.xml',
      'Geometry/TrackerCommonData/data/tobrodpar.xml',
      'Geometry/TrackerCommonData/data/tobrod0c.xml',
      'Geometry/TrackerCommonData/data/tobrod0l.xml',
      'Geometry/TrackerCommonData/data/tobrod0h.xml',
      'Geometry/TrackerCommonData/data/tobrod0.xml',
      'Geometry/TrackerCommonData/data/tobrod1l.xml',
      'Geometry/TrackerCommonData/data/tobrod1h.xml',
      'Geometry/TrackerCommonData/data/tobrod1.xml',
      'Geometry/TrackerCommonData/data/tobrod2c.xml',
      'Geometry/TrackerCommonData/data/tobrod2l.xml',
      'Geometry/TrackerCommonData/data/tobrod2h.xml',
      'Geometry/TrackerCommonData/data/tobrod2.xml',
      'Geometry/TrackerCommonData/data/tobrod3l.xml',
      'Geometry/TrackerCommonData/data/tobrod3h.xml',
      'Geometry/TrackerCommonData/data/tobrod3.xml',
      'Geometry/TrackerCommonData/data/tobrod4c.xml',
      'Geometry/TrackerCommonData/data/tobrod4l.xml',
      'Geometry/TrackerCommonData/data/tobrod4h.xml',
      'Geometry/TrackerCommonData/data/tobrod4.xml',
      'Geometry/TrackerCommonData/data/tobrod5l.xml',
      'Geometry/TrackerCommonData/data/tobrod5h.xml',
      'Geometry/TrackerCommonData/data/tobrod5.xml',
      'Geometry/TrackerCommonData/data/tob.xml',
      'Geometry/TrackerCommonData/data/tecmaterial.xml',
      'Geometry/TrackerCommonData/data/tecmodpar.xml',
      'Geometry/TrackerCommonData/data/tecmodule0.xml',
      'Geometry/TrackerCommonData/data/tecmodule0r.xml',
      'Geometry/TrackerCommonData/data/tecmodule0s.xml',
      'Geometry/TrackerCommonData/data/tecmodule1.xml',
      'Geometry/TrackerCommonData/data/tecmodule1r.xml',
      'Geometry/TrackerCommonData/data/tecmodule1s.xml',
      'Geometry/TrackerCommonData/data/tecmodule2.xml',
      'Geometry/TrackerCommonData/data/tecmodule3.xml',
      'Geometry/TrackerCommonData/data/tecmodule4.xml',
      'Geometry/TrackerCommonData/data/tecmodule4r.xml',
      'Geometry/TrackerCommonData/data/tecmodule4s.xml',
      'Geometry/TrackerCommonData/data/tecmodule5.xml',
      'Geometry/TrackerCommonData/data/tecmodule6.xml',
      'Geometry/TrackerCommonData/data/tecpetpar.xml',
      'Geometry/TrackerCommonData/data/tecring0.xml',
      'Geometry/TrackerCommonData/data/tecring1.xml',
      'Geometry/TrackerCommonData/data/tecring2.xml',
      'Geometry/TrackerCommonData/data/tecring3.xml',
      'Geometry/TrackerCommonData/data/tecring4.xml',
      'Geometry/TrackerCommonData/data/tecring5.xml',
      'Geometry/TrackerCommonData/data/tecring6.xml',
      'Geometry/TrackerCommonData/data/tecring0f.xml',
      'Geometry/TrackerCommonData/data/tecring1f.xml',
      'Geometry/TrackerCommonData/data/tecring2f.xml',
      'Geometry/TrackerCommonData/data/tecring3f.xml',
      'Geometry/TrackerCommonData/data/tecring4f.xml',
      'Geometry/TrackerCommonData/data/tecring5f.xml',
      'Geometry/TrackerCommonData/data/tecring6f.xml',
      'Geometry/TrackerCommonData/data/tecring0b.xml',
      'Geometry/TrackerCommonData/data/tecring1b.xml',
      'Geometry/TrackerCommonData/data/tecring2b.xml',
      'Geometry/TrackerCommonData/data/tecring3b.xml',
      'Geometry/TrackerCommonData/data/tecring4b.xml',
      'Geometry/TrackerCommonData/data/tecring5b.xml',
      'Geometry/TrackerCommonData/data/tecring6b.xml',
      'Geometry/TrackerCommonData/data/tecpetalf.xml',
      'Geometry/TrackerCommonData/data/tecpetalb.xml',
      'Geometry/TrackerCommonData/data/tecpetal0.xml',
      'Geometry/TrackerCommonData/data/tecpetal0f.xml',
      'Geometry/TrackerCommonData/data/tecpetal0b.xml',
      'Geometry/TrackerCommonData/data/tecpetal3.xml',
      'Geometry/TrackerCommonData/data/tecpetal3f.xml',
      'Geometry/TrackerCommonData/data/tecpetal3b.xml',
      'Geometry/TrackerCommonData/data/tecpetal6f.xml',
      'Geometry/TrackerCommonData/data/tecpetal6b.xml',
      'Geometry/TrackerCommonData/data/tecpetal8f.xml',
      'Geometry/TrackerCommonData/data/tecpetal8b.xml',
      'Geometry/TrackerCommonData/data/tecwheel.xml',
      'Geometry/TrackerCommonData/data/tecwheela.xml',
      'Geometry/TrackerCommonData/data/tecwheelb.xml',
      'Geometry/TrackerCommonData/data/tecwheelc.xml',
      'Geometry/TrackerCommonData/data/tecwheeld.xml',
      'Geometry/TrackerCommonData/data/tecwheel6.xml',
      'Geometry/TrackerCommonData/data/tecservices.xml',
      'Geometry/TrackerCommonData/data/tecbackplate.xml',
      'Geometry/TrackerCommonData/data/tec.xml',
      'Geometry/TrackerCommonData/data/trackermaterial.xml',
      'Geometry/TrackerCommonData/data/tracker.xml',
      'Geometry/TrackerCommonData/data/trackerpixbar.xml',
      'Geometry/TrackerCommonData/data/trackerpixfwd.xml',
      'Geometry/TrackerCommonData/data/trackertibtidservices.xml',
      'Geometry/TrackerCommonData/data/trackertib.xml',
      'Geometry/TrackerCommonData/data/trackertid.xml',
      'Geometry/TrackerCommonData/data/trackertob.xml',
      'Geometry/TrackerCommonData/data/trackertec.xml',
      'Geometry/TrackerCommonData/data/trackerbulkhead.xml',
      'Geometry/TrackerCommonData/data/trackerother.xml',
      'Geometry/EcalCommonData/data/eregalgo.xml',
      'Geometry/EcalCommonData/data/ebalgo.xml',
      'Geometry/EcalCommonData/data/ebcon.xml',
      'Geometry/EcalCommonData/data/ebrot.xml',
      'Geometry/EcalCommonData/data/eecon.xml',
      'Geometry/EcalCommonData/data/eefixed.xml',
      'Geometry/EcalCommonData/data/eehier.xml',
      'Geometry/EcalCommonData/data/eealgo.xml',
      'Geometry/EcalCommonData/data/escon.xml',
      'Geometry/EcalCommonData/data/esalgo.xml',
      'Geometry/EcalCommonData/data/eeF.xml',
      'Geometry/EcalCommonData/data/eeB.xml',
      'Geometry/HcalCommonData/data/hcalrotations.xml',
      'Geometry/HcalCommonData/data/hcalalgo.xml',
      'Geometry/HcalCommonData/data/hcalbarrelalgo.xml',
      'Geometry/HcalCommonData/data/hcalendcapalgo.xml',
      'Geometry/HcalCommonData/data/hcalouteralgo.xml',
      'Geometry/HcalCommonData/data/hcalforwardalgo.xml',
      'Geometry/HcalCommonData/data/hcalforwardfibre.xml',
      'Geometry/HcalCommonData/data/hcalforwardmaterial.xml',
      'Geometry/MuonCommonData/data/mbCommon.xml',
      'Geometry/MuonCommonData/data/mb1.xml',
      'Geometry/MuonCommonData/data/mb2.xml',
      'Geometry/MuonCommonData/data/mb3.xml',
      'Geometry/MuonCommonData/data/mb4.xml',
      'Geometry/MuonCommonData/data/muonYoke.xml',
      'Geometry/MuonCommonData/data/mf.xml',
      'Geometry/ForwardCommonData/data/forward.xml',
      'Geometry/ForwardCommonData/data/forwardshield.xml',
      'Geometry/ForwardCommonData/data/brmrotations.xml',
      'Geometry/ForwardCommonData/data/brm.xml',
      'Geometry/ForwardCommonData/data/totemMaterials.xml',
      'Geometry/ForwardCommonData/data/totemRotations.xml',
      'Geometry/ForwardCommonData/data/totemt1.xml',
      'Geometry/ForwardCommonData/data/totemt2.xml',
      'Geometry/ForwardCommonData/data/ionpump.xml',
      'Geometry/ForwardCommonData/data/castor.xml',
      'Geometry/ForwardCommonData/data/zdcmaterials.xml',
      'Geometry/ForwardCommonData/data/lumimaterials.xml',
      'Geometry/ForwardCommonData/data/zdcrotations.xml',
      'Geometry/ForwardCommonData/data/lumirotations.xml',
      'Geometry/ForwardCommonData/data/zdc.xml',
      'Geometry/ForwardCommonData/data/zdclumi.xml',
      'Geometry/ForwardCommonData/data/cmszdc.xml',
      'Geometry/MuonCommonData/data/muonNumbering.xml',
      'Geometry/TrackerCommonData/data/trackerStructureTopology.xml',
      'Geometry/TrackerSimData/data/trackersens.xml',
      'Geometry/TrackerRecoData/data/trackerRecoMaterial.xml',
      'Geometry/EcalSimData/data/ecalsens.xml',
      'Geometry/HcalCommonData/data/hcalsens.xml',
      'Geometry/HcalSimData/data/CaloUtil.xml',
      'Geometry/MuonSimData/data/muonSens.xml',
      'Geometry/DTGeometryBuilder/data/dtSpecsFilter.xml',
      'Geometry/CSCGeometryBuilder/data/cscSpecsFilter.xml',
      'Geometry/CSCGeometryBuilder/data/cscSpecs.xml',
      'Geometry/RPCGeometryBuilder/data/RPCSpecs.xml',
      'Geometry/ForwardCommonData/data/brmsens.xml',
      'Geometry/ForwardSimData/data/totemsensT1.xml',
      'Geometry/ForwardSimData/data/totemsensT2.xml',
      'Geometry/ForwardSimData/data/castorsens.xml',
      'Geometry/ForwardSimData/data/zdcsens.xml')+cms.vstring( 'Geometry/HcalSimData/data/CaloProdCuts.xml',
      'Geometry/HcalSimData/data/HcalProdCuts.xml',
      'Geometry/EcalSimData/data/EcalProdCuts.xml',
      'Geometry/TrackerSimData/data/trackerProdCuts.xml',
      'Geometry/TrackerSimData/data/trackerProdCutsBEAM.xml',
      'Geometry/MuonSimData/data/muonProdCuts.xml',
      'Geometry/ForwardSimData/data/CastorProdCuts.xml',
      'Geometry/ForwardSimData/data/zdcProdCuts.xml',
      'Geometry/ForwardSimData/data/ForwardShieldProdCuts.xml',
      'Geometry/CMSCommonData/data/FieldParameters.xml') )
)
process.eegeom = cms.ESSource( "EmptyESSource",
    recordName = cms.string( "EcalMappingRcd" ),
    iovIsRunNotTime = cms.bool( True ),
    appendToDataLabel = cms.string( "" ),
    firstValid = cms.vuint32( 1 )
)
process.es_hardcode = cms.ESSource( "HcalHardcodeCalibrations",
    toGet = cms.untracked.vstring( 'GainWidths' ),
    appendToDataLabel = cms.string( "" )
)
process.magfield = cms.ESSource( "XMLIdealGeometryESSource",
    rootNodeName = cms.string( "cmsMagneticField:MAGF" ),
    appendToDataLabel = cms.string( "" ),
    geomXMLFiles = cms.vstring( 'Geometry/CMSCommonData/data/normal/cmsextent.xml',
      'Geometry/CMSCommonData/data/cms.xml',
      'Geometry/CMSCommonData/data/cmsMagneticField.xml',
      'MagneticField/GeomBuilder/data/MagneticFieldVolumes_1103l.xml',
      'MagneticField/GeomBuilder/data/MagneticFieldParameters_07_2pi.xml' )
)

process.AnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  ComponentName = cms.string( "AnalyticalPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  MaxDPhi = cms.double( 1.6 ),
  appendToDataLabel = cms.string( "" )
)
process.AnyDirectionAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  ComponentName = cms.string( "AnyDirectionAnalyticalPropagator" ),
  PropagationDirection = cms.string( "anyDirection" ),
  MaxDPhi = cms.double( 1.6 ),
  appendToDataLabel = cms.string( "" )
)
process.CSCGeometryESModule = cms.ESProducer( "CSCGeometryESModule",
  alignmentsLabel = cms.string( "" ),
  appendToDataLabel = cms.string( "" ),
  useRealWireGeometry = cms.bool( True ),
  useOnlyWiresInME1a = cms.bool( False ),
  useGangedStripsInME1a = cms.bool( True ),
  useCentreTIOffsets = cms.bool( False ),
  useDDD = cms.bool( True ),
  applyAlignment = cms.bool( True )
)
process.CaloGeometryBuilder = cms.ESProducer( "CaloGeometryBuilder",
  appendToDataLabel = cms.string( "" ),
  SelectedCalos = cms.vstring( 'HCAL',
    'ZDC',
    'EcalBarrel',
    'EcalEndcap',
    'EcalPreshower',
    'TOWER' )
)
process.CaloTopologyBuilder = cms.ESProducer( "CaloTopologyBuilder",
  appendToDataLabel = cms.string( "" )
)
process.CaloTowerConstituentsMapBuilder = cms.ESProducer( "CaloTowerConstituentsMapBuilder",
  MapFile = cms.untracked.string( "Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz" ),
  appendToDataLabel = cms.string( "" )
)
process.CaloTowerHardcodeGeometryEP = cms.ESProducer( "CaloTowerHardcodeGeometryEP",
  appendToDataLabel = cms.string( "" )
)
process.Chi2EstimatorForRefit = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  ComponentName = cms.string( "Chi2EstimatorForRefit" ),
  MaxChi2 = cms.double( 100000.0 ),
  nSigma = cms.double( 3.0 ),
  appendToDataLabel = cms.string( "" )
)
process.Chi2MeasurementEstimator = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  ComponentName = cms.string( "Chi2" ),
  MaxChi2 = cms.double( 30.0 ),
  nSigma = cms.double( 3.0 ),
  appendToDataLabel = cms.string( "" )
)
process.CkfTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "CkfTrajectoryBuilder" ),
  updator = cms.string( "KFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  estimator = cms.string( "Chi2" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  MeasurementTrackerName = cms.string( "" ),
  trajectoryFilterName = cms.string( "ckfBaseTrajectoryFilter" ),
  maxCand = cms.int32( 5 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( True ),
  alwaysUseInvalidHits = cms.bool( True ),
  appendToDataLabel = cms.string( "" )
)
process.DTGeometryESModule = cms.ESProducer( "DTGeometryESModule",
  alignmentsLabel = cms.string( "" ),
  appendToDataLabel = cms.string( "" ),
  fromDDD = cms.bool( True ),
  applyAlignment = cms.bool( True )
)
process.ESUnpackerWorkerESProducer = cms.ESProducer( "ESUnpackerWorkerESProducer",
  ComponentName = cms.string( "esRawToRecHit" ),
  appendToDataLabel = cms.string( "" ),
  DCCDataUnpacker = cms.PSet(  LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" ) ),
  RHAlgo = cms.PSet(  Type = cms.string( "ESRecHitWorker" ) )
)
process.EcalBarrelGeometryEP = cms.ESProducer( "EcalBarrelGeometryEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( False )
)
process.EcalElectronicsMappingBuilder = cms.ESProducer( "EcalElectronicsMappingBuilder",
  appendToDataLabel = cms.string( "" )
)
process.EcalEndcapGeometryEP = cms.ESProducer( "EcalEndcapGeometryEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( False )
)
process.EcalLaserCorrectionService = cms.ESProducer( "EcalLaserCorrectionService",
  appendToDataLabel = cms.string( "" )
)
process.EcalPreshowerGeometryEP = cms.ESProducer( "EcalPreshowerGeometryEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( False )
)
process.EcalRegionCablingESProducer = cms.ESProducer( "EcalRegionCablingESProducer",
  appendToDataLabel = cms.string( "" ),
  esMapping = cms.PSet(  LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" ) )
)
process.EcalUnpackerWorkerESProducer = cms.ESProducer( "EcalUnpackerWorkerESProducer",
  ComponentName = cms.string( "" ),
  appendToDataLabel = cms.string( "" ),
  DCCDataUnpacker = cms.PSet( 
    tccUnpacking = cms.bool( True ),
    orderedDCCIdList = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ),
    srpUnpacking = cms.bool( False ),
    syncCheck = cms.bool( False ),
    headerUnpacking = cms.bool( False ),
    orderedFedList = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    feUnpacking = cms.bool( True ),
    feIdCheck = cms.bool( True ),
    memUnpacking = cms.bool( False )
  ),
  ElectronicsMapper = cms.PSet( 
    numbXtalTSamples = cms.uint32( 10 ),
    numbTriggerTSamples = cms.uint32( 1 )
  ),
  UncalibRHAlgo = cms.PSet(  Type = cms.string( "EcalUncalibRecHitWorkerWeights" ) ),
  CalibRHAlgo = cms.PSet( 
    Type = cms.string( "EcalRecHitWorkerSimple" ),
    ChannelStatusToBeExcluded = cms.vint32(  ),
    flagsMapDBReco = cms.vint32( 0, 0, 0, 0, 4, -1, -1, -1, 4, 4, 6, 6, 6, 7, 8 ),
    killDeadChannels = cms.bool( True )
  )
)
process.FastSteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  ComponentName = cms.string( "FastSteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "anyDirection" ),
  useInTeslaFromMagField = cms.bool( False ),
  SetVBFPointer = cms.bool( False ),
  useMagVolumes = cms.bool( True ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  ApplyRadX0Correction = cms.bool( True ),
  AssumeNoMaterial = cms.bool( False ),
  NoErrorPropagation = cms.bool( False ),
  debug = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  returnTangentPlane = cms.bool( True ),
  sendLogWarning = cms.bool( False ),
  useTuningForL2Speed = cms.bool( True ),
  useEndcapShiftsInZ = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  appendToDataLabel = cms.string( "" )
)
process.FastSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  ComponentName = cms.string( "FastSteppingHelixPropagatorOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useInTeslaFromMagField = cms.bool( False ),
  SetVBFPointer = cms.bool( False ),
  useMagVolumes = cms.bool( True ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  ApplyRadX0Correction = cms.bool( True ),
  AssumeNoMaterial = cms.bool( False ),
  NoErrorPropagation = cms.bool( False ),
  debug = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  returnTangentPlane = cms.bool( True ),
  sendLogWarning = cms.bool( False ),
  useTuningForL2Speed = cms.bool( True ),
  useEndcapShiftsInZ = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  appendToDataLabel = cms.string( "" )
)
process.FitterRK = cms.ESProducer( "KFTrajectoryFitterESProducer",
  ComponentName = cms.string( "FitterRK" ),
  Propagator = cms.string( "RungeKuttaTrackerPropagator" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2" ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.FittingSmootherRK = cms.ESProducer( "KFFittingSmootherESProducer",
  ComponentName = cms.string( "FittingSmootherRK" ),
  Fitter = cms.string( "FitterRK" ),
  Smoother = cms.string( "SmootherRK" ),
  EstimateCut = cms.double( -1.0 ),
  MinNumberOfHits = cms.int32( 5 ),
  RejectTracks = cms.bool( True ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.GlobalTrackingGeometryESProducer = cms.ESProducer( "GlobalTrackingGeometryESProducer",
  appendToDataLabel = cms.string( "" )
)
process.GroupedCkfTrajectoryBuilder = cms.ESProducer( "GroupedCkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "GroupedCkfTrajectoryBuilder" ),
  updator = cms.string( "KFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  estimator = cms.string( "Chi2" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  MeasurementTrackerName = cms.string( "" ),
  trajectoryFilterName = cms.string( "ckfBaseTrajectoryFilter" ),
  inOutTrajectoryFilterName = cms.string( "" ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 5 ),
  lostHitPenalty = cms.double( 30.0 ),
  foundHitBonus = cms.double( 5.0 ),
  intermediateCleaning = cms.bool( True ),
  alwaysUseInvalidHits = cms.bool( True ),
  lockHits = cms.bool( True ),
  bestHitOnly = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  appendToDataLabel = cms.string( "" )
)
process.HITTRHBuilderWithoutRefit = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "HITTRHBuilderWithoutRefit" ),
  StripCPE = cms.string( "Fake" ),
  PixelCPE = cms.string( "Fake" ),
  Matcher = cms.string( "Fake" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.HcalHardcodeGeometryEP = cms.ESProducer( "HcalHardcodeGeometryEP",
  appendToDataLabel = cms.string( "" )
)
process.HcalTopologyIdealEP = cms.ESProducer( "HcalTopologyIdealEP",
  appendToDataLabel = cms.string( "" )
)
process.KFFitterForRefitInsideOut = cms.ESProducer( "KFTrajectoryFitterESProducer",
  ComponentName = cms.string( "KFFitterForRefitInsideOut" ),
  Propagator = cms.string( "SmartPropagatorAny" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2EstimatorForRefit" ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.KFFitterSmootherForL2Muon = cms.ESProducer( "KFFittingSmootherESProducer",
  ComponentName = cms.string( "KFFitterSmootherForL2Muon" ),
  Fitter = cms.string( "KFTrajectoryFitterForL2Muon" ),
  Smoother = cms.string( "KFTrajectorySmootherForL2Muon" ),
  EstimateCut = cms.double( -1.0 ),
  MinNumberOfHits = cms.int32( 5 ),
  RejectTracks = cms.bool( True ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.KFSmootherForMuonTrackLoader = cms.ESProducer( "KFTrajectorySmootherESProducer",
  ComponentName = cms.string( "KFSmootherForMuonTrackLoader" ),
  Propagator = cms.string( "SmartPropagatorAnyOpposite" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2" ),
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.KFSmootherForRefitInsideOut = cms.ESProducer( "KFTrajectorySmootherESProducer",
  ComponentName = cms.string( "KFSmootherForRefitInsideOut" ),
  Propagator = cms.string( "SmartPropagatorAnyOpposite" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2EstimatorForRefit" ),
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.KFTrajectoryFitterForL2Muon = cms.ESProducer( "KFTrajectoryFitterESProducer",
  ComponentName = cms.string( "KFTrajectoryFitterForL2Muon" ),
  Propagator = cms.string( "FastSteppingHelixPropagatorAny" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2" ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.KFTrajectorySmootherForL2Muon = cms.ESProducer( "KFTrajectorySmootherESProducer",
  ComponentName = cms.string( "KFTrajectorySmootherForL2Muon" ),
  Propagator = cms.string( "FastSteppingHelixPropagatorOpposite" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2" ),
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.KFUpdatorESProducer = cms.ESProducer( "KFUpdatorESProducer",
  ComponentName = cms.string( "KFUpdator" ),
  appendToDataLabel = cms.string( "" )
)
process.L3MuKFFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  ComponentName = cms.string( "L3MuKFFitter" ),
  Propagator = cms.string( "SmartPropagatorAny" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2" ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.MaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  ComponentName = cms.string( "PropagatorWithMaterial" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  Mass = cms.double( 0.105 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False ),
  ptMin = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" )
)
process.MeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  ComponentName = cms.string( "" ),
  PixelCPE = cms.string( "PixelCPEGeneric" ),
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  HitMatcher = cms.string( "StandardMatcher" ),
  Regional = cms.bool( True ),
  OnDemand = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripModuleQualityDB = cms.bool( False ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( False ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  MaskBadAPVFibers = cms.bool( False ),
  UseStripStripQualityDB = cms.bool( False ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  stripClusterProducer = cms.string( "hltSiStripClusters" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  appendToDataLabel = cms.string( "" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  inactiveStripDetectorLabels = cms.VInputTag(  )
)
process.MuonCkfTrajectoryBuilder = cms.ESProducer( "MuonCkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "muonCkfTrajectoryBuilder" ),
  updator = cms.string( "KFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  estimator = cms.string( "Chi2" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  MeasurementTrackerName = cms.string( "" ),
  trajectoryFilterName = cms.string( "muonCkfTrajectoryFilter" ),
  useSeedLayer = cms.bool( False ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  appendToDataLabel = cms.string( "" ),
  maxCand = cms.int32( 5 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( False ),
  alwaysUseInvalidHits = cms.bool( True )
)
process.MuonDetLayerGeometryESProducer = cms.ESProducer( "MuonDetLayerGeometryESProducer",
  appendToDataLabel = cms.string( "" )
)
process.MuonNumberingInitialization = cms.ESProducer( "MuonNumberingInitialization",
  appendToDataLabel = cms.string( "" )
)
process.MuonTransientTrackingRecHitBuilderESProducer = cms.ESProducer( "MuonTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "MuonRecHitBuilder" ),
  appendToDataLabel = cms.string( "" )
)
process.OppositeMaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  ComponentName = cms.string( "PropagatorWithMaterialOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  Mass = cms.double( 0.105 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False ),
  ptMin = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" )
)
process.ParametrizedMagneticFieldProducer = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  label = cms.untracked.string( "parametrizedField" ),
  version = cms.string( "OAE_1103l_071212" ),
  appendToDataLabel = cms.string( "" ),
  parameters = cms.PSet(  BValue = cms.string( "3_8T" ) )
)
process.PixelCPEGenericESProducer = cms.ESProducer( "PixelCPEGenericESProducer",
  ComponentName = cms.string( "PixelCPEGeneric" ),
  eff_charge_cut_lowX = cms.double( 0.0 ),
  eff_charge_cut_lowY = cms.double( 0.0 ),
  eff_charge_cut_highX = cms.double( 1.0 ),
  eff_charge_cut_highY = cms.double( 1.0 ),
  size_cutX = cms.double( 3.0 ),
  size_cutY = cms.double( 3.0 ),
  EdgeClusterErrorX = cms.double( 50.0 ),
  EdgeClusterErrorY = cms.double( 85.0 ),
  inflate_errors = cms.bool( False ),
  inflate_all_errors_no_trk_angle = cms.bool( False ),
  UseErrorsFromTemplates = cms.bool( True ),
  TruncatePixelCharge = cms.bool( True ),
  IrradiationBiasCorrection = cms.bool( False ),
  DoCosmics = cms.bool( False ),
  LoadTemplatesFromDB = cms.bool( True ),
  appendToDataLabel = cms.string( "" ),
  TanLorentzAnglePerTesla = cms.double( 0.106 ),
  PixelErrorParametrization = cms.string( "NOTcmsim" ),
  Alpha2Order = cms.bool( True ),
  ClusterProbComputationFlag = cms.int32( 0 )
)
process.RPCGeometryESModule = cms.ESProducer( "RPCGeometryESModule",
  appendToDataLabel = cms.string( "" )
)
process.RungeKuttaTrackerPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  ComponentName = cms.string( "RungeKuttaTrackerPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  Mass = cms.double( 0.105 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( True ),
  ptMin = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" )
)
process.SiStripGainESProducer = cms.ESProducer( "SiStripGainESProducer",
  AutomaticNormalization = cms.bool( False ),
  NormalizationFactor = cms.double( 1.0 ),
  printDebug = cms.untracked.bool( False ),
  APVGain = cms.string( "" )
)
process.SiStripRecHitMatcherESProducer = cms.ESProducer( "SiStripRecHitMatcherESProducer",
  ComponentName = cms.string( "StandardMatcher" ),
  NSigmaInside = cms.double( 3.0 ),
  appendToDataLabel = cms.string( "" )
)
process.SiStripRegionConnectivity = cms.ESProducer( "SiStripRegionConnectivity",
  EtaDivisions = cms.untracked.uint32( 20 ),
  PhiDivisions = cms.untracked.uint32( 20 ),
  EtaMax = cms.untracked.double( 2.5 )
)
process.SmartPropagator = cms.ESProducer( "SmartPropagatorESProducer",
  ComponentName = cms.string( "SmartPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAlong" ),
  appendToDataLabel = cms.string( "" )
)
process.SmartPropagatorAny = cms.ESProducer( "SmartPropagatorESProducer",
  ComponentName = cms.string( "SmartPropagatorAny" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  appendToDataLabel = cms.string( "" )
)
process.SmartPropagatorAnyOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  ComponentName = cms.string( "SmartPropagatorAnyOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  appendToDataLabel = cms.string( "" )
)
process.SmartPropagatorOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  ComponentName = cms.string( "SmartPropagatorOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorOpposite" ),
  appendToDataLabel = cms.string( "" )
)
process.SmootherRK = cms.ESProducer( "KFTrajectorySmootherESProducer",
  ComponentName = cms.string( "SmootherRK" ),
  Propagator = cms.string( "RungeKuttaTrackerPropagator" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2" ),
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.SteppingHelixPropagatorAlong = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  ComponentName = cms.string( "SteppingHelixPropagatorAlong" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  useInTeslaFromMagField = cms.bool( False ),
  SetVBFPointer = cms.bool( False ),
  useMagVolumes = cms.bool( True ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  ApplyRadX0Correction = cms.bool( True ),
  AssumeNoMaterial = cms.bool( False ),
  NoErrorPropagation = cms.bool( False ),
  debug = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  returnTangentPlane = cms.bool( True ),
  sendLogWarning = cms.bool( False ),
  useTuningForL2Speed = cms.bool( False ),
  useEndcapShiftsInZ = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  appendToDataLabel = cms.string( "" )
)
process.SteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  ComponentName = cms.string( "SteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "anyDirection" ),
  useInTeslaFromMagField = cms.bool( False ),
  SetVBFPointer = cms.bool( False ),
  useMagVolumes = cms.bool( True ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  ApplyRadX0Correction = cms.bool( True ),
  AssumeNoMaterial = cms.bool( False ),
  NoErrorPropagation = cms.bool( False ),
  debug = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  returnTangentPlane = cms.bool( True ),
  sendLogWarning = cms.bool( False ),
  useTuningForL2Speed = cms.bool( False ),
  useEndcapShiftsInZ = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  appendToDataLabel = cms.string( "" )
)
process.SteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  ComponentName = cms.string( "SteppingHelixPropagatorOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useInTeslaFromMagField = cms.bool( False ),
  SetVBFPointer = cms.bool( False ),
  useMagVolumes = cms.bool( True ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  ApplyRadX0Correction = cms.bool( True ),
  AssumeNoMaterial = cms.bool( False ),
  NoErrorPropagation = cms.bool( False ),
  debug = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  returnTangentPlane = cms.bool( True ),
  sendLogWarning = cms.bool( False ),
  useTuningForL2Speed = cms.bool( False ),
  useEndcapShiftsInZ = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  appendToDataLabel = cms.string( "" )
)
process.StripCPEfromTrackAngleESProducer = cms.ESProducer( "StripCPEfromTrackAngleESProducer",
  ComponentName = cms.string( "StripCPEfromTrackAngle" ),
  appendToDataLabel = cms.string( "" )
)
process.TTRHBuilderPixelOnly = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "TTRHBuilderPixelOnly" ),
  StripCPE = cms.string( "Fake" ),
  PixelCPE = cms.string( "PixelCPEGeneric" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.TrackerDigiGeometryESModule = cms.ESProducer( "TrackerDigiGeometryESModule",
  alignmentsLabel = cms.string( "" ),
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( True ),
  fromDDD = cms.bool( True )
)
process.TrackerGeometricDetESModule = cms.ESProducer( "TrackerGeometricDetESModule",
  fromDDD = cms.bool( True ),
  appendToDataLabel = cms.string( "" )
)
process.TrackerRecoGeometryESProducer = cms.ESProducer( "TrackerRecoGeometryESProducer",
  appendToDataLabel = cms.string( "" )
)
process.TransientTrackBuilderESProducer = cms.ESProducer( "TransientTrackBuilderESProducer",
  ComponentName = cms.string( "TransientTrackBuilder" ),
  appendToDataLabel = cms.string( "" )
)
process.VolumeBasedMagneticFieldESProducer = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  label = cms.untracked.string( "" ),
  version = cms.string( "grid_1103l_090322_3_8t" ),
  overrideMasterSector = cms.bool( False ),
  useParametrizedTrackerField = cms.bool( True ),
  paramLabel = cms.string( "parametrizedField" ),
  appendToDataLabel = cms.string( "" ),
  scalingVolumes = cms.vint32( 14100, 14200, 17600, 17800, 17900, 18100, 18300, 18400, 18600, 23100, 23300, 23400, 23600, 23800, 23900, 24100, 28600, 28800, 28900, 29100, 29300, 29400, 29600, 28609, 28809, 28909, 29109, 29309, 29409, 29609, 28610, 28810, 28910, 29110, 29310, 29410, 29610, 28611, 28811, 28911, 29111, 29311, 29411, 29611 ),
  scalingFactors = cms.vdouble( 1.0, 1.0, 0.994, 1.004, 1.004, 1.005, 1.004, 1.004, 0.994, 0.965, 0.958, 0.958, 0.953, 0.958, 0.958, 0.965, 0.918, 0.924, 0.924, 0.906, 0.924, 0.924, 0.918, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991 ),
  findVolumeTolerance = cms.double( 0.0 ),
  cacheLastVolume = cms.untracked.bool( True ),
  timerOn = cms.untracked.bool( False )
)
process.WithTrackAngle = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "WithTrackAngle" ),
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  PixelCPE = cms.string( "PixelCPEGeneric" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.ZdcHardcodeGeometryEP = cms.ESProducer( "ZdcHardcodeGeometryEP",
  appendToDataLabel = cms.string( "" )
)
process.bJetRegionalTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "bJetRegionalTrajectoryBuilder" ),
  updator = cms.string( "KFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  estimator = cms.string( "Chi2" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  MeasurementTrackerName = cms.string( "" ),
  trajectoryFilterName = cms.string( "bJetRegionalTrajectoryFilter" ),
  maxCand = cms.int32( 1 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( True ),
  alwaysUseInvalidHits = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.bJetRegionalTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "bJetRegionalTrajectoryFilter" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet( 
    chargeSignificance = cms.double( -1.0 ),
    minPt = cms.double( 1.0 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 8 ),
    maxConsecLostHits = cms.int32( 1 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minimumNumberOfHits = cms.int32( 5 )
  )
)
process.ckfBaseTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "ckfBaseTrajectoryFilter" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet( 
    chargeSignificance = cms.double( -1.0 ),
    minPt = cms.double( 0.9 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( -1 ),
    maxConsecLostHits = cms.int32( 1 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minimumNumberOfHits = cms.int32( 5 )
  )
)
process.hcalRecAlgos = cms.ESProducer( "HcalRecAlgoESProducer",
  SeverityLevels = cms.VPSet( 
    cms.PSet(  Level = cms.int32( 0 ),
      RecHitFlags = cms.vstring( '' ),
      ChannelStatus = cms.vstring( '' )
    )
  ),
  RecoveredRecHitBits = cms.vstring( '' ),
  appendToDataLabel = cms.string( "" ),
  DropChannelStatusBits = cms.vstring( '' )
)
process.hcal_db_producer = cms.ESProducer( "HcalDbProducer",
  appendToDataLabel = cms.string( "" ),
  dump = cms.untracked.vstring( '' )
)
process.hltCkfTrajectoryBuilderMumu = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "hltCkfTrajectoryBuilderMumu" ),
  updator = cms.string( "KFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  estimator = cms.string( "Chi2" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  MeasurementTrackerName = cms.string( "" ),
  trajectoryFilterName = cms.string( "hltCkfTrajectoryFilterMumu" ),
  maxCand = cms.int32( 3 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( True ),
  alwaysUseInvalidHits = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.hltCkfTrajectoryFilterMumu = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "hltCkfTrajectoryFilterMumu" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet( 
    chargeSignificance = cms.double( -1.0 ),
    minPt = cms.double( 3.0 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 5 ),
    maxConsecLostHits = cms.int32( 1 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minimumNumberOfHits = cms.int32( 5 )
  )
)
process.hltKFFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  ComponentName = cms.string( "hltKFFitter" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2" ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.hltKFFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  ComponentName = cms.string( "hltKFFittingSmoother" ),
  Fitter = cms.string( "hltKFFitter" ),
  Smoother = cms.string( "hltKFSmoother" ),
  EstimateCut = cms.double( -1.0 ),
  MinNumberOfHits = cms.int32( 5 ),
  RejectTracks = cms.bool( True ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.hltKFSmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  ComponentName = cms.string( "hltKFSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2" ),
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.mixedlayerpairs = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "MixedLayerPairs" ),
  layerList = cms.vstring( 'BPix1+BPix2',
    'BPix1+BPix3',
    'BPix2+BPix3',
    'BPix1+FPix1_pos',
    'BPix1+FPix1_neg',
    'BPix1+FPix2_pos',
    'BPix1+FPix2_neg',
    'BPix2+FPix1_pos',
    'BPix2+FPix1_neg',
    'BPix2+FPix2_pos',
    'BPix2+FPix2_neg',
    'FPix1_pos+FPix2_pos',
    'FPix1_neg+FPix2_neg',
    'FPix2_pos+TEC1_pos',
    'FPix2_pos+TEC2_pos',
    'TEC1_pos+TEC2_pos',
    'TEC2_pos+TEC3_pos',
    'FPix2_neg+TEC1_neg',
    'FPix2_neg+TEC2_neg',
    'TEC1_neg+TEC2_neg',
    'TEC2_neg+TEC3_neg' ),
  BPix = cms.PSet( 
    hitErrorRZ = cms.double( 0.0060 ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  FPix = cms.PSet( 
    hitErrorRZ = cms.double( 0.0036 ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  TEC = cms.PSet( 
    TTRHBuilder = cms.string( "WithTrackAngle" ),
    minRing = cms.int32( 1 ),
    maxRing = cms.int32( 1 ),
    useRingSlector = cms.bool( True )
  )
)
process.muonCkfTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "muonCkfTrajectoryFilter" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet( 
    minimumNumberOfHits = cms.int32( 5 ),
    minPt = cms.double( 0.9 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( -1 ),
    maxConsecLostHits = cms.int32( 1 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  )
)
process.navigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
  ComponentName = cms.string( "SimpleNavigationSchool" ),
  appendToDataLabel = cms.string( "" )
)
process.pixellayerpairs = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "PixelLayerPairs" ),
  layerList = cms.vstring( 'BPix1+BPix2',
    'BPix1+BPix3',
    'BPix2+BPix3',
    'BPix1+FPix1_pos',
    'BPix1+FPix1_neg',
    'BPix1+FPix2_pos',
    'BPix1+FPix2_neg',
    'BPix2+FPix1_pos',
    'BPix2+FPix1_neg',
    'BPix2+FPix2_pos',
    'BPix2+FPix2_neg',
    'FPix1_pos+FPix2_pos',
    'FPix1_neg+FPix2_neg' ),
  BPix = cms.PSet( 
    hitErrorRZ = cms.double( 0.0060 ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  FPix = cms.PSet( 
    hitErrorRZ = cms.double( 0.0036 ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  TEC = cms.PSet(  )
)
process.pixellayertriplets = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "PixelLayerTriplets" ),
  layerList = cms.vstring( 'BPix1+BPix2+BPix3',
    'BPix1+BPix2+FPix1_pos',
    'BPix1+BPix2+FPix1_neg',
    'BPix1+FPix1_pos+FPix2_pos',
    'BPix1+FPix1_neg+FPix2_neg' ),
  BPix = cms.PSet( 
    hitErrorRZ = cms.double( 0.0060 ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  FPix = cms.PSet( 
    hitErrorRZ = cms.double( 0.0036 ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  TEC = cms.PSet(  )
)
process.sistripconn = cms.ESProducer( "SiStripConnectivity" )
process.softLeptonByDistance = cms.ESProducer( "LeptonTaggerByDistanceESProducer",
  appendToDataLabel = cms.string( "" ),
  distance = cms.double( 0.5 )
)
process.softLeptonByPt = cms.ESProducer( "LeptonTaggerByPtESProducer",
  appendToDataLabel = cms.string( "" ),
  ipSign = cms.string( "any" )
)
process.trackCounting3D2nd = cms.ESProducer( "TrackCountingESProducer",
  appendToDataLabel = cms.string( "" ),
  nthTrack = cms.int32( 2 ),
  impactParameterType = cms.int32( 0 ),
  deltaR = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 5.0 ),
  maximumDistanceToJetAxis = cms.double( 0.07 ),
  trackQualityClass = cms.string( "any" )
)
process.trajBuilderL3 = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "trajBuilderL3" ),
  updator = cms.string( "KFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  estimator = cms.string( "Chi2" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  MeasurementTrackerName = cms.string( "" ),
  trajectoryFilterName = cms.string( "trajFilterL3" ),
  maxCand = cms.int32( 5 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( True ),
  alwaysUseInvalidHits = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.trajFilterL3 = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "trajFilterL3" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet( 
    chargeSignificance = cms.double( -1.0 ),
    minPt = cms.double( 0.9 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 7 ),
    maxConsecLostHits = cms.int32( 1 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minimumNumberOfHits = cms.int32( 5 )
  )
)
process.trajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "TrajectoryCleanerBySharedHits" ),
  appendToDataLabel = cms.string( "" ),
  fractionShared = cms.double( 0.5 )
)

process.MessageLogger = cms.Service( "MessageLogger",
    destinations = cms.untracked.vstring( 'warnings',
      'errors',
      'infos',
      'debugs',
      'cout',
      'cerr' ),
    categories = cms.untracked.vstring( 'FwkJob',
      'FwkReport',
      'FwkSummary',
      'Root_NoDictionary' ),
    statistics = cms.untracked.vstring( 'cerr' ),
    cerr = cms.untracked.PSet( 
      noTimeStamps = cms.untracked.bool( False ),
      threshold = cms.untracked.string( "INFO" ),
      INFO = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      default = cms.untracked.PSet(  limit = cms.untracked.int32( 10000000 ) ),
      FwkReport = cms.untracked.PSet( 
        limit = cms.untracked.int32( 10000000 ),
        reportEvery = cms.untracked.int32( 1 )
      ),
      FwkSummary = cms.untracked.PSet( 
        limit = cms.untracked.int32( 10000000 ),
        reportEvery = cms.untracked.int32( 1 )
      ),
      FwkJob = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      Root_NoDictionary = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) )
    ),
    cout = cms.untracked.PSet(  placeholder = cms.untracked.bool( True ) ),
    errors = cms.untracked.PSet(  placeholder = cms.untracked.bool( True ) ),
    warnings = cms.untracked.PSet(  placeholder = cms.untracked.bool( True ) ),
    infos = cms.untracked.PSet( 
      placeholder = cms.untracked.bool( True ),
      Root_NoDictionary = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) )
    ),
    debugs = cms.untracked.PSet(  placeholder = cms.untracked.bool( True ) ),
    fwkJobReports = cms.untracked.vstring( 'FrameworkJobReport' ),
    FrameworkJobReport = cms.untracked.PSet( 
      default = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkJob = cms.untracked.PSet(  limit = cms.untracked.int32( 10000000 ) )
    ),
)
process.UpdaterService = cms.Service( "UpdaterService",
)

process.hltGetRaw = cms.EDAnalyzer( "HLTGetRaw",
    RawDataCollection = cms.InputTag( "rawDataCollector" )
)
process.hltTriggerType = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
process.hltEventNumber = cms.EDFilter( "HLTEventNumberFilter",
    period = cms.uint32( 4096 ),
    invert = cms.bool( True )
)
process.hltGtDigis = cms.EDProducer( "L1GlobalTriggerRawToDigi",
    DaqGtInputTag = cms.InputTag( "rawDataCollector" ),
    DaqGtFedId = cms.untracked.int32( 813 ),
    ActiveBoardsMask = cms.uint32( 0xffff ),
    UnpackBxInEvent = cms.int32( 1 )
)
process.hltGctDigis = cms.EDProducer( "GctRawToDigi",
    inputLabel = cms.InputTag( "rawDataCollector" ),
    gctFedId = cms.int32( 745 ),
    hltMode = cms.bool( True ),
    unpackSharedRegions = cms.bool( False ),
    unpackerVersion = cms.uint32( 0 )
)
process.hltL1GtObjectMap = cms.EDProducer( "L1GlobalTrigger",
    GmtInputTag = cms.InputTag( "hltGtDigis" ),
    GctInputTag = cms.InputTag( "hltGctDigis" ),
    CastorInputTag = cms.InputTag( "castorL1Digis" ),
    ProduceL1GtDaqRecord = cms.bool( False ),
    ProduceL1GtEvmRecord = cms.bool( False ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    WritePsbL1GtDaqRecord = cms.bool( False ),
    ReadTechnicalTriggerRecords = cms.bool( True ),
    EmulateBxInEvent = cms.int32( 1 ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    AlternativeNrBxBoardEvm = cms.uint32( 0 ),
    BstLengthBytes = cms.int32( -1 ),
    TechnicalTriggersInputTags = cms.VInputTag( 'simBscDigis' ),
    RecordLength = cms.vint32( 3, 0 )
)
process.hltL1extraParticles = cms.EDProducer( "L1ExtraParticlesProd",
    produceMuonParticles = cms.bool( True ),
    muonSource = cms.InputTag( "hltGtDigis" ),
    produceCaloParticles = cms.bool( True ),
    isolatedEmSource = cms.InputTag( 'hltGctDigis','isoEm' ),
    nonIsolatedEmSource = cms.InputTag( 'hltGctDigis','nonIsoEm' ),
    centralJetSource = cms.InputTag( 'hltGctDigis','cenJets' ),
    forwardJetSource = cms.InputTag( 'hltGctDigis','forJets' ),
    tauJetSource = cms.InputTag( 'hltGctDigis','tauJets' ),
    etTotalSource = cms.InputTag( "hltGctDigis" ),
    etHadSource = cms.InputTag( "hltGctDigis" ),
    etMissSource = cms.InputTag( "hltGctDigis" ),
    htMissSource = cms.InputTag( "hltGctDigis" ),
    hfRingEtSumsSource = cms.InputTag( "hltGctDigis" ),
    hfRingBitCountsSource = cms.InputTag( "hltGctDigis" ),
    centralBxOnly = cms.bool( True ),
    ignoreHtMiss = cms.bool( False )
)
process.hltOfflineBeamSpot = cms.EDProducer( "BeamSpotProducer" )
process.hltPreFirstPath = cms.EDFilter( "HLTPrescaler" )
process.hltBoolFirstPath = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
process.hltHIL1sJet50U = cms.EDFilter( "HLTLevel1GTSeed",
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet15" ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" )
)
process.hltHIPreJet50U = cms.EDFilter( "HLTPrescaler" )
process.hltEcalRawToRecHitFacility = cms.EDProducer( "EcalRawToRecHitFacility",
    sourceTag = cms.InputTag( "rawDataCollector" ),
    workerName = cms.string( "" )
)
process.hltEcalRegionalRestFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
    sourceTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
    type = cms.string( "all" ),
    doES = cms.bool( False ),
    sourceTag_es = cms.InputTag( "NotNeededoESfalse" ),
    MuJobPSet = cms.PSet(  ),
    JetJobPSet = cms.VPSet( 
    ),
    EmJobPSet = cms.VPSet( 
    ),
    CandJobPSet = cms.VPSet( 
    )
)
process.hltEcalRecHitAll = cms.EDProducer( "EcalRawToRecHitProducer",
    lazyGetterTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
    sourceTag = cms.InputTag( "hltEcalRegionalRestFEDs" ),
    splitOutput = cms.bool( True ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    rechitCollection = cms.string( "NotNeededsplitOutputTrue" )
)
process.hltHcalDigis = cms.EDProducer( "HcalRawToDigi",
    InputLabel = cms.InputTag( "rawDataCollector" ),
    UnpackCalib = cms.untracked.bool( True ),
    UnpackZDC = cms.untracked.bool( True ),
    firstSample = cms.int32( 0 ),
    lastSample = cms.int32( 9 ),
    FilterDataQuality = cms.bool( True )
)
process.hltHbhereco = cms.EDProducer( "HcalSimpleReconstructor",
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    dropZSmarkedPassed = cms.bool( True ),
    Subdetector = cms.string( "HBHE" ),
    firstSample = cms.int32( 4 ),
    samplesToAdd = cms.int32( 4 ),
    correctForTimeslew = cms.bool( True ),
    correctForPhaseContainment = cms.bool( True ),
    correctionPhaseNS = cms.double( 13.0 )
)
process.hltHfreco = cms.EDProducer( "HcalSimpleReconstructor",
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    dropZSmarkedPassed = cms.bool( True ),
    Subdetector = cms.string( "HF" ),
    firstSample = cms.int32( 3 ),
    samplesToAdd = cms.int32( 1 ),
    correctForTimeslew = cms.bool( False ),
    correctForPhaseContainment = cms.bool( False ),
    correctionPhaseNS = cms.double( 0.0 )
)
process.hltHoreco = cms.EDProducer( "HcalSimpleReconstructor",
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    dropZSmarkedPassed = cms.bool( True ),
    Subdetector = cms.string( "HO" ),
    firstSample = cms.int32( 4 ),
    samplesToAdd = cms.int32( 4 ),
    correctForTimeslew = cms.bool( True ),
    correctForPhaseContainment = cms.bool( True ),
    correctionPhaseNS = cms.double( 13.0 )
)
process.hltTowerMakerForAll = cms.EDProducer( "CaloTowersCreator",
    EBThreshold = cms.double( 0.09 ),
    EEThreshold = cms.double( 0.45 ),
    UseEtEBTreshold = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    UseSymEBTreshold = cms.bool( False ),
    UseSymEETreshold = cms.bool( False ),
    HcalThreshold = cms.double( -1000.0 ),
    HBThreshold = cms.double( 0.9 ),
    HESThreshold = cms.double( 1.4 ),
    HEDThreshold = cms.double( 1.4 ),
    HOThreshold0 = cms.double( 1.1 ),
    HOThresholdPlus1 = cms.double( 1.1 ),
    HOThresholdMinus1 = cms.double( 1.1 ),
    HOThresholdPlus2 = cms.double( 1.1 ),
    HOThresholdMinus2 = cms.double( 1.1 ),
    HF1Threshold = cms.double( 1.2 ),
    HF2Threshold = cms.double( 1.8 ),
    EBWeight = cms.double( 1.0 ),
    EEWeight = cms.double( 1.0 ),
    HBWeight = cms.double( 1.0 ),
    HESWeight = cms.double( 1.0 ),
    HEDWeight = cms.double( 1.0 ),
    HOWeight = cms.double( 1.0E-99 ),
    HF1Weight = cms.double( 1.0 ),
    HF2Weight = cms.double( 1.0 ),
    EcutTower = cms.double( -1000.0 ),
    EBSumThreshold = cms.double( 0.2 ),
    EESumThreshold = cms.double( 0.45 ),
    UseHO = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHBDepth = cms.double( 0.2 ),
    MomHEDepth = cms.double( 0.4 ),
    MomEBDepth = cms.double( 0.3 ),
    MomEEDepth = cms.double( 0.0 ),
    hbheInput = cms.InputTag( "hltHbhereco" ),
    hoInput = cms.InputTag( "hltHoreco" ),
    hfInput = cms.InputTag( "hltHfreco" ),
    AllowMissingInputs = cms.bool( False ),
    HcalAcceptSeverityLevel = cms.uint32( 999 ),
    EcalAcceptSeverityLevel = cms.uint32( 1 ),
    UseHcalRecoveredHits = cms.bool( True ),
    UseEcalRecoveredHits = cms.bool( True ),
    EBGrid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    EEWeights = cms.vdouble(  ),
    HBGrid = cms.vdouble(  ),
    HBWeights = cms.vdouble(  ),
    HESGrid = cms.vdouble(  ),
    HESWeights = cms.vdouble(  ),
    HEDGrid = cms.vdouble(  ),
    HEDWeights = cms.vdouble(  ),
    HOGrid = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    HF1Grid = cms.vdouble(  ),
    HF1Weights = cms.vdouble(  ),
    HF2Grid = cms.vdouble(  ),
    HF2Weights = cms.vdouble(  ),
    ecalInputs = cms.VInputTag( 'hltEcalRecHitAll:EcalRecHitsEB','hltEcalRecHitAll:EcalRecHitsEE' )
)
process.hltIterativeCone5PileupSubtractionCaloJets = cms.EDProducer( "IterativeConePilupSubtractionJetProducer",
    seedThreshold = cms.double( 1.0 ),
    coneRadius = cms.double( 0.5 ),
    src = cms.InputTag( "hltTowerMakerForAll" ),
    verbose = cms.untracked.bool( False ),
    inputEtMin = cms.double( 0.5 ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    alias = cms.untracked.string( "IC5PUCaloJet" ),
    debugLevel = cms.untracked.int32( 0 ),
    jetType = cms.untracked.string( "CaloJetPileupSubtraction" ),
    inputEMin = cms.double( 0.0 ),
    inputEtJetMin = cms.double( 10.0 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    jetPtMin = cms.double( 0.0 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 )
)
process.hltMCJetCorJetIcone5PU = cms.EDProducer( "CaloJetCorrectionProducer",
    src = cms.InputTag( "hltIterativeCone5PileupSubtractionCaloJets" ),
    verbose = cms.untracked.bool( False ),
    alias = cms.untracked.string( "MCJetCorJetIcone5PU" ),
    correctors = cms.vstring( 'MCJetCorrectorIcone5' )
)
process.hltHI1jet50U = cms.EDFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( "hltIterativeCone5PileupSubtractionCaloJets" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 50.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
process.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)
process.hltHIL1sJet75U = cms.EDFilter( "HLTLevel1GTSeed",
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet15" ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" )
)
process.hltHIPreJet75U = cms.EDFilter( "HLTPrescaler" )
process.hltHI1jet75U = cms.EDFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( "hltIterativeCone5PileupSubtractionCaloJets" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 75.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
process.hltHIL1sJet90U = cms.EDFilter( "HLTLevel1GTSeed",
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet15" ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" )
)
process.hltHIPreJet90U = cms.EDFilter( "HLTPrescaler" )
process.hltHI1jet90U = cms.EDFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( "hltIterativeCone5PileupSubtractionCaloJets" ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 90.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
process.hltHIL1sPhoton10 = cms.EDFilter( "HLTLevel1GTSeed",
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG5" ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" )
)
process.hltHIPrePhoton10 = cms.EDFilter( "HLTPrescaler" )
process.hltIslandBasicClustersHI = cms.EDProducer( "IslandClusterProducer",
    VerbosityLevel = cms.string( "ERROR" ),
    barrelHitProducer = cms.string( "hltEcalRecHitAll" ),
    endcapHitProducer = cms.string( "hltEcalRecHitAll" ),
    barrelHitCollection = cms.string( "EcalRecHitsEB" ),
    endcapHitCollection = cms.string( "EcalRecHitsEE" ),
    barrelClusterCollection = cms.string( "islandBarrelBasicClustersHI" ),
    endcapClusterCollection = cms.string( "islandEndcapBasicClustersHI" ),
    IslandBarrelSeedThr = cms.double( 0.5 ),
    IslandEndcapSeedThr = cms.double( 0.18 ),
    posCalc_logweight = cms.bool( True ),
    posCalc_t0_barl = cms.double( 7.4 ),
    posCalc_t0_endc = cms.double( 3.1 ),
    posCalc_t0_endcPresh = cms.double( 1.2 ),
    posCalc_w0 = cms.double( 4.2 ),
    posCalc_x0 = cms.double( 0.89 ),
    clustershapecollectionEB = cms.string( "islandBarrelShape" ),
    clustershapecollectionEE = cms.string( "islandEndcapShape" ),
    barrelShapeAssociation = cms.string( "islandBarrelShapeAssoc" ),
    endcapShapeAssociation = cms.string( "islandEndcapShapeAssoc" )
)
process.hltIslandSuperClustersHI = cms.EDProducer( "SuperClusterProducer",
    VerbosityLevel = cms.string( "ERROR" ),
    endcapClusterProducer = cms.string( "hltIslandBasicClustersHI" ),
    barrelClusterProducer = cms.string( "hltIslandBasicClustersHI" ),
    endcapClusterCollection = cms.string( "islandEndcapBasicClustersHI" ),
    barrelClusterCollection = cms.string( "islandBarrelBasicClustersHI" ),
    endcapSuperclusterCollection = cms.string( "islandEndcapSuperClustersHI" ),
    barrelSuperclusterCollection = cms.string( "islandBarrelSuperClustersHI" ),
    doBarrel = cms.bool( True ),
    doEndcaps = cms.bool( True ),
    barrelEtaSearchRoad = cms.double( 0.06 ),
    barrelPhiSearchRoad = cms.double( 0.8 ),
    endcapEtaSearchRoad = cms.double( 0.14 ),
    endcapPhiSearchRoad = cms.double( 0.6 ),
    seedTransverseEnergyThreshold = cms.double( 1.0 )
)
process.hltCorrectedIslandBarrelSuperClustersHI = cms.EDProducer( "EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEB' ),
    rawSuperClusterProducer = cms.InputTag( 'hltIslandSuperClustersHI','islandBarrelSuperClustersHI' ),
    superClusterAlgo = cms.string( "Island" ),
    applyEnergyCorrection = cms.bool( True ),
    sigmaElectronicNoise = cms.double( 0.03 ),
    etThresh = cms.double( 0.0 ),
    corectedSuperClusterCollection = cms.string( "" ),
    hyb_fCorrPset = cms.PSet(  ),
    isl_fCorrPset = cms.PSet( 
      brLinearLowThr = cms.double( 0.0 ),
      fEtEtaVec = cms.vdouble( 0.0 ),
      brLinearHighThr = cms.double( 0.0 ),
      fBremVec = cms.vdouble( 0.0 )
    ),
    dyn_fCorrPset = cms.PSet(  ),
    fix_fCorrPset = cms.PSet(  )
)
process.hltCorrectedIslandEndcapSuperClustersHI = cms.EDProducer( "EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRecHitAll','EcalRecHitsEE' ),
    rawSuperClusterProducer = cms.InputTag( 'hltIslandSuperClustersHI','islandEndcapSuperClustersHI' ),
    superClusterAlgo = cms.string( "Island" ),
    applyEnergyCorrection = cms.bool( True ),
    sigmaElectronicNoise = cms.double( 0.15 ),
    etThresh = cms.double( 0.0 ),
    corectedSuperClusterCollection = cms.string( "" ),
    hyb_fCorrPset = cms.PSet(  ),
    isl_fCorrPset = cms.PSet( 
      brLinearLowThr = cms.double( 0.0 ),
      fEtEtaVec = cms.vdouble( 0.0 ),
      brLinearHighThr = cms.double( 0.0 ),
      fBremVec = cms.vdouble( 0.0 )
    ),
    dyn_fCorrPset = cms.PSet(  ),
    fix_fCorrPset = cms.PSet(  )
)
process.hltRecoHIEcalCandidate = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scHybridBarrelProducer = cms.InputTag( "hltCorrectedIslandBarrelSuperClustersHI" ),
    scIslandEndcapProducer = cms.InputTag( "hltCorrectedIslandEndcapSuperClustersHI" ),
    recoEcalCandidateCollection = cms.string( "" )
)
process.hltHIPhoton10 = cms.EDFilter( "HLT1Photon",
    inputTag = cms.InputTag( "hltRecoHIEcalCandidate" ),
    MinPt = cms.double( 10.0 ),
    MaxEta = cms.double( 1.479 ),
    MinN = cms.int32( 1 )
)
process.hltHIL1sPhoton20 = cms.EDFilter( "HLTLevel1GTSeed",
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG5" ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" )
)
process.hltHIPrePhoton20 = cms.EDFilter( "HLTPrescaler" )
process.hltHIPhoton20 = cms.EDFilter( "HLT1Photon",
    inputTag = cms.InputTag( "hltRecoHIEcalCandidate" ),
    MinPt = cms.double( 20.0 ),
    MaxEta = cms.double( 1.479 ),
    MinN = cms.int32( 1 )
)
process.hltHIL1sPhoton30 = cms.EDFilter( "HLTLevel1GTSeed",
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG5" ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" )
)
process.hltHIPrePhoton30 = cms.EDFilter( "HLTPrescaler" )
process.hltHIPhoton30 = cms.EDFilter( "HLT1Photon",
    inputTag = cms.InputTag( "hltRecoHIEcalCandidate" ),
    MinPt = cms.double( 30.0 ),
    MaxEta = cms.double( 1.479 ),
    MinN = cms.int32( 1 )
)
process.hltHIPreMML1 = cms.EDFilter( "HLTPrescaler" )
process.hltHIMML1Seed = cms.EDFilter( "HLTLevel1GTSeed",
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMuOpen" ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" )
)
process.hltMuonDTDigis = cms.EDProducer( "DTUnpackingModule",
    dataType = cms.string( "DDU" ),
    fedbyType = cms.untracked.bool( False ),
    inputLabel = cms.untracked.InputTag( "rawDataCollector" ),
    readOutParameters = cms.PSet( 
      localDAQ = cms.untracked.bool( False ),
      performDataIntegrityMonitor = cms.untracked.bool( False ),
      debug = cms.untracked.bool( False ),
      rosParameters = cms.PSet( 
        localDAQ = cms.untracked.bool( False ),
        readingDDU = cms.untracked.bool( True ),
        writeSC = cms.untracked.bool( True ),
        readDDUIDfromDDU = cms.untracked.bool( True ),
        performDataIntegrityMonitor = cms.untracked.bool( False ),
        debug = cms.untracked.bool( False )
      )
    )
)
process.hltDt1DRecHits = cms.EDProducer( "DTRecHitProducer",
    debug = cms.untracked.bool( False ),
    dtDigiLabel = cms.InputTag( "hltMuonDTDigis" ),
    recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
    recAlgoConfig = cms.PSet( 
      tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
      tTrigModeConfig = cms.PSet( 
        debug = cms.untracked.bool( False ),
        vPropWire = cms.double( 24.4 ),
        doT0Correction = cms.bool( True ),
        doTOFCorrection = cms.bool( True ),
        tofCorrType = cms.int32( 1 ),
        doWirePropCorrection = cms.bool( True ),
        wirePropCorrType = cms.int32( 1 )
      ),
      minTime = cms.double( -3.0 ),
      maxTime = cms.double( 420.0 ),
      debug = cms.untracked.bool( False )
    )
)
process.hltDt4DSegments = cms.EDProducer( "DTRecSegment4DProducer",
    debug = cms.untracked.bool( False ),
    recHits1DLabel = cms.InputTag( "hltDt1DRecHits" ),
    recHits2DLabel = cms.InputTag( "dt2DSegments" ),
    Reco4DAlgoName = cms.string( "DTCombinatorialPatternReco4D" ),
    Reco4DAlgoConfig = cms.PSet( 
      Reco2DAlgoConfig = cms.PSet( 
        recAlgoConfig = cms.PSet( 
          tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
          tTrigModeConfig = cms.PSet( 
            debug = cms.untracked.bool( False ),
            vPropWire = cms.double( 24.4 ),
            doT0Correction = cms.bool( True ),
            doTOFCorrection = cms.bool( True ),
            tofCorrType = cms.int32( 1 ),
            doWirePropCorrection = cms.bool( True ),
            wirePropCorrType = cms.int32( 1 )
          ),
          minTime = cms.double( -3.0 ),
          maxTime = cms.double( 420.0 ),
          debug = cms.untracked.bool( False )
        ),
        recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
        MaxAllowedHits = cms.uint32( 50 ),
        AlphaMaxTheta = cms.double( 0.1 ),
        AlphaMaxPhi = cms.double( 1.0 ),
        debug = cms.untracked.bool( False ),
        nSharedHitsMax = cms.int32( 2 ),
        nUnSharedHitsMin = cms.int32( 2 ),
        segmCleanerMode = cms.int32( 1 ),
        performT0SegCorrection = cms.bool( False ),
        performT0_vdriftSegCorrection = cms.bool( False ),
        hit_afterT0_resolution = cms.double( 0.03 )
      ),
      Reco2DAlgoName = cms.string( "DTCombinatorialPatternReco" ),
      recAlgoConfig = cms.PSet( 
        tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
        tTrigModeConfig = cms.PSet( 
          debug = cms.untracked.bool( False ),
          vPropWire = cms.double( 24.4 ),
          doT0Correction = cms.bool( True ),
          doTOFCorrection = cms.bool( True ),
          tofCorrType = cms.int32( 1 ),
          doWirePropCorrection = cms.bool( True ),
          wirePropCorrType = cms.int32( 1 )
        ),
        minTime = cms.double( -3.0 ),
        maxTime = cms.double( 420.0 ),
        debug = cms.untracked.bool( False )
      ),
      recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
      AllDTRecHits = cms.bool( True ),
      debug = cms.untracked.bool( False ),
      nSharedHitsMax = cms.int32( 2 ),
      nUnSharedHitsMin = cms.int32( 2 ),
      segmCleanerMode = cms.int32( 1 ),
      performT0SegCorrection = cms.bool( False ),
      performT0_vdriftSegCorrection = cms.bool( False ),
      hit_afterT0_resolution = cms.double( 0.03 )
    )
)
process.hltMuonCSCDigis = cms.EDProducer( "CSCDCCUnpacker",
    InputObjects = cms.InputTag( "rawDataCollector" ),
    UseExaminer = cms.bool( True ),
    ExaminerMask = cms.uint32( 0x1febf3f6 ),
    UseSelectiveUnpacking = cms.bool( True ),
    ErrorMask = cms.uint32( 0x0 ),
    UnpackStatusDigis = cms.bool( False ),
    UseFormatStatus = cms.bool( True ),
    PrintEventNumber = cms.untracked.bool( False )
)
process.hltCsc2DRecHits = cms.EDProducer( "CSCRecHitDProducer",
    CSCUseCalibrations = cms.bool( True ),
    stripDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCStripDigi' ),
    wireDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCWireDigi' ),
    CSCstripWireDeltaTime = cms.int32( 8 ),
    CSCUseStaticPedestals = cms.bool( False ),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32( 2 ),
    CSCStripPeakThreshold = cms.double( 10.0 ),
    CSCStripClusterChargeCut = cms.double( 25.0 ),
    CSCWireClusterDeltaT = cms.int32( 1 ),
    CSCStripxtalksOffset = cms.double( 0.03 ),
    NoiseLevel_ME1a = cms.double( 7.0 ),
    XTasymmetry_ME1a = cms.double( 0.0 ),
    ConstSyst_ME1a = cms.double( 0.022 ),
    NoiseLevel_ME1b = cms.double( 8.0 ),
    XTasymmetry_ME1b = cms.double( 0.0 ),
    ConstSyst_ME1b = cms.double( 0.0070 ),
    NoiseLevel_ME12 = cms.double( 9.0 ),
    XTasymmetry_ME12 = cms.double( 0.0 ),
    ConstSyst_ME12 = cms.double( 0.0 ),
    NoiseLevel_ME13 = cms.double( 8.0 ),
    XTasymmetry_ME13 = cms.double( 0.0 ),
    ConstSyst_ME13 = cms.double( 0.0 ),
    NoiseLevel_ME21 = cms.double( 9.0 ),
    XTasymmetry_ME21 = cms.double( 0.0 ),
    ConstSyst_ME21 = cms.double( 0.0 ),
    NoiseLevel_ME22 = cms.double( 9.0 ),
    XTasymmetry_ME22 = cms.double( 0.0 ),
    ConstSyst_ME22 = cms.double( 0.0 ),
    NoiseLevel_ME31 = cms.double( 9.0 ),
    XTasymmetry_ME31 = cms.double( 0.0 ),
    ConstSyst_ME31 = cms.double( 0.0 ),
    NoiseLevel_ME32 = cms.double( 9.0 ),
    XTasymmetry_ME32 = cms.double( 0.0 ),
    ConstSyst_ME32 = cms.double( 0.0 ),
    NoiseLevel_ME41 = cms.double( 9.0 ),
    XTasymmetry_ME41 = cms.double( 0.0 ),
    ConstSyst_ME41 = cms.double( 0.0 ),
    readBadChannels = cms.bool( False ),
    readBadChambers = cms.bool( False ),
    UseAverageTime = cms.bool( False ),
    UseParabolaFit = cms.bool( False ),
    UseFourPoleFit = cms.bool( True ),
    UseFivePoleFit = cms.bool( True )
)
process.hltCscSegments = cms.EDProducer( "CSCSegmentProducer",
    inputObjects = cms.InputTag( "hltCsc2DRecHits" ),
    algo_type = cms.int32( 1 ),
    algo_psets = cms.VPSet( 
      cms.PSet(  chamber_types = cms.vstring( 'ME1/a',
  'ME1/b',
  'ME1/2',
  'ME1/3',
  'ME2/1',
  'ME2/2',
  'ME3/1',
  'ME3/2',
  'ME4/1',
  'ME4/2' ),
        algo_name = cms.string( "CSCSegAlgoST" ),
        parameters_per_chamber_type = cms.vint32( 2, 1, 1, 1, 1, 1, 1, 1, 1, 1 ),
        algo_psets = cms.VPSet( 
          cms.PSet(  maxRatioResidualPrune = cms.double( 3.0 ),
            yweightPenalty = cms.double( 1.5 ),
            maxRecHitsInCluster = cms.int32( 20 ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            BPMinImprovement = cms.double( 10000.0 ),
            tanPhiMax = cms.double( 0.5 ),
            onlyBestSegment = cms.bool( False ),
            dRPhiFineMax = cms.double( 8.0 ),
            curvePenalty = cms.double( 2.0 ),
            dXclusBoxMax = cms.double( 4.0 ),
            BrutePruning = cms.bool( True ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            useShowering = cms.bool( False ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            minHitsPerSegment = cms.int32( 3 ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            dPhiFineMax = cms.double( 0.025 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            preClustering = cms.bool( True ),
            maxDPhi = cms.double( 999.0 ),
            maxDTheta = cms.double( 999.0 ),
            Pruning = cms.bool( True ),
            dYclusBoxMax = cms.double( 8.0 )
          ),
          cms.PSet(  maxRatioResidualPrune = cms.double( 3.0 ),
            yweightPenalty = cms.double( 1.5 ),
            maxRecHitsInCluster = cms.int32( 24 ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            BPMinImprovement = cms.double( 10000.0 ),
            tanPhiMax = cms.double( 0.5 ),
            onlyBestSegment = cms.bool( False ),
            dRPhiFineMax = cms.double( 8.0 ),
            curvePenalty = cms.double( 2.0 ),
            dXclusBoxMax = cms.double( 4.0 ),
            BrutePruning = cms.bool( True ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            useShowering = cms.bool( False ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            minHitsPerSegment = cms.int32( 3 ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            dPhiFineMax = cms.double( 0.025 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            preClustering = cms.bool( True ),
            maxDPhi = cms.double( 999.0 ),
            maxDTheta = cms.double( 999.0 ),
            Pruning = cms.bool( True ),
            dYclusBoxMax = cms.double( 8.0 )
          )
        )
      )
    )
)
process.hltMuonRPCDigis = cms.EDProducer( "RPCUnpackingModule",
    InputLabel = cms.InputTag( "rawDataCollector" ),
    doSynchro = cms.bool( False )
)
process.hltRpcRecHits = cms.EDProducer( "RPCRecHitProducer",
    rpcDigiLabel = cms.InputTag( "hltMuonRPCDigis" ),
    recAlgo = cms.string( "RPCRecHitStandardAlgo" ),
    maskSource = cms.string( "File" ),
    maskvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat" ),
    deadSource = cms.string( "File" ),
    deadvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat" ),
    recAlgoConfig = cms.PSet(  )
)
process.hltL2MuonSeeds = cms.EDProducer( "L2MuonSeedGenerator",
    InputObjects = cms.InputTag( "hltL1extraParticles" ),
    GMTReadoutCollection = cms.InputTag( "hltGtDigis" ),
    Propagator = cms.string( "SteppingHelixPropagatorAny" ),
    L1MinPt = cms.double( 0.0 ),
    L1MaxEta = cms.double( 2.5 ),
    L1MinQuality = cms.uint32( 1 ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'SteppingHelixPropagatorAny' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    )
)
process.hltL2Muons = cms.EDProducer( "L2MuonProducer",
    InputObjects = cms.InputTag( "hltL2MuonSeeds" ),
    L2TrajBuilderParameters = cms.PSet( 
      RefitterParameters = cms.PSet( 
        FitterName = cms.string( "KFFitterSmootherForL2Muon" ),
        NumberOfIterations = cms.uint32( 3 ),
        ForceAllIterations = cms.bool( False ),
        MaxFractionOfLostHits = cms.double( 0.05 ),
        RescaleError = cms.double( 100.0 )
      ),
      DoRefit = cms.bool( True ),
      SeedPropagator = cms.string( "FastSteppingHelixPropagatorAny" ),
      NavigationType = cms.string( "Standard" ),
      SeedTransformerParameters = cms.PSet( 
        Fitter = cms.string( "KFFitterSmootherForL2Muon" ),
        RescaleError = cms.double( 100.0 ),
        MuonRecHitBuilder = cms.string( "MuonRecHitBuilder" ),
        Propagator = cms.string( "FastSteppingHelixPropagatorAny" ),
        NMinRecHits = cms.uint32( 2 )
      ),
      DoBackwardFilter = cms.bool( True ),
      SeedPosition = cms.string( "in" ),
      BWFilterParameters = cms.PSet( 
        NumberOfSigma = cms.double( 3.0 ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        FitDirection = cms.string( "outsideIn" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        MaxChi2 = cms.double( 100.0 ),
        MuonTrajectoryUpdatorParameters = cms.PSet( 
          MaxChi2 = cms.double( 25.0 ),
          Granularity = cms.int32( 2 ),
          RescaleErrorFactor = cms.double( 100.0 ),
          RescaleError = cms.bool( False ),
          UseInvalidHits = cms.bool( True )
        ),
        EnableRPCMeasurement = cms.bool( True ),
        BWSeedType = cms.string( "fromGenerator" ),
        EnableDTMeasurement = cms.bool( True ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        EnableCSCMeasurement = cms.bool( True ),
        Propagator = cms.string( "FastSteppingHelixPropagatorAny" )
      ),
      DoSeedRefit = cms.bool( False ),
      FilterParameters = cms.PSet( 
        NumberOfSigma = cms.double( 3.0 ),
        FitDirection = cms.string( "insideOut" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        MaxChi2 = cms.double( 1000.0 ),
        MuonTrajectoryUpdatorParameters = cms.PSet( 
          MaxChi2 = cms.double( 25.0 ),
          Granularity = cms.int32( 0 ),
          RescaleErrorFactor = cms.double( 100.0 ),
          RescaleError = cms.bool( False ),
          UseInvalidHits = cms.bool( True )
        ),
        EnableRPCMeasurement = cms.bool( True ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        EnableDTMeasurement = cms.bool( True ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        EnableCSCMeasurement = cms.bool( True ),
        Propagator = cms.string( "FastSteppingHelixPropagatorAny" )
      )
    ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'FastSteppingHelixPropagatorAny',
        'FastSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    TrackLoaderParameters = cms.PSet( 
      Smoother = cms.string( "KFSmootherForMuonTrackLoader" ),
      DoSmoothing = cms.bool( False ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPosition = cms.vdouble( 0.0, 0.0, 0.0 ),
        Propagator = cms.string( "FastSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( True )
    )
)
process.hltL2MuonCandidates = cms.EDProducer( "L2MuonCandidateProducer",
    InputObjects = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
process.hltSiPixelDigis = cms.EDProducer( "SiPixelRawToDigi",
    IncludeErrors = cms.bool( False ),
    CheckPixelOrder = cms.bool( False ),
    InputLabel = cms.InputTag( "rawDataCollector" )
)
process.hltSiPixelClusters = cms.EDProducer( "SiPixelClusterProducer",
    src = cms.InputTag( "hltSiPixelDigis" ),
    payloadType = cms.string( "HLT" ),
    ChannelThreshold = cms.int32( 1000 ),
    SeedThreshold = cms.int32( 1000 ),
    ClusterThreshold = cms.double( 3000.0 ),
    VCaltoElectronGain = cms.int32( 65 ),
    VCaltoElectronOffset = cms.int32( -414 ),
    MissCalibrate = cms.untracked.bool( True ),
    SplitClusters = cms.bool( False )
)
process.hltSiPixelRecHits = cms.EDProducer( "SiPixelRecHitConverter",
    src = cms.InputTag( "hltSiPixelClusters" ),
    CPE = cms.string( "PixelCPEGeneric" )
)
process.hltHIPixelTracks = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( False ),
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "HITrackingRegionProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originHalfLength = cms.double( 15.9 ),
        directionYCoord = cms.double( 1.0 ),
        originYPos = cms.double( 0.0 ),
        directionXCoord = cms.double( 1.0 ),
        directionZCoord = cms.double( 0.0 ),
        VertexCollection = cms.string( "hltHIPixelVertices" ),
        ptMin = cms.double( 0.5 ),
        originXPos = cms.double( 0.0 ),
        siPixelRecHits = cms.string( "hltSiPixelRecHits" ),
        originZPos = cms.double( 0.0 ),
        useFoundVertices = cms.bool( False ),
        originRadius = cms.double( 0.1 )
      )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet( 
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.06 ),
        useMultScattering = cms.bool( True ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" ),
        extraHitRZtolerance = cms.double( 0.06 )
      ),
      SeedingLayers = cms.string( "PixelLayerTriplets" )
    ),
    FitterPSet = cms.PSet( 
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" )
    ),
    FilterPSet = cms.PSet( 
      chi2 = cms.double( 1000.0 ),
      nSigmaTipMaxTolerance = cms.double( 0.0 ),
      ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
      nSigmaInvPtTolerance = cms.double( 0.0 ),
      ptMin = cms.double( 0.1 ),
      tipMax = cms.double( 1.0 )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "PixelTrackCleanerBySharedHits" ) )
)
process.hltHIPixelVertices = cms.EDProducer( "PixelVertexProducerMedian",
    TrackCollection = cms.string( "hltHIPixelTracks" ),
    PtMin = cms.double( 0.5 )
)
process.hltSiStripRawToClustersFacility = cms.EDProducer( "SiStripRawToClusters",
    ProductLabel = cms.InputTag( "rawDataCollector" ),
    Clusterizer = cms.PSet( 
      Algorithm = cms.string( "ThreeThresholdAlgorithm" ),
      ChannelThreshold = cms.double( 2.0 ),
      SeedThreshold = cms.double( 3.0 ),
      ClusterThreshold = cms.double( 5.0 ),
      MaxSequentialHoles = cms.uint32( 0 ),
      MaxSequentialBad = cms.uint32( 1 ),
      MaxAdjacentBad = cms.uint32( 0 ),
      QualityLabel = cms.string( "" )
    ),
    Algorithms = cms.PSet( 
      SiStripFedZeroSuppressionMode = cms.uint32( 4 ),
      CommonModeNoiseSubtractionMode = cms.string( "Median" )
    )
)
process.hltSiStripClusters = cms.EDProducer( "MeasurementTrackerSiStripRefGetterProducer",
    InputModuleLabel = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    measurementTrackerName = cms.string( "" )
)
process.hltHIMML3Filter = cms.EDFilter( "TestMuL1L2Filter",
    PrimaryVertexTag = cms.InputTag( "hltHIPixelVertices" ),
    NavigationPSet = cms.PSet(  ComponentName = cms.string( "SimpleNavigationSchool" ) ),
    L2CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    rphiRecHits = cms.InputTag( 'siStripMatchedRecHits','rphiRecHit' ),
    TTRHBuilder = cms.string( "HITTRHBuilderWithoutRefit" )
)
process.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    processName = cms.string( "@" )
)
process.hltPreTriggerSummaryRAW = cms.EDFilter( "HLTPrescaler" )
process.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)
process.hltBoolFinalPath = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
process.hltL1GtTrigReport = cms.EDAnalyzer( "L1GtTrigReport",
    UseL1GlobalTriggerRecord = cms.bool( False ),
    L1GtRecordInputTag = cms.InputTag( "hltGtDigis" )
)
process.hltTrigReport = cms.EDAnalyzer( "HLTrigReport",
    HLTriggerResults = cms.InputTag( 'TriggerResults','','HLT' )
)
process.hltDefaultOutput = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "file:HLTDefaultOutput.root" ),
    compressionLevel = cms.untracked.int32( 1 ),
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_HIDoubleMu',
  'HLT_HIJet50U',
  'HLT_HIJet75U',
  'HLT_HIJet90U',
  'HLT_HIPhoton10',
  'HLT_HIPhoton20',
  'HLT_HIPhoton30',
  'HLTriggerFinalPath',
  'HLTriggerFirstPath' ) ),
    outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*',
      'keep *_hltL1GtObjectMap_*_*' )
)
process.hltDefaultOutputWithFEDs = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "file:HLTDefaultOutputWithFEDs.root" ),
    compressionLevel = cms.untracked.int32( 1 ),
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_HIDoubleMu',
  'HLT_HIJet50U',
  'HLT_HIJet75U',
  'HLT_HIJet90U',
  'HLT_HIPhoton10',
  'HLT_HIPhoton20',
  'HLT_HIPhoton30',
  'HLTriggerFinalPath',
  'HLTriggerFirstPath' ) ),
    outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*',
      'keep *_hltL1GtObjectMap_*_*' )
)
process.hltPreDebugOutput = cms.EDFilter( "HLTPrescaler" )
process.hltDebugOutput = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "file:HLTDebugOutput.root" ),
    compressionLevel = cms.untracked.int32( 1 ),
    basketSize = cms.untracked.int32( 4096 ),
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_HIDoubleMu',
  'HLT_HIJet50U',
  'HLT_HIJet75U',
  'HLT_HIJet90U',
  'HLT_HIPhoton10',
  'HLT_HIPhoton20',
  'HLT_HIPhoton30',
  'HLTriggerFinalPath',
  'HLTriggerFirstPath' ) ),
    dataset = cms.untracked.PSet(  dataTier = cms.untracked.string( "RECO" ) ),
    outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*',
      'keep triggerTriggerEventWithRefs_*_*_*',
      'keep *_hltTowerMakerForAll_*_*',
      'keep *_hltCtfL1IsoWithMaterialTracks_*_*',
      'keep *_hltMuonTauIsoL3IsoFiltered_*_*',
      'keep *_hltElectronL1NonIsoLargeWindowDetaDphi_*_*',
      'keep *_hltBLifetimeL3BJetTagsStartup_*_*',
      'keep *_hltL1NonIsoLargeWindowElectronPixelSeeds_*_*',
      'keep *_hltL1NonIsolatedPhotonEcalIsol_*_*',
      'keep *_hltRpcRecHits_*_*',
      'keep *_hltL1HLTDoubleLooseIsoTau15JetsMatch_*_*',
      'keep *_hltL3TkTracksOIFromL2_*_*',
      'keep *_hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated_*_*',
      'keep *_hltBSoftMuonL3BJetTagsUByPt_*_*',
      'keep *_hltPixelVertices_*_*',
      'keep *_hltBLifetimeRegionalCtfWithMaterialTracksStartup_*_*',
      'keep *_hltCtfL1NonIsoWithMaterialTracks_*_*',
      'keep *_hltBSoftMuonL25BJetTagsUByDR_*_*',
      'keep *_hltHITIPTCorrector8E29_*_*',
      'keep *_hltL1HLTSingleIsoTau30JetsMatch_*_*',
      'keep *_hltMuTracks_*_*',
      'keep *_hltL25TauPixelTracksConeIsolation_*_*',
      'keep *_hltMuonTauL1Filtered_*_*',
      'keep *_hltL3MuonCandidates_*_*',
      'keep *_hltL25TauPixelTracksConeIsolationNoL2_*_*',
      'keep *_hltL2TauIsolationProducer_*_*',
      'keep *_hltMumukPixelSeedFromL2Candidate_*_*',
      'keep *_hltBSoftMuonL25JetsU_*_*',
      'keep *_hltL1NonIsolatedElectronHcalIsol_*_*',
      'keep *_hltL3TrackCandidateFromL2_*_*',
      'keep *_hltSiStripRawToClustersFacility_*_*',
      'keep *_hltIsolPixelTrackProd8E29_*_*',
      'keep *_hltPixelMatchLargeWindowElectronsL1Iso_*_*',
      'keep *_hltL25TauPixelTracksLeadingTrackPtCutSelector_*_*',
      'keep *_hltL2TauRelaxingIsolationSelector_*_*',
      'keep *_hltL3MuonCandidatesOI_*_*',
      'keep *_hltMuonTauIsoL3PreFiltered_*_*',
      'keep *_hltMet_*_*',
      'keep *_hltL25TauCtfWithMaterialTracks_*_*',
      'keep *_hltL1NonIsoElectronTrackIsol_*_*',
      'keep *_hltCorrectedHybridSuperClustersL1NonIsolated_*_*',
      'keep *_hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated_*_*',
      'keep *_hltBLifetimeL25TagInfosStartup_*_*',
      'keep *_hltBLifetimeL25AssociatorStartup_*_*',
      'keep *_hltCsc2DRecHits_*_*',
      'keep *_hltBLifetimeL25BJetTagsStartup_*_*',
      'keep *_hltBSoftMuonL3BJetTagsUByDR_*_*',
      'keep *_hltL1NonIsoElectronsRegionalCTFFinalFitWithMaterial_*_*',
      'keep *_hltMuonTauIsoL3IsoFilteredNoL1Tau_*_*',
      'keep *_hltBLifetimeL3JetsStartup_*_*',
      'keep *_hltL2MuonSeeds_*_*',
      'keep *_hltBLifetimeL25JetsStartup_*_*',
      'keep *_hltHtMet_*_*',
      'keep *_hltMuonTauIsoL2IsoFilteredNoL1Tau_*_*',
      'keep *_hltMulti5x5SuperClustersL1Isolated_*_*',
      'keep *_hltL2TauNarrowConeIsolationProducer_*_*',
      'keep *_hltL3MuonIsolations_*_*',
      'keep *_hltL25TauJetTracksAssociator_*_*',
      'keep *_hltCtfL1IsoLargeWindowWithMaterialTracks_*_*',
      'keep *_hltGctDigis_*_*',
      'keep *_hltL1IsolatedElectronHcalIsol_*_*',
      'keep *_hltL3MuonsOI_*_*',
      'keep *_hltL25TauPixelTracksIsolationSelectorNoL2_*_*',
      'keep *_hltBLifetimeL25BJetTagsStartupU_*_*',
      'keep *_hltHITIPTCorrector1E31_*_*',
      'keep *_hltOfflineBeamSpot_*_*',
      'keep *_hltMCJetCorJetIcone5PU_*_*',
      'keep *_hltL1NonIsoStartUpElectronPixelSeeds_*_*',
      'keep *_hltBLifetimeL25AssociatorStartupU_*_*',
      'keep *_hltL1IsoStartUpElectronPixelSeeds_*_*',
      'keep *_hltHITCtfWithMaterialTracks8E29_*_*',
      'keep *_hltHybridSuperClustersL1NonIsolated_*_*',
      'keep *_hltMulti5x5SuperClustersL1NonIsolated_*_*',
      'keep *_hltL3TauIsolationSelector_*_*',
      'keep *_hltMumuPixelSeedFromL2Candidate_*_*',
      'keep *_hltDt4DSegments_*_*',
      'keep *_hltL25TauLeadingTrackPtCutSelector_*_*',
      'keep *_hltSelector4Jets_*_*',
      'keep *_hltIsolPixelTrackProd1E31_*_*',
      'keep *_hltL25TauPixelTracksLeadingTrackPtCutSelectorNoL2_*_*',
      'keep *_hltCkfTrackCandidatesMumuk_*_*',
      'keep *_hltPixelMatchLargeWindowElectronsL1NonIso_*_*',
      'keep *_hltMCJetCorJetIcone5Regional_*_*',
      'keep *_hltSelector4JetsU_*_*',
      'keep *_hltL1IsoElectronsRegionalCTFFinalFitWithMaterial_*_*',
      'keep *_hltL1HLTDoubleLooseIsoTau15Trk5JetsMatch_*_*',
      'keep *_hltIterativeCone5CaloJets_*_*',
      'keep *_hltL3TauCtfWithMaterialTracks_*_*',
      'keep *_hltSiPixelRecHits_*_*',
      'keep *_hltBSoftMuonL25TagInfosU_*_*',
      'keep *_hltCtfWithMaterialTracksMumuk_*_*',
      'keep *_hltL3TauConeIsolation_*_*',
      'keep *_hltMCJetCorJetIcone5HF07_*_*',
      'keep *_hltL25TauJetPixelTracksAssociator_*_*',
      'keep *_hltDt1DRecHits_*_*',
      'keep *_hltHybridSuperClustersL1Isolated_*_*',
      'keep *_hltL25TauJetPixelTracksAssociatorNoL2_*_*',
      'keep *_hltPixelMatchElectronsL1Iso_*_*',
      'keep *_hltTowerMakerForMuons_*_*',
      'keep *_hltIterativeCone5CaloJetsRegional_*_*',
      'keep *_hltCorrectedHybridSuperClustersL1Isolated_*_*',
      'keep *_hltGtDigis_*_*',
      'keep *_hltMuonTauIsoL2PreFiltered_*_*',
      'keep *_hltL1NonIsoHLTClusterShape_*_*',
      'keep *_hltMuonTauIsoL2PreFilteredNoL1Tau_*_*',
      'keep *_hltBLifetimeL25JetsStartupU_*_*',
      'keep *_hltL2TauIsolationSelectorNoCut_*_*',
      'keep *_hltBLifetimeRegionalCtfWithMaterialTracksStartupU_*_*',
      'keep *_hltBLifetimeL3TagInfosStartup_*_*',
      'keep *_hltSiPixelClusters_*_*',
      'keep *_hltElectronL1IsoLargeWindowDetaDphi_*_*',
      'keep *_hltL3Muons_*_*',
      'keep *_hltBLifetimeL3JetsStartupU_*_*',
      'keep *_hltL1NonIsolatedPhotonHcalIsol_*_*',
      'keep *_hltL1IsoRecoEcalCandidate_*_*',
      'keep *_hltL1extraParticles_*_*',
      'keep *_hltL3TrajectorySeed_*_*',
      'keep *_hltL1IsoLargeWindowElectronPixelSeeds_*_*',
      'keep *_hltL1NonIsoPhotonHollowTrackIsol_*_*',
      'keep *_hltL1IsolatedPhotonEcalIsol_*_*',
      'keep *_hltCscSegments_*_*',
      'keep *_hltBLifetimeL3AssociatorStartupU_*_*',
      'keep *_hltMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated_*_*',
      'keep *_hltL1IsoEgammaRegionalCTFFinalFitWithMaterial_*_*',
      'keep *_hltBLifetimeL25TagInfosStartupU_*_*',
      'keep *_hltL1GtObjectMap_*_*',
      'keep *_hltL3TauJetTracksAssociator_*_*',
      'keep *_hltL3TrajectorySeedOI_*_*',
      'keep *_hltMuonTauIsoL2IsoFiltered_*_*',
      'keep *_hltSelector4JetsRegional_*_*',
      'keep *_hltL3TkTracksFromL2_*_*',
      'keep *_hltL1IsoElectronTrackIsol_*_*',
      'keep *_hltL1HLTSingleLooseIsoTau20JetsMatch_*_*',
      'keep *_hltL2Muons_*_*',
      'keep *_hltBLifetimeL3BJetTagsStartupU_*_*',
      'keep *_hltL1IsoHLTClusterShape_*_*',
      'keep *_hltBLifetimeL3TagInfosStartupU_*_*',
      'keep *_hltMCJetCorJetIcone5_*_*',
      'keep *_hltPixelTracks_*_*',
      'keep *_hltL25TauPixelTracksIsolationSelector_*_*',
      'keep *_hltL2MuonIsolations_*_*',
      'keep *_hltL25TauConeIsolation_*_*',
      'keep *_hltPixelMatchElectronsL1NonIso_*_*',
      'keep *_hltMuonTauIsoL3PreFilteredNoL1Tau_*_*',
      'keep *_hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial_*_*',
      'keep *_hltL2MuonCandidates_*_*',
      'keep *_hltL1IsoPhotonHollowTrackIsol_*_*',
      'keep *_hltBSoftMuonL3TagInfosU_*_*',
      'keep *_hltL1IsolatedPhotonHcalIsol_*_*',
      'keep *_hltL1NonIsoRecoEcalCandidate_*_*',
      'keep *_hltCtfWithMaterialTracksMumu_*_*',
      'keep *_hltMulti5x5EndcapSuperClustersWithPreshowerL1Isolated_*_*',
      'keep *_hltBLifetimeL3AssociatorStartup_*_*',
      'keep *_hltHITCtfWithMaterialTracks1E31_*_*',
      'keep *_hltCtfL1NonIsoLargeWindowWithMaterialTracks_*_*',
      'keep *_hltCkfTrackCandidatesMumu_*_*',
      'keep *_hltMuonTauL1FilteredNoL1Tau_*_*',
      'keep *_hltL2TauJets_*_*',
      'keep *_hltMumukAllConeTracks_*_*' )
)
process.hltDebugWithAlCaOutput = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "file:HLTDebugWithAlCaOutput.root" ),
    compressionLevel = cms.untracked.int32( 1 ),
    basketSize = cms.untracked.int32( 4096 ),
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_HIDoubleMu',
  'HLT_HIJet50U',
  'HLT_HIJet75U',
  'HLT_HIJet90U',
  'HLT_HIPhoton10',
  'HLT_HIPhoton20',
  'HLT_HIPhoton30',
  'HLTriggerFinalPath',
  'HLTriggerFirstPath' ) ),
    dataset = cms.untracked.PSet(  dataTier = cms.untracked.string( "RECO" ) ),
    outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*',
      'keep triggerTriggerEventWithRefs_*_*_*',
      'keep *_hltTowerMakerForAll_*_*',
      'keep *_hltCtfL1IsoWithMaterialTracks_*_*',
      'keep *_hltMuonTauIsoL3IsoFiltered_*_*',
      'keep *_hltElectronL1NonIsoLargeWindowDetaDphi_*_*',
      'keep *_hltBLifetimeL3BJetTagsStartup_*_*',
      'keep *_hltL1NonIsoLargeWindowElectronPixelSeeds_*_*',
      'keep *_hltL1NonIsolatedPhotonEcalIsol_*_*',
      'keep *_hltRpcRecHits_*_*',
      'keep *_hltL1HLTDoubleLooseIsoTau15JetsMatch_*_*',
      'keep *_hltL3TkTracksOIFromL2_*_*',
      'keep *_hltAlCaEtaRegRecHits_*_*',
      'keep *_hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated_*_*',
      'keep *_hltBSoftMuonL3BJetTagsUByPt_*_*',
      'keep *_hltPixelVertices_*_*',
      'keep *_hltBLifetimeRegionalCtfWithMaterialTracksStartup_*_*',
      'keep *_hltCtfL1NonIsoWithMaterialTracks_*_*',
      'keep *_hltBSoftMuonL25BJetTagsUByDR_*_*',
      'keep *_hltHITIPTCorrector8E29_*_*',
      'keep *_hltL1HLTSingleIsoTau30JetsMatch_*_*',
      'keep *_hltMuTracks_*_*',
      'keep *_hltL25TauPixelTracksConeIsolation_*_*',
      'keep *_hltMuonTauL1Filtered_*_*',
      'keep *_hltL3MuonCandidates_*_*',
      'keep *_hltL25TauPixelTracksConeIsolationNoL2_*_*',
      'keep *_hltL2TauIsolationProducer_*_*',
      'keep *_hltMumukPixelSeedFromL2Candidate_*_*',
      'keep *_hltBSoftMuonL25JetsU_*_*',
      'keep *_hltL1NonIsolatedElectronHcalIsol_*_*',
      'keep *_hltL3TrackCandidateFromL2_*_*',
      'keep *_hltSiStripRawToClustersFacility_*_*',
      'keep *_hltIsolPixelTrackProd8E29_*_*',
      'keep *_hltAlCaPhiSymStream_*_*',
      'keep *_hltPixelMatchLargeWindowElectronsL1Iso_*_*',
      'keep *_hltL25TauPixelTracksLeadingTrackPtCutSelector_*_*',
      'keep *_hltL2TauRelaxingIsolationSelector_*_*',
      'keep *_hltL3MuonCandidatesOI_*_*',
      'keep *_hltMuonTauIsoL3PreFiltered_*_*',
      'keep *_hltMet_*_*',
      'keep *_hltL25TauCtfWithMaterialTracks_*_*',
      'keep *_hltAlCaPi0RegRecHits_*_*',
      'keep *_hltL1NonIsoElectronTrackIsol_*_*',
      'keep *_hltCorrectedHybridSuperClustersL1NonIsolated_*_*',
      'keep *_hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated_*_*',
      'keep *_hltBLifetimeL25TagInfosStartup_*_*',
      'keep *_hltBLifetimeL25AssociatorStartup_*_*',
      'keep *_hltCsc2DRecHits_*_*',
      'keep *_hltBLifetimeL25BJetTagsStartup_*_*',
      'keep *_hltBSoftMuonL3BJetTagsUByDR_*_*',
      'keep *_hltL1NonIsoElectronsRegionalCTFFinalFitWithMaterial_*_*',
      'keep *_hltMuonTauIsoL3IsoFilteredNoL1Tau_*_*',
      'keep *_hltBLifetimeL3JetsStartup_*_*',
      'keep *_hltL2MuonSeeds_*_*',
      'keep *_hltBLifetimeL25JetsStartup_*_*',
      'keep *_hltHtMet_*_*',
      'keep *_hltMuonTauIsoL2IsoFilteredNoL1Tau_*_*',
      'keep *_hltMulti5x5SuperClustersL1Isolated_*_*',
      'keep *_hltL2TauNarrowConeIsolationProducer_*_*',
      'keep *_hltL3MuonIsolations_*_*',
      'keep *_hltL25TauJetTracksAssociator_*_*',
      'keep *_hltCtfL1IsoLargeWindowWithMaterialTracks_*_*',
      'keep *_hltGctDigis_*_*',
      'keep *_hltL1IsolatedElectronHcalIsol_*_*',
      'keep *_hltL3MuonsOI_*_*',
      'keep *_hltL25TauPixelTracksIsolationSelectorNoL2_*_*',
      'keep *_hltBLifetimeL25BJetTagsStartupU_*_*',
      'keep *_hltHITIPTCorrector1E31_*_*',
      'keep *_hltOfflineBeamSpot_*_*',
      'keep *_hltMCJetCorJetIcone5PU_*_*',
      'keep *_hltL1NonIsoStartUpElectronPixelSeeds_*_*',
      'keep *_hltBLifetimeL25AssociatorStartupU_*_*',
      'keep *_hltL1IsoStartUpElectronPixelSeeds_*_*',
      'keep *_hltHITCtfWithMaterialTracks8E29_*_*',
      'keep *_hltHybridSuperClustersL1NonIsolated_*_*',
      'keep *_hltMulti5x5SuperClustersL1NonIsolated_*_*',
      'keep *_hltL3TauIsolationSelector_*_*',
      'keep *_hltMumuPixelSeedFromL2Candidate_*_*',
      'keep *_hltDt4DSegments_*_*',
      'keep *_hltL25TauLeadingTrackPtCutSelector_*_*',
      'keep *_hltSelector4Jets_*_*',
      'keep *_hltIsolPixelTrackProd1E31_*_*',
      'keep *_hltL25TauPixelTracksLeadingTrackPtCutSelectorNoL2_*_*',
      'keep *_hltCkfTrackCandidatesMumuk_*_*',
      'keep *_hltPixelMatchLargeWindowElectronsL1NonIso_*_*',
      'keep *_hltMCJetCorJetIcone5Regional_*_*',
      'keep *_hltSelector4JetsU_*_*',
      'keep *_hltL1IsoElectronsRegionalCTFFinalFitWithMaterial_*_*',
      'keep *_hltL1HLTDoubleLooseIsoTau15Trk5JetsMatch_*_*',
      'keep *_hltIterativeCone5CaloJets_*_*',
      'keep *_hltL3TauCtfWithMaterialTracks_*_*',
      'keep *_hltSiPixelRecHits_*_*',
      'keep *_hltBSoftMuonL25TagInfosU_*_*',
      'keep *_hltCtfWithMaterialTracksMumuk_*_*',
      'keep *_hltL3TauConeIsolation_*_*',
      'keep *_hltMCJetCorJetIcone5HF07_*_*',
      'keep *_hltL25TauJetPixelTracksAssociator_*_*',
      'keep *_hltDt1DRecHits_*_*',
      'keep *_hltHybridSuperClustersL1Isolated_*_*',
      'keep *_hltL25TauJetPixelTracksAssociatorNoL2_*_*',
      'keep *_hltPixelMatchElectronsL1Iso_*_*',
      'keep *_hltTowerMakerForMuons_*_*',
      'keep *_hltIterativeCone5CaloJetsRegional_*_*',
      'keep *_hltCorrectedHybridSuperClustersL1Isolated_*_*',
      'keep *_hltGtDigis_*_*',
      'keep *_hltMuonTauIsoL2PreFiltered_*_*',
      'keep *_hltAlCaPi0RegRecHitsCosmics_*_*',
      'keep *_hltL1NonIsoHLTClusterShape_*_*',
      'keep *_hltMuonTauIsoL2PreFilteredNoL1Tau_*_*',
      'keep *_hltBLifetimeL25JetsStartupU_*_*',
      'keep *_hltL2TauIsolationSelectorNoCut_*_*',
      'keep *_hltBLifetimeRegionalCtfWithMaterialTracksStartupU_*_*',
      'keep *_hltBLifetimeL3TagInfosStartup_*_*',
      'keep *_hltSiPixelClusters_*_*',
      'keep *_hltElectronL1IsoLargeWindowDetaDphi_*_*',
      'keep *_hltL3Muons_*_*',
      'keep *_hltBLifetimeL3JetsStartupU_*_*',
      'keep *_hltL1NonIsolatedPhotonHcalIsol_*_*',
      'keep *_hltL1IsoRecoEcalCandidate_*_*',
      'keep *_hltL1extraParticles_*_*',
      'keep *_hltL3TrajectorySeed_*_*',
      'keep *_hltL1IsoLargeWindowElectronPixelSeeds_*_*',
      'keep *_hltL1NonIsoPhotonHollowTrackIsol_*_*',
      'keep *_hltL1IsolatedPhotonEcalIsol_*_*',
      'keep *_hltCscSegments_*_*',
      'keep *_hltBLifetimeL3AssociatorStartupU_*_*',
      'keep *_hltMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated_*_*',
      'keep *_hltL1IsoEgammaRegionalCTFFinalFitWithMaterial_*_*',
      'keep *_hltBLifetimeL25TagInfosStartupU_*_*',
      'keep *_hltL1GtObjectMap_*_*',
      'keep *_hltL3TauJetTracksAssociator_*_*',
      'keep *_hltL3TrajectorySeedOI_*_*',
      'keep *_hltMuonTauIsoL2IsoFiltered_*_*',
      'keep *_hltSelector4JetsRegional_*_*',
      'keep *_hltL3TkTracksFromL2_*_*',
      'keep *_hltAlCaEtaRegRecHitsCosmics_*_*',
      'keep *_hltL1IsoElectronTrackIsol_*_*',
      'keep *_hltL1HLTSingleLooseIsoTau20JetsMatch_*_*',
      'keep *_hltL2Muons_*_*',
      'keep *_hltBLifetimeL3BJetTagsStartupU_*_*',
      'keep *_hltL1IsoHLTClusterShape_*_*',
      'keep *_hltBLifetimeL3TagInfosStartupU_*_*',
      'keep *_hltMCJetCorJetIcone5_*_*',
      'keep *_hltPixelTracks_*_*',
      'keep *_hltL25TauPixelTracksIsolationSelector_*_*',
      'keep *_hltL2MuonIsolations_*_*',
      'keep *_hltL25TauConeIsolation_*_*',
      'keep *_hltPixelMatchElectronsL1NonIso_*_*',
      'keep *_hltMuonTauIsoL3PreFilteredNoL1Tau_*_*',
      'keep *_hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial_*_*',
      'keep *_hltL2MuonCandidates_*_*',
      'keep *_hltL1IsoPhotonHollowTrackIsol_*_*',
      'keep *_hltBSoftMuonL3TagInfosU_*_*',
      'keep *_hltAlCaHcalFEDSelector_*_*',
      'keep *_hltL1IsolatedPhotonHcalIsol_*_*',
      'keep *_hltL1NonIsoRecoEcalCandidate_*_*',
      'keep *_hltCtfWithMaterialTracksMumu_*_*',
      'keep *_hltMulti5x5EndcapSuperClustersWithPreshowerL1Isolated_*_*',
      'keep *_hltBLifetimeL3AssociatorStartup_*_*',
      'keep *_hltHITCtfWithMaterialTracks1E31_*_*',
      'keep *_hltCtfL1NonIsoLargeWindowWithMaterialTracks_*_*',
      'keep *_hltCkfTrackCandidatesMumu_*_*',
      'keep *_hltMuonTauL1FilteredNoL1Tau_*_*',
      'keep *_hltL2TauJets_*_*',
      'keep *_hltMumukAllConeTracks_*_*' )
)
process.hltPreAlCaOutput = cms.EDFilter( "HLTPrescaler" )
process.hltEcalPhiSymOutput = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "AlCaRawEcalPhiSymStream.root" ),
    compressionLevel = cms.untracked.int32( 1 ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*',
      'keep *_hltAlCaPhiSymStream_*_*' )
)
process.hltHcalPhiSymOutput = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "AlCaRawHcalPhiSymStream.root" ),
    compressionLevel = cms.untracked.int32( 1 ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep triggerTriggerEvent_*_*_*',
      'keep *_hltAlCaHcalFEDSelector_*_*',
      'keep *_hltGctDigis_*_*',
      'keep *_hltL1GtObjectMap_*_*',
      'keep *_hltL1extraParticles_*_*',
      'keep *_hltGtDigis_*_*' )
)
process.hltEcalPi0EtaOutput = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "AlCaRawEcalPi0Stream.root" ),
    compressionLevel = cms.untracked.int32( 1 ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*',
      'keep *_hltAlCaEtaRegRecHits_*_*',
      'keep *_hltAlCaPi0RegRecHits_*_*' )
)
process.hltRPCMuonOutput = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "AlCaRawRPCMuonStream.root" ),
    compressionLevel = cms.untracked.int32( 1 ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep edmTriggerResults_*_*_*',
      'keep *_hltRpcRecHits_*_*',
      'keep *_hltMuonDTDigis_*_*',
      'keep *_hltDt4DSegments_*_*',
      'keep *_hltGtDigis_*_*',
      'keep *_hltCscSegments_*_*' )
)

process.HLTBeginSequence = cms.Sequence( process.hltTriggerType + process.hltEventNumber + process.hltGtDigis + process.hltGctDigis + process.hltL1GtObjectMap + process.hltL1extraParticles + process.hltOfflineBeamSpot )
process.HLTDoLocalHcalSequence = cms.Sequence( process.hltHcalDigis + process.hltHbhereco + process.hltHfreco + process.hltHoreco )
process.HLTDoCaloSequence = cms.Sequence( process.hltEcalRawToRecHitFacility + process.hltEcalRegionalRestFEDs + process.hltEcalRecHitAll + process.HLTDoLocalHcalSequence + process.hltTowerMakerForAll )
process.HLTDoHIJetRecoSequence = cms.Sequence( process.HLTDoCaloSequence + process.hltIterativeCone5PileupSubtractionCaloJets + process.hltMCJetCorJetIcone5PU )
process.HLTEndSequence = cms.Sequence( process.hltBoolEnd )
process.HLTDoHIEcalClusSequence = cms.Sequence( process.hltIslandBasicClustersHI + process.hltIslandSuperClustersHI + process.hltCorrectedIslandBarrelSuperClustersHI + process.hltCorrectedIslandEndcapSuperClustersHI + process.hltRecoHIEcalCandidate )
process.HLTL2muonrecoNocandSequence = cms.Sequence( process.hltMuonDTDigis + process.hltDt1DRecHits + process.hltDt4DSegments + process.hltMuonCSCDigis + process.hltCsc2DRecHits + process.hltCscSegments + process.hltMuonRPCDigis + process.hltRpcRecHits + process.hltL2MuonSeeds + process.hltL2Muons )
process.HLTL2muonrecoSequence = cms.Sequence( process.HLTL2muonrecoNocandSequence + process.hltL2MuonCandidates )
process.HLTDoLocalPixelSequence = cms.Sequence( process.hltSiPixelDigis + process.hltSiPixelClusters + process.hltSiPixelRecHits )
process.HLTHIRecopixelvertexingSequence = cms.Sequence( process.hltHIPixelTracks + process.hltHIPixelVertices )
process.HLTDoLocalStripSequence = cms.Sequence( process.hltSiStripRawToClustersFacility + process.hltSiStripClusters )

process.HLTriggerFirstPath = cms.Path( process.hltGetRaw + process.HLTBeginSequence + process.hltPreFirstPath + process.hltBoolFirstPath )
#process.HLT_HIJet50U = cms.Path( process.HLTBeginSequence + process.hltHIL1sJet50U + process.hltHIPreJet50U + process.HLTDoHIJetRecoSequence + process.hltHI1jet50U + process.HLTEndSequence )
#process.HLT_HIJet75U = cms.Path( process.HLTBeginSequence + process.hltHIL1sJet75U + process.hltHIPreJet75U + process.HLTDoHIJetRecoSequence + process.hltHI1jet75U + process.HLTEndSequence )
#process.HLT_HIJet90U = cms.Path( process.HLTBeginSequence + process.hltHIL1sJet90U + process.hltHIPreJet90U + process.HLTDoHIJetRecoSequence + process.hltHI1jet90U + process.HLTEndSequence )
#process.HLT_HIPhoton10 = cms.Path( process.HLTBeginSequence + process.hltHIL1sPhoton10 + process.hltHIPrePhoton10 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusSequence + process.hltHIPhoton10 + process.HLTEndSequence )
#process.HLT_HIPhoton20 = cms.Path( process.HLTBeginSequence + process.hltHIL1sPhoton20 + process.hltHIPrePhoton20 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusSequence + process.hltHIPhoton20 + process.HLTEndSequence )
#process.HLT_HIPhoton30 = cms.Path( process.HLTBeginSequence + process.hltHIL1sPhoton30 + process.hltHIPrePhoton30 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusSequence + process.hltHIPhoton30 + process.HLTEndSequence )
process.HLT_HIDoubleMu = cms.Path( process.HLTBeginSequence + process.hltHIPreMML1 + process.hltHIMML1Seed + process.HLTL2muonrecoSequence + process.HLTDoLocalPixelSequence + process.HLTHIRecopixelvertexingSequence + process.HLTDoLocalStripSequence + process.hltHIMML3Filter + process.HLTEndSequence )
process.HLTriggerFinalPath = cms.Path( process.hltTriggerSummaryAOD + process.hltPreTriggerSummaryRAW + process.hltTriggerSummaryRAW + process.hltBoolFinalPath )
process.HLTAnalyzerEndpath = cms.EndPath( process.hltL1GtTrigReport + process.hltTrigReport )
#process.HLTOutput = cms.EndPath( process.hltDefaultOutput + process.hltDefaultOutputWithFEDs + process.hltPreDebugOutput + process.hltDebugOutput + process.hltDebugWithAlCaOutput )
#process.AlCaOutput = cms.EndPath( process.hltPreAlCaOutput + process.hltEcalPhiSymOutput + process.hltHcalPhiSymOutput + process.hltEcalPi0EtaOutput + process.hltRPCMuonOutput )

