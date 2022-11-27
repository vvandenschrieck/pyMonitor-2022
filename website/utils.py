from probes import state_probes
from website.website import Website


def load_sites(filename):
    """Creates a list of Website objects based on the content of a file
        This file must contain one website per line, one line having 3 parameters separeted by ; :
            - The name of the site
            - The DNS name of the site
            - The list of test to apply, comma-separated.
        followed by ; then the DNS name of the site (no http/https), then
    """
    sites = []
    probe_dict = {"ping": state_probes.test_status_with_ping,
                  "nmap": state_probes.test_port_443_with_nmap}

    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            name, url, probes = line.split(";")
            site = Website(name, url)
            for probe in probes.split(","):
                site.add_probe(probe_dict[probe])
            sites.append(site)
    return sites
