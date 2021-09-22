"""
so I have a router that has a model name and an IP address
let's begin with these two attributes
I can manage this router pretty easily but my company requires me to automate the process of configuring it and we're planning to scale up to 100 routers
so we know they're all routers but have different IP addresses to route the packets
you can define a router as a dictionary that has keys and values
router = {
        'model': 'TP-Link',
        'IP': '192.168.1.1',
    }
however I want the IP to be configurable, so it would change automatically every time there's a change in the network
so maybe something like this:
router_floor_1 = {
        'model': 'TP-Link',
        'IP': '192.168.1.1'
    }


router_floor_2 = {
        'model': 'TP-Link',
        'IP': '192.168.2.1',
        'next_hop': router_floor_1['IP']
    }

"""