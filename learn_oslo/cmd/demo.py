__author__ = 'evan'
import sys
from learn_oslo.cmd.api import main as api_main
from learn_oslo.cmd.api_service import main as service_main


if __name__ == '__main__':
    # sys.exit(api_main())
    sys.exit(service_main())