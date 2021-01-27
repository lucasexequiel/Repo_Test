designFile = "C:/Users/Public/Documents/Altium/Projects/Prueba_1/PDNAnalyzer_Output/PCB1/odb.tgz"

powerNets = ["+5", "NetP2_1"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("P1", "2") ],
"ground_pins": [ ("P1", "1") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("R1", "2") ],
"ground_pins": [ ("R1", "1") ],
"resistance": 1E-09,
"Rpin": 500,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("P2", "1") ],
"ground_pins": [ ("P2", "2") ],
"current": 1,
"Rpin": 0.1,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("R3", "2") ],
"ground_pins": [ ("R3", "1") ],
"resistance": 1E-09,
"Rpin": 500,
}
]


voltage_regulators = [
{
"id": "4",
"type": "linear",

"in": [ ("R2", "1") ],
"out": [ ("R2", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 500,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.8, 'Thickness': 0.00032004},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
