__author__ = 'evan'
import sys

from oslo_config import cfg


service_opts = [
    cfg.StrOpt('api_config',
               default="api-paste.ini",
               help='File name for rm-api'),
    cfg.IntOpt('client_socket_timeout', default=900,
               help="Timeout for client connections' socket operations. "
                    "If an incoming connection is idle for this number of "
                    "seconds it will be closed. A value of '0' means "
                    "wait forever."),
]

CONF = cfg.CONF
CONF.register_opts(service_opts)


def main():
    CONF.par

if __name__ == '__main__':
    sys.exit(main())
