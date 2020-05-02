import argparse
from baseline import pretrain, train, pretest, test, evaluation

def parse_args(argv):
	parser = argparse.ArgumentParser(description='SpaceNet 6 Baseline Algorithm')
    	#Which operations to carry out
	parser.add_argument('--pretrain', action='store_true',\
                        help='Whether to format training data')
	parser.add_argument('--train', action='store_true',\
                        help='Whether to train model')
	parser.add_argument('--pretest', action='store_true',\
                        help='Whether to format testing data')
	parser.add_argument('--test', action='store_true',\
                        help='Whether to test model')
	parser.add_argument('--eval', action='store_true',\
                        help='Whether to evaluate test output')
	#Training: Input file paths
	parser.add_argument('--sardir',\
                        help='Folder of SAR training imagery files')
	parser.add_argument('--opticaldir',\
                        help='Folder of optical imagery files')
	parser.add_argument('--labeldir',\
                        help='Folder of building footprint vector files')
	parser.add_argument('--rotationfile',\
                        help='File of data acquisition directions')
	#Training: Preprocessed file paths
	parser.add_argument('--rotationfilelocal',\
                        help='Where to save a copy of directions file')
	parser.add_argument('--maskdir',\
                        help='Where to save building footprint masks')
	parser.add_argument('--sarprocdir',\
                        help='Where to save preprocessed SAR training files')
	parser.add_argument('--opticalprocdir',\
                        help='Where to save preprocessed optical image files')
	#Training and inference: YAML and Reference CSV file paths
	parser.add_argument('--traincsv',\
                        help='Where to save reference CSV of training data')
	parser.add_argument('--validcsv',\
                        help='Where to save reference CSV of validation data')
	parser.add_argument('--opticaltraincsv',\
                        help='Where to save CSV of optical training data')
	parser.add_argument('--opticalvalidcsv',\
                        help='Where to save CSV of optical validation data')
	parser.add_argument('--testcsv',\
                        help='Where to save reference CSV of testing data')
	parser.add_argument('--yamlpath',\
                        help='Where to save YAML file')
	parser.add_argument('--opticalyamlpath',\
                        help='Where to save transfer learning YAML file')
	#Training and inference: Model weights file path
	parser.add_argument('--modeldir',\
                        help='Where to save model weights')
	#Inference (testing) file paths
	parser.add_argument('--testdir',\
                        help='Folder of SAR testing imagery files')
	parser.add_argument('--testprocdir',\
                        help='Where to save preprocessed SAR testing files')
	parser.add_argument('--testoutdir', \
                        help='Where to save test continuous segmentation maps')
	parser.add_argument('--testbinarydir',\
                        help='Where to save test binary segmentation maps')
	parser.add_argument('--testvectordir',\
                        help='Where to save test vector label output')
	parser.add_argument('--outputcsv',\
                        help='Where to save labels inferred from test data')
	#Algorithm settings
	parser.add_argument('--rotate', action='store_true',\
                        help='Rotate tiles to align imaging direction')
	parser.add_argument('--transferoptical', action='store_true',\
                        help='Train model on optical before training on SAR')
	parser.add_argument('--mintrainsize',\
                        help='Minimum building size (m^2) for training')
	parser.add_argument('--mintestsize',\
                        help='Minimum size to output during testing')
	parser.add_argument('--uselastmodel', action='store_true',\
                        help='Do not overwrite last model with best model')
	parser.add_argument('--earlycutoff',\
                        help='Limit tiles used, for debugging purposes')
	args = parser.parse_args(argv[1:])

def invoke(args):
	if args.pretrain:
        	pretrain(args)
	if args.train:
		train(args)
	if args.pretest:
		pretest(args)
	if args.test:
		test(args)
	if args.eval:
		evaluation(args)
