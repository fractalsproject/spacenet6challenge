
from spacenet6.cosmiq import utils

if __name__ == "__main__":

    import sys
    sys.path.append(".")
    print("path=", sys.argv[1] )
    model = utils.load_pytorch_model_fromfile( sys.argv[1] )
    print(model)

