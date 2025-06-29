r"""
C:\VirtualEnvs\misc\Scripts\Activate.ps1
cd D:\GitHub\mapserver-templates\scripts
pip install -e D:\GitHub\mappyfile
python services.py
"""

import mappyfile
import json
import os
import subprocess


def check_metadata(d, keys):

    if "web" in d and "metadata" in d["web"]:
        md = d["web"]["metadata"]
        for k in keys:
            key = f"{k}_enable_request"
            if key in md:
                if md[key] == "*" or "GetCapabilities" in md[key]:
                    return True
    return False


def generate_index(root, cfg):

    linkset = []

    for alias, mf in cfg.items():
        alias = alias.lower()

        filename = os.path.basename(mf)
        link = {
            "anchor": f"{root}/{alias}/",
            "service-desc": [
                {
                    "href": f"{root}/{alias}/api-catalog.json",  # TODO replace with ?f=json
                    "title": f"{filename}",
                    "type": "application/vnd.oai.openapi+json",
                }
            ],
            "service-doc": [
                {
                    "href": f"{root}/{alias}/",  # TODO replace with ?f=html
                    "title": f"{filename}",
                    "type": "text/html",
                }
            ],
        }

        linkset.append(link)

    jsn = {"linkset": linkset}

    return jsn


def generate_oapif(anchor):

    return [{
        "anchor": f"{anchor}",
        "service-desc": [
            {
                "href": f"{anchor}/ogcapi/",
                "title": f"OGC API Landing Page",
                "service": "OAPIF",
                "type": "application/json",
            }
        ],
        "service-doc": [
            {
                "href": f"{anchor}/ogcapi/",
                "title": f"OGC API Landing Page",
                "service": "OAPIF",
                "type": "application/json",
            }
        ],
    }]


def generate_wms(anchor):

    versions = ["1.0.0", "1.0.6", "1.0.7", "1.1.0", "1.1.1", "1.3.0"]

    # check if WMS is supported
    # in C also check USE_WMS_SVR

    services = []

    for version in versions:
        service = {
            "href": f"{anchor}/?version={version}&request=GetCapabilities&service=WMS",
            "title": f"WMS GetCapabilities URL (version {version})",
            "service": "WMS",
            "type": "text/xml",
        }
        services.append(service)

    return services


def generate_wfs(anchor):
    versions = ["1.0.0", "1.1.0", "2.0.0"]

    # check if WFS is supported
    # in C also check USE_WFS_SVR

    services = []

    for version in versions:
        service = {
            "href": f"{anchor}/?version={version}&request=GetCapabilities&service=WFS",
            "title": f"WFS GetCapabilities URL (version {version})",
            "service": "WFS",
            "type": "text/xml",
        }
        services.append(service)

    return services


def generate_wcs(anchor):
    versions = ["1.0.0", "1.1.0", "2.0.0", "2.0.1"]

    # check if WCS is supported
    # in C also check USE_WCS_SVR

    services = []

    for version in versions:
        service = {
            "href": f"{anchor}/?version={version}&request=GetCapabilities&service=WCS",
            "title": f"WCS GetCapabilities URL (version {version})",
            "service": "WCS",
            "type": "text/xml",
        }
        services.append(service)

    return services


def generate_json(mf, root, alias):
    d = mappyfile.open(mf)

    ows_services = []
    ogc_services = []

    jsn = {}
    anchor = f"{root}" # /{alias}" # these are relative to current folder

    if check_metadata(d, keys=["wms", "ows"]):
        ows_services += generate_wms(anchor)

    if check_metadata(d, keys=["wfs", "ows"]):
        ows_services += generate_wfs(anchor)

    if check_metadata(d, keys=["wcs", "ows"]):
        ows_services += generate_wcs(anchor)

    if check_metadata(d, keys=["oga"]):
        ogc_services += generate_oapif(anchor)

    linkset = []

    if len(ogc_services) > 0:
        linkset += ogc_services

    if len(ows_services) > 0:
        ows_link = {
            "anchor": f"{anchor}/",
            "title": "OWS Services",
            "description": "Mapfile Description",
            "service-desc": ows_services,
        }
        linkset.append(ows_link)

    jsn = {"linkset": linkset}

    return jsn


def main():

    # create output folder

    root_folder = "./dist"
    os.makedirs(root_folder, exist_ok=True)

    # parse the config file
    cf = r"D:\GitHub\mapserver-templates\mapfiles\mapserver-windows.conf"
    # d = mappyfile.open(cf)
    # print(d)

    cfg = {
        "WMSDEMO": r"D:\GitHub\mapserver-templates\mapfiles\wms.map",
        "WFSDEMO": r"D:\GitHub\mapserver-templates\mapfiles\wfs.map",
        "WCSDEMO": r"D:\GitHub\mapserver-templates\mapfiles\wcs.map",
        "OAPIFDEMO": r"D:\GitHub\mapserver-templates\mapfiles\oapif.map",
        "CGIDEMO": r"D:\GitHub\mapserver-templates\mapfiles\cgi.map",
        "KITCHENSINK": r"D:\GitHub\mapserver-templates\mapfiles\kitchensink.map"
    }

    root = "."
    jsn = generate_index(root, cfg)

    index = os.path.join(root_folder, "api-catalog.json")
    with open(index, "w") as f:
        f.write(json.dumps(jsn, indent=4))

    exe_path = "../build/Debug/mapserver-templates.exe"

    for alias, mf in cfg.items():
        alias = alias.lower()
        fld = os.path.join(root_folder, alias)
        os.makedirs(fld, exist_ok=True)
        jsn = generate_json(mf, root, alias)

        fn = os.path.join(fld, "api-catalog.json")
        with open(fn, "w") as f:
            f.write(json.dumps(jsn, indent=4))

        command = [
            exe_path,
            "../mapserver-index/html-bootstrap4/map.html",
            os.path.join(fld, "api-catalog.json"),
        ]

        # Open the output file for writing
        with open(os.path.join(fld, "index.html"), "w") as outfile:
            subprocess.run(command, stdout=outfile, check=True)

    # run HTML template generation
    command = [
        exe_path,
        "../mapserver-index/html-bootstrap4/landing.html",
        "./dist/api-catalog.json",
    ]

    # Open the output file for writing
    with open("./dist/index.html", "w") as outfile:
        subprocess.run(command, stdout=outfile, check=True)


if __name__ == "__main__":
    main()