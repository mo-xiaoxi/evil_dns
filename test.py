import dns.resolver


def test_server(server, domain):
    resolver = dns.resolver.Resolver()
    resolver.lifetime = resolver.timeout = 20.0
    try:
        resolver.nameservers = [server]
        answers = resolver.query(domain)  # test lookup a existed domain
        for a in answers:
            print(a)
    except:
        print('[+] Check DNS Server %s <Fail>   Domain %s' % (server.ljust(16), domain))


server = '127.0.0.1'
domain = 'baidu.com'
test_server(server, domain)
