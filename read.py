# REQUIRED PACKAGES
import ROOT
#import dunestyle.root as dunestyle

root_file = ROOT.TFile('/pnfs/dune/persistent/users/LBL_TDR/throws_v4/final_np_15yr.root')
keys = root_file.GetListOfKeys()
for key in keys:
    obj = key.ReadObj()
    obj.Print()

tree = root_file.Get("oct_fit_info")
canvas = ROOT.TCanvas("canvas", "Plot")
tree.Draw("SpectraRNGSeeds")
canvas.Draw()
canvas.SaveAs("myCanvas.png")

# Close the ROOT file
root_file.Close()