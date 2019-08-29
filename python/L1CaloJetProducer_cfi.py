import FWCore.ParameterSet.Config as cms

L1CaloJetProducer = cms.EDProducer("L1CaloJetProducer",
    debug = cms.bool(False),
    HcalTpEtMin = cms.double(0.5),
    EcalTpEtMin = cms.double(0.5),
    HGCalHadTpEtMin = cms.double(0.5),
    HGCalEmTpEtMin = cms.double(0.5),
    HFTpEtMin = cms.double(0.5),
    EtMinForSeedHit = cms.double(2.5), # was 2.5
    EtMinForCollection = cms.double(10),
    EtMinForTauCollection = cms.double(10),
    L1TrackInputTag = cms.InputTag("TTTracksFromTracklet", "Level1TTTracks"), #Victor's edit: add track input tag
    l1CaloTowers = cms.InputTag("L1TowerCalibrationProducer","L1CaloTowerCalibratedCollection"),
    L1CrystalClustersInputTag = cms.InputTag("L1EGammaClusterEmuProducer", "L1EGXtalClusterEmulator"),
    #L1HgcalTowersInputTag = cms.InputTag("hgcalTriggerPrimitiveDigiProducer","tower"),
    #hcalDigis = cms.InputTag("simHcalTriggerPrimitiveDigis"),

    # Calibrations derived 18 April 2019 on 10_3_X MTD QCD sample
	jetPtBins = cms.vdouble([ 0.0,5.0,7.5,10.0,12.5,15.0,17.5,20.0,22.5,25.0,27.5,30.0,35.0,40.0,45.0,50.0,55.0,60.0,65.0,70.0,75.0,80.0,85.0,90.0,95.0,100.0,110.0,120.0,130.0,140.0,150.0,160.0,170.0,180.0,190.0,200.0,225.0,250.0,275.0,300.0,325.0,400.0,500.0]),
	emFractionBinsBarrel = cms.vdouble([ 0.00,0.31,0.40,0.47,0.53,0.58,0.63,0.69,0.76,0.84,1.05]),
	absEtaBinsBarrel = cms.vdouble([ 0.00,0.30,0.60,1.00,1.50]),
	jetCalibrationsBarrel = cms.vdouble([
		1.640, 1.626, 1.617, 1.608, 1.599, 1.591, 1.583, 1.574, 1.566, 1.559, 1.551, 1.540, 1.525, 1.512, 1.498, 1.486, 1.474, 1.462, 1.451, 1.441, 1.431, 1.421, 1.412, 1.404, 1.396, 1.385, 1.372, 1.360, 1.350, 1.341, 1.334, 1.329, 1.325, 1.322, 1.320, 1.320, 1.325, 1.336, 1.352, 1.373, 1.428, 1.553,
		1.855, 1.839, 1.829, 1.819, 1.809, 1.800, 1.790, 1.781, 1.771, 1.762, 1.753, 1.740, 1.723, 1.706, 1.690, 1.674, 1.659, 1.645, 1.631, 1.617, 1.604, 1.591, 1.579, 1.568, 1.556, 1.540, 1.520, 1.501, 1.484, 1.469, 1.454, 1.441, 1.430, 1.419, 1.410, 1.396, 1.382, 1.374, 1.370, 1.372, 1.386, 1.443,
		1.993, 1.978, 1.967, 1.957, 1.947, 1.937, 1.927, 1.918, 1.908, 1.898, 1.889, 1.875, 1.857, 1.839, 1.822, 1.805, 1.789, 1.773, 1.757, 1.742, 1.727, 1.713, 1.699, 1.685, 1.672, 1.653, 1.629, 1.606, 1.584, 1.564, 1.545, 1.527, 1.511, 1.495, 1.481, 1.459, 1.434, 1.414, 1.400, 1.392, 1.391, 1.431,
		2.155, 2.135, 2.123, 2.110, 2.097, 2.085, 2.073, 2.061, 2.049, 2.037, 2.026, 2.009, 1.987, 1.965, 1.944, 1.924, 1.905, 1.885, 1.867, 1.849, 1.832, 1.815, 1.798, 1.783, 1.767, 1.745, 1.717, 1.691, 1.666, 1.643, 1.622, 1.602, 1.583, 1.566, 1.550, 1.525, 1.495, 1.470, 1.451, 1.437, 1.422, 1.424,
		2.305, 2.284, 2.271, 2.257, 2.244, 2.231, 2.218, 2.205, 2.193, 2.180, 2.168, 2.150, 2.126, 2.103, 2.081, 2.059, 2.037, 2.017, 1.996, 1.976, 1.957, 1.938, 1.920, 1.902, 1.884, 1.859, 1.827, 1.797, 1.768, 1.741, 1.715, 1.691, 1.668, 1.647, 1.627, 1.595, 1.556, 1.523, 1.497, 1.477, 1.451, 1.446,
		2.555, 2.528, 2.510, 2.492, 2.474, 2.457, 2.440, 2.423, 2.406, 2.390, 2.373, 2.349, 2.318, 2.288, 2.258, 2.229, 2.201, 2.174, 2.148, 2.122, 2.097, 2.072, 2.049, 2.026, 2.004, 1.971, 1.930, 1.892, 1.856, 1.822, 1.790, 1.761, 1.733, 1.707, 1.683, 1.645, 1.600, 1.563, 1.535, 1.515, 1.493, 1.505,
		2.850, 2.815, 2.792, 2.770, 2.747, 2.725, 2.703, 2.682, 2.661, 2.640, 2.619, 2.589, 2.549, 2.511, 2.473, 2.437, 2.401, 2.367, 2.334, 2.301, 2.270, 2.239, 2.209, 2.181, 2.153, 2.112, 2.062, 2.014, 1.969, 1.927, 1.888, 1.852, 1.818, 1.787, 1.758, 1.712, 1.658, 1.616, 1.585, 1.563, 1.544, 1.576,
		3.386, 3.325, 3.286, 3.248, 3.210, 3.174, 3.138, 3.103, 3.069, 3.036, 3.004, 2.956, 2.896, 2.838, 2.783, 2.730, 2.680, 2.632, 2.586, 2.543, 2.501, 2.461, 2.423, 2.387, 2.352, 2.303, 2.242, 2.187, 2.136, 2.090, 2.047, 2.008, 1.973, 1.940, 1.910, 1.863, 1.806, 1.760, 1.721, 1.688, 1.636, 1.572,
		4.450, 4.344, 4.276, 4.210, 4.146, 4.083, 4.022, 3.962, 3.904, 3.847, 3.792, 3.712, 3.610, 3.513, 3.420, 3.333, 3.250, 3.171, 3.096, 3.025, 2.958, 2.894, 2.833, 2.776, 2.721, 2.645, 2.552, 2.468, 2.393, 2.325, 2.265, 2.210, 2.162, 2.118, 2.079, 2.021, 1.956, 1.908, 1.873, 1.849, 1.822, 1.818,
		6.912, 6.764, 6.667, 6.571, 6.477, 6.384, 6.293, 6.203, 6.114, 6.027, 5.941, 5.814, 5.650, 5.491, 5.336, 5.187, 5.042, 4.903, 4.767, 4.637, 4.511, 4.389, 4.272, 4.159, 4.050, 3.894, 3.700, 3.522, 3.359, 3.210, 3.076, 2.954, 2.846, 2.750, 2.667, 2.549, 2.438, 2.390, 2.400, 2.463, 2.731, 3.577,
		1.536, 1.527, 1.521, 1.515, 1.509, 1.503, 1.497, 1.491, 1.486, 1.480, 1.475, 1.467, 1.457, 1.447, 1.437, 1.428, 1.419, 1.411, 1.403, 1.395, 1.388, 1.380, 1.374, 1.367, 1.361, 1.353, 1.342, 1.333, 1.325, 1.319, 1.313, 1.309, 1.305, 1.303, 1.302, 1.302, 1.307, 1.317, 1.333, 1.354, 1.409, 1.544,
		1.740, 1.730, 1.723, 1.716, 1.709, 1.702, 1.696, 1.689, 1.683, 1.676, 1.670, 1.661, 1.648, 1.636, 1.624, 1.613, 1.602, 1.590, 1.580, 1.569, 1.559, 1.549, 1.539, 1.530, 1.521, 1.507, 1.490, 1.474, 1.459, 1.445, 1.432, 1.420, 1.409, 1.399, 1.389, 1.375, 1.360, 1.350, 1.345, 1.346, 1.363, 1.439,
		1.869, 1.858, 1.851, 1.843, 1.836, 1.829, 1.822, 1.815, 1.808, 1.801, 1.795, 1.785, 1.771, 1.758, 1.746, 1.733, 1.721, 1.709, 1.697, 1.686, 1.674, 1.663, 1.652, 1.642, 1.631, 1.616, 1.597, 1.578, 1.560, 1.543, 1.527, 1.512, 1.498, 1.485, 1.472, 1.452, 1.427, 1.408, 1.393, 1.383, 1.377, 1.407,
		2.010, 1.997, 1.988, 1.980, 1.971, 1.963, 1.954, 1.946, 1.938, 1.930, 1.922, 1.910, 1.894, 1.879, 1.864, 1.849, 1.834, 1.820, 1.806, 1.792, 1.779, 1.766, 1.753, 1.740, 1.728, 1.709, 1.686, 1.664, 1.642, 1.622, 1.603, 1.584, 1.567, 1.550, 1.534, 1.509, 1.478, 1.451, 1.430, 1.414, 1.396, 1.407,
		2.171, 2.155, 2.144, 2.134, 2.123, 2.113, 2.103, 2.093, 2.083, 2.073, 2.063, 2.049, 2.030, 2.012, 1.994, 1.976, 1.959, 1.942, 1.925, 1.909, 1.893, 1.877, 1.862, 1.847, 1.833, 1.812, 1.785, 1.759, 1.734, 1.710, 1.688, 1.667, 1.646, 1.627, 1.609, 1.579, 1.542, 1.509, 1.482, 1.459, 1.426, 1.401,
		2.366, 2.345, 2.332, 2.319, 2.306, 2.293, 2.280, 2.268, 2.255, 2.243, 2.231, 2.213, 2.189, 2.166, 2.144, 2.122, 2.100, 2.079, 2.058, 2.038, 2.018, 1.999, 1.980, 1.962, 1.944, 1.918, 1.884, 1.853, 1.822, 1.794, 1.766, 1.741, 1.716, 1.693, 1.671, 1.636, 1.591, 1.554, 1.522, 1.497, 1.461, 1.441,
		2.680, 2.647, 2.626, 2.605, 2.584, 2.564, 2.544, 2.525, 2.506, 2.487, 2.469, 2.442, 2.407, 2.373, 2.340, 2.309, 2.278, 2.249, 2.221, 2.193, 2.167, 2.142, 2.117, 2.093, 2.070, 2.038, 1.996, 1.958, 1.922, 1.888, 1.857, 1.828, 1.801, 1.775, 1.751, 1.713, 1.666, 1.626, 1.592, 1.563, 1.516, 1.459,
		3.093, 3.051, 3.023, 2.995, 2.969, 2.942, 2.916, 2.890, 2.865, 2.840, 2.816, 2.780, 2.733, 2.688, 2.644, 2.602, 2.561, 2.522, 2.484, 2.447, 2.411, 2.376, 2.343, 2.311, 2.280, 2.235, 2.178, 2.126, 2.077, 2.031, 1.988, 1.949, 1.912, 1.878, 1.846, 1.796, 1.735, 1.685, 1.646, 1.614, 1.571, 1.543,
		4.080, 3.996, 3.941, 3.888, 3.836, 3.785, 3.735, 3.686, 3.638, 3.591, 3.546, 3.479, 3.393, 3.312, 3.233, 3.159, 3.087, 3.019, 2.953, 2.891, 2.831, 2.774, 2.720, 2.668, 2.618, 2.548, 2.462, 2.383, 2.312, 2.247, 2.188, 2.134, 2.086, 2.042, 2.003, 1.943, 1.875, 1.825, 1.788, 1.763, 1.738, 1.747,
		6.659, 6.494, 6.387, 6.282, 6.179, 6.078, 5.978, 5.881, 5.785, 5.691, 5.599, 5.463, 5.289, 5.122, 4.961, 4.806, 4.657, 4.514, 4.378, 4.246, 4.121, 4.001, 3.886, 3.776, 3.671, 3.522, 3.341, 3.177, 3.030, 2.899, 2.783, 2.682, 2.594, 2.519, 2.456, 2.373, 2.311, 2.307, 2.355, 2.447, 2.743, 3.536,
		1.519, 1.512, 1.507, 1.502, 1.498, 1.493, 1.488, 1.484, 1.479, 1.475, 1.471, 1.464, 1.456, 1.448, 1.440, 1.433, 1.425, 1.418, 1.412, 1.405, 1.399, 1.393, 1.387, 1.381, 1.376, 1.369, 1.359, 1.351, 1.344, 1.337, 1.332, 1.327, 1.323, 1.320, 1.318, 1.317, 1.319, 1.326, 1.339, 1.356, 1.404, 1.530,
		1.719, 1.710, 1.705, 1.699, 1.693, 1.688, 1.682, 1.677, 1.671, 1.666, 1.661, 1.653, 1.642, 1.632, 1.622, 1.613, 1.603, 1.594, 1.584, 1.575, 1.567, 1.558, 1.550, 1.541, 1.533, 1.522, 1.507, 1.492, 1.479, 1.466, 1.454, 1.443, 1.432, 1.422, 1.413, 1.399, 1.382, 1.369, 1.361, 1.356, 1.359, 1.401,
		1.860, 1.851, 1.844, 1.838, 1.832, 1.826, 1.820, 1.814, 1.808, 1.802, 1.796, 1.787, 1.775, 1.764, 1.753, 1.742, 1.731, 1.720, 1.710, 1.699, 1.689, 1.679, 1.669, 1.660, 1.650, 1.636, 1.618, 1.601, 1.584, 1.568, 1.553, 1.538, 1.524, 1.511, 1.498, 1.478, 1.451, 1.428, 1.410, 1.394, 1.374, 1.373,
		1.993, 1.982, 1.974, 1.967, 1.960, 1.953, 1.946, 1.938, 1.931, 1.924, 1.917, 1.907, 1.894, 1.880, 1.867, 1.854, 1.841, 1.828, 1.816, 1.804, 1.792, 1.780, 1.768, 1.757, 1.746, 1.729, 1.708, 1.687, 1.667, 1.648, 1.629, 1.612, 1.595, 1.578, 1.563, 1.537, 1.504, 1.475, 1.451, 1.430, 1.402, 1.388,
		2.146, 2.131, 2.122, 2.113, 2.104, 2.095, 2.086, 2.077, 2.068, 2.059, 2.051, 2.038, 2.021, 2.004, 1.988, 1.972, 1.957, 1.941, 1.926, 1.911, 1.897, 1.883, 1.869, 1.855, 1.842, 1.822, 1.797, 1.773, 1.749, 1.727, 1.706, 1.685, 1.665, 1.647, 1.629, 1.599, 1.561, 1.527, 1.497, 1.472, 1.431, 1.389,
		2.336, 2.319, 2.307, 2.296, 2.285, 2.273, 2.262, 2.251, 2.240, 2.230, 2.219, 2.203, 2.182, 2.162, 2.142, 2.122, 2.103, 2.084, 2.065, 2.047, 2.029, 2.012, 1.994, 1.978, 1.961, 1.937, 1.906, 1.876, 1.848, 1.820, 1.794, 1.769, 1.745, 1.722, 1.700, 1.665, 1.618, 1.578, 1.543, 1.512, 1.465, 1.420,
		2.594, 2.571, 2.556, 2.541, 2.526, 2.511, 2.497, 2.482, 2.468, 2.453, 2.439, 2.419, 2.391, 2.364, 2.338, 2.312, 2.287, 2.262, 2.238, 2.214, 2.191, 2.168, 2.146, 2.124, 2.103, 2.072, 2.032, 1.993, 1.957, 1.922, 1.889, 1.857, 1.827, 1.799, 1.772, 1.728, 1.672, 1.625, 1.585, 1.552, 1.507, 1.482,
		3.016, 2.982, 2.959, 2.937, 2.915, 2.893, 2.872, 2.851, 2.830, 2.809, 2.788, 2.758, 2.718, 2.679, 2.641, 2.604, 2.568, 2.533, 2.499, 2.465, 2.432, 2.400, 2.369, 2.339, 2.309, 2.266, 2.211, 2.160, 2.111, 2.064, 2.020, 1.979, 1.940, 1.904, 1.870, 1.815, 1.749, 1.694, 1.651, 1.618, 1.580, 1.590,
		4.054, 3.966, 3.909, 3.854, 3.800, 3.747, 3.696, 3.646, 3.597, 3.549, 3.503, 3.435, 3.348, 3.266, 3.187, 3.112, 3.041, 2.974, 2.909, 2.848, 2.790, 2.734, 2.681, 2.631, 2.583, 2.516, 2.434, 2.360, 2.292, 2.232, 2.178, 2.128, 2.084, 2.045, 2.009, 1.955, 1.895, 1.850, 1.817, 1.794, 1.769, 1.766,
		6.752, 6.570, 6.452, 6.337, 6.224, 6.113, 6.004, 5.898, 5.795, 5.693, 5.594, 5.449, 5.263, 5.085, 4.915, 4.752, 4.597, 4.449, 4.308, 4.173, 4.045, 3.923, 3.808, 3.697, 3.593, 3.446, 3.269, 3.110, 2.969, 2.846, 2.738, 2.644, 2.564, 2.497, 2.442, 2.372, 2.323, 2.327, 2.374, 2.459, 2.718, 3.371,
		1.615, 1.605, 1.599, 1.593, 1.587, 1.581, 1.575, 1.570, 1.564, 1.558, 1.553, 1.545, 1.534, 1.524, 1.514, 1.504, 1.494, 1.485, 1.476, 1.468, 1.460, 1.452, 1.444, 1.437, 1.429, 1.419, 1.407, 1.395, 1.385, 1.375, 1.367, 1.360, 1.353, 1.348, 1.344, 1.339, 1.336, 1.340, 1.349, 1.364, 1.410, 1.537,
		1.867, 1.856, 1.849, 1.841, 1.834, 1.827, 1.820, 1.813, 1.806, 1.799, 1.792, 1.782, 1.768, 1.755, 1.742, 1.730, 1.718, 1.705, 1.694, 1.682, 1.671, 1.660, 1.649, 1.638, 1.628, 1.613, 1.594, 1.575, 1.558, 1.542, 1.526, 1.512, 1.498, 1.485, 1.474, 1.455, 1.433, 1.417, 1.406, 1.401, 1.404, 1.458,
		2.037, 2.025, 2.017, 2.009, 2.001, 1.993, 1.985, 1.977, 1.970, 1.962, 1.954, 1.943, 1.928, 1.914, 1.899, 1.885, 1.871, 1.858, 1.844, 1.831, 1.818, 1.805, 1.793, 1.781, 1.769, 1.751, 1.728, 1.707, 1.686, 1.666, 1.647, 1.629, 1.612, 1.596, 1.580, 1.555, 1.524, 1.498, 1.477, 1.462, 1.445, 1.461,
		2.206, 2.192, 2.183, 2.174, 2.165, 2.156, 2.148, 2.139, 2.130, 2.122, 2.113, 2.101, 2.084, 2.068, 2.052, 2.037, 2.021, 2.006, 1.992, 1.977, 1.963, 1.949, 1.935, 1.922, 1.908, 1.889, 1.864, 1.840, 1.817, 1.795, 1.773, 1.753, 1.733, 1.714, 1.696, 1.666, 1.628, 1.593, 1.562, 1.536, 1.492, 1.444,
		2.401, 2.385, 2.375, 2.365, 2.355, 2.346, 2.336, 2.326, 2.317, 2.307, 2.298, 2.284, 2.265, 2.247, 2.229, 2.212, 2.195, 2.178, 2.161, 2.144, 2.128, 2.112, 2.097, 2.081, 2.066, 2.044, 2.015, 1.988, 1.961, 1.935, 1.910, 1.886, 1.862, 1.840, 1.818, 1.782, 1.735, 1.692, 1.653, 1.618, 1.559, 1.487,
		2.637, 2.620, 2.609, 2.599, 2.588, 2.577, 2.567, 2.556, 2.546, 2.536, 2.525, 2.510, 2.490, 2.470, 2.451, 2.432, 2.413, 2.394, 2.376, 2.357, 2.339, 2.322, 2.304, 2.287, 2.270, 2.245, 2.213, 2.182, 2.151, 2.122, 2.093, 2.065, 2.038, 2.012, 1.986, 1.944, 1.887, 1.835, 1.787, 1.742, 1.665, 1.561,
		2.952, 2.935, 2.924, 2.913, 2.902, 2.891, 2.879, 2.868, 2.858, 2.847, 2.836, 2.820, 2.798, 2.777, 2.756, 2.736, 2.715, 2.695, 2.675, 2.655, 2.635, 2.616, 2.597, 2.578, 2.559, 2.531, 2.495, 2.459, 2.424, 2.390, 2.357, 2.325, 2.293, 2.262, 2.233, 2.182, 2.114, 2.050, 1.992, 1.938, 1.844, 1.721,
		3.403, 3.388, 3.378, 3.368, 3.359, 3.349, 3.339, 3.330, 3.320, 3.311, 3.301, 3.287, 3.268, 3.249, 3.231, 3.213, 3.194, 3.176, 3.158, 3.140, 3.123, 3.105, 3.088, 3.070, 3.053, 3.028, 2.994, 2.961, 2.928, 2.896, 2.865, 2.834, 2.803, 2.773, 2.743, 2.692, 2.621, 2.554, 2.488, 2.425, 2.307, 2.120,
		4.386, 4.363, 4.347, 4.332, 4.317, 4.302, 4.287, 4.272, 4.258, 4.243, 4.229, 4.208, 4.180, 4.153, 4.127, 4.101, 4.075, 4.051, 4.026, 4.003, 3.979, 3.956, 3.934, 3.912, 3.891, 3.860, 3.821, 3.783, 3.747, 3.712, 3.680, 3.649, 3.620, 3.592, 3.566, 3.524, 3.471, 3.427, 3.390, 3.361, 3.323, 3.312,
		6.918, 6.864, 6.829, 6.794, 6.759, 6.724, 6.690, 6.656, 6.623, 6.589, 6.556, 6.507, 6.443, 6.380, 6.319, 6.258, 6.199, 6.142, 6.085, 6.030, 5.976, 5.923, 5.872, 5.821, 5.773, 5.702, 5.612, 5.528, 5.449, 5.376, 5.308, 5.245, 5.189, 5.138, 5.092, 5.027, 4.964, 4.939, 4.953, 5.005, 5.233, 6.041,
	]),
	emFractionBinsHGCal = cms.vdouble([ 0.00,0.55,0.67,0.77,1.05]),
	absEtaBinsHGCal = cms.vdouble([ 1.50,1.90,2.40,3.00]),
	jetCalibrationsHGCal = cms.vdouble([
		1.395, 1.394, 1.394, 1.394, 1.394, 1.394, 1.393, 1.393, 1.393, 1.393, 1.393, 1.393, 1.392, 1.392, 1.392, 1.391, 1.391, 1.391, 1.390, 1.390, 1.390, 1.389, 1.389, 1.389, 1.388, 1.388, 1.387, 1.387, 1.386, 1.385, 1.385, 1.384, 1.383, 1.383, 1.382, 1.381, 1.379, 1.378, 1.376, 1.374, 1.371, 1.365,
		1.575, 1.574, 1.574, 1.574, 1.574, 1.574, 1.573, 1.573, 1.573, 1.573, 1.572, 1.572, 1.572, 1.571, 1.571, 1.570, 1.570, 1.569, 1.569, 1.569, 1.568, 1.568, 1.567, 1.567, 1.566, 1.566, 1.565, 1.564, 1.563, 1.562, 1.561, 1.560, 1.559, 1.559, 1.558, 1.556, 1.554, 1.552, 1.549, 1.547, 1.543, 1.535,
		1.846, 1.845, 1.845, 1.844, 1.844, 1.843, 1.843, 1.842, 1.842, 1.841, 1.841, 1.840, 1.839, 1.839, 1.838, 1.837, 1.836, 1.835, 1.834, 1.833, 1.832, 1.831, 1.830, 1.829, 1.829, 1.827, 1.825, 1.824, 1.822, 1.820, 1.818, 1.816, 1.814, 1.813, 1.811, 1.808, 1.803, 1.799, 1.794, 1.790, 1.780, 1.765,
		3.377, 3.355, 3.341, 3.326, 3.312, 3.298, 3.283, 3.269, 3.255, 3.242, 3.228, 3.207, 3.180, 3.154, 3.128, 3.102, 3.077, 3.051, 3.027, 3.002, 2.979, 2.955, 2.932, 2.909, 2.886, 2.853, 2.811, 2.769, 2.729, 2.691, 2.654, 2.618, 2.584, 2.551, 2.519, 2.467, 2.400, 2.341, 2.291, 2.248, 2.186, 2.149,
		1.085, 1.087, 1.088, 1.089, 1.090, 1.091, 1.092, 1.093, 1.094, 1.095, 1.097, 1.098, 1.100, 1.103, 1.105, 1.107, 1.109, 1.111, 1.113, 1.116, 1.118, 1.120, 1.122, 1.124, 1.126, 1.130, 1.134, 1.138, 1.143, 1.147, 1.151, 1.156, 1.160, 1.164, 1.169, 1.176, 1.187, 1.198, 1.209, 1.220, 1.242, 1.280,
		61.559, 11.087, 4.083, 1.971, 1.335, 1.145, 1.090, 1.074, 1.072, 1.072, 1.074, 1.078, 1.083, 1.088, 1.093, 1.098, 1.103, 1.108, 1.112, 1.117, 1.122, 1.127, 1.132, 1.137, 1.142, 1.149, 1.159, 1.169, 1.179, 1.189, 1.199, 1.209, 1.218, 1.228, 1.238, 1.255, 1.280, 1.305, 1.329, 1.354, 1.403, 1.490,
		89.821, 15.567, 5.416, 2.387, 1.485, 1.218, 1.140, 1.119, 1.115, 1.116, 1.118, 1.123, 1.129, 1.135, 1.141, 1.147, 1.153, 1.159, 1.165, 1.171, 1.178, 1.184, 1.190, 1.196, 1.202, 1.211, 1.223, 1.236, 1.248, 1.260, 1.272, 1.284, 1.297, 1.309, 1.321, 1.342, 1.373, 1.403, 1.434, 1.464, 1.525, 1.632,
		83.760, 19.529, 8.102, 3.961, 2.461, 1.918, 1.721, 1.650, 1.624, 1.615, 1.612, 1.611, 1.611, 1.611, 1.612, 1.612, 1.613, 1.613, 1.614, 1.614, 1.615, 1.616, 1.616, 1.617, 1.617, 1.618, 1.619, 1.620, 1.621, 1.622, 1.623, 1.624, 1.625, 1.626, 1.628, 1.629, 1.632, 1.635, 1.637, 1.640, 1.645, 1.655,
		1.262, 1.261, 1.260, 1.259, 1.259, 1.258, 1.257, 1.256, 1.256, 1.255, 1.254, 1.253, 1.252, 1.250, 1.249, 1.247, 1.246, 1.244, 1.243, 1.242, 1.240, 1.239, 1.237, 1.236, 1.234, 1.232, 1.229, 1.226, 1.223, 1.221, 1.218, 1.215, 1.212, 1.209, 1.206, 1.201, 1.194, 1.186, 1.179, 1.172, 1.157, 1.132,
		1.328, 1.327, 1.326, 1.326, 1.325, 1.325, 1.324, 1.324, 1.323, 1.323, 1.322, 1.322, 1.321, 1.320, 1.319, 1.318, 1.317, 1.316, 1.315, 1.314, 1.313, 1.312, 1.311, 1.310, 1.309, 1.308, 1.306, 1.304, 1.302, 1.300, 1.298, 1.296, 1.294, 1.292, 1.290, 1.287, 1.282, 1.277, 1.272, 1.267, 1.257, 1.240,
		1.463, 1.461, 1.460, 1.459, 1.458, 1.457, 1.456, 1.455, 1.454, 1.453, 1.452, 1.451, 1.449, 1.447, 1.445, 1.443, 1.440, 1.438, 1.436, 1.434, 1.432, 1.430, 1.428, 1.426, 1.424, 1.421, 1.417, 1.413, 1.409, 1.405, 1.401, 1.397, 1.393, 1.389, 1.385, 1.377, 1.367, 1.357, 1.347, 1.337, 1.316, 1.281,
		44.899, 14.731, 7.692, 4.568, 3.180, 2.562, 2.285, 2.159, 2.101, 2.072, 2.057, 2.043, 2.031, 2.021, 2.011, 2.001, 1.991, 1.982, 1.972, 1.962, 1.952, 1.942, 1.932, 1.922, 1.912, 1.897, 1.878, 1.858, 1.838, 1.818, 1.798, 1.779, 1.759, 1.739, 1.719, 1.685, 1.635, 1.586, 1.536, 1.487, 1.387, 1.214,
	]),
	emFractionBinsHF = cms.vdouble([ 0.00,1.05]),
	absEtaBinsHF = cms.vdouble([ 3.00,3.60,6.00]),
	jetCalibrationsHF = cms.vdouble([
		3.223, 2.140, 1.683, 1.364, 1.142, 0.987, 0.879, 0.804, 0.752, 0.716, 0.691, 0.667, 0.651, 0.644, 0.641, 0.641, 0.641, 0.642, 0.644, 0.645, 0.647, 0.648, 0.650, 0.651, 0.653, 0.655, 0.658, 0.662, 0.665, 0.668, 0.671, 0.674, 0.677, 0.681, 0.684, 0.689, 0.697, 0.705, 0.713, 0.721, 0.736, 0.764,
		2.598, 1.813, 1.462, 1.206, 1.019, 0.883, 0.783, 0.711, 0.658, 0.620, 0.592, 0.564, 0.543, 0.532, 0.526, 0.524, 0.523, 0.524, 0.524, 0.525, 0.526, 0.527, 0.528, 0.529, 0.530, 0.532, 0.534, 0.536, 0.538, 0.541, 0.543, 0.545, 0.547, 0.549, 0.552, 0.556, 0.561, 0.567, 0.572, 0.578, 0.589, 0.608,
	]),

    # Testing tau calibrations derived for March workshop, 20 March 2019
	tauPtBins = cms.vdouble([ 0.0,5.0,7.5,10.0,12.5,15.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,55.0,60.0,70.0,80.0,100.0,150.0,200.0]),
	tauAbsEtaBinsBarrel = cms.vdouble([ 0.00,0.30,0.60,1.00,1.50]),
	tauL1egInfoBarrel = cms.VPSet(
		cms.PSet(
			l1egCount = cms.double( 0.0 ),
			l1egEmFractions = cms.vdouble([ 0.0, 0.091, 0.317, 1.05]),
		),
		cms.PSet(
			l1egCount = cms.double( 1.0 ),
			l1egEmFractions = cms.vdouble([ 0.0, 0.634, 0.888, 1.05]),
		),
		cms.PSet(
			l1egCount = cms.double( 2.0 ),
			l1egEmFractions = cms.vdouble([ 0.0, 0.821, 0.957, 1.05]),
		),
	),
	tauCalibrationsBarrel = cms.vdouble([
		1.917, 1.714, 1.605, 1.514, 1.437, 1.344, 1.252, 1.188, 1.142, 1.110, 1.087, 1.071, 1.059, 1.051, 1.044, 1.038, 1.034, 1.032, 1.032,
		1.856, 1.729, 1.655, 1.589, 1.530, 1.453, 1.369, 1.301, 1.248, 1.205, 1.170, 1.143, 1.121, 1.103, 1.084, 1.066, 1.050, 1.037, 1.034,
		2.053, 1.884, 1.788, 1.702, 1.627, 1.530, 1.426, 1.345, 1.282, 1.233, 1.194, 1.164, 1.141, 1.122, 1.102, 1.084, 1.070, 1.059, 1.057,
		1.783, 1.659, 1.588, 1.524, 1.466, 1.391, 1.309, 1.244, 1.191, 1.149, 1.116, 1.089, 1.068, 1.050, 1.031, 1.013, 0.998, 0.986, 0.983,
		1.896, 1.713, 1.613, 1.527, 1.453, 1.362, 1.270, 1.202, 1.152, 1.115, 1.088, 1.069, 1.054, 1.044, 1.033, 1.024, 1.018, 1.015, 1.014,
		1.936, 1.677, 1.544, 1.437, 1.350, 1.249, 1.156, 1.095, 1.055, 1.028, 1.011, 1.000, 0.992, 0.987, 0.983, 0.980, 0.978, 0.978, 0.978,
		1.850, 1.683, 1.590, 1.509, 1.439, 1.351, 1.258, 1.188, 1.135, 1.096, 1.065, 1.043, 1.025, 1.012, 0.999, 0.987, 0.979, 0.973, 0.972,
		2.066, 1.784, 1.638, 1.517, 1.418, 1.301, 1.189, 1.114, 1.063, 1.029, 1.006, 0.990, 0.979, 0.972, 0.965, 0.961, 0.958, 0.957, 0.957,
		1.074, 1.063, 1.056, 1.050, 1.043, 1.034, 1.022, 1.011, 1.001, 0.992, 0.983, 0.974, 0.966, 0.959, 0.949, 0.937, 0.921, 0.895, 0.874,
		2.053, 1.757, 1.609, 1.489, 1.394, 1.285, 1.186, 1.123, 1.083, 1.057, 1.040, 1.029, 1.022, 1.018, 1.014, 1.012, 1.010, 1.010, 1.010,
		1.733, 1.628, 1.567, 1.513, 1.463, 1.399, 1.328, 1.270, 1.224, 1.187, 1.157, 1.133, 1.114, 1.098, 1.081, 1.064, 1.050, 1.038, 1.035,
		2.009, 1.852, 1.762, 1.682, 1.611, 1.518, 1.417, 1.337, 1.274, 1.224, 1.184, 1.153, 1.128, 1.108, 1.086, 1.066, 1.049, 1.036, 1.033,
		1.806, 1.669, 1.591, 1.522, 1.461, 1.382, 1.296, 1.230, 1.177, 1.136, 1.103, 1.078, 1.058, 1.043, 1.025, 1.010, 0.998, 0.988, 0.986,
		1.944, 1.725, 1.609, 1.512, 1.431, 1.334, 1.239, 1.173, 1.126, 1.094, 1.071, 1.056, 1.045, 1.037, 1.030, 1.024, 1.021, 1.019, 1.019,
		1.900, 1.631, 1.496, 1.389, 1.304, 1.208, 1.122, 1.068, 1.034, 1.012, 0.999, 0.990, 0.984, 0.981, 0.978, 0.976, 0.975, 0.975, 0.975,
		1.682, 1.577, 1.516, 1.460, 1.409, 1.342, 1.266, 1.203, 1.152, 1.109, 1.075, 1.046, 1.022, 1.003, 0.980, 0.958, 0.937, 0.918, 0.913,
		1.928, 1.693, 1.569, 1.466, 1.381, 1.280, 1.183, 1.116, 1.070, 1.038, 1.016, 1.001, 0.991, 0.984, 0.977, 0.973, 0.970, 0.969, 0.969,
		1.067, 1.058, 1.052, 1.047, 1.041, 1.033, 1.023, 1.014, 1.005, 0.997, 0.989, 0.981, 0.974, 0.968, 0.959, 0.948, 0.933, 0.908, 0.886,
		1.883, 1.663, 1.548, 1.453, 1.375, 1.282, 1.193, 1.133, 1.091, 1.063, 1.044, 1.031, 1.022, 1.016, 1.010, 1.006, 1.004, 1.003, 1.003,
		1.688, 1.595, 1.541, 1.492, 1.448, 1.390, 1.325, 1.271, 1.228, 1.193, 1.164, 1.140, 1.121, 1.105, 1.087, 1.070, 1.055, 1.041, 1.037,
		2.251, 2.020, 1.891, 1.779, 1.682, 1.561, 1.434, 1.339, 1.267, 1.213, 1.173, 1.142, 1.119, 1.102, 1.084, 1.069, 1.058, 1.051, 1.050,
		1.799, 1.654, 1.572, 1.501, 1.438, 1.359, 1.275, 1.211, 1.162, 1.125, 1.096, 1.074, 1.057, 1.044, 1.030, 1.019, 1.009, 1.003, 1.002,
		1.780, 1.630, 1.547, 1.475, 1.413, 1.335, 1.254, 1.193, 1.148, 1.114, 1.089, 1.070, 1.056, 1.045, 1.034, 1.025, 1.018, 1.014, 1.013,
		1.750, 1.549, 1.445, 1.359, 1.288, 1.205, 1.126, 1.072, 1.036, 1.012, 0.995, 0.984, 0.976, 0.971, 0.966, 0.963, 0.961, 0.960, 0.960,
		1.736, 1.610, 1.537, 1.472, 1.414, 1.339, 1.257, 1.192, 1.141, 1.100, 1.067, 1.041, 1.021, 1.005, 0.986, 0.970, 0.956, 0.945, 0.942,
		1.961, 1.712, 1.582, 1.474, 1.386, 1.281, 1.181, 1.114, 1.068, 1.036, 1.015, 1.001, 0.991, 0.984, 0.978, 0.974, 0.971, 0.970, 0.970,
		1.065, 1.056, 1.051, 1.046, 1.040, 1.033, 1.023, 1.014, 1.005, 0.997, 0.989, 0.982, 0.974, 0.968, 0.958, 0.946, 0.930, 0.900, 0.872,
		2.047, 1.810, 1.683, 1.575, 1.485, 1.375, 1.266, 1.188, 1.133, 1.094, 1.066, 1.046, 1.032, 1.022, 1.012, 1.005, 1.000, 0.998, 0.997,
		2.022, 1.861, 1.768, 1.686, 1.613, 1.519, 1.418, 1.338, 1.275, 1.226, 1.187, 1.157, 1.133, 1.114, 1.093, 1.074, 1.059, 1.047, 1.045,
		2.503, 2.236, 2.087, 1.956, 1.843, 1.699, 1.548, 1.434, 1.347, 1.281, 1.231, 1.192, 1.164, 1.142, 1.118, 1.099, 1.084, 1.074, 1.072,
		2.253, 2.007, 1.872, 1.755, 1.654, 1.529, 1.401, 1.305, 1.235, 1.182, 1.143, 1.115, 1.093, 1.078, 1.061, 1.048, 1.039, 1.033, 1.033,
		2.228, 2.010, 1.888, 1.782, 1.690, 1.574, 1.453, 1.361, 1.292, 1.239, 1.200, 1.170, 1.147, 1.130, 1.112, 1.097, 1.085, 1.078, 1.077,
		2.527, 2.136, 1.934, 1.769, 1.633, 1.475, 1.326, 1.226, 1.159, 1.114, 1.084, 1.064, 1.051, 1.042, 1.034, 1.028, 1.025, 1.024, 1.024,
		2.097, 1.908, 1.801, 1.706, 1.622, 1.514, 1.398, 1.308, 1.238, 1.183, 1.140, 1.106, 1.080, 1.060, 1.038, 1.018, 1.002, 0.991, 0.988,
		2.479, 2.106, 1.912, 1.753, 1.623, 1.470, 1.326, 1.229, 1.163, 1.120, 1.090, 1.070, 1.057, 1.048, 1.040, 1.034, 1.031, 1.029, 1.029,
		2.097, 1.906, 1.796, 1.699, 1.612, 1.500, 1.378, 1.281, 1.205, 1.145, 1.098, 1.060, 1.031, 1.007, 0.981, 0.958, 0.939, 0.923, 0.920,
	]),
	tauAbsEtaBinsHGCal = cms.vdouble([ 1.50,1.90,2.40,3.00]),
	tauL1egInfoHGCal = cms.VPSet(
		cms.PSet(
			l1egCount = cms.double( 0.0 ),
			l1egEmFractions = cms.vdouble([ 0.0, 0.473, 0.72, 0.894, 1.05]),
		),
	),
	tauCalibrationsHGCal = cms.vdouble([
		1.665, 1.556, 1.495, 1.443, 1.398, 1.342, 1.285, 1.242, 1.211, 1.188, 1.170, 1.158, 1.148, 1.141, 1.134, 1.128, 1.124, 1.122, 1.121,
		1.646, 1.525, 1.459, 1.402, 1.353, 1.293, 1.231, 1.186, 1.153, 1.129, 1.112, 1.099, 1.089, 1.082, 1.075, 1.069, 1.065, 1.063, 1.063,
		1.826, 1.630, 1.528, 1.444, 1.376, 1.294, 1.218, 1.166, 1.130, 1.107, 1.091, 1.080, 1.072, 1.067, 1.063, 1.060, 1.058, 1.057, 1.057,
		2.031, 1.762, 1.624, 1.514, 1.424, 1.321, 1.226, 1.164, 1.124, 1.098, 1.081, 1.069, 1.062, 1.057, 1.053, 1.050, 1.049, 1.048, 1.048,
		1.396, 1.328, 1.291, 1.259, 1.232, 1.198, 1.164, 1.139, 1.120, 1.107, 1.097, 1.089, 1.084, 1.080, 1.076, 1.073, 1.071, 1.070, 1.070,
		1.242, 1.214, 1.197, 1.182, 1.168, 1.149, 1.128, 1.111, 1.097, 1.085, 1.075, 1.067, 1.060, 1.055, 1.048, 1.042, 1.036, 1.030, 1.029,
		1.491, 1.368, 1.305, 1.253, 1.211, 1.161, 1.115, 1.084, 1.064, 1.050, 1.041, 1.035, 1.031, 1.028, 1.026, 1.024, 1.023, 1.023, 1.023,
		1.348, 1.289, 1.255, 1.225, 1.199, 1.165, 1.127, 1.098, 1.075, 1.057, 1.043, 1.031, 1.022, 1.016, 1.008, 1.001, 0.995, 0.991, 0.990,
		1.422, 1.373, 1.345, 1.320, 1.297, 1.266, 1.232, 1.205, 1.183, 1.165, 1.150, 1.138, 1.128, 1.120, 1.111, 1.102, 1.095, 1.088, 1.086,
		1.350, 1.322, 1.304, 1.288, 1.272, 1.250, 1.224, 1.201, 1.180, 1.162, 1.146, 1.132, 1.119, 1.108, 1.093, 1.078, 1.061, 1.038, 1.026,
		1.440, 1.373, 1.334, 1.300, 1.270, 1.231, 1.189, 1.155, 1.129, 1.108, 1.092, 1.079, 1.069, 1.061, 1.053, 1.045, 1.038, 1.033, 1.032,
		1.356, 1.317, 1.293, 1.271, 1.250, 1.221, 1.186, 1.156, 1.129, 1.105, 1.085, 1.067, 1.051, 1.037, 1.019, 1.000, 0.980, 0.954, 0.941,
	]),
)

