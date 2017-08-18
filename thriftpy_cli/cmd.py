#! /usr/bin/env python
# -*- coding: utf-8 -*-

import click
import thriftpy
import IPython

from thriftpy.protocol import TCyBinaryProtocolFactory
from thriftpy.transport import TCyBufferedTransportFactory
from thriftpy.rpc import client_context


@click.command()
@click.option("-t", "--thrift", help="thrift file path", required=True)
@click.option("-h", "--host", default="localhost", type=str, help="server hostname")
@click.option("-p", "--port", default=8010, type=int, help="server port")
@click.option("-s", "--service", type=str, help="Service", required=True)
def client(thrift, host, port, service):
    calc_thrift = thriftpy.load(str(thrift))
    with client_context(getattr(calc_thrift, service), host, port,
                        proto_factory=TCyBinaryProtocolFactory(),
                        trans_factory=TCyBufferedTransportFactory()) as client:
        IPython.embed(header="Call client.api(*args)")
