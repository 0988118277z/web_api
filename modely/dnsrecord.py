from dns.asyncresolver import Resolver

async def dns_parser(domain, types, names, dnsip):
    my_resolver = Resolver()
    record_list = {'target': domain}
    for name,ip in zip(names,dnsip):
        my_resolver.nameservers = [ip]
        my_resolver.timeout = 5.0
        my_resolver.lifetime = 5.0
        try:
            answers = await my_resolver.resolve(domain, types)
            templist = sorted([ str(i) for i in answers ])
            record_list[name] = templist
        except Exception as e:
            print(e)
            record_list[name] = None
    return record_list
