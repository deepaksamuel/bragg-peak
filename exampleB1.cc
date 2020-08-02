//
// ********************************************************************
// * License and Disclaimer                                           *
// *                                                                  *
// * The  Geant4 software  is  copyright of the Copyright Holders  of *
// * the Geant4 Collaboration.  It is provided  under  the terms  and *
// * conditions of the Geant4 Software License,  included in the file *
// * LICENSE and available at  http://cern.ch/geant4/license .  These *
// * include a list of copyright holders.                             *
// *                                                                  *
// * Neither the authors of this software system, nor their employing *
// * institutes,nor the agencies providing financial support for this *
// * work  make  any representation or  warranty, express or implied, *
// * regarding  this  software system or assume any liability for its *
// * use.  Please see the license in the file  LICENSE  and URL above *
// * for the full disclaimer and the limitation of liability.         *
// *                                                                  *
// * This  code  implementation is the result of  the  scientific and *
// * technical work of the GEANT4 collaboration.                      *
// * By using,  copying,  modifying or  distributing the software (or *
// * any work based  on the software)  you  agree  to acknowledge its *
// * use  in  resulting  scientific  publications,  and indicate your *
// * acceptance of all terms of the Geant4 Software license.          *
// ********************************************************************
//
//
/// \file exampleB1.cc
/// \brief Main program of the B1 example

#include "B1DetectorConstruction.hh"
#include "B1ActionInitialization.hh"

#ifdef G4MULTITHREADED
#include "G4MTRunManager.hh"
#else
#include "G4RunManager.hh"
#endif

#include "G4UImanager.hh"
#include "QBBC.hh"

#include "G4VisExecutive.hh"
#include "G4UIExecutive.hh"

#include "Randomize.hh"

#include "G4ScoringManager.hh"
#include <string>
//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

int main(int argc,char** argv)
{


    // First argument: threads, Second: Energy Third: Events
    // Detect interactive mode (if no arguments) and define UI session
    //
    G4cout<<"Please enter the variables: Number of threads, Particle Energy (MeV), Number of Events\n";
    //    float min_energy=100.0;
    //    float max_energy=100.0;
    //    float step_size =100.0;
    float energy=100;
    int nevents=100;
    int nthreads=1;

    if(argc==4){
        nthreads=atoi(argv[1]);
        energy= atof(argv[2]);
        nevents=atoi(argv[3]);
    }

    if(argc==6){//generate commands for looping
        G4cout<<"Please enter the variables: Number of threads, Min Energy (MeV), Max Energy (MeV), Step size, Number of Events\n";
        G4cout<<"A series of commands are generated which you can copy paste on your terminal to fake a loop\n";
        nthreads=atoi(argv[1]);
        float min_energy= atof(argv[2]);
        float max_energy= atof(argv[3]);
        float step_size =atof(argv[4]);
        nevents=atoi(argv[5]);

        for(energy=min_energy; energy<=max_energy; energy=energy+step_size)
        {
            G4cout<<"./exampleB1 "<<nthreads<<" "<<energy<<" "<<nevents<<";";
        }
        G4cout<<"\n";
        exit(1);
    }

    // for(float energy=min_energy; energy<=max_energy; energy=energy+step_size) // this does not work as G4 event loop in not sync with main loop
    { // we loop from min_energy to max_energy in steps of step_size; each file will have the energy as part of filename

        G4UIExecutive* ui = 0;
        if ( argc != 4 ) {
            ui = new G4UIExecutive(argc, argv);
        }

        //    if(argc!=4){
        //        G4cout<<"Please enter the variables: Number of threads, Particle Energy (MeV) and Number of Events\n";
        //        exit(0);
        //    }

        // Optionally: choose a different Random engine...
        // G4Random::setTheEngine(new CLHEP::MTwistEngine);

        // Construct the default run manager
        //
#ifdef G4MULTITHREADED
        G4MTRunManager* runManager = new G4MTRunManager;
#else
        G4RunManager* runManager = new G4RunManager;
#endif

        // Set mandatory initialization classes
        //
        // Detector construction
        runManager->SetUserInitialization(new B1DetectorConstruction());
        G4ScoringManager* scoringManager =  G4ScoringManager::GetScoringManager();

        // Physics list
        G4VModularPhysicsList* physicsList = new QBBC;
        physicsList->SetVerboseLevel(0);
        runManager->SetUserInitialization(physicsList);

        // User action initialization
        runManager->SetUserInitialization(new B1ActionInitialization(energy));

        // Initialize visualization
        //
        G4VisManager* visManager = new G4VisExecutive;
        // G4VisExecutive can take a verbosity argument - see /vis/verbose guidance.
        // G4VisManager* visManager = new G4VisExecutive("Quiet");
        visManager->Initialize();

        // Get the pointer to the User Interface manager
        G4UImanager* UImanager = G4UImanager::GetUIpointer();

        // Process macro or start UI session
        //
        if ( ! ui ) {
            // batch mode
            //G4String command = "/control/execute ";
            //G4String fileName = argv[1];
            //UImanager->ApplyCommand(command+fileName);
            runManager->SetNumberOfThreads(nthreads);
            UImanager->ApplyCommand("/run/initialize");
            UImanager->ApplyCommand("/run/verbose 0");
            UImanager->ApplyCommand("/event/verbose 0");
            UImanager->ApplyCommand("/track/verbose 0");
            UImanager->ApplyCommand("/score/create/boxMesh boxMesh_1");
            UImanager->ApplyCommand("/score/mesh/boxSize 2.5 2.5 15. cm");
            UImanager->ApplyCommand("/score/mesh/nBin 1 1 300");
            UImanager->ApplyCommand("/score/quantity/energyDeposit doseScorer");
            UImanager->ApplyCommand("/score/close");

            G4String beamOn = "/run/beamOn ";
            beamOn.append(std::to_string(nevents));
            UImanager->ApplyCommand(beamOn);
            G4String str = "/score/dumpQuantityToFile boxMesh_1 doseScorer ";
            str.append(std::to_string(energy)).append("-MEV-");
            str.append(std::to_string(nevents)).append("-EVTS.txt");
            UImanager->ApplyCommand(str);
        }
        else {
            // interactive mode
            UImanager->ApplyCommand("/control/execute init_vis.mac");
            ui->SessionStart();
            delete ui;
        }

        // Job termination
        // Free the store: user actions, physics_list and detector_description are
        // owned and deleted by the run manager, so they should not be deleted
        // in the main() program !

        delete visManager;
        delete runManager;
        G4cout<<"Energy: "<<energy<<" MeV completed\n";
    }
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo.....
