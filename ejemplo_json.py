import json

x1=[36.23, 72.46, 108.7, 144.93, 181.16, 217.39, 253.62, 289.86, 326.09, 362.32, 398.55, 434.78, 471.01, 507.25, 543.48, 579.71, 615.94, 652.17, 688.41, 724.64, 760.87, 797.1, 833.33, 869.57, 905.8, 942.03, 978.26, 1014.49, 1050.72, 1086.96, 1123.19, 1159.42, 1195.65, 1231.88, 1268.12, 1304.35, 1340.58, 1376.81, 1413.04, 1449.28, 1485.51, 1521.74, 1557.97, 1594.2, 1630.43, 1666.67, 1702.9, 1739.13, 1775.36, 1811.59, 1847.83, 1884.06, 1920.29, 1956.52, 1992.75, 2028.99, 2065.22, 2101.45, 2137.68, 2173.91, 2210.15, 2246.38, 2282.61, 2318.84, 2355.07, 2391.3, 2427.54, 2463.77, 2500, 2536.23, 2572.46, 2608.7, 2644.93, 2681.16, 2717.39, 2753.62, 2789.85, 2826.09, 2862.32, 2898.55, 2934.78, 2971.01, 3007.25, 3043.48, 3079.71, 3115.94, 3152.17, 3188.41, 3224.64, 3260.87, 3297.1, 3333.33, 3369.57, 3405.8, 3442.03, 3478.26, 3514.49, 3550.72, 3586.96, 3623.19, 3659.42, 3695.65, 3731.88, 3768.12, 3804.35, 3840.58, 3876.81, 3913.04, 3949.28, 3985.51, 4021.74, 4057.97, 4094.2, 4130.43, 4166.67, 4202.9, 4239.13, 4275.36, 4311.59, 4347.83, 4384.06, 4420.29, 4456.52, 4492.75, 4528.99, 4565.22, 4601.45, 4637.68, 4673.91, 4710.15, 4746.38, 4782.61, 4818.84, 4855.07, 4891.3, 4927.54, 4963.77, 5000, 5036.23, 5072.46, 5108.7, 5144.93, 5181.16, 5217.39, 5253.62, 5289.85, 5326.09, 5362.32, 5398.55, 5434.78, 5471.01, 5507.25, 5543.48, 5579.71, 5615.94, 5652.17, 5688.41, 5724.64, 5760.87, 5797.1, 5833.33, 5869.57, 5905.8, 5942.03, 5978.26, 6014.49, 6050.72, 6086.96, 6123.19, 6159.42, 6195.65, 6231.88, 6268.12, 6304.35, 6340.58, 6376.81, 6413.04, 6449.28, 6485.51, 6521.74, 6557.97, 6594.2, 6630.43, 6666.67, 6702.9, 6739.13, 6775.36, 6811.59, 6847.83, 6884.06, 6920.29, 6956.52, 6992.75, 7028.99, 7065.22, 7101.45, 7137.68, 7173.91, 7210.15, 7246.38, 7282.61, 7318.84, 7355.07, 7391.3, 7427.54, 7463.77, 7500, 7536.23, 7572.46, 7608.7, 7644.93, 7681.16, 7717.39, 7753.62, 7789.85, 7826.09, 7862.32, 7898.55, 7934.78, 7971.01, 8007.25, 8043.48, 8079.71, 8115.94, 8152.17, 8188.41, 8224.64, 8260.87, 8297.1, 8333.33, 8369.57, 8405.8, 8442.03, 8478.26, 8514.49, 8550.72, 8586.96, 8623.19, 8659.42, 8695.65, 8731.88, 8768.12, 8804.35, 8840.58, 8876.81, 8913.04, 8949.28, 8985.51, 9021.74, 9057.97, 9094.2, 9130.43, 9166.67, 9202.9, 9239.13, 9275.36, 9311.59, 9347.83, 9384.06, 9420.29, 9456.52, 9492.75, 9528.99, 9565.22, 9601.45, 9637.68, 9673.91, 9710.14, 9746.38, 9782.61, 9818.84, 9855.07, 9891.3, 9927.54, 9963.77, 10000, 10036.23, 10072.46, 10108.7, 10144.93, 10181.16, 10217.39, 10253.62, 10289.86, 10326.09, 10362.32, 10398.55, 10434.78, 10471.01, 10507.25, 10543.48, 10579.71, 10615.94, 10652.17, 10688.41, 10724.64, 10760.87, 10797.1, 10833.33, 10869.57, 10905.8, 10942.03, 10978.26, 11014.49, 11050.72, 11086.96, 11123.19, 11159.42, 11195.65, 11231.88, 11268.12, 11304.35, 11340.58, 11376.81, 11413.04, 11449.28, 11485.51, 11521.74, 11557.97, 11594.2, 11630.43, 11666.67, 11702.9, 11739.13, 11775.36, 11811.59, 11847.83, 11884.06, 11920.29, 11956.52, 11992.75, 12028.99, 12065.22, 12101.45, 12137.68, 12173.91, 12210.14, 12246.38, 12282.61, 12318.84, 12355.07, 12391.3, 12427.54, 12463.77, 12500, 12536.23, 12572.46, 12608.7, 12644.93, 12681.16, 12717.39, 12753.62, 12789.86, 12826.09, 12862.32, 12898.55, 12934.78, 12971.01, 13007.25, 13043.48, 13079.71, 13115.94, 13152.17, 13188.41, 13224.64, 13260.87, 13297.1, 13333.33, 13369.57, 13405.8, 13442.03, 13478.26, 13514.49, 13550.72, 13586.96, 13623.19, 13659.42, 13695.65, 13731.88, 13768.12, 13804.35, 13840.58, 13876.81, 13913.04, 13949.28, 13985.51, 14021.74, 14057.97, 14094.2, 14130.43, 14166.67, 14202.9, 14239.13, 14275.36, 14311.59, 14347.83, 14384.06, 14420.29, 14456.52, 14492.75, 14528.99, 14565.22, 14601.45, 14637.68, 14673.91, 14710.14, 14746.38, 14782.61, 14818.84, 14855.07, 14891.3, 14927.54, 14963.77, 15000, 15036.23, 15072.46, 15108.7, 15144.93, 15181.16, 15217.39, 15253.62, 15289.86, 15326.09, 15362.32, 15398.55, 15434.78, 15471.01, 15507.25, 15543.48, 15579.71, 15615.94, 15652.17, 15688.41, 15724.64, 15760.87, 15797.1, 15833.33, 15869.57, 15905.8, 15942.03, 15978.26, 16014.49, 16050.72, 16086.96, 16123.19, 16159.42, 16195.65, 16231.88, 16268.12, 16304.35, 16340.58, 16376.81, 16413.04, 16449.28, 16485.51, 16521.74, 16557.97, 16594.2, 16630.44, 16666.67, 16702.9, 16739.13, 16775.36, 16811.59, 16847.83, 16884.06, 16920.29, 16956.52, 16992.75, 17028.99, 17065.22, 17101.45, 17137.68, 17173.91, 17210.14, 17246.38, 17282.61, 17318.84, 17355.07, 17391.3, 17427.54, 17463.77, 17500, 17536.23, 17572.46, 17608.7, 17644.93, 17681.16, 17717.39, 17753.62, 17789.86, 17826.09, 17862.32, 17898.55, 17934.78, 17971.01, 18007.25, 18043.48, 18079.71, 18115.94, 18152.17, 18188.41, 18224.64, 18260.87, 18297.1, 18333.33, 18369.56, 18405.8, 18442.03, 18478.26, 18514.49]
x2=json.dumps(x1) # paso lista a string

print("Data en x1:",x1,"\n\nData en x2:", x2, "\n")
print(type(x1), type(x2))

x3=json.loads(x2) # paso string a lista
print(type(x2), type(x3))