"""
heatmap of table
"""

import os
import matplotlib.pyplot as plt
import pandas as pd
import re

__author__ = "Xue Chunxu"
__contact__ = "xuechunxu@outlook.com"
__version__ = "0.5"

def heatmap(abundance_table):
    print("\n" + 'Heatmap starting...Please wait. This may take a while'.center(70, '*'))
    os.mkdir('heatmap_tmp')
    dict_table = {}
    head = ''
    with open(abundance_table) as table:
        for line in table:
            line = line.strip('\n')
            if line.startswith('#'):
                head = line
            else:
                pathway = line.split('\t')[0]
                abundance = line.split('\t')
                del abundance[0]
                dict_table[pathway] = abundance

    carbon_cycle = ['Photosystem II',
                    'Photosystem I',
                    'Cytochrome b6/f complex',
                    'Anoxygenic photosystem II (pufML)',
                    'Anoxygenic photosystem I (pscABCD)',
                    'RuBisCo',
                    'CBB Cycle',
                    'rTCA Cycle',
                    'Wood-Ljungdahl',
                    '3-Hydroxypropionate Bicycle',
                    'Dicarboxylate-hydroxybutyrate cycle',
                    'Pectinesterase',
                    'Diacetylchitobiose deacetylase',
                    'Glucoamylase',
                    'D-galacturonate epimerase',
                    'exo-poly-alpha-galacturonosidase',
                    'Oligogalacturonide lyase',
                    'Cellulase',
                    'exopolygalacturonase',
                    'Chitinase',
                    'Basic endochitinase B',
                    'bifunctional chitinase/lysozyme',
                    'beta-N-acetylhexosaminidase',
                    'D-galacturonate isomerase',
                    'alpha-amylase',
                    'beta-glucosidase',
                    'pullulanase',
                    'glycolysis',
                    'Entner-Doudoroff pathway, glucose-6P -> glyceraldehyde-3P + pyruvate',
                    'gluconeogenesis, oxaloacetate -> fructose-6P',
                    'TCA Cycle',
                    'Methanogenesis, methanol -> methane',
                    'Methanogenesis, methylamine -> methane',
                    'Methanogenesis, dimethylamine -> methane',
                    'Methanogenesis, trimethylamine -> methane',
                    'Methanogenesis, acetate -> methane',
                    'Methanogenesis, CO2 -> methane',
                    'Methane oxidation, methane -> methanol',
                    'Methane oxidation, methanol -> Formaldehyde',
                    'Mixed acid: lactate (pyruvate -> lactate)',
                    'Mixed acid: formate (pyruvate -> formate)',
                    'Mixed acid: Formate -> CO2 & H2',
                    'Mixed acid: acetate (pyruvate -> acetate)',
                    'Mixed acid: acetate (acetyl-CoA -> acetate)',
                    'Mixed acid: acetate (lactate -> acetate)',
                    'Mixed acid: ethanol, acetate to acetylaldehyde',
                    'Mixed acid: ethanol, acetyl-CoA to acetylaldehyde (reversible)',
                    'Mixed acid: ethanol, acetylaldehyde to ethanol',
                    'Mixed acid: succinate (phosphoenolpyruvate to succinate via oxaloacetate, malate & fumarate)',
                    'Anaplerotic genes (pyruvate -> oxaloacetate)']

    nitrogen_cycle = ['Dissimilatory nitrate reduction to nitrite',
                      'Dissimilatory nitrite reduction to ammonia',
                      'Assimilatory nitrate reduction to nitrite',
                      'Assimilatory nitrite reduction to ammonia',
                      'Assimilatory nitrate reduction to ammonia',
                      'Denitrification, NO2 -> NO',
                      'Denitrification, NO -> N2O',
                      'Denitrification, N2O -> N2',
                      'Nitrogen fixation',
                      'Nitrification, ammonia -> hydroxylamine (AmoCAB)',
                      'Nitrification, hydroxylamine -> nitrite (hao)',
                      'Nitrification, nitrite -> nitrate (nxrAB)',
                      'Anammox, NO + NH3 -> N2H4',
                      'Anammox, N2H4 -> N2']

    sulfur_cycle = ['Assimilatory sulfate reduction to sulfite',
                    'Assimilatory sulfite reduction to sulfide (cysJI, sir)',
                    'Dissimilatory sulfate reduction to sulfite (reversible)',
                    'Dissimilatory sulfite reduction to sulfide (reversible)',
                    'Thiosulfate oxidation by SOX complex, thiosulfate -> sulfate',
                    'Alternative thiosulfate oxidation (doxAD)',
                    'Alternative thiosulfate oxidation (tsdA)',
                    'Thiosulfate oxidation (SOX, doxAD and tsdA)',
                    'Sulfur reduction, sulfur -> sulfide (sreABC)',
                    'Thiosulfate disproportionation, thiosulfate -> sulfide & sulfite (phsABC)',
                    'Sulfhydrogenase, (sulfide)n -> (sulfide)n-1',
                    'Sulfur disproportionation, sulfur -> sulfide & sulfite',
                    'Sulfur dioxygenase',
                    'Sulfite oxidation, sulfite -> sulfate (sorB, SUOX, soeABC)',
                    'Sulfide oxidation, sulfide -> sulfur (fccAB)']

    other = ['F-type ATPase',
             'V/A-type ATPase',
             'NADH-quinone oxidoreductase',
             'NAD(P)H-quinone oxidoreductase',
             'Succinate dehydrogenase (ubiquinone)',
             'Cytochrome c oxidase, cbb3-type',
             'Cytochrome bd ubiquinol oxidase',
             'Cytochrome o ubiquinol oxidase',
             'Cytochrome c oxidase, prokaryotes',
             'Cytochrome aa3-600 menaquinol oxidase',
             'Cytochrome bc1 complex',
             'Phosphate transporter',
             'Phosphonate transporter',
             'Thiamin transporter',
             'Vitamin B12 transporter',
             'Urea transporter',
             'Type I Secretion',
             'Type III Secretion',
             'Type II Secretion',
             'Type IV Secretion',
             'Type VI Secretion',
             'Sec-SRP',
             'Twin arginine targeting',
             'Type Vabc secretion',
             'Bacterial chemotaxis',
             'Flagellum assembly',
             'Dissimilatory arsenic reduction']

    with open('heatmap_tmp/carbon_cycle.tab', 'w') as carbon_out:
        carbon_out.write(head)
        for i in carbon_cycle:
            carbon_out.write(i + '\t' + dict_table[i] + '\n')

    with open('heatmap_tmp/nitrogen_cycle.tab', 'w') as nitrogen_out:
        nitrogen_out.write(head)
        for i in nitrogen_cycle:
            nitrogen_out.write(i + '\t' + dict_table[i] + '\n')

    with open('heatmap_tmp/sulfur_cycle.tab', 'w') as sulfur_out:
        sulfur_out.write(head)
        for i in sulfur_cycle:
            sulfur_out.write(i + '\t' + dict_table[i] + '\n')

    with open('heatmap_tmp/other_cycle.tab', 'w') as other_out:
        other_out.write(head)
        for i in other:
            other_out.write(i + '\t' + dict_table[i] + '\n')

    tables = ['carbon_cycle.tab',
              'nitrogen_cycle.tab',
              'sulfur_cycle.tab',
              'other_cycle.tab']

    for i in tables:
        file_in = open(i, "r")
        data = pd.read_table(file_in, index_col=0)
        import seaborn as sns
        sns.set(font_scale=1.2)
        ax = sns.heatmap(data, cmap='PiYG', linewidths=2, linecolor='k', square=True, xticklabels=True, yticklabels=True)
        ax.xaxis.tick_top()
        #ax.set_yticklabels(ax.get_yticklabels(), rotation=90)
        plt.xticks(rotation=90)
        plt.yticks(rotation=0)
        # get figure (usually obtained via "fig,ax=plt.subplots()" with matplotlib)
        fig = ax.get_figure()
        # specify dimensions and save
        fig.set_size_inches(35, 35)
        out_name = re.sub('.tab', i)
        fig.savefig(out_name + '.png', dpi = 600)