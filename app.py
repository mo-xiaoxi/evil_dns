from config import *
from twisted.internet import reactor, defer
from twisted.names import client, dns, error, server

record = {}


class DynamicResolver(object):
    def handle_rebind_domain(self, name):
        if name not in record or record[name] < 1:
            ip = "222.185.163.135"
        else:
            ip = "127.0.0.1"
        if name not in record:
            record[name] = 0
        record[name] += 1
        return self.make_reply(name, ip)

    def handle_fake_domain(self, name):
        ip = FAKE_DOMAIN[name]
        return self.make_reply(name, ip)

    def make_reply(self, name, ip):
        logger.info(name + " ===> " + ip)
        answer = dns.RRHeader(
            name=name,
            type=dns.A,
            cls=dns.IN,
            ttl=0,
            payload=dns.Record_A(address=ip, ttl=0)
        )
        answers = [answer]
        authority = []
        additional = []
        return answers, authority, additional

    def query(self, query, timeout=None):
        name = query.name.name.decode('utf-8')
        if query.type != 1:
            logger.warn('Not A query!! Send real results: {}'.format(name))
            return self.get_real_results(query)
        if name in REBIND_DOMAIN:
            logger.info('DNS rebind: {}'.format(name))
            return defer.succeed(self.handle_rebind_domain(name))
        if name in FAKE_DOMAIN:
            logger.info('DNS Fake: {}'.format(name))
            return defer.succeed(self.handle_fake_domain(name))
        logger.info(' Send real results: {}'.format(name))
        return self.get_real_results(query)

    def get_real_results(self, query):
        resolver = client.Resolver(resolv='/etc/resolv.conf')
        return resolver.query(query)


def main():
    factory = server.DNSServerFactory(
        clients=[DynamicResolver()]
    )
    protocol = dns.DNSDatagramProtocol(controller=factory)
    reactor.listenUDP(53, protocol)
    reactor.run()


if __name__ == '__main__':
    raise SystemExit(main())
